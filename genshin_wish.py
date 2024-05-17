import random
mondstadt = ["Albedo", "Amber", "Barbara", "Bennett", "Diluc", "Diona", "Eula", "Fischl", "Jean", "Kaeya", "Klee", "Lisa", "Mika", "Mona", "Noelle", "Razor", "Rosaria", "Sucrose", "Venti"]
liyue = ["Baizhu", "Beidou", "Chongyun", "Gaming", "Ganyu", "Hu Tao", "Keqing", "Ningguang", "Qiqi", "Shenhe", "Xiangling", "Xianyun", "Xiao", "Xingqiu", "Xinyan", "Yanfei", "Yaoyao", "Yelan", "Yun Jin", "Zhongli"]
inazuma = ["Itto", "Chiori", "Gorou", "Kazuha", "Ayaka", "Ayato", "Kirara", "Sara", "Shinobu", "Ei", "Kokomi", "Sayu", "Heizou", "Thoma", "Yae Miko", "Yoimiya"]
sumeru = ["Alhaitham", "Candace", "Collei", "Cyno", "Dehya", "Dori", "Faruzan", "Kaveh", "Layla", "Nahida", "Nilou", "Tighnari", "Wanderer"]
fontaine = ["Charlotte", "Chevreuse", "Freminet", "Furina", "Lynette", "Lyney", "Navia", "Neuvillette", "Wriothesley", "Clorinde", "Sigewinne"]
natlan = [""]
snezhnaya = ["Childe", "Arlecchino"]
pull = ""
pc = mondstadt + liyue + inazuma + sumeru + fontaine + snezhnaya
albedocons = []
ambercons = []
barbaracons = []
bennettcons = []

