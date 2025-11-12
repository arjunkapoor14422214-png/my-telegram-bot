import telebot
from telebot import types

BOT_TOKEN = "7859887919:AAGKKu1OXB7w9bXjKdS_EkQ8daWSYPgans8"

bot = telebot.TeleBot(BOT_TOKEN)

user_language = {}

LANGS = {
    "EN": "🇬🇧 English",
    "RU": "🇷🇺 Русский",
    "AR": "🇸🇦 العربية",
    "HI": "🇮🇳 हिंदी",
    "BN": "🇧🇩 বাংলা"
}

# Тексты
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
        "EN": "Create your account using the link:\nhttps://888starz-main.in/registration\n\nSend your email to your manager, or if you don't have one, contact our head manager for further assistance.\n\nTelegram: @miles888starzz",
        "RU": "Создайте свой аккаунт по ссылке:\nhttps://888starz-main.in/registration\n\nОтправьте вашу почту вашему менеджеру или, если его нет, свяжитесь с нашим главным менеджером.\n\nTelegram: @miles888starzz",
        "AR": "أنشئ حسابك عبر الرابط:\nhttps://888starz-main.in/registration\n\nأرسل بريدك الإلكتروني إلى مديرك، أو إذا لم يكن لديك، فاتصل بمديرنا الرئيسي.\n\nTelegram: @miles888starzz",
        "HI": "इस लिंक से अपना अकाउंट बनाएं:\nhttps://888starz-main.in/registration\n\nअपना ईमेल अपने मैनेजर को भेजें या यदि आपके पास मैनेजर नहीं है तो हमारे मुख्य मैनेजर से संपर्क करें।\n\nTelegram: @miles888starzz",
        "BN": "এই লিঙ্ক দিয়ে আপনার অ্যাকাউন্ট তৈরি করুন:\nhttps://888starz-main.in/registration\n\nআপনার ইমেইল আপনার ম্যানেজারকে পাঠান অথবা যদি ম্যানেজার না থাকে তাহলে আমাদের প্রধান ম্যানেজারের সাথে যোগাযোগ করুন।\n\nTelegram: @miles888starzz",
    },
    "agent_choose": {
        "EN": "Choose agent type:",
        "RU": "Выберите тип агента:",
        "AR": "اختر نوع الوكيل:",
        "HI": "एजेंट प्रकार चुनें:",
        "BN": "এজেন্টের ধরন নির্বাচন করুন:",
    },
    "agent_bank": {
        "EN": """Please provide the following information:

1. Full name:
2. Date of birth:
3. NID number:
4. Current location:
5. Wallets (geos) for payments:
6. Weekly volumes through bank:
7. Ready for advance payment in two parts:
8. Ensure 24/7 availability:
9. Attach NID photos and selfie.

Send this information to: @miles888starzz""",
        "RU": """Пожалуйста, предоставьте следующую информацию:

1. ФИО:
2. Дата рождения:
3. Номер NID:
4. Текущее местоположение:
5. Кошельки для платежей:
6. Еженедельные объемы через банк:
7. Готовы сделать предоплату в два этапа:
8. Обеспечите доступность 24/7:
9. Прикрепите фото NID и селфи.

Отправьте эту информацию: @miles888starzz""",
        "AR": """يرجى تقديم المعلومات التالية:

1. الاسم الكامل:
2. تاريخ الميلاد:
3. رقم الهوية:
4. الموقع الحالي:
5. المحافظ للمدفوعات:
6. الأحجام الأسبوعية عبر البنك:
7. هل أنت مستعد للدفع المسبق على جزأين:
8. ضمان التوفر 24/7:
9. أرفق صور الهوية وصورة شخصية.

أرسل هذه المعلومات إلى: @miles888starzz""",
        "HI": """कृपया निम्न जानकारी दें:

1. पूरा नाम:
2. जन्म तिथि:
3. NID नंबर:
4. वर्तमान स्थान:
5. भुगतान के लिए वॉलेट्स:
6. बैंक के माध्यम से साप्ताहिक वॉल्यूम:
7. दो हिस्सों में अग्रिम भुगतान के लिए तैयार:
8. 24/7 उपलब्धता सुनिश्चित करें:
9. NID फोटो और सेल्फी संलग्न करें।

यह जानकारी भेजें: @miles888starzz""",
        "BN": """অনুগ্রহ করে নিম্নলিখিত তথ্য প্রদান করুন:

1. পুরো নাম:
2. জন্ম তারিখ:
3. NID নম্বর:
4. বর্তমান অবস্থান:
5. পেমেন্টের জন্য ওয়ালেট:
6. ব্যাংকের মাধ্যমে সাপ্তাহিক ভলিউম:
7. দুই অংশে অগ্রিম প্রদানের জন্য প্রস্তুত:
8. 24/7 উপলব্ধতা নিশ্চিত করুন:
9. NID ছবি এবং সেলফি সংযুক্ত করুন।

এই তথ্য পাঠান: @miles888starzz"""
    },
    "agent_mobcash": {
        "EN": "Hello! Fill out the form to create MobCash account. Then send your account ID to your manager or main manager.\nTelegram: @miles888starzz",
        "RU": "Здравствуйте! Заполните форму для создания MobCash аккаунта. Затем отправьте ID аккаунта вашему менеджеру или главному менеджеру.\nTelegram: @miles888starzz",
        "AR": "مرحبًا! املأ النموذج لإنشاء حساب MobCash. ثم أرسل معرف الحساب إلى مديرك أو المدير الرئيسي.\nTelegram: @miles888starzz",
        "HI": "नमस्ते! MobCash अकाउंट बनाने के लिए फॉर्म भरें। फिर अपना अकाउंट ID अपने मैनेजर या मुख्य मैनेजर को भेजें।\nTelegram: @miles888starzz",
        "BN": "হ্যালো! MobCash অ্যাকাউন্ট তৈরি করতে ফর্ম পূরণ করুন। তারপর আপনার অ্যাকাউন্ট ID আপনার ম্যানেজার বা প্রধান ম্যানেজারের কাছে পাঠান।\nTelegram: @miles888starzz"
    },
    "support": {
        "EN": "Support contacts:\nTelegram: @miles888starzz\nEmail: huihuihui@gmail.com\nWhatsApp: +777127381239",
        "RU": "Контакты поддержки:\nTelegram: @miles888starzz\nEmail: huihuihui@gmail.com\nWhatsApp: +777127381239",
        "AR": "دعم العملاء:\nTelegram: @miles888starzz\nEmail: huihuihui@gmail.com\nWhatsApp: +777127381239",
        "HI": "सपोर्ट संपर्क:\nTelegram: @miles888starzz\nEmail: huihuihui@gmail.com\nWhatsApp: +777127381239",
        "BN": "সাপোর্ট যোগাযোগ:\nTelegram: @miles888starzz\nEmail: huihuihui@gmail.com\nWhatsApp: +777127381239",
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
        "HI": "✅ यह हमारा आधिकारिक मैनेजर है। आप उन पर भरोसा कर सकते हैं।",
        "BN": "✅ এটি আমাদের অফিসিয়াল ম্যানেজার। আপনি তাকে বিশ্বাস করতে পারেন।",
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
    markup.add(
        "✅ " + ("Become Partner" if lang=="EN" else TEXTS["partner"][lang][:20]+"..."),
        "💸 " + ("Be Payment Agent" if lang=="EN" else TEXTS["agent_choose"][lang])
    )
    markup.add(
        "📞 " + ("Support" if lang=="EN" else TEXTS["support"][lang][:20]+"..."),
        "🕵️ " + ("Verify Manager" if lang=="EN" else TEXTS["verify"][lang][:20]+"...")
    )
    markup.add("🌐 " + ("Change Language" if lang=="EN" else TEXTS["start"][lang][:20]+"..."))

    bot.send_message(chat_id, TEXTS["menu"][lang], reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for code, name in LANGS.items():
        markup.add(name)
    bot.send_message(msg.chat.id, TEXTS["start"]["EN"], reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in LANGS.values())
def set_language(msg):
    lang_code = [k for k,v in LANGS.items() if v == msg.text][0]
    user_language[msg.chat.id] = lang_code
    main_menu(msg.chat.id)

@bot.message_handler(func=lambda m: True)
def menu_handler(msg):
    chat_id = msg.chat.id
    lang = get_lang(chat_id)
    t = msg.text

    if "✅" in t: 
        bot.send_message(chat_id, TEXTS["partner"][lang])
        return
    if "💸" in t:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("🏦 Bank-transfer", "📱 MobCash")
        markup.add("⬅️ Back")
        bot.send_message(chat_id, TEXTS["agent_choose"][lang], reply_markup=markup)
        return
    if "📞" in t: 
        bot.send_message(chat_id, TEXTS["support"][lang])
        return
    if "🕵️" in t: 
        bot.send_message(chat_id, TEXTS["verify"][lang])
        return
    if "🌐" in t:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for code, name in LANGS.items(): 
            markup.add(name)
        bot.send_message(chat_id, TEXTS["start"][lang], reply_markup=markup)
        return
    if "🏦" in t: 
        bot.send_message(chat_id, TEXTS["agent_bank"][lang])
        return
    if "📱" in t: 
        bot.send_message(chat_id, TEXTS["agent_mobcash"][lang])
        return
    if "⬅️" in t:
        main_menu(chat_id)
        return
    if t.startswith("@"):
        if t in valid_managers: 
            bot.send_message(chat_id, TEXTS["valid"][lang])
        else: 
            bot.send_message(chat_id, TEXTS["invalid"][lang])
        main_menu(chat_id)
        return

bot.infinity_polling()
