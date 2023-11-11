import requests
import requests_html as rhtml
from bs4 import BeautifulSoup
#from selenium import webdriver
import step1.main as st

st.run()

URL = "https://www.pcdiga.com/portatil-asus-zenbook-15-oled-um3504da-r77bohdcb1-90nb1163-m00dk0-4711387272008"

header = {
  "Use-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}
doc = """<a class="mt-1 h-8 text-xs font-bold duration-150 rounded-md cursor-pointer md:h-12 with-tab md:text-base-sm md:leading-6 line-clamp-2 hover:text-primary" href="/portatil-asus-zenbook-15-oled-um3504da-r77bohdcb1-90nb1163-m00dk0-4711387272008">"""

try:
  #req = requests.Session()
  response = requests.get(URL)
  soup1 = BeautifulSoup(response.text, 'html.parser')
  dynamic_content_url = soup1.find('script',
                                  {'class': 'dynamic-content'})#.get('src')
  response1 = requests.get(dynamic_content_url)
  data=response1.json()
  print(data)
  #print(soup1.prettify())
  #print()
  #print()
  session = rhtml.HTMLSession()
  response = session.get(URL)
  soup = BeautifulSoup(response.html.raw_html, features="lxml")
  #print(soup)
  #title = response.html.render()
  #print(title.find('link'))
except requests.exceptions.RequestException as e:
  print(e)
#session = rhtml.HTML(html=doc)#HTMLSession()
#print(session.links)
#response = session.get(URL, headers=header)
#print(response.html.render())#find("#body-overlay > div.flex.flex-col.justify-between.min-h-screen.z-1 > div.z-1.base-container.py-5.bg-background.pb-28.flex-grow > main > div.grid.items-start.w-full.lg\:grid-cols-product-page.gap-x-6 > div.max-w-full.mt-6 > div.p-4.bg-background-off.rounded-md.grid.gap-y-4 > div:nth-child(5) > div > div > div.flex.gap-x-4.items-center > div", first=True))
#response.html.render(sleep=1)
#soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

#price_element = soup.select("div.text-primary")
#print(price_element)