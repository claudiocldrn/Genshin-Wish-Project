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
def wish(input):
    if input == "yes":
        for i in range(1):
            pull = pc[random.randint(0,80)]
            print(pull)
            if pull == "Albedo":
                print("The Alchemy Fucc")
            elif pull == "Amber":
                print("Baron Bunny gonna be twerking as a distraction")
            elif pull == "Barbara":
                print("Oh fuck not this bitch again!!")
            elif pull == "Bennett":
                print("knock him out before his bad luck gets you")
            elif pull == "Diluc":
                print("I'm not saying he's Mondstadt Batman, but I've never seen him and Mondstadt Batman in the same room")
            elif pull == "Diona":
                print("she sniffin for alcohol on your breath")
            elif pull == "Eula":
                print("God she's hot")
            elif pull == "Fischl":
                print("she is O-fischl-y yours... ok I'll stop asking Cyno for jokes")
            elif pull == "Jean":
                print("Sir put the work down")
            elif pull == "Kaeya":
                print("Just waiting for the next Khaenri'ah lore dump funny immortal man")
            elif pull == "Klee":
                print("I'm scared of that thing")
            elif pull == "Lisa":
                print("Lemme smash before you go")
            elif pull == "Mika":
                print("you better take care of Noelle >:(")
            elif pull == "Mona":
                print("I'm tryna make you Mona if you catch my drift")
            elif pull == "Noelle":
                print("too precious for this world. Stop endagering yourself, and work as a team >:(")
            elif pull == "Razor":
                print("Oh look prototype Cyno")
            elif pull == "Rosaria":
                print("I support your devotion to not work")
            elif pull == "Sucrose":
                print("Sweetest little baby in the room.")
            elif pull == "Venti":
                print("I know you're hiding something you fucking twink")
            elif pull == "Baizhu":
                print("Dear God man how are you still standing?")
            elif pull == "Beidou":
                print("Lore alone you should have been a 5 star")
            elif pull == "Chongyun":
                print("The girl with the bear told me to give you this, she said don't worry it's not spicy,\nbut i don't trust her about that.")
            elif pull == "Gaming":
                print("MLG *air horn noises*")
            elif pull == "Ganyu":
                print("Hi you're perfect ily")
            elif pull == "Hu Tao":
                print("You're autistic af about the afterlife, and make bad jokes. I fucks with that.")
            elif pull == "Keqing":
                print("I'm still mad at you pity breaker. I don't care how pretty you are")
            elif pull == "Ningguang":
                print("You pulled yourself out of poverty into being the richest bitch in all of Teyvat...\nMad fuckin respect")
            elif pull == "Qiqi":
                print("I hear you are a pity breaker for a lot of people lmao...\nYou stay the fuck away from me")
            elif pull == "Shenhe":
                print("You're so fuckin autistic ilysm")
            elif pull == "Xiangling":
                print("Ah yes the secret Harbinger")
            elif pull == "Xianyun":
                print("Hot birb lady")
            elif pull == "Xiao":
                print("Hah short")
            elif pull == "Xingqiu":
                print("Water Twink")
            elif pull == "Xinyan":
                print("Why do you sound like you're from Texas???")
            elif pull == "Yanfei":
                print("Hi ily")
            elif pull == "Yaoyao":
                print("Idk much about you, but on principle you are a child therefore ew.")
            elif pull == "Yelan":
                print("Idk what possessed both you and water twink to get that atrocious haircut\n(lemme smash tho)")
            elif pull == "Yun Jin":
                print("I should do your hangout event frfr")
            elif pull == "Zhongli":
                print("Have you heard the good news about Ozmanthus Wine?\nYou're about to.. a lot")
            elif pull == "Itto":
                print("The One and Oni")
            elif pull == "Chiori":
                print("I love you small fashion woman")
            elif pull == "Gorou":
                print("I hear Yae Miko was looking for you")
            elif pull == "Kazuha":
                print("What is it with you and pilfering headwear?")
            elif pull == "Ayaka":
                print("Will stab someone who gets in her way of getting with traveler")
            elif pull == "Ayato":
                print("Has most likely stabbed someone")
            elif pull == "Kirara":
                print("Meow?")
            elif pull == "Sara":
                print("Eh")
            elif pull == "Shinobu":
                print("She hot")
            elif pull == "Ei":
                print("2 for 1 special")
            elif pull == "Kokomi":
                print("Kokomelon is fish lady")
            elif pull == "Sayu":
                print("I forget you exist ngl")
            elif pull == "Heizou":
                print("ACAB")
            elif pull == "Thoma":
                print("quite efficient cleaner")
            elif pull == "Yae Miko":
                print("Hot fox lady")
            elif pull == "Yoimiya":
                print("you really shouldn't be a 5 star")
            elif pull == "Alhaitham":
                print("Smarty pants")
            elif pull == "Candace":
                print("You are gorgeous omg")
            elif pull == "Collei":
                print("I will tear that fucker apart in your name")
            elif pull == "Cyno":
                print("I'd say ACAB, but you actually do your job right so you and you're bad, but funny jokes are cool \n but you're on thin fucking ice")
            elif pull == "Dehya":
                print("I love you, and they did you dirty with your kit.")
            elif pull == "Dori":
                print("You can join Dottore in his suffering. He will be the appetizer")
            elif pull == "Faruzan":
                print("you old ass Hatsune Miku looking mf")
            elif pull == "Kaveh":
                print("You are perf, and deserve better")
            elif pull == "Layla":
                print("Sleepiest little baby in the room")
            elif pull == "Nahida":
                print("You got games on your phone?")
            elif pull == "Nilou":
                print("you are v pretty, but you definitely shouldn't be a 5 star")
            elif pull == "Tighnari":
                print("I respect you, and the fact you kept Dottore at bay you funky lil mushroom enjoyer")
            elif pull == "Wanderer":
                print("You sure do talk a lot of shit for someone who I can easily rename babygirl")
            elif pull == "Charlotte":
                print("Why does your healing passive only work better the more fontainians are in your team?\nYou racist or something??")
            elif pull == "Chevreuse":
                print("Such a snacky fiend you are wonderful.")
            elif pull == "Freminet":
                print("I'm sorry you look goofy with in your ult")
            elif pull == "Furina":
                print("Hi you are perfect, and deserve whatever you want. You worked so hard. ilysm")
            elif pull == "Lynette":
                print("I wish to give you a forehead kith")
            elif pull == "Lyney":
                print("A small Inazuman woman with a sword heard that you were trying to hook up with The Traveler\nI would run")
            elif pull == "Navia":
                print("I'll come back for you I swear")
            elif pull == "Neuvillette":
                print("Oratrice Mecanique D'analyse Cardinale")
            elif pull == "Wriothesley":
                print("Keep your tea away from Rice Cake over here")
            elif pull == "Clorinde":
                print("How is your top button holding up?")
            elif pull == "Sigewinne":
                print("You are a sneaky lil hoe. I love you")
            elif pull == "Childe":
                print("Ready for all the Childe abuse??")
            elif pull == "Arlecchino":
                print("You are no longer Fatherless congrats")
            else:
                print("Havent done one for you yet. wait your turn")
    else:
        print("oh ok have a nice gamble free day sir")
while True:
    wish(input("do you wanna make a wish? yes or no? "))
#print(len(pc))