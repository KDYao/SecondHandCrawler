# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from Tkinter import *
import urllib2
import time
import smtplib
headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
shoppingList = list()
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("username","password")

app = Tk()
app.title("Bargain Finder")
frame = Frame(app)
frame.pack(fill= BOTH, expand = True)
app.geometry('600x400+100+100')
labelText = StringVar()
labelText.set("You need to input keywords you need to search")
label1 = Label(frame,textvariable = labelText, height = 4)

keyword1 = Label( app, text="keyword1")
E1 = Entry(app, bd =5)

keyword2 = Label( app, text="keyword2")
E2 = Entry(app, bd =5)

keyword3 = Label( app, text="keyword3")
E3 = Entry(app, bd =5)
items = []
def Submit():
    if E1.get()=="":
        pass
    else:
        items.append(str(E1.get()).encode('utf-8'))
    if E2.get()=="":
        pass
    else:
        items.append(str(E2.get()).encode('utf-8'))
    if E3.get()=="":
        pass
    else:
        items.append(str(E3.get()).encode('utf-8'))

def Start():
    while (True):
        Req = urllib2.Request("http://www.mengchenghui.com/forum-ershou-1.html", headers=headers)
        content = urllib2.urlopen(Req).read()
        soup = BeautifulSoup(content, 'html.parser')
        for aTag in soup.find_all('a', attrs={"onclick": "atarget(this)"}):
            # items = ["iphone", "手机壳"]
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
                        server.sendmail("kundiyao@gmail.com", "yaokundi19930126@gmail.com", msg)
                    else:
                        pass
        time.sleep(60)

submitButton = Button(app,text="Submit",command = Submit)
startButotn = Button(app,text="Start",command = Start)
label1.pack()
keyword1.pack()
E1.pack()
keyword2.pack()
E2.pack()
keyword3.pack()
E3.pack()
submitButton.pack()
startButotn.pack()
app.mainloop()


