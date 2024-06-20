import user_Login
import webbrowser
from URL_check import check_url
from IP_Address_check import check_IP

user = user_Login.login()


if check_IP(user[2]) == 0:
    pass
else:
    url = input("Enter a Website you Want to Enter: ")
    check_url(url)
    if user[0] == "Admin":
        x = input("Website is malicious, Press x for run anyway.")
        if x == "x":
            webbrowser.open(url)