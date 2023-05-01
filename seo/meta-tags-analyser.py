import requests
from bs4 import BeautifulSoup



url = "https://replit.com"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')



seo_tags = [
  'title',
  'description',
  'keywords',
  'robots',
  'language',
  'author'
]

# meta_tags = soup.find_all("meta")
# print(meta_tags[0].attrs)



# SEO check
for seo_tag in seo_tags:
  value = soup.find('meta', {'name': seo_tag})
  
  if value:
    print(f"{seo_tag}: {value['content']}")
    print("\n")
  

twitter = []