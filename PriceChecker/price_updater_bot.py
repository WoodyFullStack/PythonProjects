"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import Token
import price_getter
import price_processor
import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi')


def my_id(update, context):
    """Send a message when the command /my_id is issued."""
    update.message.reply_text(f' Твой id {update.message.chat_id}')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def price_check(context):
    items = price_processor.check_prices()
    if not items:
        context.bot.send_message(chat_id=Token.user_id, text="Prices doesn't changed")
    else:
        for item in range(len(items)):
            context.bot.send_message(chat_id=Token.user_id, text=items[item])
            context.bot.send_message(chat_id=593393716, text=items[item])


def favourites_list(update, context):
    items_list = price_getter.get_list_of_items('cart.txt')
    message = ''
    for item in items_list:
        message = message + item +'\n'
    update.message.reply_text(message)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(Token.Telegram_bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("my_id", my_id))
    dp.add_handler(CommandHandler("my_list", favourites_list))

    # on noncommand i.e. message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    j = updater.job_queue
    j.run_once(price_check, 10)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
