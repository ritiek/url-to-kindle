import requests
import shutil
import time
import json
import argparse

DEVICE = "Kindle Paperwhite 3"


class UnexpectedStatus(Exception):
    def __init__(self, message=None):
        super(UnexpectedStatus, self).__init__(message)


class Downloader:
    def __init__(self, job_id, output_id):
        self.job_id = job_id
        self.output_id = output_id

    def download_file(self, filename):
        print("Fetching download link:")
        download_link = "https://www.online-convert.com/downloadFile/{job_id}/{output_id}".format(
            job_id=self.job_id, output_id=self.output_id
        )
        print(download_link)
        print("")
        print("Saving as {filename} ...".format(filename=filename))
        response = requests.get(download_link, stream=True)
        with open(filename, "wb") as fout:
            shutil.copyfileobj(response.raw, fout)


class CreateWorkspace:
    def __init__(self):
        self.job_id, self.conversion_id = self._create_job()
        self.base_url = "https://www.online-convert.com/api/jobs/"
        self.input_url = "{base_url}/{job_id}/input".format(
            base_url=self.base_url, job_id=self.job_id
        )
        self.start_url = "{base_url}/{job_id}/start".format(
            base_url=self.base_url, job_id=self.job_id
        )
        self.callback_url = "{base_url}/{job_id}/callbackstatus".format(
            base_url=self.base_url, job_id=self.job_id
        )

    def _create_job(self):
        create_job = requests.post(
            "https://www.online-convert.com/api/jobs",
            headers={"origin": "https://ebook.online-convert.com"},
            data={
                "fail_on_input_error": "false",
                "process": "false",
                "target": "mobi",
                "category": "ebook",
            },
        )
        parsed_response = json.loads(create_job.text)
        job_id = parsed_response["id"]
        conversion_id = parsed_response["conversion"][0]["id"]
        print("Create Job:")
        print(create_job.text)
        print("")
        return job_id, conversion_id

    def add_job(self, url):
        add_job = requests.post(
            self.input_url,
            headers={"origin": "https://ebook.online-convert.com"},
            data={"type": "remote", "source": url},
        )
        print("Add Job:")
        print(add_job.text)
        print("")
        parsed_response = json.loads(add_job.text)
        add_id = parsed_response["id"]
        return add_id

    def start_job(self, reader="default", title="", author=""):
        start_job = requests.post(
            self.start_url,
            headers={"origin": "https://ebook.online-convert.com"},
            data={
                "target": "mobi",
                "category": "ebook",
                "reader": reader,
                "title": title,
                "author": author,
                "border": "",
                "base_font_size": "",
                "encoding": "",
                "string_method": "convert-to-mobi",
                "conversion_id": self.conversion_id,
            },
        )
        print("Starting Job..")
        print("")
        output_id = self._wait_for_completion()
        return Downloader(self.job_id, output_id)

    def _wait_for_completion(self):
        incomplete_statuses = ("downloading", "processing")
        completed_status = "completed"
        while True:
            callback_response = requests.get(self.callback_url)
            parsed_response = json.loads(callback_response.text)
            status = parsed_response["status"]
            print("Server status: {}".format(status))
            if status == completed_status:
                print("")
                return parsed_response["output"][0]["id"]
            elif status not in incomplete_statuses:
                raise UnexpectedStatus(
                    "Server returned unexpected status: {}".format(status)
                )
            time.sleep(3)


def _get_arguments(raw_args=None):
    parser = argparse.ArgumentParser(
        description="Convert a webpage, PDF, etc. from URL to MOBI via ebook.online-convert.com, designed for (jailbroken) Kindles",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("url", metavar="URL", help="webpage url to download as MOBI")
    parser.add_argument(
        "-f", "--filename", required=True, help="download MOBI to this path"
    )
    parser.add_argument("-t", "--title", default="", help="set title of the book")
    parser.add_argument("-a", "--author", default="", help="set author of the book")

    parsed = parser.parse_args(raw_args)
    return parsed


def _command_line():
    args = _get_arguments()
    workspace = CreateWorkspace()
    workspace.add_job(args.url)
    completed_job = workspace.start_job(
        reader=DEVICE, title=args.title, author=args.author
    )
    completed_job.download_file(args.filename)


if __name__ == "__main__":
    _command_line()
