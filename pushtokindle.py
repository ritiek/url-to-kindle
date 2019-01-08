import requests

FROM = "my_kindle_approved_email@gmail.com"
EMAIL= "my_kinde_email@kindle.com"

_, domain_name = EMAIL.split("@")
available_domain_names = ("free.kindle.com", "kindle.com", "kindle.cn", "iduokan.com", "pbsync.com")
domain_int = available_domain_names.index(domain_name) + 1

params = (
    ('context', 'send'),
    ('url', 'https://meltdownattack.com/meltdown.pdf'),
)


data = {"from":  FROM,
        "title": "",
        "email": EMAIL,
        "domain": domain_int,}

response = requests.post('https://pushtokindle.fivefilters.org/send.php', params=params, data=data)
