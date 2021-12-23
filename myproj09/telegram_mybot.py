token = "여기에 봇 토근을 넣으세요"
bot = telepot.Bot(token)

info = bot.getMe()
pprint.pprint(info)