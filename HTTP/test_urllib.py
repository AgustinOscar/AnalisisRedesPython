import urllib.request

print('Starting download...')

url = 'https://www.python.org/static/img/python-logo.png'

#Descargamos el archivo con urlretrieve.
urllib.request.urlretrieve(url, 'python.png')

#Descargamos un archivo con urlopen.
with urllib.request.urlopen(url) as response:
    print('Status: ', response.status)
    print('Downloading python.png')
    with open('python.png', 'wb') as image:
        image.write(response.read())