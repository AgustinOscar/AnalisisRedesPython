import requests
from requests.auth import HTTPDigestAuth
from getpass import getpass

user = input('Enter username: ')
password = getpass()

response = requests.get('http://httpbin.org/digest-auth/auth/user/pass',
                        auth=HTTPDigestAuth(user, password))

print('Headers request:')
for header, value in response.request.headers.items():
        print(header, '--->', value)