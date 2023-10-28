import os
import time
urls = [
  "smallseo.tools",
  "reddit.com",
  "vercel.com",
  "replit.com",
  "smallseotools.link",
  "smallseotools.com",
  "archive.org",
  "youtube.org",
  "etherscan.io",
  "namecheap.com",
  "godaddy.com",
  "smallpdf.com",
  "ilovepdf.com",
  "whatsapp.com"
]

csv = "Domain name,Registry Domain ID,Registrar WHOIS Server,Registrar URL,Updated Date,Creation Date,Registrar Registration Expiration Date,Registrar,Registrar IANA ID,Registrar Abuse Contact Email,Registrar Abuse Contact Phone,Reseller,Domain Status,Registry Registrant ID,Registrant Name,Registrant Organization,Registrant Street,Registrant City,Registrant State/Province,Registrant Postal Code,Registrant Country,Registrant Phone,Registrant Phone Ext,Registrant Fax,Registrant Fax Ext,Registrant Email,Registry Admin ID,Admin Name,Admin Organization,Admin Street,Admin City,Admin State/Province,Admin Postal Code,Admin Country,Admin Phone,Admin Phone Ext,Admin Fax,Admin Fax Ext,Admin Email,Registry Tech ID,Tech Name,Tech Organization,Tech Street,Tech City,Tech State/Province,Tech Postal Code,Tech Country,Tech Phone,Tech Phone Ext,Tech Fax,Tech Fax Ext,Tech Email,Name Server,Name Server\n"

for url in urls:
  os.system(f"whois -h $(whois {url} | grep 'Registrar WHOIS Server:' | cut -f2- -d:) {url} > whois.txt")
  
  data = open("whois.txt").read()
  lines = data.split("\n")
  usefull_data = {}
  csv_line = ""
  for line in lines:
    if ":" not in line:
      continue
      

      
    if "[Querying " in line:
      continue
  
    if "DNSSEC: " in line:
      break
      
    key = line.split(":")[0]
    value = ":".join(line.split(":")[1:]).strip()
    print(f"{key}: {value}")
    usefull_data[key] = value
    csv_line = csv_line + f'"{value}",'

  csv = csv + csv_line + "\n"
  
  print("-" * 80)
  time.sleep(1)
csv_file = open("whois.csv", "w")
csv_file.write(csv)
csv_file.close()  
