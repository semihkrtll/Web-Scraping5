import requests
from bs4 import BeautifulSoup

headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" }

Url= "https://www.amazon.com.tr/HP-Bilgisayar-i5-14500HX-Performans-9J207EA/dp/B0CQRN9TQ5/ref=sr_1_7?dib=eyJ2IjoiMSJ9.pnHb6RHxzGDXkS768_lcjjyoD8-LBOVsqwEi3uwHwm6QlzH6ValxtJiV4Osnfh5UDChBsucGT0MvFsNjlejMunqAsVGLoyLXB44rTlxZKxLmbUTUgZ8M0IX-CYpeC5dsftz6ARtJd7ryXzaiayn5At2-bsPwo3BTZ6wq3roH2rV1c2UcI6vRelOoCJhY9LB7H2PFbyRakpdNlSx3AEo4GQQhhyNplLbscKqwAvacoP0Y5Fd-z-kvXIGrQpZgWRMjndr3WT-dsuPKbxZtRCA3kDWFVFgObVyU94_bEOc2aZ4.amYyUnDLH1VAvkPiJ1UleUKvoNbveHDolCCEoYrji8U&dib_tag=se&keywords=bilgisayar&qid=1723898934&sr=8-7"
sayfa=requests.get(Url,headers=headers)
icerik=BeautifulSoup(sayfa.content,"html.parser")

urunAdi=icerik.find(id="productTitle").get_text().strip()
print(urunAdi)

ucreti=icerik.find("span",{"class":"aok-offscreen"}).get_text()
print(ucreti)





