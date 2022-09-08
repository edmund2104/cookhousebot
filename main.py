import telebot

from SECRET import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode="html")


@bot.message_handler(commands=["hello"])
def send_help_message(msg):
    bot.reply_to(msg, "Good Day!")


@bot.message_handler(commands=["help", "commands", "start"])
def send_help_message(msg):
    bot.reply_to(
        msg,
        "You can see the menu through these commands: \nFor the breakfast menu on Monday, type /mondaybreakfast \nFor the lunch menu on Monday, type /mondaylunch \nFor the dinner menu on Monday, type /mondaydinner \n\nAnd so on for the respective days!")


@bot.message_handler(content_types=[
    "photo", "sticker", "audio", "voice", "document", "contact", "Video",
    "videonote"
])
def send_content_message(msg):
    bot.reply_to(msg, "I know you like cookhouse food!!")


@bot.message_handler(
    commands=["mondaybreakfast", "Mondaybreakfast", "mondaybf", "Mondaybf"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nSmall Pau \nChicken Puff \nCookies & Cream Cream Roll \n\n<b>Vegetarian Chinese</b> \nFried Vegetarian Bee Hoon \nVegetarian Spring Roll")


@bot.message_handler(commands=["mondaylunch", "Mondaylunch", "MondayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \n<u>Nasi Lemak Set</u> \nNasi Lemak Rice (80% white rice+20% brown rice) \nBaked Chicken Wing \nFried Fish Cake \nSambal Telur Goreng \nSambal Chilli Sauce Retort \nStir Fried Chye Sim with Bean Sprout \nRed Bean Sago \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSambal Mock Chicken \nHot and Spicy Tau Hoo \nSauteed French Bean with Chinese Mushroom")


@bot.message_handler(
    commands=["mondaydinner", "MondayDinner", "mondayDinner", "Mondaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nMee Goreng Yellow Noodles \nBaked Chicken \nSambal Fried Fish Cake \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nStewed Mock Chicken with Chestnut \nStir Fried Mock Fungus Roll with Pineapple \nStir Fried Lady Finger")


@bot.message_handler(commands=[
    "tuesdaybreakfast", "TuesdayBreakfast", "Tuesdaybf", "tuesdaybf",
    "Tuesdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg, "<b>Non Muslim</b> \nSausage Roll \nRed Bean Pau \nButter Sugar Cream Roll \n\n<b>Vegetarian Chinese</b> \nHot Dog Bun \nYam Pau \nPepper Sausage")


@bot.message_handler(commands=["tuesdaylunch", "Tuesdaylunch", "TuesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \nSteamed Rice \nChicken Mirchi \nEgg Bhurji \nFried Wan Tan (Baked) \nStir Fried Honey Peas with Mixed Vegetables \nPotato and Carrot Soup  \n\n<u>Set B</u> \n<u>Chicken Noodle Soup with Prawn Dumpling Set</u> Noodle Soup Stock \nMinced Chicken \nBaked Chicken Wing \nJapanese Prawn Dumpling \nChye Sim \nCarrot Strip \nLemon Barley Dessert \n \n\n<b>Vegetarian Chinese</b> \nVegetarian Mee Goreng \nMock Fish Curry \nFried Samosa Curry \nKang Kong with Chilli")


@bot.message_handler(
    commands=["tuesdaydinner", "TuesdayDinner", "tuesdayDinner", "Tuesdaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBaked Rosemary Chix Set 2 \nPotato Wedges \nBaked Rosemary Chicken \nOnion Borwn Sauce \nGyoza Chicken Japanese \nFrench Bean with Button Mushroom \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nMock Duck With Yam \nFried Mock Chicken with Tau See \nBroccoli with Corn Kernel")


@bot.message_handler(commands=[
    "wednesdaybreakfast", "WednesdayBreakfast", "Wednesdaybf", "wednesdaybf",
    "Wednesdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBig Pau \nApple Puff \nMaple Muffin \n\n<b>Vegetarian Chinese</b> \nFried Kway Teow \nCookies & Cream Cream Roll")


@bot.message_handler(
    commands=["wednesdaylunch", "Wednesdaylunch", "WednesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A </u> \nShrimp Paste Chicken with Steamed Rice Set \nPineapple Rice \nShrimp Paste Chicken \nNgoh Hiang \nTraditional Egg Fu-Yong \nBraised Long Cabbage \nTurnip with Gou Ji Soup \n\n<u>Set B</u> \nPorridge Set \nPlain Porridge \nSteamed Chicken with Szechuan Vegetable \nMei Chye Pork \nFried Egg with Tomato \nCabbage with Button Mushroom \nRed Bean and Sweet Corn Dessert\n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \Mock Char Siew \nStir Fried Vegetarian Golden Slice with Mushroom \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(commands=[
    "wednesdaydinner", "WednesdayDinner", "wednesdayDinner", "Wednesdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBaked Black Pepper Chicken with Fried Noodle Set \nFried Noodle \nBaked Black Pepper Chicken \nBlack Pepper Sauce Retort \nSeaweed Chicken \nOriental Mixed Vegetable \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nBraised Mock Duck with Black Vinegar \nBraised Tau Kwa with Mock Char Siew \nBraised Hairy Gourd Lemak")


@bot.message_handler(commands=[
    "thursdaybreakfast", "ThursdayBreakfast", "Thursdaybf", "thursdaybf",
    "Thursdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBee Hoon Kati Thai Style \nPain Au Raisin \n\n<b>Vegetarian Chinese</b> \nHamburger Bun \nMargarine \nPandan Pao \nRed Bean Pao \nVegetarian Ham")


@bot.message_handler(
    commands=["thursdaylunch", "Thursdaylunch", "ThursdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A</u> Chicken Beryani Set \nNasi Beryani \nChicken Beryani \nBeryani Sauce \nBaked Fish with Tomato Sauce \nLemak Cauliflower \nSop Ayam Bawang \n\n<b>Vegetarian Chinese</b> \nVegetarian Fried Rice (80% White and 20% Brown Rice) \nVegetarian Crispy Chicken \nVegetarian Chilli Fish Balls \nStir Fried Broccoli with Chinese Mushroom")


@bot.message_handler(commands=[
    "thursdaydinner", "ThursdayDinner", "thursdayDinner", "Thursdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nChina Town Claypot Rice \nPlain Claypot Rice \nBraised Chicken with Dried Mushroom \nBBQ Chicken Sausage \nChinese Red Wine Sausage  \nSou Peh Chye with Oyster Sauce \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nStewed Mock Chicken with Potato \nBraised Tau Hoo With Mushroom \nFried Bayam with Carrot")                                                                                                                                           
@bot.message_handler(commands=[
    "fridaybreakfast", "FridayBreakfast", "Fridaybf", "fridaybf",
    "Fridaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
"<b>Non Muslim</b> \nChar Siew Pau \nDonut Red Bean \nDanish Apple \n\n<b>Vegetarian Chinese</b> \nFried Macaroni \nVegetarian Spring Rolls")


@bot.message_handler(commands=["fridaylunch", "Fridaylunch", "FridayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A </u> \nNasi Lemak \nBaked Chicken Wing \nSambal Telur Goreng \nSambal Chili Sauce Retort \nPulau Hitam \nSayur Lodeh \nPulot Hitam \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSweet and Sour Mock Fish \nTau Kwa Sambal \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(
    commands=["fridaydinner", "FridayDinner", "fridayDinner", "Fridaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> Pasta Agilo Olio Style with Mushroom Set \nPasta Agilo Olio with Mushroom \n Baked Chicken with Chicago Grill Sauce \nChicken Chipolata \nButtered Colourful Vegetable \n\n<b>Vegetarian Chinese</b>")


bot.polling()
