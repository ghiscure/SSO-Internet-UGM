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

except:
    print("open file error")
    pass


def login():
    username = input("username : ")
    password = getpass.getpass()
    session = requests.Session()
    data["username"] = username
    data["password"] = password

    response = session.get(
        'https://internet.ugm.ac.id/sso/login')
    contents = (response.content)

    soup = BeautifulSoup(contents, "lxml")
    lt = soup.find("input", {'name': "lt"}).attrs['value']

    params = (
        ('service', 'https://internet.ugm.ac.id/sso/login'),
    )
    data["lt"] = lt

    response = session.post('https://sso.ugm.ac.id/cas/login',
                            params=params, data=data)

    if ping("10.13.10.13") == True:
        return True
    else:
        return False


if __name__ == "__main__":
    if(login()):
        print("Login Success")
    else:
        print("Login Failure")
