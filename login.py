import getpass
import requests
from bs4 import BeautifulSoup
import json
try:
    with open("config.json") as json_data_files:
        json_data = json.load(json_data_files)
        print("open file success")
    data = json_data["credentials"]
    headers_2 = json_data["headers_2"]
    headers_1 = json_data["headers_1"]
except:
    print("open file error")
    pass
username = name = input("username : ")
password = getpass.getpass()
data["username"] = username
data["password"] = password


session = requests.Session()
response = session.get(
    'https://internet.ugm.ac.id/sso/login', headers=headers_1)
cookies = session.cookies.get_dict()
contents = (response.content)

soup = BeautifulSoup(contents, "lxml")
lt = soup.find("input", {'name': "lt"}).attrs['value']


params = (
    ('service', 'https://internet.ugm.ac.id/sso/login'),
)
data["lt"] = lt


response = session.post('https://sso.ugm.ac.id/cas/login;jsessionid=07C11FADDB7E2690F6CD1458691CDD7A',
                        headers=headers_2, params=params, cookies=cookies, data=data)
# print(response.content)
soup = BeautifulSoup(response.content, "lxml")
if soup.find_all("span", {"class": "text-xs"}):
    print("Login Success")
else:
    print("Login failure")
