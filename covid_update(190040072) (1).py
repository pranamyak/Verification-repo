from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

head = {"User-Agent" : "Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = head)
link=urlopen(req)


obj = bs(link ,features="html.parser")
cases = obj.find("li",{"class":"news_li"}).strong.text.split()[0]
deaths = list(obj.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

notification = ToastNotifier()
text2 = "New Cases - " + cases + "\nDeath -" + deaths
notification.show_toast(title="Covid-19 Update" , msg = text2 , duration= 7)