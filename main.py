import telebot
from telebot import types
import json
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Логгирование ошибок в файл
logging.basicConfig(filename='errors.log', level=logging.ERROR)

DEBTS_FILE = "debts.json"
if os.path.exists(DEBTS_FILE):
    with open(DEBTS_FILE, "r") as f:
        debts = json.load(f)
else:
    debts = []

users = {}

def save_debts():
    with open(DEBTS_FILE, "w") as f:
        json.dump(debts, f, ensure_ascii=False, indent=2)

def get_user_name(user):
    return user.username if user.username else f"{user.first_name}"

@bot.message_handler(commands=["start"])
def send_welcome(message):
    users[message.chat.id] = get_user_name(message.from_user)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("/owe"),
        types.KeyboardButton("/debts"),
        types.KeyboardButton("/credits"),
        types.KeyboardButton("/help")
    )
    bot.send_message(message.chat.id, "Привет! Я бот для учёта долгов. Используй кнопки ниже или команды.", reply_markup=markup)

@bot.message_handler(commands=["help"])
def show_help(message):
    help_text = """
Я помогу тебе вести учёт долгов. Вот что я умею:

/owe @username сумма — создать долг пользователю
/confirm долг_ID — подтвердить долг
/reject долг_ID — отклонить долг
/paid долг_ID — отметить долг как оплаченный
/debts — список долгов, которые ты должен
/credits — список долгов, которые должны тебе
/help — показать это сообщение
"""
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=["owe"])
def add_debt(message):
    parts = message.text.split()
    if len(parts) != 3 or not parts[2].isdigit():
        bot.send_message(message.chat.id, "Формат: /owe @username сумма")
        return

    to_user = parts[1].lstrip("@")
    amount = int(parts[2])
    from_user = get_user_name(message.from_user)

    for d in debts:
        if d["from"] == from_user and d["to"] == to_user and d["amount"] == amount and d["status"] == "pending":
            bot.send_message(message.chat.id, "Такой долг уже существует и ожидает подтверждения.")
            return

    debt_id = len(debts) + 1
    debts.append({
        "id": debt_id,
        "from": from_user,
        "to": to_user,
        "amount": amount,
        "status": "pending"
    })
    save_debts()
    bot.send_message(message.chat.id, f"Долг создан и ожидает подтверждения получателем.\nID: {debt_id}")

@bot.message_handler(commands=["confirm"])
def confirm_debt(message):
    parts = message.text.split()
    if len(parts) != 2 or not parts[1].isdigit():
        bot.send_message(message.chat.id, "Формат: /confirm долг_ID")
        return

    debt_id = int(parts[1])
    username = get_user_name(message.from_user)

    for d in debts:
        if d["id"] == debt_id and d["to"] == username and d["status"] == "pending":
            d["status"] = "confirmed"
            save_debts()
            bot.send_message(message.chat.id, "Долг подтверждён.")
            return

    bot.send_message(message.chat.id, "Такого долга не найдено или вы не получатель.")

@bot.message_handler(commands=["reject"])
def reject_debt(message):
    parts = message.text.split()
    if len(parts) != 2 or not parts[1].isdigit():
        bot.send_message(message.chat.id, "Формат: /reject долг_ID")
        return

    debt_id = int(parts[1])
    username = get_user_name(message.from_user)

    for d in debts:
        if d["id"] == debt_id and d["to"] == username and d["status"] == "pending":
            d["status"] = "rejected"
            save_debts()
            bot.send_message(message.chat.id, "Долг отклонён.")
            return

    bot.send_message(message.chat.id, "Такого долга не найдено или вы не получатель.")

@bot.message_handler(commands=["paid"])
def mark_as_paid(message):
    parts = message.text.split()
    if len(parts) != 2 or not parts[1].isdigit():
        bot.send_message(message.chat.id, "Формат: /paid долг_ID")
        return

    debt_id = int(parts[1])
    username = get_user_name(message.from_user)

    for d in debts:
        if d["id"] == debt_id and (d["from"] == username or d["to"] == username) and d["status"] == "confirmed":
            d["status"] = "paid"
            save_debts()
            bot.send_message(message.chat.id, "Долг отмечен как оплаченный.")
            return

    bot.send_message(message.chat.id, "Такой подтверждённый долг не найден.")

@bot.message_handler(commands=["debts"])
def list_debts(message):
    username = get_user_name(message.from_user)
    user_debts = [d for d in debts if d["from"] == username and d["status"] in ("pending", "confirmed")]

    if not user_debts:
        bot.send_message(message.chat.id, "У тебя нет долгов.")
        return

    msg = "Ты должен:\n"
    for d in user_debts:
        msg += f'#{d["id"]} → @{d["to"]}: {d["amount"]} ₽ (статус: {d["status"]})\n'
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=["credits"])
def list_credits(message):
    username = get_user_name(message.from_user)
    user_credits = [d for d in debts if d["to"] == username and d["status"] in ("pending", "confirmed")]

    if not user_credits:
        bot.send_message(message.chat.id, "Тебе никто не должен.")
        return

    msg = "Тебе должны:\n"
    for d in user_credits:
        msg += f'#{d["id"]} ← @{d["from"]}: {d["amount"]} ₽ (статус: {d["status"]})\n'
    bot.send_message(message.chat.id, msg)

bot.send_message = lambda chat_id, text, **kwargs: telebot.TeleBot.send_message(bot, chat_id, text, **kwargs)

print("Бот запущен...")

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logging.error("Ошибка в polling:", exc_info=True)
        print("Бот упал с ошибкой, перезапуск через 10 секунд...")
        time.sleep(10)
