import os
import time
import telebot
from telebot import types
from flask import Flask
import telebot.apihelper

# Настройки telebot: период жизни сессии (уменьшает шансы на ConnectionError)
telebot.apihelper.SESSION_TIME_TO_LIVE = 5

# Flask app (один экземпляр)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Бот работает!'

# Берём токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Ошибка: переменная окружения BOT_TOKEN не задана!")

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Словарь для хранения выбранного языка пользователями (в памяти)
user_language = {}

LANGS = {
    "EN": "🇬🇧 English",
    "RU": "🇷🇺 Русский",
    "AR": "🇸🇦 العربية",
    "HI": "🇮🇳 हिंदी",
    "BN": "🇧🇩 বাংলা"
}

TEXTS = {
    "start": {
        "EN": "Welcome! Please choose your language 🌐",
        "RU": "Добро пожаловать! Пожалуйста, выберите язык 🌐",
        "AR": "مرحبًا! يرجى اختيار لغتك 🌐",
        "HI": "स्वागत है! कृपया अपनी भाषा चुनें 🌐",
        "BN": "স্বাগতম! আপনার ভাষা নির্বাচন করুন 🌐",
    },
    "menu": {
        "EN": "Please choose an option:",
        "RU": "Пожалуйста, выберите действие:",
        "AR": "يرجى اختيار خيار:",
        "HI": "कृपया विकल्प चुनें:",
        "BN": "অনুগ্রহ করে একটি বিকল্প নির্বাচন করুন:",
    },
    "partner": {
        "EN": "To become a partner, follow the instructions...",
        "RU": "Чтобы стать партнёром, следуйте инструкциям...",
        "AR": "لتصبح شريكًا، اتبع التعليمات...",
        "HI": "साझेदार बनने के लिए, निर्देशों का पालन करें...",
        "BN": "পার্টনার হতে নির্দেশাবলী অনুসরণ করুন...",
    },
    "support": {
        "EN": "Contact support: @support",
        "RU": "Связаться с поддержкой: @support",
        "AR": "اتصل بالدعم: @support",
        "HI": "सहायता से संपर्क करें: @support",
        "BN": "সমর্থনের সাথে যোগাযোগ করুন: @support",
    },
    "verify": {
        "EN": "Enter manager username in format @USERNAME:",
        "RU": "Введите имя менеджера в формате @USERNAME:",
        "AR": "أدخل اسم المدير بتنسيق @USERNAME:",
        "HI": "@USERNAME फॉर्मेट में मैनेजर का नाम दर्ज करें:",
        "BN": "@USERNAME ফরম্যাটে ম্যানেজারের ইউজারনেম লিখুন:",
    },
    "valid": {
        "EN": "✅ This is our official manager. You can trust them.",
        "RU": "✅ Это наш менеджер, вы можете ему доверять.",
        "AR": "✅ هذا مدير رسمي. يمكنك الوثوق به.",
        "HI": "✅ यह हमारा आधिकारिक मैनेजर है।",
        "BN": "✅ এটি আমাদের অফিসিয়াল ম্যানেজার।",
    },
    "invalid": {
        "EN": "⛔ This is not our manager. Contact @support",
        "RU": "⛔ Это не наш менеджер. Свяжитесь с @support",
        "AR": "⛔ هذا ليس مديرنا. اتصل بـ @support",
        "HI": "⛔ यह हमारा मैनेजर नहीं है। @support से संपर्क करें",
        "BN": "⛔ এটি আমাদের ম্যানেজার নয়। যোগাযোগ করুন @support",
    }
}

# Список валидных менеджеров (пример)
valid_managers = ["@NAME"]

def get_lang(chat_id):
    return user_language.get(chat_id, "EN")

def main_menu(chat_id):
    lang = get_lang(chat_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ Become Partner", "💸 Be Payment Agent")
    markup.add("📞 Support", "🕵️ Verify Manager")
    markup.add("🌐 Change Language")
    bot.send_message(chat_id, TEXTS["menu"][lang], reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for code, name in LANGS.items():
        markup.add(name)
    # Показываем приветствие на языке по-умолчанию (EN) — пользователь затем выберет язык
    bot.send_message(msg.chat.id, TEXTS["start"]["EN"], reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in LANGS.values())
def set_language(msg):
    # устанавливаем язык пользователя
    lang_code = [k for k, v in LANGS.items() if v == msg.text][0]
    user_language[msg.chat.id] = lang_code
    main_menu(msg.chat.id)

@bot.message_handler(func=lambda m: True)
def menu_handler(msg):
    chat_id = msg.chat.id
    lang = get_lang(chat_id)
    t = msg.text or ""

    if "✅" in t:
        bot.send_message(chat_id, TEXTS["partner"][lang])
    elif "📞" in t:
        bot.send_message(chat_id, TEXTS["support"][lang])
    elif "🕵️" in t:
        bot.send_message(chat_id, TEXTS["verify"][lang])
    elif "🌐" in t:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for code, name in LANGS.items():
            markup.add(name)
        bot.send_message(chat_id, TEXTS["start"][lang], reply_markup=markup)
    elif t.startswith("@"):
        if t in valid_managers:
            bot.send_message(chat_id, TEXTS["valid"][lang])
        else:
            bot.send_message(chat_id, TEXTS["invalid"][lang])
    else:
        main_menu(chat_id)

# Flask "keep-alive" для Render (эндпоинт здоровья)
@app.route('/health')
def health():
    return "ok"

# Запуск polling (только при запуске через python main.py)
if __name__ == "__main__":
    print("✅ Бот запускается (polling)...")
    # Бесконечный цикл с авто-переподключением при ошибках сети
    while True:
        try:
            bot.infinity_polling(skip_pending=True, timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"⚠️ Ошибка соединения: {e}. Переподключаемся через 5s...")
            time.sleep(5)
