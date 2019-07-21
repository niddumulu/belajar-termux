import os
import time
from config import *

seconds= float(0)
minutes= int(-1)
hours= int(0)

aiditele = input("Id telegram or group sasaran: ")
run = input("Ketik pass, dia : ")
while run.lower()=="dia":
  if seconds > 529:
      seconds = 0
      minutes = minutes+1      
      baris = minutes
      my_file = open("data.txt", "r")
      puisi = my_file.readlines()
      dataok = (puisi[baris])
      print (dataok)
      my_file.close()
      with TelegramClient('anon', api_id, api_hash) as client: client.send_message(aiditele,dataok)
      #print ('Pesan terkirim')
  if minutes > 8 :
     minutes = -1
     hours = hours+1
     
  os.system('clear')
  seconds = (seconds+1)
  #print (hours," : ",minutes," : ", seconds)
  print ("menunggu 530 detik ",seconds)
  time.sleep(1)
