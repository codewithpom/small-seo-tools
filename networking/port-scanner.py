import socket 
import threading
import time


file = open("port-scanning-results.txt", 'w')
file.write("")
file.close()

most_common_ports = open("1000-most-common-ports.txt").read().split(",")
target = "github.com"   # scan github
def port_scanner(port):
  try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(1)
      s.connect((target, port))
      print(f"Port {port} is open")
      while True:
        try:
          file = open("port-scanning-results.txt", 'a')
          file.write(str(port) + "\n")
          file.close()
          break
          
        except Exception:
          time.sleep(2)
          continue
  except:
      pass

  # print("Thread ended")
  return  

for port in most_common_ports:

  while True:
    try:
      thread = threading.Thread(target=port_scanner, args=[int(port)])
      thread.start()
      break
      
    except Exception as e:
      time.sleep(1)
      print(e)
      continue


print("Created all threads!")