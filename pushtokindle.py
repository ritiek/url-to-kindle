import requests
import sys

FROM = "my_kindle_approved_email@gmail.com"
TO = "my_kindle_email@kindle.com"

email, domain_name = TO.split("@")
available_domain_names = ("free.kindle.com", "kindle.com", "kindle.cn", "iduokan.com", "pbsync.com")
domain_int = available_domain_names.index(domain_name) + 1

params = (
    ("context", "send"),
    ("url", sys.argv[1]),
)


data = {"from":  FROM,
        "title": "",
        "email": email,
        "domain": domain_int,}

response = requests.post("https://pushtokindle.fivefilters.org/send.php", params=params, data=data)
print(response.text)
