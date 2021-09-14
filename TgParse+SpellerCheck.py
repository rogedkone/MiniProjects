from telethon import TelegramClient, events
import requests
import re

TOKEN = "==paste=="
REGEXP = r"(?i)[А-Яа-яЁёСсЙй]+"

BOT_TOKEN = "==paste=="
rogedkone_id = "==paste=="

api_id = ==paste==
api_hash = '==paste=='
my_channel_id = "==paste=="
# CHANNEL = "==paste==" 
CHANNEL = "==paste=="
client = TelegramClient('anon', api_id, api_hash)
client.start()

send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + rogedkone_id + '&text=' + f"Бот Telegram запущен и исправно работает"
response = requests.get(send_text)

def yandexSpeller(data):
	text = re.findall(REGEXP, data.text)
	for i in text:
		response = requests.get("https://speller.yandex.net/services/spellservice/checkText",
								params={
									"text": i
								}
								)
		yandexRes = response.text
		if "error" in yandexRes:
			print(f"найдена ошибка в {i} отправляю Ирчику....")
			post_link = f"https://t.me/{CHANNEL}/{data.id}"
			send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + rogedkone_id + '&text=' + f"Привет. Кажется в слове {i} ошибка. Вот ссылка на пост {post_link}"
			response = requests.get(send_text)

@client.on(events.NewMessage(chats=(CHANNEL)))
async def normal_handler(event):
    messages = await client.get_messages(CHANNEL)
    data = messages[0]
    yandexSpeller(data)

client.run_until_disconnected()
