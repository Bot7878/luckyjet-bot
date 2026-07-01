import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from scraper import get_results

TOKEN = os.getenv("BOT_TOKEN")

def analyze(data):
    if not data:
        return None

    avg = sum(data) / len(data)
    low = len([x for x in data if x < 2])
    high = len([x for x in data if x > 5])

    return avg, low, high

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot Lucky Jet actif sur Render")

async def last(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_results()
    await update.message.reply_text("\n".join([f"{x}x" for x in data]))

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_results()
    stats = analyze(data)

    if not stats:
        await update.message.reply_text("Pas de données")
        return

    avg, low, high = stats

    msg = f"""
📊 STATISTIQUES

Moyenne: {round(avg,2)}x
<2x : {low}
>5x : {high}
"""

    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("last", last))
    app.add_handler(CommandHandler("stats", stats))

    app.run_polling()

if __name__ == "__main__":
    main()
