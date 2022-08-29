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
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \n<u>Chicken Char Siew Rice Set</u> \nChicken Rice \nBaked Char Siew \nFish Nugget \nBean Sprout \nChicken with White Fungus Soup \n\n<b>Set B</b> \nMee Soto \nEgg \Chicken \nPotato Cake \nBean Sprout \nCheng Teng \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSambal Mock Chicken \nHot and Spicy Tau Hoo \nSauteed French Bean with Chinese Mushroom")


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
        msg, "<b>Non Muslim</b> \nFried Mee \nChicken with Seaweed Wrap x2 \nCrab Dumpling x2 \n\n<b>Vegetarian Chinese</b> \nHot Dog Bun \nYam Pau \nPepper Sausage")


@bot.message_handler(commands=["tuesdaylunch", "Tuesdaylunch", "TuesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \nNasi Lemak Rice \nFried Chicken Wing \nSambal Telar Goreng \nPotato Cake \nSavur Lodeh \nOpor Ayam \n\n<u>Set B</u> \n<u>Kway Chap Set</u> \nKway Teow \nLor Gravy \nBraised Pork Collar \nLor Egg \nBraised Tau Kwa \nTau Pok \nBraised Salted Vegetables \nCheng Teng \n\n<b>Vegetarian Chinese</b> \nVegetarian Mee Goreng \nMock Fish Curry \nFried Samosa Curry \nKang Kong with Chilli")


@bot.message_handler(
    commands=["tuesdaydinner", "TuesdayDinner", "tuesdayDinner", "Tuesdaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nLaksa Bee Hoon Goreng \nBaked Black Pepper Chicken Bone \nSambal Chilli Sauce Retort \nFried Fish Cake \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nMock Duck With Yam \nFried Mock Chicken with Tau See \nBroccoli with Corn Kernel")


@bot.message_handler(commands=[
    "wednesdaybreakfast", "WednesdayBreakfast", "Wednesdaybf", "wednesdaybf",
    "Wednesdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBig Pau \nDanish Apple \nChicken Curry Puff \n\n<b>Vegetarian Chinese</b> \nFried Kway Teow \nCookies & Cream Cream Roll")


@bot.message_handler(
    commands=["wednesdaylunch", "Wednesdaylunch", "WednesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \nSteamed Rice \nKung Poh Chicken with Cashew Nuts \nSweet and Sour Fish \nBroccoli with Shrimp \nOld Cucumber Soup \n\n<u>Set B</u> \n<u>Mee Bandang Maur Set</u> \nYellow Noodles \nMee Bandang Soup \nBaked Chicken \nTau Kwa \nChye Sim \nBean Sprout \nCrabmeat Stick \nBobo Cha Cha \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \Mock Char Siew \nStir Fried Vegetarian Golden Slice with Mushroom \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(commands=[
    "wednesdaydinner", "WednesdayDinner", "wednesdayDinner", "Wednesdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nSteamed Rice (80% white rice+20% brown rice) \nStir Fried Chicken with Black Pepper Sauce \nCrabmeat Otah \nSou Peh Chye with Abalonne Mushroom and Wolfberry \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nBraised Mock Duck with Black Vinegar \nBraised Tau Kwa with Mock Char Siew \nBraised Hairy Gourd Lemak")


@bot.message_handler(commands=[
    "thursdaybreakfast", "ThursdayBreakfast", "Thursdaybf", "thursdaybf",
    "Thursdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nMee Tai Mak Goreng \nPain Au Raisin \n\n<b>Vegetarian Chinese</b> \nHamburger Bun \nMargarine \nPandan Pao \nRed Bean Pao \nVegetarian Ham")


@bot.message_handler(
    commands=["thursdaylunch", "Thursdaylunch", "ThursdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \n<u>Chicken Beryani Set</u> \nRice (80% White Rice+20% Brown Rice) \nChicken Beryani \nBervani Sauce \nLong Bean with Dried Shrimp \nSoto Ayam \n\n<u>Set B</u> \n<u>Lor Mee Set</u> \nYellow Noodles \nLor Mee Gravy \nFried Fish \nLor Egg \nNgoh Hiang \nBean Sprout \n\n<b>Vegetarian Chinese</b> \nVegetarian Fried Rice (80% White and 20% Brown Rice) \nVegetarian Crispy Chicken \nVegetarian Chilli Fish Balls \nStir Fried Broccoli with Chinese Mushroom")


@bot.message_handler(commands=[
    "thursdaydinner", "ThursdayDinner", "thursdayDinner", "Thursdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nWestern Fried Rice (80% White Rice+20% Brown Rice) \nTeriyaki Chicken(Baked) \nTeriyaki Sauce CFS \nStir Fried Honey Peas with Mixed Vegetables \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nStewed Mock Chicken with Potato \nBraised Tau Hoo With Mushroom \nFried Bayam with Carrot")


@bot.message_handler(commands=[
    "fridaybreakfast", "FridayBreakfast", "Fridaybf", "fridaybf",
    "Fridaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
"<b>Non Muslim</b> \nGlutinous Rice with Lor Chicken \nChar Siew Pau \nLemon Muffin \n\n<b>Vegetarian Chinese</b> \nFried Macaroni \nVegetarian Spring Rolls")


@bot.message_handler(commands=["fridaylunch", "Fridaylunch", "FridayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \n<b>Chilli Seafood Burger Set</b> \nBurger \nFries \nBaked Chicken Chop \nCorn \nMushroom Soup \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSweet and Sour Mock Fish \nTau Kwa Sambal \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(
    commands=["fridaydinner", "FridayDinner", "fridayDinner", "Fridaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nSoya Sauce Chicken Rice \n\n<b>Vegetarian Chinese</b>")


bot.polling()
