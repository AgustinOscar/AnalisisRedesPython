'''
    Este programa cuenta el número de palabras que tiene una
    página web.
'''

import urllib.request
import urllib.error

def count_words_file(url):
    try:
        file_response = urllib.request.urlopen(url)
    except urllib.error.URLError as error:
        print('Exception: ', error)
        print('Reason: ', error.reason)
    else:
        content = file_response.read()
        return len(content.split())

print(count_words_file('https://github.com/trustedsec/hate_crack/blob/master/readme.md'))
