from telethon.sync import TelegramClient 

api_id = api 
api_hash = 'apihash' 

kirimpesan = input('Mau mengirim pesan apa? ')
print ('Pesan terkirim yaitu : ' + kirimpesan)
pesan = kirimpesan

with TelegramClient('anon', api_id, api_hash) as client: client.send_message('niddumulu', pesan)