import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("❌ BOT_TOKEN manquant")
    exit()

print("🤖 Bot en cours de démarrage...")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📩 /start reçu")
    await update.message.reply_text("🤖 Bot actif OK")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot lancé")
    app.run_polling()

if __name__ == "__main__":
    main()
