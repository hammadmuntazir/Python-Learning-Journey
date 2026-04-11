# html = "<html><title class='Ali'>My Page</title><h3 class='heading' id='3'>LeBron James</h3></html>"
import requests
from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'html.parser')
# # # print(soup)
# # tag_object=soup.title
# # # print(tag_object.text)
# # # print(tag_object.attrs)
# # # print(tag_object.__class__)
# # # print(tag_object.child)
# # # print(tag_object.parent)
# # print(tag_object.nextSibling)
# # print(tag_object['class'])
# # for child in soup.html.children:
# #     # print(f'{child} \n')
# print(soup.html)

# print('\n')
with open('menu.html','r',encoding='utf-8')as file:
    html=file.read()
table=BeautifulSoup(html,"html.parser")
rows=(table.find_all('tr'))
for row in rows:
    cells=row.find_all('td')
    for cell in cells:
        print(cell.string)