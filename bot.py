import logging
import os
from telegram import Update, error
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
from video_splitter import Video_splitter
import settings

vs = Video_splitter()

## to do
# host bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start bot"""
    user = update.message.from_user
    logger.info("%s started the bot", user.first_name.title())
    await update.message.reply_text(
        "I am Video Splitter. Send a video. Split size is 30 seconds."
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message to bot."""
    user = update.message.from_user
    message = f"""
	Hello {user.first_name}, welcome to Video Splitter by @yaw_o_k .
	Commands:
	/start : Start the bot
	/help : Show this information
	/split_size (args: seconds): Change split size seconds. eg "/split_size 5" ie. Changes split size from 30 seconds(default) to 5 seconds
    """
    logger.info("%s started the bot", user.first_name.title())
    await update.message.reply_text(message)
