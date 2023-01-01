import requests

domain = input('Enter the hostname http://')

response = requests.get('http://' + domain)

print(response.json)

print('Code status: ' + str(response.status_code))

print('Headers response: ')
for header, value in response.headers.items():
    print(header, '--->', value)

print('Headers request: ')
for header, value in response.request.headers.items():
    print(header, '--->', value)