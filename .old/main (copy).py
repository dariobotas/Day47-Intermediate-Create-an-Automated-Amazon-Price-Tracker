import lxml
import requests
import requests_html as rhtml
from bs4 import BeautifulSoup
#from selenium import webdriver

URL = "https://www.pcdiga.com/portatil-asus-zenbook-15-oled-um3504da-r77bohdcb1-90nb1163-m00dk0-4711387272008/"#"https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"#"https://www.amazon.com/Apple-2022-MacBook-512GB-Storage/dp/B0BB8SK52N/ref=psdc_565108_t1_B0BB8BHKB8/"#?language=pt_BR&currency=EUR"

header = {
  "Use-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}
#dr = webdriver.Chrome()
#dr.get(URL)

req = requests.Session()
response = req.get(URL, headers=header)
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

#price_element = soup.select_one("span.a-offscreen")
price_element = soup.find("div", 
                          class_=("text-primary","text-2xl.md:text-3xl","font-black"))
print(price_element)
#price_article = price_element
#price_without_curr = price_element.split("EUR")[1]
#price_as_float = price_without_curr.replace(",", ".")
#price = float(price_without_curr)
#print(price)

#print("Element not found!")