from telethon.sync import TelegramClient 

api_id = 682610 
api_hash = '030132b51d598e464419ccee7f20212d' 

kirimpesan = input('Mau mengirim pesan apa? ')
kirimke = input('Masukkan username atau id group : ')

with TelegramClient('anon', api_id, api_hash) as client: client.send_message(kirimke, kirimpesan)
print ('Pesan terkirim')
