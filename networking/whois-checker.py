import whois
url = "google.com"
data = whois.query(url)
print(data.__dict__)