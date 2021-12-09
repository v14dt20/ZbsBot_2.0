import random
import json
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD
from vkbottle import GroupEventType, GroupTypes, VKAPIError
from vkbottle import BaseStateGroup
from vkbottle import CtxStorage
from time import sleep

bot = Bot(token='b067dde30ea3aedcd5c4319c6341d9129aa8a9e5be63d4d224c6dec4451febbfd361d0060276f4f9b02b7')
bot.labeler.vbml_ignore_case = True

ctx = CtxStorage()

class StateAll(BaseStateGroup):
        NONE = 0
        GACHI_FILE_EDIT_NUM = 1
        GACHI_FILE_EDIT_STR = 2
        GACHI_FILE_ADD = 3
        GACHI_FILE_DELETE = 4
        PRICE_FILE_EDIT_NUM = 5
        PRICE_FILE_EDIT_STR = 6
        PRICE_FILE_ADD = 7
        PRICE_FILE_DELETE = 8
        VKUS_FILE_EDIT_NUM = 9
        VKUS_FILE_EDIT_STR = 10
        VKUS_FILE_ADD = 11
        VKUS_FILE_DELETE = 12
        VIDEO_FILE_EDIT_NUM = 13
        VIDEO_FILE_EDIT_STR = 14
        VIDEO_FILE_ADD = 15
        VIDEO_FILE_DELETE = 16
        GUESSING_GAME = 17
        START = 18
        GUESSING_GAME_EDIT = 19
        PRICE = 20
        ORDER = 21
        GACHI = 22
        BAD = 23
        NAH = 24
        GOOD = 25
        BY = 26
        DEV = 27
        GAME = 28
        

msg_start = ["начать", "привет", "старт"]
msg_vkus = ["вкусы", "вкус"]
msg_price = ["цены", "цена", "стоимость"]
msg_order = ["заказать", "заказ"]
msg_gachi = ["гачи", "гачи анекдот", "анекдот"]
msg_bad = ["долбаёб", "пиздюк", "дурак", "пидр", "долбаеб", "дибил", "пидарас", "дебил"]
msg_nah = ["пошёл нахуй", "пошел нахуй", "нахуй", "иди нахуй"]
msg_good = ["хорошо", "спасибо", "хаха", "ахах", "хах", "ахаха"]
msg_by = ["пока", "выход"]

@bot.labeler.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_message_new(event: GroupTypes.GroupJoin):
        try:
                bot.api.messages.send(
                        user_id=event.object.user_id,
                        attachment="video-209400635_456239053",
                        random_id=0
                )
        except VKAPIError(30):
                pass

#=============================================================================================================================================================================================================================================================
#Меню разработчика
#=============================================================================================================================================================================================================================================================



@bot.on.message(payload={"dev": "menu"})
@bot.on.message(text="dev", state=None)
async def menu_dev(message: Message):
        if message.from_id == 403603979:
                keyboard = Keyboard()
                
                keyboard.add(Text("gachi.txt", {"dev": "gachi"}))
                keyboard.row()
                keyboard.add(Text("price.txt", {"dev": "price"}))
                keyboard.row()
                keyboard.add(Text("vkus.txt", {"dev": "vkus"}))
                keyboard.row()
                keyboard.add(Text("video.txt", {"dev": "video"}))
                keyboard.row()
                keyboard.add(Text("Exit", {"cmd": "menu"}), color=KeyboardButtonColor.NEGATIVE)
                
                await message.answer("Dev menu: \ngachi.txt \nprice.txt \nvkus.txt \nvideo.txt \nExit", keyboard = keyboard)
                await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        else:
                await message.answer(f"Ты не мой папа! {message.from_id}")

@bot.on.message(payload={"dev": "gachi"}, state=StateAll.DEV)
async def gachi_dev(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("View", {"dev": "view_gachi"}))
        keyboard.add(Text("Edit", {"dev": "edit_gachi"}))
        keyboard.add(Text("Add", {"dev": "add_gachi"}))
        keyboard.add(Text("Delete", {"dev": "delete_gachi"}))
        keyboard.row()
        keyboard.add(Text("Back", {"dev": "menu"}), color=KeyboardButtonColor.NEGATIVE)

        await message.answer("Edit mode", keyboard=keyboard)

