import telepot

token = "2134126588:AAEQSkgh5Y2zAxhu7zvOINfyw-zPT9rmrc8"
bot = telepot.Bot(token)

# 봇 정보 확인하기
# info = bot.getMe()
# pprint.pprint(info)#
# resp = bot.getUpdates()
# pprint.pprint(resp)

chat_id = 2102622767
bot.sendMessage(chat_id=chat_id, text="안녕 !!!")
