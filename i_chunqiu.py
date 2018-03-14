import requests
import re
url = 'https://www.ichunqiu.com/courses/website-all-0-0-0-2-1'
r = requests.get(url)
print r.text
