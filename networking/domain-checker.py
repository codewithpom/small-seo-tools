
import socket
domains = [
  "google.com",
  "facebook.com",
  "notregisted.co",
  "replit.com",
  "hashnode.com",
  "gibberishjbjdgbjgb.com",
  "news.com",
  "me.com"
]
 

for domain in domains:
  try:
    # Query for socket information to connect to the domain
    addrInfo = socket.gethostbyname(domain)
    print(f"{domain} is not available! IP: {addrInfo}")
    
  except:
    print(f"{domain} is available!")




