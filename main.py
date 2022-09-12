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
        msg, "<b>Non Muslim</b> \nMee Tai Mak Goreng /n Mee Tai Mak /nPrawn meat /negg /nbean sprout /nButter Cream Roll


@bot.message_handler(commands=["tuesdaylunch", "Tuesdaylunch", "TuesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A (Outration Set)</u> \nPandan Rice with Chicken Manchrian Set \nPandan Rice \nChicken Opor \nStir fried pork with Thai Basil \nCabbage with Minced Chicken Lemak \nOld cucumber Soup \n<b>Set B</u> \nGinger Flower Braised Chicken Noodle Set \nIpoh Hor Fun \nGinger Flower Soya Base Gravy \nBaked Garlic Chicken \nPork Slice \nSou Peh Chye with Abalone Mushroom and Wolfberry \nLemon Barley Dessert \n<b>Vegetarian Chinese</b> \nVegetarian Mee Goreng \nMock Fish Curry \nFried Samosa Curry \nKang Kong with Chilli")


@bot.message_handler(
    commands=["tuesdaydinner", "TuesdayDinner", "tuesdayDinner", "Tuesdaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nSFIM Pinya Baked Chicken Set \nChili Tomato Fried Noodle \nChili Seafood Sauce \nPinya Baked Chicken \nFried Egg with Tomato \nBroccoli with Shrimp \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nMock Duck With Yam \nFried Mock Chicken with Tau See \nBroccoli with Corn Kernel")


@bot.message_handler(commands=[
    "wednesdaybreakfast", "WednesdayBreakfast", "Wednesdaybf", "wednesdaybf",
    "Wednesdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nBig Pau /nSausage Roll /nDanish Apple \n\n<b>Vegetarian Chinese</b> \nFried Kway Teow \nCookies & Cream Cream Roll")


@bot.message_handler(
    commands=["wednesdaylunch", "Wednesdaylunch", "WednesdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A </u> \nSausage and Corn Rice set \nSausage and Corn Rice \nChicken Masak Merah \nCrab Dumpling \nHomemade Otar \nCauliflower with green peas \nPotato and Carrot Soup \n\n<u>Set B</u> \nMee Siam Set \nBee Hoon \nMee Siam Gravy \nEgg \nChicken Wing \nFishcake \nBean sprouts \nTau Kwa \nTau Pok \nSnow Fungus with Longan Dessert \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \Mock Char Siew \nStir Fried Vegetarian Golden Slice with Mushroom \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(commands=[
    "wednesdaydinner", "WednesdayDinner", "wednesdayDinner", "Wednesdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nLemongrass TomYam Chicken with Pineapple Rice Set \nPineapple Rice \nLemongrass TomYam Chicken \nStir Fried Pork with Black Pepper Sauce \nBean Sprout with Tau Pok \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nBraised Mock Duck with Black Vinegar \nBraised Tau Kwa with Mock Char Siew \nBraised Hairy Gourd Lemak")


@bot.message_handler(commands=[
    "thursdaybreakfast", "ThursdayBreakfast", "Thursdaybf", "thursdaybf",
    "Thursdaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nFried Hong Kong Noodles \nInstant Noodles \nEgg \nPrawn Meat \nChicken Ham \nCarrot /nBean Sprout /nOnion \nCrab Ball \nChicken Meatball \n\n<b>Vegetarian Chinese</b> \nHamburger Bun \nMargarine \nPandan Pao \nRed Bean Pao \nVegetarian Ham")


@bot.message_handler(
    commands=["thursdaylunch", "Thursdaylunch", "ThursdayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A</u> \nGoing Green Special Lunch - Lu "Dou" Fan Set \nRice \nLu "Dou" \Braised Tau Kwa \nButtered Broccoli \nButtered Carrot \nButtered Corn \Red Dates Chicken Broth \n\n<u>Set B</u> \nLaksa Set \nLaksa Bee Hoon \nTau Pok \nFried Chicken Wing \nBean Sprout \nHard Boiled Egg \nFish Cake \nSago Gula Melaka with Sweet Potatoes  \n\n<b>Vegetarian Chinese</b> \nVegetarian Fried Rice (80% White and 20% Brown Rice) \nVegetarian Crispy Chicken \nVegetarian Chilli Fish Balls \nStir Fried Broccoli with Chinese Mushroom")


@bot.message_handler(commands=[
    "thursdaydinner", "ThursdayDinner", "thursdayDinner", "Thursdaydin"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nLong Bean Fried Rice Set \nLong Bean Fried Rice \nAyam Assam Melaka \nOtar Fish Cake \nStir Fried Chye Sim with Tau Kee and Carrot \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nStewed Mock Chicken with Potato \nBraised Tau Hoo With Mushroom \nFried Bayam with Carrot")                                                                                                                                           
@bot.message_handler(commands=[
    "fridaybreakfast", "FridayBreakfast", "Fridaybf", "fridaybf",
    "Fridaybreakfast"
])
def send_multi_message(msg):
    bot.reply_to(
        msg,
"<b>Non Muslim</b> \nChar Siew Pau \nTau Sar Delight \nPain Au Raisin \n\n<b>Vegetarian Chinese</b> \nFried Macaroni \nVegetarian Spring Rolls")


@bot.message_handler(commands=["fridaylunch", "Fridaylunch", "FridayLunch"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \n<u>Set A </u> \nWasabi Fish Burger with Buffalo Wing Set \nHamburger \nFrench Fries \nFried Breaded Chicken Burger \nBaked Buffalo Chicken Wing Stick \nButtered Corn \nCreme of Corn \n\n<b>Vegetarian Chinese</b> \nSteamed Rice (80% white rice+20% brown rice) \nSweet and Sour Mock Fish \nTau Kwa Sambal \nSou Peh Chye with Oyster Sauce")


@bot.message_handler(
    commands=["fridaydinner", "FridayDinner", "fridayDinner", "Fridaydin"])
def send_multi_message(msg):
    bot.reply_to(
        msg,
        "<b>Non Muslim</b> \nChar Siew Chicken Rice Set \nChicken Rice \nBaked Char Siew Chicken \nFried Egg with Sausage \nNgoh Hiang \nStir Fried Honey Peas with Mixed Vegetables \n\n<b>Vegetarian Chinese</b>")


bot.polling()

