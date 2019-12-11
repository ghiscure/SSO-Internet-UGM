#!/usr/bin/env python3
import platform    
import subprocess  
import getpass
import requests
from bs4 import BeautifulSoup
import json


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess
    import platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if platform.system().lower() == "windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0


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

if ping("8.8.8.8") == True:
    print("Login Success")
else:
    print("Login Failure")
