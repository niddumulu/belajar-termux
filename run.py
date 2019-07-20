from config import *

#kirimpesan = input('Mau mengirim pesan apa? ')
#kirimke = input('Masukkan username atau group : ')

with TelegramClient('anon', api_id, api_hash) as client: client.send_message('niddumulu', "tokobaju")
#client.send_message('kirimke', kirimpesan)

print ('Pesan terkirim')
