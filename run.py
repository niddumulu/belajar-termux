import os
import time
from config import *

seconds= float(0)
minutes= int(0)
hours= int(0)

run = input("Enter r : ")
while run.lower()=="r":
  if seconds > 540:
      seconds = 0
      minutes = minutes+1
      with TelegramClient('anon', api_id, api_hash) as client: client.send_message('dogetipbotgroup', "be active here guys")
      #print ('Pesan terkirim')     
  if minutes > 60:
     minutes = 0
     hours = hours+1
       
  os.system('clear')
  #from coba import *
  seconds = (seconds+1)
  #print (hours," : ",minutes," : ", seconds)
  print (seconds)
  time.sleep(1)
