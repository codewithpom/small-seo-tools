import requests


def google_search(keyword, key, engine_id, page_token, limit):
  url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={engine_id}&q={keyword}&start={page_token}&num={limit}"
  response = requests.get(url)
  search_results = response.json()
  return search_results

def rank_checker(keyword, site, key, code):
  rank = None
  j = 0
  for i in range(1, 6):
    items  = google_search(keyword, key, code, i, 10)['items']
    for item in items:
      j += 1
      if item['displayLink'] == site:
        rank = j
        break
        
  return rank
