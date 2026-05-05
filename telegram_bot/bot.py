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

# ==========================================
# CONFIG
# ==========================================
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://tigrigna-fake-news-detection-using-nlp-1.onrender.com/predict"


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
# HElP (REUSABLE)
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
        response = requests.post(API_URL, json={"text": user_text}, timeout=60)
        result = response.json()

        print("BACKEND RESPONSE:", result)

        # ERROR HANDLING
        if "detail" in result:
            await loading.edit_text(
                f"⚠️ {result['detail']}", reply_markup=main_keyboard()
            )
            return

        label = result.get("label", "Unknown")
        confidence = result.get("confidence", 0)
        risk = result.get("risk_level", "Unknown")
        model = result.get("model_used", "AI Model")

        emoji = "🚨" if label.upper() == "FAKE" else "✅"

        # CONFIDENCE BAR
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

        # 🔥 IMPORTANT FIX: ADD BUTTONS HERE TOO
        await loading.edit_text(
            message, parse_mode="Markdown", reply_markup=main_keyboard()
        )

    except Exception as e:
        await loading.edit_text(f"❌ Error: {str(e)}", reply_markup=main_keyboard())


# ==========================================
# BUTTON HANDLER
# ==========================================
# ==========================================
# BUTTON HANDLER
# ==========================================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # ==========================================
    # HELP
    # ==========================================
    if data == "help":

        await query.edit_message_text(
            get_help_text(),
            reply_markup=main_keyboard(),
        )

    # ==========================================
    # HISTORY
    # ==========================================
    elif data == "history":

        try:

            res = requests.get(
                "https://tigrigna-fake-news-detection-using-nlp-1.onrender.com/history",
                timeout=30,
            )

            # CHECK STATUS
            if res.status_code != 200:
                raise Exception("Backend API failed")

            # JSON RESPONSE
            data_json = res.json()

            # GET RESULTS
            history = data_json.get("results", [])

            # EMPTY HISTORY
            if not history:

                await query.edit_message_text(
                    "📭 No prediction history found.",
                    reply_markup=main_keyboard(),
                )

                return

            # MESSAGE
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

    # ==========================================
    # CLEAR HISTORY
    # ==========================================
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

    # ==========================================
    # ANALYZE
    # ==========================================
    elif data == "analyze":

        await query.edit_message_text(
            "📩 Send me a news text to analyze.",
            reply_markup=main_keyboard(),
        )


# ==========================================
# MAIN FUNCTION
# ==========================================
def main():

    print("🤖 Advanced Telegram Bot Running...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, predict_news))

    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
