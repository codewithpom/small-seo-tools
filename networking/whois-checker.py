import whois
url = "google.com"
data = whois.query(url).__dict__
for key in data.keys():
  print(f"{key} : {data[key]}")