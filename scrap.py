import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.bikewale.com/royalenfield-bikes/"
page = requests.get(url)



soup = BeautifulSoup(page.content,'html.parser')


#images

'''img1 = []
image = soup.findAll('div',class_="imageWrapper")

for i in image:
    j = i.img['src']
    img1.append(j)'''

#links

'''links = []
link = soup.findAll('div',class_ = 'bikeDescWrapper')
for i in link:
    j = i.a['href']
    links.append(j)'''

#Texts

texts = []
text = soup.findAll('div',class_ = 'bikeDescWrapper')
for i in text :
    j = i.a.text
    texts.append(j)
    print(texts)

#USING CSV we have to store the data
'''with open('il.csv','w') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(image)
    for i in image:
        j = i.img['src']
        img1.append(j)
    write.writerow(img1) '''  
