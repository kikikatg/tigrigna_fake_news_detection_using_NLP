from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    CallbackQueryHandler,
)

import requests
import asyncio
import os

# ✅ NEW (for web service)
from fastapi import FastAPI, Request

# ==========================================
# CONFIG
# ==========================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://tigrigna-fake-news-detection-using-nlp-1.onrender.com/predict"

# ==========================================
# FASTAPI APP (NEW)
# ==========================================
app_web = FastAPI()

# ==========================================
# TELEGRAM APP (SAME)
# ==========================================
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()


# ==========================================
# MAIN KEYBOARD (REUSABLE)
# ==========================================
def main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🧠 Analyze News", callback_data="analyze"),
            InlineKeyboardButton("📊 History", callback_data="history"),
        ],
        [
            InlineKeyboardButton("🗑 Clear History", callback_data="clear"),
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


# ==========================================
# HELP (REUSABLE)
# ==========================================
def get_help_text():
    return """
🤖 TIGRIGNA FAKE NEWS AI DETECTOR - HELP

WHAT THIS BOT DOES
- Detects Fake or Real news
- Uses Machine Learning + NLP model

HOW TO USE
1. Send any Tigrigna news text
2. Wait for prediction
3. Get result instantly

EXAMPLE
መንግስቲ ሓድሽ ፕሮጀክት ኣጀሚሩ

RESULTS YOU GET
- Fake or Real label
- Confidence score (%)
- Risk level
- Model information

FEATURES
- Fake News Detection
- Confidence Visualization
- History Tracking
- AI Risk Analysis

TIP
Send full news text for better accuracy.
"""


# ==========================================
# START COMMAND
# ==========================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🤖 TIGRIGNA FAKE NEWS AI DETECTOR

Welcome!

Send any news text and I will analyze it:
✅ Real or Fake
📊 Confidence score
⚠️ Risk level
""",
        reply_markup=main_keyboard(),
    )


# ==========================================
# HELP COMMAND
# ==========================================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_help_text(), reply_markup=main_keyboard())


# ==========================================
# PREDICTION FUNCTION
# ==========================================
async def predict_news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_text = update.message.text
    loading = await update.message.reply_text("⏳ Analyzing news...")

    try:
        response = requests.post(
            API_URL,
            json={"text": user_text},
            timeout=120,
        )

        print("STATUS CODE:", response.status_code)
        print("RAW RESPONSE:", response.text)

        if response.status_code != 200:
            await loading.edit_text(
                f"⚠️ Backend Error\n\nStatus: {response.status_code}",
                reply_markup=main_keyboard(),
            )
            return

        try:
            result = response.json()
        except Exception:
            await loading.edit_text(
                "⚠️ Invalid response from backend server.",
                reply_markup=main_keyboard(),
            )
            return

        label = result.get("label", "Unknown")
        confidence = result.get("confidence", 0)
        risk = result.get("risk_level", "Unknown")
        model = result.get("model_used", "AI Model")

        emoji = "🚨" if label.upper() == "FAKE" else "✅"

        bar_length = int(confidence // 10)
        bar = "█" * bar_length + "░" * (10 - bar_length)

        message = f"""
{emoji} *Prediction Result*

📰 News: {label}

📊 Confidence: {confidence}%
[{bar}]

⚠️ Risk: {risk}

🧠 Model: {model}
"""

        await loading.edit_text(
            message,
            parse_mode="Markdown",
            reply_markup=main_keyboard(),
        )

    except Exception as e:
        print("PREDICTION ERROR:", e)
        await loading.edit_text(
            f"❌ Error: {str(e)}",
            reply_markup=main_keyboard(),
        )


# ==========================================
# BUTTON HANDLER
# ==========================================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "help":
        await query.edit_message_text(
            get_help_text(),
            reply_markup=main_keyboard(),
        )

    elif data == "history":
        try:
            res = requests.get(
                "https://tigrigna-fake-news-detection-using-nlp-1.onrender.com/history",
                timeout=30,
            )

            if res.status_code != 200:
                raise Exception("Backend API failed")

            data_json = res.json()
            history = data_json.get("results", [])

            if not history:
                await query.edit_message_text(
                    "📭 No prediction history found.",
                    reply_markup=main_keyboard(),
                )
                return

            text = "📊 *Recent Predictions*\n\n"

            for item in history:
                emoji = "🚨" if item["label"].upper() == "FAKE" else "✅"

                text += (
                    f"{emoji} *{item['label']}*\n"
                    f"📊 Confidence: {item['confidence']}%\n"
                    f"⚠️ Risk: {item['risk_level']}\n"
                    f"🕒 {item['created_at']}\n\n"
                )

            await query.edit_message_text(
                text,
                parse_mode="Markdown",
                reply_markup=main_keyboard(),
            )

        except Exception as e:
            print("HISTORY ERROR:", e)
            await query.edit_message_text(
                "⚠️ Failed to load history",
                reply_markup=main_keyboard(),
            )

    elif data == "clear":
        try:
            requests.delete(
                "https://tigrigna-fake-news-detection-using-nlp-1.onrender.com/history"
            )
            await query.edit_message_text(
                "🗑 History cleared successfully!",
                reply_markup=main_keyboard(),
            )
        except Exception as e:
            print("CLEAR ERROR:", e)
            await query.edit_message_text(
                "⚠️ Failed to clear history",
                reply_markup=main_keyboard(),
            )

    elif data == "analyze":
        await query.edit_message_text(
            "📩 Send me a news text to analyze.",
            reply_markup=main_keyboard(),
        )


# ==========================================
# REGISTER HANDLERS (NEW LOCATION)
# ==========================================
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, predict_news))
telegram_app.add_handler(CallbackQueryHandler(button_handler))


# ==========================================
# WEBHOOK ROUTE (NEW)
# ==========================================
@app_web.post(f"/{BOT_TOKEN}")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}


# ==========================================
# HEALTH CHECK (NEW)
# ==========================================
@app_web.get("/")
def home():
    return {"message": "Bot is running"}


# ==========================================
# STARTUP (SET WEBHOOK)
# ==========================================
@app_web.on_event("startup")
async def on_startup():
    webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{BOT_TOKEN}"
    await telegram_app.bot.set_webhook(webhook_url)
    print("Webhook set to:", webhook_url)
