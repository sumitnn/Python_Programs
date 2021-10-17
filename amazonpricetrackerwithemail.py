# get amazon price of our item and other details
import requests
from bs4 import BeautifulSoup as bs
import smtplib


data = {
    1: ["Apple iPhone 13 Pro Max (1TB) - Silver", "https://www.amazon.in/Apple-iPhone-Pro-Max-1TB/dp/B09G9CV8NX/ref=sr_1_7?dchild=1&keywords=iphone+13&qid=1634456619&sr=8-7", "priceblock_ourprice"],
    2: ["Sony HT-RT40 600 Watt Real 5.1 Channel Wireless Bluetooth ", "https://www.amazon.in/Sony-HT-RT40-Digital-Soundbar-Theatre/dp/B073RLK59B/ref=sr_1_4?dchild=1&keywords=sony+home+theater&pd_rd_r=464890a8-01ad-4a51-b776-3c0a3174e2a9&pd_rd_w=b1KJc&pd_rd_wg=TiFL1&pf_rd_p=206c771a-9255-43c3-91ee-be3d883c7b95&pf_rd_r=5AVPHAP1BTZ3YWWZQZTV&qid=1634456995&sr=8-4", "priceblock_dealprice"]

}


# def sendmail(l):
#     try:

#         s = smtplib.SMTP('smtp.gmail.com', 587)

#         s.starttls()

#         s.login("man@gmailcom", "mmkehvpetbjpjphc")

#         message = str(l)

#         s.sendmail("m@gmailcom",
#                    "m@gmailcom", message)

#         s.quit()
#     except Exception as e:
#         print(e)


def getprice(url, name, id):
    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"})
    soup = bs(r.content, 'html.parser')
    res = soup.find(id=id).text.replace('₹', '')
    actualprice = float(res.replace(',', ''))
    l = f"name:{name}\n price:{actualprice}\n url:{url}"
    # sendmail(l)
    return l


for key, value in data.items():
    a = getprice(value[1], value[0], value[2])
    print(a)
    print()
