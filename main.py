from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, Filters, MessageHandler

button_help = 'Помогу по понятиям'

def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='А вот и кореша на помощь спешат!',
        reply_markup = ReplyKeyboardRemove(),
    )


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context= context)
    reply_markup =ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
            ],
        ],
        resize_keyboard=True
    )

    update.message.reply_text(
        text='Здорова, бандит! Тыкай на кнопку снизу! Будет четко!',
        reply_markup=reply_markup,
    )

def main():
    updater = Updater(
        token='1519801549:AAEpCGgq4F4O2QAKG1QOn01c5hPlQc4H1rw',
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    main()