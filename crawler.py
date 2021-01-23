import requests
import datetime
import time
import smtplib
import SMS_LFC
import email_LFC

from bs4 import BeautifulSoup

links = [
'https://appointments.lacounty.gov/vaccinestaffing/Calendar/63/3011/',
'https://appointments.lacounty.gov/vaccinestaffing/Calendar/64/3001/',
'https://appointments.lacounty.gov/vaccinestaffing/Calendar/65/3003/',
'https://appointments.lacounty.gov/vaccinestaffing/Calendar/66/3005/',
'https://appointments.lacounty.gov/vaccinestaffing/Calendar/67/3007/'
]

keyword = 'All Shifts Filled'

# pagenums = ['0', '1', '2', '3']
# pagenums = [str(i) for i in range(4)]
maxPage = 4
# <body /  <div class="container"> / <div class="row form-row bg-light border mb-2 ">…</div> * 7

# def openShift(links, keyword, pagenums):
def openShift(links, keyword, maxPage):
    count = 0
    for link in links:
        # for page in pagenums:
        for page in range(maxPage):
            url = link + str(page)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            divs = soup.find_all(class_="col-sm-10 pt-2 d-flex flex-wrap align-items-center justify-content-center justify-content-sm-start")
            for div in divs:
                count += 1
                if str(div).find(keyword) < 0:
                    message = '\n Vaccine volunteer slot available sign up here: ' + url
                    email_LFC.sendEmail(message)
                    SMS_LFC.sendSMS(message)
                    time.sleep(300)
                else:
                    print('None today', count)
            

def main():
    while 1:
        openShift(links, keyword, maxPage)
        time.sleep(10)

main()