def wish(x):
    while x != "no":
        for i in range(1):
            if x == "yes":
                pull = pc[random.randint(0,80)]
                print(pull)
                if pull == "Albedo":
                    if len(albedocons) == 0:
                        print("The Alchemy Fucc\n")
                        albedocons.append("*")
                    elif len(albedocons) == 1:
                        print("Go ahead and paint your constellation for me\n")
                        albedocons.append("*")
                    elif len(albedocons) == 2:
                        print("I love how clearly autistic you are")
                        albedocons.append("*")
                    elif len(albedocons) == 3:
                        print("getting nice and stronk")
                        albedocons.append("*")
                    elif len(albedocons) == 4:
                        print("Geo elevator go wee")
                        albedocons.append("*")
                    elif len(albedocons) == 5:
                        print("So what did you get Gold for mother's day?")
                        albedocons.append("*")
                    elif len(albedocons) == 6:
                        print("you are max stronk now")
                    x = input("do you want to do another?\n\n")
                elif pull == "Amber":
                    if len(ambercons) == 0:
                        print("Baron Bunny gonna be twerking as a distraction")
                        ambercons.append("*")
                    elif len(ambercons) == 1:
                        print("so is your wing glider license up todate?")
                        ambercons.append("*")
                    elif len(ambercons) == 2:
                        print("Colleiflower would like to see you again")
                        ambercons.append("*")
                    elif len(ambercons) == 3:
                        print("Baron Bunny breaking it down now")
                        ambercons.append("*")
                    elif len(ambercons) == 4:
                        print("Your stuffed animal is tryna pay off your wing glider fines, and exam fees")
                        ambercons.append("*")
                    elif len(ambercons) == 5:
                        print("You've become quite the powerful pocket lighter")
                        ambercons.append("*")
                    elif len(ambercons) == 6:
                        print("Baron Bunny throwin it back and spinnin on the stripper pole. Fan Favorite")
                    x = input("do you want to do another?\n\n")
                elif pull == "Barbara":
                    if len(barbaracons) == 0:
                        print("Oh fuck not this bitch again!!")
                        barbaracons.append("*")
                    elif len(barbaracons) == 1:
                        print("wild that you got your own fan club filled with adults..")
                        barbaracons.append("*")
                    elif len(barbaracons) == 2:
                        print("Ok here is a stick. now go beat your stalkers with it")
                        barbaracons.append("*")
                    elif len(barbaracons) == 3:
                        print("Ok now take that stick and go make your sister take a break")
                        barbaracons.append("*")
                    elif len(barbaracons) == 4:
                        print("I keep pulling you too much. Go away >:(")
                        barbaracons.append("*")
                    elif len(barbaracons) == 5:
                        print("go splash some water on someone else for a change >:(")
                        barbaracons.append("*")
                    elif len(barbaracons) == 6:
                        print("is this what beings stalked is like?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Bennett":
                    if len(bennettcons) == 0:
                        print("knock him out before his bad luck gets you")
                        bennettcons.append("*")
                    elif len(bennettcons) == 1:
                        print("You gonna be Meta for awhile Bennothy")
                        bennettcons.append("*")
                    elif len(bennettcons) == 2:
                        print("Don't worry someday Benny's adventure team will be the top Mondstadt team.")
                        bennettcons.append("*")
                    elif len(bennettcons) == 3:
                        print("ok Benny you are starting to get too many cons... slow down there buddy.")
                        bennettcons.append("*")
                    elif len(bennettcons) == 4:
                        print("Now you can protecc Fischl when y'all go adventuring better.")
                        bennettcons.append("*")
                    elif len(bennettcons) == 5:
                        print("Bennothy slow tf down.")
                        bennettcons.append("*")
                    elif len(bennettcons) == 6:
                        print("great a perfectly good Bennington got ruined for team comps")
                    x = input("do you want to do another?\n\n")
                elif pull == "Diluc":
                    print("I'm not saying he's Mondstadt Batman, but I've never seen him and Mondstadt Batman in the same room")
                    x = input("do you want to do another?\n\n")
                elif pull == "Diona":
                    print("she sniffin for alcohol on your breath")
                    x = input("do you want to do another?\n\n")
                elif pull == "Eula":
                    print("God she's hot")
                    x = input("do you want to do another?\n\n")
                elif pull == "Fischl":
                    print("she is O-fischl-y yours... ok I'll stop asking Cyno for jokes")
                    x = input("do you want to do another?\n\n")
                elif pull == "Jean":
                    print("Sir put the work down")
                    x = input("do you want to do another?\n\n")
                elif pull == "Kaeya":
                    print("Just waiting for the next Khaenri'ah lore dump funny immortal man")
                    x = input("do you want to do another?\n\n")
                elif pull == "Klee":
                    print("I'm scared of that thing")
                    x = input("do you want to do another?\n\n")
                elif pull == "Lisa":
                    print("Lemme smash before you go")
                    x = input("do you want to do another?\n\n")
                elif pull == "Mika":
                    print("you better take care of Noelle >:(")
                    x = input("do you want to do another?\n\n")
                elif pull == "Mona":
                    print("I'm tryna make you Mona if you catch my drift")
                    x = input("do you want to do another?\n\n")
                elif pull == "Noelle":
                    print("too precious for this world. Stop endagering yourself, and work as a team >:(")
                    x = input("do you want to do another?\n\n")
                elif pull == "Razor":
                    print("Oh look prototype Cyno")
                    x = input("do you want to do another?\n\n")
                elif pull == "Rosaria":
                    print("I support your devotion to not work")
                    x = input("do you want to do another?\n\n")
                elif pull == "Sucrose":
                    print("Sweetest little baby in the room.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Venti":
                    print("I know you're hiding something you fucking twink")
                    x = input("do you want to do another?\n\n")
                elif pull == "Baizhu":
                    print("Dear God man how are you still standing?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Beidou":
                    print("Lore alone you should have been a 5 star")
                    x = input("do you want to do another?\n\n")
                elif pull == "Chongyun":
                    print("The girl with the bear told me to give you this, she said don't worry it's not spicy,\nbut i don't trust her about that.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Gaming":
                    print("MLG *air horn noises*")
                    x = input("do you want to do another?\n\n")
                elif pull == "Ganyu":
                    print("Hi you're perfect ily")
                    x = input("do you want to do another?\n\n")
                elif pull == "Hu Tao":
                    print("You're autistic af about the afterlife, and make bad jokes. I fucks with that.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Keqing":
                    print("I'm still mad at you pity breaker. I don't care how pretty you are")
                    x = input("do you want to do another?\n\n")
                elif pull == "Ningguang":
                    print("You pulled yourself out of poverty into being the richest bitch in all of Teyvat...\nMad fuckin respect")
                    x = input("do you want to do another?\n\n")
                elif pull == "Qiqi":
                    print("I hear you are a pity breaker for a lot of people lmao...\nYou stay the fuck away from me")
                    x = input("do you want to do another?\n\n")
                elif pull == "Shenhe":
                    print("You're so fuckin autistic ilysm")
                    x = input("do you want to do another?\n\n")
                elif pull == "Xiangling":
                    print("Ah yes the secret Harbinger")
                    x = input("do you want to do another?\n\n")
                elif pull == "Xianyun":
                    print("Hot birb lady")
                    x = input("do you want to do another?\n\n")
                elif pull == "Xiao":
                    print("Hah short")
                    x = input("do you want to do another?\n\n")
                elif pull == "Xingqiu":
                    print("Water Twink")
                    x = input("do you want to do another?\n\n")
                elif pull == "Xinyan":
                    print("Why do you sound like you're from Texas???")
                    x = input("do you want to do another?\n\n")
                elif pull == "Yanfei":
                    print("Hi ily")
                    x = input("do you want to do another?\n\n")
                elif pull == "Yaoyao":
                    print("Idk much about you, but on principle you are a child therefore ew.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Yelan":
                    print("Idk what possessed both you and water twink to get that atrocious haircut\n(lemme smash tho)")
                    x = input("do you want to do another?\n\n")
                elif pull == "Yun Jin":
                    print("I should do your hangout event frfr")
                    x = input("do you want to do another?\n\n")
                elif pull == "Zhongli":
                    print("Have you heard the good news about Ozmanthus Wine?\nYou're about to.. a lot")
                    x = input("do you want to do another?\n\n")
                elif pull == "Itto":
                    print("The One and Oni")
                    x = input("do you want to do another?\n\n")
                elif pull == "Chiori":
                    print("I love you small fashion woman")
                    x = input("do you want to do another?\n\n")
                elif pull == "Gorou":
                    print("I hear Yae Miko was looking for you")
                    x = input("do you want to do another?\n\n")
                elif pull == "Kazuha":
                    print("What is it with you and pilfering headwear?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Ayaka":
                    print("Will stab someone who gets in her way of getting with traveler")
                    x = input("do you want to do another?\n\n")
                elif pull == "Ayato":
                    print("Has most likely stabbed someone")
                    x = input("do you want to do another?\n\n")
                elif pull == "Kirara":
                    print("Meow?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Sara":
                    print("Eh")
                    x = input("do you want to do another?\n\n")
                elif pull == "Shinobu":
                    print("She hot")
                    x = input("do you want to do another?\n\n")
                elif pull == "Ei":
                    print("2 for 1 special")
                    x = input("do you want to do another?\n\n")
                elif pull == "Kokomi":
                    print("Kokomelon is fish lady")
                    x = input("do you want to do another?\n\n")
                elif pull == "Sayu":
                    print("I forget you exist ngl")
                    x = input("do you want to do another?\n\n")
                elif pull == "Heizou":
                    print("ACAB")
                    x = input("do you want to do another?\n\n")
                elif pull == "Thoma":
                    print("quite efficient cleaner")
                    x = input("do you want to do another?\n\n")
                elif pull == "Yae Miko":
                    print("Hot fox lady")
                    x = input("do you want to do another?\n\n")
                elif pull == "Yoimiya":
                    print("you really shouldn't be a 5 star")
                    x = input("do you want to do another?\n\n")
                elif pull == "Alhaitham":
                    print("Smarty pants")
                    x = input("do you want to do another?\n\n")
                elif pull == "Candace":
                    print("You are gorgeous omg")
                    x = input("do you want to do another?\n\n")
                elif pull == "Collei":
                    print("I will tear that fucker apart in your name")
                    x = input("do you want to do another?\n\n")
                elif pull == "Cyno":
                    print("I'd say ACAB, but you actually do your job right so you and you're bad, but funny jokes are cool \n but you're on thin fucking ice")
                    x = input("do you want to do another?\n\n")
                elif pull == "Dehya":
                    print("I love you, and they did you dirty with your kit.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Dori":
                    print("You can join Dottore in his suffering. He will be the appetizer")
                    x = input("do you want to do another?\n\n")
                elif pull == "Faruzan":
                    print("you old ass Hatsune Miku looking mf")
                    x = input("do you want to do another?\n\n")
                elif pull == "Kaveh":
                    print("You are perf, and deserve better")
                    x = input("do you want to do another?\n\n")
                elif pull == "Layla":
                    print("Sleepiest little baby in the room")
                    x = input("do you want to do another?\n\n")
                elif pull == "Nahida":
                    print("You got games on your phone?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Nilou":
                    print("you are v pretty, but you definitely shouldn't be a 5 star")
                    x = input("do you want to do another?\n\n")
                elif pull == "Tighnari":
                    print("I respect you, and the fact you kept Dottore at bay you funky lil mushroom enjoyer")
                    x = input("do you want to do another?\n\n")
                elif pull == "Wanderer":
                    print("You sure do talk a lot of shit for someone who I can easily rename babygirl")
                    x = input("do you want to do another?\n\n")
                elif pull == "Charlotte":
                    print("Why does your healing passive only work better the more fontainians are in your team?\nYou racist or something??")
                    x = input("do you want to do another?\n\n")
                elif pull == "Chevreuse":
                    print("Such a snacky fiend you are wonderful.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Freminet":
                    print("I'm sorry you look goofy with in your ult")
                    x = input("do you want to do another?\n\n")
                elif pull == "Furina":
                    print("Hi you are perfect, and deserve whatever you want. You worked so hard. ilysm")
                    x = input("do you want to do another?\n\n")
                elif pull == "Lynette":
                    print("I wish to give you a forehead kith")
                    x = input("do you want to do another?\n\n")
                elif pull == "Lyney":
                    print("A small Inazuman woman with a sword heard that you were trying to hook up with The Traveler\nI would run")
                    x = input("do you want to do another?\n\n")
                elif pull == "Navia":
                    print("I'll come back for you I swear")
                    x = input("do you want to do another?\n\n")
                elif pull == "Neuvillette":
                    print("Oratrice Mecanique D'analyse Cardinale")
                    x = input("do you want to do another?\n\n")
                elif pull == "Wriothesley":
                    print("Keep your tea away from Rice Cake over here")
                    x = input("do you want to do another?\n\n")
                elif pull == "Clorinde":
                    print("How is your top button holding up?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Sigewinne":
                    print("You are a sneaky lil hoe. I love you")
                    x = input("do you want to do another?\n\n")
                elif pull == "Childe":
                    print("Ready for all the Childe abuse??")
                    x = input("do you want to do another?\n\n")
                elif pull == "Arlecchino":
                    print("You are no longer Fatherless congrats")
                    x = input("do you want to do another?\n\n")
                else:
                    print("Havent done one for you yet. wait your turn")
                    x = input("do you want to do another?")
            elif x != "yes":
                print("oh ok have a nice gamble free day sir")
                x = input("so do you wanna do a pull yes or no?? \n\n")

def ask():
    return input("do you wanna make a wish?\n\n")

x = ask()

wish(x)
print("Ok have a nice day :)")
#print(len(pc))