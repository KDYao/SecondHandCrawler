# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time
import smtplib
import getpass


print 'Prove your authentication'
sender_email = raw_input('Please input sender\'s email address:\n')
password = getpass.getpass(prompt='Please input your password:\n')

# Get receiver's email
receiver_email = raw_input('Please input receiver\'s email address:\n')

headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}

# Add a shopping list to restore detected items, to remove conflicts
shoppingList = list()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login(user=sender_email, password=password)


# Not sure if mandarin input support in terminal
items = ["火锅", "烧烤","电视"]


def Start():
    while (True):
        Req = urllib2.Request("http://www.mengchenghui.com/forum-ershou-1.html", headers=headers)
        content = urllib2.urlopen(Req).read()
        soup = BeautifulSoup(content, 'html.parser')
        for aTag in soup.find_all('a', attrs={"onclick": "atarget(this)"}):
            itemText = aTag.get_text()
            itemText = itemText.encode('utf-8')
            itemUrl = "http://www.mengchenghui.com/" + str(aTag).split('href="')[1].split('"')[0]
            for item in items:
                if item.lower() in itemText.lower():
                    if not itemUrl in shoppingList:
                        print itemText
                        print itemUrl
                        shoppingList.append(itemUrl)
                        msg = "\n" + "你要找的:" + itemText + "现在粗线啦，快去 " + itemUrl + " 抢吧"
                        server.sendmail(sender_email, receiver_email, msg)
                    else:
                        pass
        time.sleep(60)


if __name__ == '__main__':
    Start()