@bot.on.message(payload={"dev": "price"}, state=StateAll.DEV)
async def price_dev(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("View", {"dev": "view_price"}))
        keyboard.add(Text("Edit", {"dev": "edit_price"}))
        keyboard.add(Text("Add", {"dev": "add_price"}))
        keyboard.add(Text("Delete", {"dev": "delete_price"}))
        keyboard.row()
        keyboard.add(Text("Back", {"dev": "menu"}), color=KeyboardButtonColor.NEGATIVE)

        await message.answer("Edit mode", keyboard=keyboard)

@bot.on.message(payload={"dev": "vkus"}, state=StateAll.DEV)
async def vkus_dev(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("View", {"dev": "view_vkus"}))
        keyboard.add(Text("Edit", {"dev": "edit_vkus"}))
        keyboard.add(Text("Add", {"dev": "add_vkus"}))
        keyboard.add(Text("Delete", {"dev": "delete_vkus"}))
        keyboard.row()
        keyboard.add(Text("Back", {"dev": "menu"}), color=KeyboardButtonColor.NEGATIVE)

        await message.answer("Edit mode", keyboard=keyboard)

@bot.on.message(payload={"dev": "video"}, state=StateAll.DEV)
async def video_dev(message:Message):
    keyboard = Keyboard()

    keyboard.add(Text("View", {"dev": "view_video"}))
    keyboard.add(Text("Edit", {"dev": "edit_video"}))
    keyboard.add(Text("Add", {"dev": "add_video"}))
    keyboard.add(Text("Delete", {"dev": "delete_video"}))
    keyboard.row()
    keyboard.add(Text("Back", {"dev": "menu"}), color=KeyboardButtonColor.NEGATIVE)

    await message.answer("Edit mode", keyboard=keyboard)

#=========================Edit for gachi.txt===============================================
@bot.on.message(payload={"dev": "view_gachi"}, state=StateAll.DEV)
async def gachi_dev_view(message: Message):
        with open('gachi.txt', 'r', encoding='utf-8') as f:
                g = f.readlines()
                for i in range(len(g)):
                        g[i] = str(i)+'.'+g[i]
                await message.answer('\n'.join(g))

@bot.on.message(payload={"dev": "edit_gachi"}, state=StateAll.DEV)
async def gachi_dev_edit(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.GACHI_FILE_EDIT_NUM)
        return "Enter number str for replace"

@bot.on.message(state=StateAll.GACHI_FILE_EDIT_NUM)
async def gachi_dev_edit_number(message: Message):
        ctx.set("gachi_num", message.text)
        await bot.state_dispenser.set(message.peer_id, StateAll.GACHI_FILE_EDIT_STR)
        return "Enter new str"

@bot.on.message(state=StateAll.GACHI_FILE_EDIT_STR)
async def gachi_dev_edit_str(message: Message):
        num = int(ctx.get("gachi_num"))
        new_str = message.text
        license_edit = []
        with open('gachi.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        license_edit.insert(num, new_str+'\n')
        f = open('gachi.txt', 'w')
        f.close()
        with open('gachi.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "add_gachi"}, state=StateAll.DEV)
async def gachi_dev_add(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.GACHI_FILE_ADD)
        return "Edit str for add"

@bot.on.message(state=StateAll.GACHI_FILE_ADD)
async def gachi_dev_add_str(message: Message):
        new_str = message.text
        with open('gachi.txt', 'a', encoding='utf-8') as f:
                f.write('\n'+new_str)
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "delete_gachi"}, state=StateAll.DEV)
async def gachi_dev_delete(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.GACHI_FILE_DELETE)
        return "Enter num str for delete"

