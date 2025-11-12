import os
import telebot
from telebot import types
from flask import Flask

# Берём токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Ошибка: переменная окружения BOT_TOKEN не задана!")

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Инициализация Flask для keep-alive на Render
app = Flask(__name__)

# Словарь для хранения выбранного языка пользователями
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
        "EN": "Create your account using the link:\nhttps://888starz-main.in/registration\n\nSend your email to your manager or contact the head manager.\n\nTelegram: @miles888starzz",
        "RU": "Создайте свой аккаунт по ссылке:\nhttps://888starz-main.in/registration\n\nОтправьте вашу почту менеджеру или свяжитесь с главным менеджером.\n\nTelegram: @miles888starzz",
        "AR": "أنشئ حسابك عبر الرابط:\nhttps://888starz-main.in/registration\n\nأرسل بريدك الإلكتروني إلى مديرك أو اتصل بالمدير الرئيسي.\n\nTelegram: @miles888starzz",
        "HI": "इस लिंक से अपना अकाउंट बनाएं:\nhttps://888starz-main.in/registration\n\nअपना ईमेल अपने मैनेजर को भेजें या मुख्य मैनेजर से संपर्क करें।\n\nTelegram: @miles888starzz",
        "BN": "এই লিঙ্ক দিয়ে আপনার অ্যাকাউন্ট তৈরি করুন:\nhttps://888starz-main.in/registration\n\nআপনার ইমেইল আপনার ম্যানেজারকে পাঠান অথবা প্রধান ম্যানেজারের সাথে যোগাযোগ করুন।\n\nTelegram: @miles888starzz",
    },
    "support": {
        "EN": "Support contacts:\nTelegram: @miles888starzz\nEmail: support@example.com\nWhatsApp: +777127381239",
        "RU": "Контакты поддержки:\nTelegram: @miles888starzz\nEmail: support@example.com\nWhatsApp: +777127381239",
        "AR": "دعم العملاء:\nTelegram: @miles888starzz\nEmail: support@example.com\nWhatsApp: +777127381239",
        "HI": "सपोर्ट संपर्क:\nTelegram: @miles888starzz\nEmail: support@example.com\nWhatsApp: +777127381239",
        "BN": "সাপোর্ট যোগাযোগ:\nTelegram: @miles888starzz\nEmail: support@example.com\nWhatsApp: +777127381239",
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
        "EN": "⛔ This is not our manager. Contact @Nazar_by_Couture",
        "RU": "⛔ Это не наш менеджер. Свяжитесь с @Nazar_by_Couture",
        "AR": "⛔ هذا ليس مديرنا. اتصل بـ @Nazar_by_Couture",
        "HI": "⛔ यह हमारा मैनेजर नहीं है। @Nazar_by_Couture से संपर्क करें",
        "BN": "⛔ এটি আমাদের ম্যানেজার নয়। যোগাযোগ করুন @Nazar_by_Couture",
    }
}

valid_managers = ["@vladtvc", "@Nazar_by_Couture", "@miles888starzz"]

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
    bot.send_message(msg.chat.id, TEXTS["start"]["EN"], reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in LANGS.values())
def set_language(msg):
    lang_code = [k for k, v in LANGS.items() if v == msg.text][0]
    user_language[msg.chat.id] = lang_code
    main_menu(msg.chat.id)

@bot.message_handler(func=lambda m: True)
def menu_handler(msg):
    chat_id = msg.chat.id
    lang = get_lang(chat_id)
    t = msg.text

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

# Flask "keep-alive" для Render
@app.route('/')
def home():
    return "Bot is running!"

import threading
threading.Thread(target=lambda: bot.infinity_polling(skip_pending=True, timeout=10)).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
