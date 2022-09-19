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
        "<b>Non Muslim</b> \nChicken Curry Puff \nYam Pau \nDanish Apple \n\n<b>Vegetarian Chinese</b> \nFried Vegetarian Bee Hoon \nVegetarian Spring Roll")


@bot.message_handler(commands=["mondaylunch", "Mondaylunch", "MondayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \n<u>Ayam Goreng Berempah Set \nNasi Kerabu \nAyam Goreng Berempah \nIkan Bilis with Large Onion Sambal \nSavor Lodeh \nSop Ayam Bawang \n\nAyam Mee Soto Set \nYellow Noodle \nChicken Wing \nPotato Cake \nHardboiled Egg \nBeansprout \nSweet Potato and Ginger Dessert \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSambal Mock Chicken \nHot and Spicy Tau Hoo \nSauteed French Bean with Chinese Mushroom")


@bot.message_handler(
    commands=["mondaydinner", "MondayDinner", "mondayDinner", "Mondaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nFried Rice with Chicken Set \nFried Rice \nBaked Chicken Chop \nWasabi Mayo \nSeaweed Chicken \nTasty Tientsin Cabbage \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nStewed Mock Chicken with Chestnut \nStir Fried Mock Fungus Roll with Pineapple \nStir Fried Lady Finger")


@bot.message_handler(commands=[
    "tuesdaybreakfast", "TuesdayBreakfast", "Tuesdaybf", "tuesdaybf",
    "Tuesdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg, "<b>Non Muslim</b> \nFried Mee \nYellow Noodles \nChicken Slice \nEgg \nChye Sim \nBean sprout \nCinnamon Danish")


@bot.message_handler(commands=["tuesdaylunch", "Tuesdaylunch", "TuesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \nPaprika Baked Chicken with Fusion Black Vinegar Paste Set \nFusion Black Vinegar Pasta \nPaprika Baked Chicken \nChicken Sausage \nButtered Colourful Vegetable \nCreme of Corn  \n\n<b>Set B</b> \nPorridge Set \nPlain Porridge \nSteamed Chicken with Salted Fish \nLor Bak \nChye Poh Omelette \nBraised Salted Vegetables \nPumpkin and Red Bean Dessert \n<b>Vegetarian Chinese</b> \nVegetarian Mee Goreng \nMock Fish Curry \nFried Samosa Curry \nKang Kong with Chilli")


@bot.message_handler(
    commands=["tuesdaydinner", "TuesdayDinner", "tuesdayDinner", "Tuesdaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nNasi Minyak with Ayam Opor Set \nNasi Minyak \nChicken Opor \nFish Masak Merah \nLong Bean Sambal  \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nMock Duck With Yam \nFried Mock Chicken with Tau See \nBroccoli with Corn Kernel")


@bot.message_handler(commands=[
    "wednesdaybreakfast", "WednesdayBreakfast", "Wednesdaybf", "wednesdaybf",
    "Wednesdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nTau Sar Delight \nTeriyaki Chicken Pau \nMilk Chocolate Muffin  \n\n<b>Vegetarian Chinese</b> \nFried Kway Teow \nCookies & Cream Cream Roll")


@bot.message_handler(
    commands=["wednesdaylunch", "Wednesdaylunch", "WednesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A </u> \nBaked Black Pepper Chicken with Fried Noodle Set \nFried Noodle \nBake Black Pepper Chicken \nWantan \nStir Fried Cauliflower with Green Pepper \nChicken Soup with Hairy Gourd and Fungus  \n\n<u>Set B</u> \nBak Kut Teh Set \nSteamed Rice \nLor Bak or Lor Chicken \nLor Tau Pok \nBraised Salted Vegetables \nBak Kut Teh Soup \nSago Gula Melaka with Sweet Potatoes \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \Mock Char Siew \nStir Fried Vegetarian Golden Slice with Mushroom \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(commands=[
    "wednesdaydinner", "WednesdayDinner", "wednesdayDinner", "Wednesdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nKung Poh Chicken Set \nPineapple Rice \nBaked Chicken with Kung Poh Sauce \nStir Fried Pork with Spring Onion \nChye Sim with Oyster Sauce\n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nBraised Mock Duck with Black Vinegar \nBraised Tau Kwa with Mock Char Siew \nBraised Hairy Gourd Lemak")


@bot.message_handler(commands=[
    "thursdaybreakfast", "ThursdayBreakfast", "Thursdaybf", "thursdaybf",
    "Thursdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nJavanese Fried Noodle \nEgg Noodle \nChicken slice \nEgg \nCarrot \nCabbage \nBean sprout \n Crab Dumplings \n\n<b>Vegetarian Chinese</b> \nHamburger Bun \nMargarine \nPandan Pao \nRed Bean Pao \nVegetarian Ham")


@bot.message_handler(
    commands=["thursdaylunch", "Thursdaylunch", "ThursdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A</u> \nChicken Char Siew Rice Set \nChicken Rice \nBaked Char Siew Chicken \Lor Egg \nStir Fried Peh Chye with Carrot and Tang Hoon \nRadish Cuttlefish Soup  \n\n<u>Set B</u> \nFried Fish Bee Hoon Soup Set \nLaksa Bee Hoon \nBee Hoon Soup \nFried Fish Fillet \nSteamed Crab Meat \nSou Peh Chye \nSteamed Tau Hoo \nTomato Wedges \nRed Bean Sago \n\n<b>Vegetarian Chinese</b> \nVegetarian Fried Rice (80% White and 20% Brown Rice) \nVegetarian Crispy Chicken \nVegetarian Chilli Fish Balls \nStir Fried Broccoli with Chinese Mushroom")


@bot.message_handler(commands=[
    "thursdaydinner", "ThursdayDinner", "thursdayDinner", "Thursdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nRosemary Chicken with Roast Potatoes Set \nBaked Potato with Herbs \nBaked Rosemary Chicken \nFish NUgget \nButtered Mixed Vegetables \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nStewed Mock Chicken with Potato \nBraised Tau Hoo With Mushroom \nFried Bayam with Carrot")                                                                                                                                           
@bot.message_handler(commands=[
    "fridaybreakfast", "FridayBreakfast", "Fridaybf", "fridaybf",
    "Fridaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
"<b>Non Muslim</b> \nUCMZ \nHamburger Bun \nMagarine \nBreaded Chicken Pattie \nSausage Roll \nPain Au Raisin \n\n<b>Vegetarian Chinese</b> \nFried Macaroni \nVegetarian Spring Rolls")


@bot.message_handler(commands=["fridaylunch", "Fridaylunch", "FridayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A</u> \nHainanese Mutton Stew with Rice \nSteamed Rice \nHainanese Mutton Stew \nSteamed Tau Hoo with Broad Bean Sauce \nStir Fried Honey Peas with Mixed Vegetables \nCheng Teng  \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSweet and Sour Mock Fish \nTau Kwa Sambal \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(
    commands=["fridaydinner", "FridayDinner", "fridayDinner", "Fridaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBee Hoon Goreng Set \nBee Hoon Goreng \nBaked Chicken Wing \nFried Fish Cake \nTau Kwa Goreng Sambal Tomato \nSambal Sauce Retort \n\n<b>Vegetarian Chinese</b>")


bot.polling()


