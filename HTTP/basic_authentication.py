import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input('Enter username: ')
password = getpass()

response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(user, password))

print('Response status code:' + str(response.status_code))

if response.status_code == 200:
    print('Login succesful:', response.txt)