@bot.on.message(state=StateAll.GACHI_FILE_DELETE)
async def gachi_dev_delete_str(message: Message):
        num = int(message.text)
        license_edit = []
        with open('gachi.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        f = open('gachi.txt', 'w')
        f.close()
        with open('gachi.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

#=========================Edit for price.txt===============================================
@bot.on.message(payload={"dev": "view_price"}, state=StateAll.DEV)
async def price_dev_view(message: Message):
        with open('price.txt', 'r', encoding='utf-8') as f:
                g = f.readlines()
                for i in range(len(g)):
                        g[i] = str(i)+'.'+g[i]
                await message.answer(''.join(g))

@bot.on.message(payload={"dev": "edit_price"}, state=StateAll.DEV)
async def price_dev_edit(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.PRICE_FILE_EDIT_NUM)
        return "Enter number str for replace"

@bot.on.message(state=StateAll.PRICE_FILE_EDIT_NUM)
async def price_dev_edit_number(message: Message):
        ctx.set("price_num", message.text)
        await bot.state_dispenser.set(message.peer_id, StateAll.PRICE_FILE_EDIT_STR)
        return "Enter new str"

@bot.on.message(state=StateAll.PRICE_FILE_EDIT_STR)
async def price_dev_edit_str(message: Message):
        num = int(ctx.get("price_num"))
        new_str = message.text
        license_edit = []
        with open('price.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        license_edit.insert(num, new_str+'\n')
        f = open('price.txt', 'w')
        f.close()
        with open('price.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "add_price"}, state=StateAll.DEV)
async def price_dev_add(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.PRICE_FILE_ADD)
        return "Edit str for add"

@bot.on.message(state=StateAll.PRICE_FILE_ADD)
async def price_dev_add_str(message: Message):
        new_str = message.text
        with open('price.txt', 'a', encoding='utf-8') as f:
                f.write('\n'+new_str)
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "delete_price"}, state=StateAll.DEV)
async def price_dev_delete(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.PRICE_FILE_DELETE)
        return "Enter num str for delete"

@bot.on.message(state=StateAll.PRICE_FILE_DELETE)
async def price_dev_delete_str(message: Message):
        num = int(message.text)
        license_edit = []
        with open('price.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        f = open('price.txt', 'w')
        f.close()
        with open('price.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

#=========================Edit for vkus.txt===============================================
@bot.on.message(payload={"dev": "view_vkus"}, state=StateAll.DEV)
async def vkus_dev_view(message: Message):
        with open('vkus.txt', 'r', encoding='utf-8') as f:
                g = f.readlines()
                for i in range(len(g)):
                        g[i] = str(i)+'.'+g[i]
                await message.answer(''.join(g))

@bot.on.message(payload={"dev": "edit_vkus"}, state=StateAll.DEV)
async def vkus_dev_edit(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.VKUS_FILE_EDIT_NUM)
        return "Enter number str for replace"

@bot.on.message(state=StateAll.VKUS_FILE_EDIT_NUM)
async def vkus_dev_edit_number(message: Message):
        ctx.set("vkus_num", message.text)
        await bot.state_dispenser.set(message.peer_id, StateAll.VKUS_FILE_EDIT_STR)
        return "Enter new str"

@bot.on.message(state=StateAll.VKUS_FILE_EDIT_STR)
async def vkus_dev_edit_str(message: Message):
        num = int(ctx.get("vkus_num"))
        new_str = message.text
        license_edit = []
        with open('vkus.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        license_edit.insert(num, new_str+'\n')
        f = open('vkus.txt', 'w')
        f.close()
        with open('vkus.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "add_vkus"}, state=StateAll.DEV)
async def vkus_dev_add(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.VKUS_FILE_ADD)
        return "Edit str for add"

@bot.on.message(state=StateAll.VKUS_FILE_ADD)
async def vkus_dev_add_str(message: Message):
        new_str = message.text
        with open('vkus.txt', 'a', encoding='utf-8') as f:
                f.write('\n'+new_str)
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "delete_vkus"}, state=StateAll.DEV)
async def vkus_dev_delete(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.VKUS_FILE_DELETE)
        return "Enter num str for delete"

@bot.on.message(state=StateAll.VKUS_FILE_DELETE)
async def vkus_dev_delete_str(message: Message):
        num = int(message.text)
        license_edit = []
        with open('vkus.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        f = open('vkus.txt', 'w')
        f.close()
        with open('vkus.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

#=========================Edit for video.txt===============================================
@bot.on.message(payload={"dev": "view_video"}, state=StateAll.DEV)
async def video_dev_view(message: Message):
        with open('video.txt', 'r', encoding='utf-8') as f:
                g = f.readlines()
                for i in range(len(g)):
                        g[i] = str(i)+'.'+g[i]
                await message.answer(''.join(g))

@bot.on.message(payload={"dev": "edit_video"}, state=StateAll.DEV)
async def video_dev_edit(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.VIDEO_FILE_EDIT_NUM)
        return "Enter number str for replace"

@bot.on.message(state=StateAll.VIDEO_FILE_EDIT_NUM)
async def video_dev_edit_number(message: Message):
        ctx.set("video_num", message.text)
        await bot.state_dispenser.set(message.peer_id, StateAll.VIDEO_FILE_EDIT_STR)
        return "Enter new str"

@bot.on.message(state=StateAll.VIDEO_FILE_EDIT_STR)
async def video_dev_edit_str(message: Message):
        num = int(ctx.get("video_num"))
        new_str = message.text
        license_edit = []
        with open('video.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        license_edit.insert(num, new_str+'\n')
        f = open('video.txt', 'w')
        f.close()
        with open('video.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "add_video"}, state=StateAll.DEV)
async def video_dev_add(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.VIDEO_FILE_ADD)
        return "Edit str for add"

@bot.on.message(state=StateAll.VIDEO_FILE_ADD)
async def video_dev_add_str(message: Message):
        new_str = message.text
        with open('video.txt', 'a', encoding='utf-8') as f:
                f.write('\n'+new_str)
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

@bot.on.message(payload={"dev": "delete_video"}, state=StateAll.DEV)
async def video_dev_delete(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.VIDEO_FILE_DELETE)
        return "Enter num str for delete"

@bot.on.message(state=StateAll.VIDEO_FILE_DELETE)
async def video_dev_delete_str(message: Message):
        num = int(message.text)
        license_edit = []
        with open('video.txt', 'r', encoding='utf-8') as f:
                license_edit = f.readlines()
        license_edit.remove(license_edit[num])
        f = open('video.txt', 'w')
        f.close()
        with open('video.txt', 'w', encoding='utf-8') as f:
                f.write(''.join(license_edit))
        await bot.state_dispenser.set(message.peer_id, StateAll.DEV)
        return "Success"

#=============================================================================================================================================================================================================================================================
#Главное меню
#=============================================================================================================================================================================================================================================================

@bot.on.message(text = msg_start, state=None)
async def message_hi(message: Message):
        keyboard = Keyboard()

        user = await bot.api.users.get(message.from_id)
        await message.answer(f"Привет, {user[0].first_name} &#128522;")
        sleep(1)
        await message.answer("Меня зовут ZbsBot")
        sleep(1)
        await message.answer("Я ещё совсем маленький, в отличии от тебя, раз ты решился тут покупать, я знаю мало комманд и совсем немного чего умею, мой папа долбаёб не научил меня ничему")
        sleep(1)

        keyboard.add(Text("Вкусы", {"cmd": "vkus"}), color=KeyboardButtonColor.POSITIVE)
        keyboard.add(Text("Цены", {"cmd": "price"}))
        keyboard.add(Text("Заказать", {"cmd": "order"}))
        keyboard.row()
        keyboard.add(Text("Гачи анекдот", {"cmd": "gachi"}), color=KeyboardButtonColor.PRIMARY)
        keyboard.add(Text("Видосик", {"cmd": "video"}))
        keyboard.add(Text("Игры", {"cmd": "game"}))
        keyboard.row()
        keyboard.add(Text("Выход", {"cmd": "exit"}), color=KeyboardButtonColor.NEGATIVE)
        keyboard.row()
        keyboard.add(OpenLink("https://www.instagram.com/zbspuff/", "Инстаграмм"))

        await message.answer("Вот несколько комманд, которые я знаю: \n- Вкусы \n- Цены \n- Заказать \n- Гачи анекдот \n- Видосик", keyboard=keyboard)
        await bot.state_dispenser.set(message.peer_id, StateAll.START)

@bot.on.message(payload = {"cmd": "menu"})
async def message_menu(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Вкусы", {"cmd": "vkus"}), color=KeyboardButtonColor.POSITIVE)
        keyboard.add(Text("Цены", {"cmd": "price"}))
        keyboard.add(Text("Заказать", {"cmd": "order"}))
        keyboard.row()
        keyboard.add(Text("Гачи анекдот", {"cmd": "gachi"}), color=KeyboardButtonColor.PRIMARY)
        keyboard.add(Text("Видосик", {"cmd": "video"}))
        keyboard.add(Text("Игры", {"cmd": "game"}))
        keyboard.row()
        keyboard.add(Text("Выход", {"cmd": "exit"}), color=KeyboardButtonColor.NEGATIVE)
        keyboard.row()
        keyboard.add(OpenLink("https://www.instagram.com/invites/contact/?i=1dh2zsizofw9a&utm_content=nbhj5jo", "Инстаграмм"))

        await message.answer("Доступные команды: \n- Вкусы \n- Цены \n- Заказать \n- Гачи анекдот \n- Видосик", keyboard=keyboard)
        await bot.state_dispenser.set(message.peer_id, StateAll.START)

@bot.on.message(text = msg_vkus, state=StateAll.START)
@bot.on.message(payload = {"cmd": "vkus"}, state=StateAll.START)
async def message_vkus(message: Message):
        keyboard = Keyboard(one_time = True)

        keyboard.add(Text("Назад", {"cmd": "menu"}), color = KeyboardButtonColor.NEGATIVE)
        with open('vkus.txt', 'r', encoding='utf-8') as f:
                await message.answer("Доступные вкусы:\n"+''.join(f.readlines()), keyboard = keyboard)

@bot.on.message(text = msg_price, state=StateAll.START)
@bot.on.message(payload = {"cmd": "price"}, state=StateAll.START)
async def message_price(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Назад", {"cmd": "menu"}), color = KeyboardButtonColor.NEGATIVE)
        with open('price.txt', 'r', encoding='utf-8') as f:
                await message.answer(''.join(f.readlines()), keyboard = keyboard)

@bot.on.message(text = msg_order, state=StateAll.START)
@bot.on.message(payload={"cmd": "order"}, state=StateAll.START)
async def message_order(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Оформить заказ", {"order": "ready"}), color=KeyboardButtonColor.POSITIVE)
        keyboard.add(Text("Назад", {"cmd": "menu"}), color=KeyboardButtonColor.NEGATIVE)
        await message.answer("Для заказа ознакомтесь с товаром, ценами и доступными вкусами!", keyboard=keyboard)

@bot.on.message(payload={"order": "ready"}, state=StateAll.START)
async def order(message: Message):
        await bot.state_dispenser.set(message.peer_id, StateAll.ORDER)
        return "Введите текст в виде: \"Товар\", \"Вкус\", \"Количество\"\nПример: Hqd 1200 тяг, клубника арбуз, 2 штуки"

@bot.on.message(state=StateAll.ORDER)
async def messge_for_dad(message: Message):
        await bot.api.messages.send(
                peer_id=403603979,
                message="Папа, заказ от @id"+str(message.from_id)+": \n"+message.text,
                random_id=0
                )
        await bot.state_dispenser.set(message.peer_id, StateAll.START)
        return "Ваш заказ успешно офрмлен, ждите, скоро с вами свяжется мой папа)))"

@bot.on.message(text = msg_gachi, state=StateAll.START)
@bot.on.message(payload = {"cmd": "gachi"}, state=StateAll.START)
async def message_gachi(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Ещё", {"cmd": "gachi"}), color = KeyboardButtonColor.PRIMARY)
        keyboard.add(Text("Назад", {"cmd": "menu"}), color = KeyboardButtonColor.NEGATIVE)
        with open('gachi.txt', 'r', encoding='utf-8') as f:
                gachi = f.readlines()
                await message.answer(gachi[random.randint(0, (len(gachi) - 1))], keyboard = keyboard)

@bot.on.message(payload = {"cmd": "video"}, state=StateAll.START)
async def message_vid(message: Message):
    keyboard = Keyboard()

    keyboard.add(Text("Ещё", {"cmd": "video"}), color = KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Назад", {"cmd": "menu"}), color = KeyboardButtonColor.NEGATIVE)
    with open('video.txt', 'r', encoding='utf-8') as f:
        video_smeh = f.readlines()
        await message.answer("", keyboard = keyboard, attachment = video_smeh[random.randint(0, (len(video_smeh) - 1))])

@bot.on.message(text = msg_bad)
async def message_bad(message: Message):
        await message.answer(attachment='video-209400635_456239049')

@bot.on.message(text=msg_nah)
async def message_nah(message: Message):
        await message.answer(attachment='video-209400635_456239017')

@bot.on.message(text = msg_good)
async def message_good(message: Message):
        await message.answer("&#128522;")

@bot.on.message(text=["(", "((", "((("])
async def message_sad(message: Message):
        await message.answer(attachment="video-209400635_456239046")

@bot.on.message(text = msg_by, state=StateAll.START)
@bot.on.message(payload = {"cmd": "exit"}, state=StateAll.START)
async def message_by(message: Message):
        await message.answer("Пока, надеюсь я тебе помог или развлёк)", keyboard = EMPTY_KEYBOARD)
        await bot.state_dispenser.delete(message.peer_id)

@bot.on.message(text="отправить")
async def handler(message: Message):
        await bot.api.messages.send(
                peer_id=403603979,
                message="Привет отец",
                random_id=0
        )

#=============================================================================================================================================================================================================================================================
#Игры
#=============================================================================================================================================================================================================================================================

@bot.on.message(payload={"cmd": "game"}, state=[StateAll.START, StateAll.GUESSING_GAME])
async def game_menu(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Угадай число", {"game": "guessing_game"}))
        keyboard.row()
        keyboard.add(Text("Назад", {"cmd": "menu"}), color=KeyboardButtonColor.NEGATIVE)

        await bot.state_dispenser.set(message.peer_id, StateAll.GAME)
        await message.answer("Выберите игру", keyboard=keyboard)

#==================================GuessingGame=============================================================
@bot.on.message(payload={"game": "guessing_game"}, state = StateAll.GAME)
async def game_enter(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Начать", {"guessing_game": "start"}), color=KeyboardButtonColor.POSITIVE)
        keyboard.row()
        keyboard.add(Text("Выход", {"cmd": "game"}), color=KeyboardButtonColor.NEGATIVE)
        
        await bot.state_dispenser.set(message.peer_id, StateAll.GUESSING_GAME)
        await message.answer("Правила игры:\nЯ загадываю число от 1 до 100, у тебя есть 7 попыток, чтобы отгадать моё число. Играем?", keyboard=keyboard)
        

@bot.on.message(payload={"guessing_game": "start"}, state=StateAll.GUESSING_GAME)
async def guessing_game_start(message: Message):
        keyboard = Keyboard()

        keyboard.add(Text("Выход", {"cmd": "game"}), color=KeyboardButtonColor.NEGATIVE)

        with open('GameDataBase.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not(str(message.from_id)) in data:
                        data[str(message.from_id)] = {"guessing_game": {"num": 0, "my_num": 0, "count": 0}}
                        data[str(message.from_id)]["guessing_game"]["num"] = random.randint(1, 100)
                else:
                        data[str(message.from_id)]["guessing_game"]["num"] = random.randint(1, 100)
                        data[str(message.from_id)]["guessing_game"]["my_num"] = 0
                        data[str(message.from_id)]["guessing_game"]["count"] = 0
        
        with open('GameDataBase.json', 'w') as file:
                json.dump(data, file, indent=2)

        await bot.state_dispenser.set(message.peer_id, StateAll.GUESSING_GAME_EDIT)
        await message.answer("Я загадал число! Введи число", keyboard=keyboard)

@bot.on.message(state=StateAll.GUESSING_GAME_EDIT)
async def guessing_game_process(message: Message):
        keyboard = Keyboard()
        keyboard.add(Text("Выход", {"cmd": "game"}), color=KeyboardButtonColor.NEGATIVE)

        with open('GameDataBase.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        try:
                data[str(message.from_id)]["guessing_game"]["my_num"] = int(message.text)
                if data[str(message.from_id)]["guessing_game"]["num"] > data[str(message.from_id)]["guessing_game"]["my_num"]:
                        await message.answer("Моё число больше")
                        data[str(message.from_id)]["guessing_game"]["count"] += 1
                elif data[str(message.from_id)]["guessing_game"]["num"] < data[str(message.from_id)]["guessing_game"]["my_num"]:
                        await message.answer("Моё число мешьше")
                        data[str(message.from_id)]["guessing_game"]["count"] += 1
                elif data[str(message.from_id)]["guessing_game"]["num"] == data[str(message.from_id)]["guessing_game"]["my_num"] and not(data[str(message.from_id)]["guessing_game"]["count"] == 7):
                        await message.answer("Ура! Ты победил! Это число "+str(data[str(message.from_id)]["guessing_game"]["num"])+"\n Количество попыток: "+str(data[str(message.from_id)]["guessing_game"]["count"] + 1), keyboard=keyboard)
                        await bot.state_dispenser.set(message.peer_id, StateAll.GUESSING_GAME)
        
                if data[str(message.from_id)]["guessing_game"]["count"] == 7:
                        await message.answer("Ты проиграл( Попробуй ещё раз", keyboard=keyboard)
                        await bot.state_dispenser.set(message.peer_id, StateAll.GUESSING_GAME)
        except ValueError:
                if message.text == "Выход":
                        await message.answer("Ты досрочно закончил игру, ну ладно", keyboard=keyboard)
                        await bot.state_dispenser.set(message.peer_id, StateAll.GUESSING_GAME)
                else:
                        await message.answer("Ты ввел не число(, давай ещё раз", keyboard=keyboard)
        with open('GameDataBase.json', 'w') as file:
                json.dump(data, file, indent=2)

bot.run_forever()
