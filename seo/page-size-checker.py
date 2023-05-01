import requests

urls = [
  "https://smallseo.tools/",
  "http://ipv4.download.thinkbroadband.com/512MB.zip",
  "https://github.com",
  "https://twitter.com",
  "https://twitter.com/PadmashreeJha",
  "https://github.com/codewithpom",
  "https://ipfs.tech",
  "https://replit.com",
  "https://ShouldNotExistAsItIsGibbrish.com"
]


file = open("page-size-checking-results.csv", 'w')
file.write("URL, Bytes, Kilo Bytes, Mega Bytes\n")
file.close()


for url in urls:
  try:
    # Make an HTTP HEAD request to the URL
    response = requests.head(url, allow_redirects=True)
    
  except Exception:
    pass
  
  # print(response.headers)
  try:
    # Get the size of the response in bytes
    size_bytes = int(response.headers["Content-Length"])
  except Exception:

    try:
      size_bytes = len(requests.get(url, timeout=2, allow_redirects=True).content)
    except Exception:
      continue

  
  # Convert the size to kilobytes
  size_kb = size_bytes / 1024
  
  # Convert the size to megabytes
  size_mb = size_kb / 1024
  file = open("page-size-checking-results.csv", 'a')
  file.write(f'"{url}","{size_bytes}","{size_kb}","{size_mb}"\n')
  file.close()
  print(f"The size of the HTML page at {url} is {size_mb} MB")
  