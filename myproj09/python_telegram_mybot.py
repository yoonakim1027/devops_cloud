from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import tasks

token = "2134126588:AAEQSkgh5Y2zAxhu7zvOINfyw-zPT9rmrc8"
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="안녕. 나는 yoonakim1027bot이야. 만나서 반가워."
    )


# 하나의 함수는 하나의 기능만 하도록 구성하는 것이 좋음
def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [
        tasks.get_current_lotto_numbers,
        tasks.ya,
        tasks.naver_search,
        tasks.predict_lotto_numbers,
        tasks.numbers_Add,
        tasks.reverse_string,
    ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
    else:
        response_text = "지원하지 않는 명령입니다."


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
