from bs4 import BeautifulSoup
import os

html = BeautifulSoup(open("./docs/template.html").read(), "html.parser")

print(html.prettify())
tag = html.new_tag('p')
html.insert_after()