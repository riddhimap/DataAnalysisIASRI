from lxml import html
import requests
from BeautifulSoup import BeautifulSoup
import sys

url = 'http://www.cropweatheroutlook.in/crida/agmet/Datacatalog.html'

page = requests.get(url)

#Check if URL exists
checkNull = page.text
checkCode = page.status_code
if checkNull != "" and checkCode == 200 : 
    tree = html.fromstring(page.content)
for i in range(3,9):
    state=tree.xpath('/html/body/table[3]/tbody/tr[i]/td[2]/font/text()'
    print i+1, state

                     
