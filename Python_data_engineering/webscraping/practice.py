# # import requests
# # from bs4 import BeautifulSoup
# # html = "<html><title>My Page</title><h3 class='heading' id='3'>LeBron James</h3></html>"

# # #  soup object represents the html as tree
# # soup=BeautifulSoup(html,'html.parser')
# # # Tag
# # # print(soup.html)
# # # print(soup.title)
# # # print(soup.h3)
# # # print(soup.title.text)
# # # print(soup.h3.string)
# # # Navigating the tree
# # tag_object=soup.title
# # # print(tag_object.child)
# # # print(tag_object.parent)
# # html_childs=soup.html.children
# # for child in html_childs:
# #     print(child)
# # for child in soup.html.children:
# #     print(child)
# # print(tag_object.next_sibling)

# import requests
# with open('menu.html','r',encoding='utf-8') as file:
#     html=file.read()
# from bs4 import BeautifulSoup

# # Parsing the html file
# table=BeautifulSoup(html, "html.parser")
# rows=table.find_all('tr')
# for row in rows:
#     print(f'{row} \n')

