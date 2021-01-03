import requests
from bs4 import BeautifulSoup
from selenium import webdriver

result = requests.get("http://appcatalogo.ifema.es/waCatalogoWeb/index.html?feria=MF17&idioma=es&_ga=2.84562589.565538334.1608543158-1318591213.1608543158#LEMPRESAS&p=1&t=TODO&access&access&access&access&access&access")
page = BeautifulSoup(result.text, 'lxml')

browser = webdriver.Chrome()
browser.get("http://appcatalogo.ifema.es/waCatalogoWeb/index.html?feria=MF17&idioma=es&_ga=2.84562589.565538334.1608543158-1318591213.1608543158#LEMPRESAS&p=1&t=TODO&access&access&access&access&access&access")

element = browser.find_element_by_css_selector("label[class='tituloEmpresa']")
element.click()