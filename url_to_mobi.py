import requests
import time
import json
import sys

create_job = requests.post("https://www.online-convert.com/api/jobs",
                           headers={"origin": "https://ebook.online-convert.com"},
                           data={"fail_on_input_error" : "false",
                                 "process"             : "false",
                                 "target"              : "mobi",
                                 "category"            : "ebook"}
                           )

parsed_response = json.loads(create_job.text)
conversion_id = parsed_response["conversion"][0]["id"]
job_id = parsed_response["id"]
print(job_id)
print(conversion_id)
print(create_job.text)


base_url = "https://www.online-convert.com/api/jobs/"
input_url = base_url + job_id + "/input"
add_job = requests.post(input_url,
                        headers={"origin": "https://ebook.online-convert.com"},
                        data={"type":   "remote",
                              "source": sys.argv[1]}
                        )
print(add_job.text)
parsed_response = json.loads(add_job.text)
add_id = parsed_response["id"]

start_url = base_url + job_id + "/start"
start_job = requests.post(start_url,
                          headers={"origin": "https://ebook.online-convert.com"},
                          data={
                          "target":         "mobi",
                          "category":       "ebook",
                          "reader":         "Kindle Paperwhite 3",
                          "title":"",
                          "author":"",
                          "border":"",
                          "base_font_size":"",
                          "encoding":"",
                          "string_method":  "convert-to-mobi",
                          "conversion_id":  conversion_id})
print(start_job.text)

callback_url = base_url + job_id + '/callbackstatus'
while True:
    callback_response = requests.get(callback_url)
    parsed_response = json.loads(callback_response.text)
    if parsed_response["status"] == "downloading":
        print("downloading")
    elif parsed_response["status"] == "processing":
        print("processing")
    elif parsed_response["status"] == "completed":
        print("completed")
        break
    time.sleep(3)

print(parsed_response)

output_id = parsed_response["output"][0]["id"]

download_link = "https://www.online-convert.com/downloadFile/" + job_id + "/" + output_id
download_response = requests.get(download_link)
with open("converted.mobi", "wb") as fout:
    fout.write(download_response.content)
