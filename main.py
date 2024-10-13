from config import dp
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import executor
import requests

from buttons.reple_buttons import start_Keybord, add_button

@dp.message_handler(commands=['start'])
async def start(message: Message):
    text = f"Assalomu allaykum {message.from_user.full_name} botga xush kelibsiz,\n1.Siz bizning botimizdan Nomoz vaqtlarini bilib olishingiz mumkin"
    await message.answer(text, reply_markup=start_Keybord)



@dp.message_handler(text='ℹ️Bot haqida malumot')
async def about(message: Message):
    text = f"Bizning botimiz nomoz vaqtlarin ko'rsatib beradi va sizga eslatib turadi."
    await message.answer(text=text, reply_markup=start_Keybord)
    pass

@dp.message_handler(text="📍Manzil tanlang")
async def adders(message: Message):
    text = f"Mazillingiz tanlang..."
    await message.answer(text, reply_markup=add_button)
    

@dp.message_handler(text='Toshkent')
async def city(message: Message):
    if message.text == "Toshkent":
        link = 'https://islomapi.uz/api/present/day?region=Toshkent'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        pass
    pass

@dp.message_handler(text='Qarshi')
async def city(message: Message):
    if message.text == "Qarshi":
        link = 'https://islomapi.uz/api/present/day?region=Qarshi'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)


@dp.message_handler(text='Farg\'ona')
async def city(message: Message):
    if message.text == "Farg\'ona":
        link = 'https://islomapi.uz/api/present/day?region=Farg\'ona'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)


@dp.message_handler(text='Namangan')
async def city(message: Message):
    if message.text == "Namangan":
        link = 'https://islomapi.uz/api/present/day?region=Namangan'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        
        

@dp.message_handler(text='Andijon')
async def city(message: Message):
    if message.text == "Andijon":
        link = 'https://islomapi.uz/api/present/day?region=Andijon'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        
        
# chipi
@dp.message_handler(text='Guliston')
async def city(message: Message):
    if message.text == "Guliston":
        link = 'https://islomapi.uz/api/present/day?region=Guliston'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        
        

@dp.message_handler(text='Jizzax')
async def city(message: Message):
    if message.text == "Jizzax":
        link = 'https://islomapi.uz/api/present/day?region=Jizzax'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        
        

@dp.message_handler(text='Samarqand')
async def city(message: Message):
    if message.text == "Samarqand":
        link = 'https://islomapi.uz/api/present/day?region=Samarqand'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)



@dp.message_handler(text='Termiz')
async def city(message: Message):
    if message.text == "Termiz":
        link = 'https://islomapi.uz/api/present/day?region=Termiz'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        

@dp.message_handler(text='Buxoro')
async def city(message: Message):
    if message.text == "Buxoro":
        link = 'https://islomapi.uz/api/present/day?region=Buxoro'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        
        

@dp.message_handler(text='Navoiy')
async def city(message: Message):
    if message.text == "Navoiy":
        link = 'https://islomapi.uz/api/present/day?region=Navoiy'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)
        
        


@dp.message_handler(text='Xiva')
async def city(message: Message):
    if message.text == "Xiva":
        link = 'https://islomapi.uz/api/present/day?region=Xiva'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)



@dp.message_handler(text='Nukus')
async def city(message: Message):
    if message.text == "Nukus":
        link = 'https://islomapi.uz/api/present/day?region=Nukus'
        
        # API orqali ma'lumot olish
        res = requests.get(link)
        data = res.json()
        
        region = data['region']
        sana = data['date']
        weekday = data['weekday']
        tong_saharlik = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom_iftor = data['times']['shom_iftor']
        hufton = data['times']['hufton']
        
        text = f"📌 Hudud: {region}\n📅 Sana: {sana}\n📆 Haftaning qaysi kuni: {weekday}\n🌑 Bomdod vaqti: {tong_saharlik}\n🌒 Qo'yosh chiqishi vaqti: {quyosh}\n🌕 Peshin: {peshin}\n🌗 Asr: {asr}\n🌘 Shom: {shom_iftor}\n🌑 Hufton: {hufton}"
        await message.answer(text, reply_markup=add_button)


if __name__ == '__main__':
    executor.start_polling(skip_updates=True, dispatcher=dp)