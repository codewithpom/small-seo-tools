import re
import smtplib
import dns.resolver
import random
import string
import time

def random_email():
  allowed_chars = string.ascii_letters
  
  return (''.join(random.choice(allowed_chars) for x in range(10))).lower()

# Address used for SMTP MAIL FROM command.
fromAddress = 'test@example.com'

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

def check_mail(addr):
  # Syntax check
  match = re.match(regex, addr)
  if match == None:
     return None
  
  # Get domain for DNS lookup
  splitAddress = addr.split('@')
  domain = str(splitAddress[1])
  # print('Domain:', domain)
  
  # MX record lookup
  records = dns.resolver.resolve(domain, 'MX')
  mxRecord = records[0].exchange
  mxRecord = str(mxRecord)
  
  
  # SMTP lib setup (use debug level for full output)
  server = smtplib.SMTP()
  server.set_debuglevel(0)
  
  # SMTP Conversation
  server.connect(mxRecord)
  server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
  server.mail(fromAddress)
  code, message = server.rcpt(str(addr))
  server.quit()
  return code

  
#print(code)
#print(message)


  
emails = [
  "hvdntwjeacrkjfnwzc@tmmbt.com", # temproray emails
  "padmashreejha717@gmail.com", # My personal Email
  "codewithpom@gmail.com", # My developer email
]

for addr in emails:
  code = check_mail(random_email() + "@" + addr.split("@")[1])
  if code == 250:
    print(f"{addr} is a temproray email!")
    
  else:
    code = check_mail(addr)
    if code == 250:
      print(f"{addr} is a nice email!!")
      
    else:
      print(f"{addr} does not exist!!")
    
  time.sleep(1)
