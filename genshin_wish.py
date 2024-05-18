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
diluccons = []
dionacons = []
eulacons = []
fischlcons = []
jeancons = []
kaeyacons = []
kleecons = []
lisacons = []
mikacons = []
monacons = []
noellecons = []
razorcons = []
rosariacons = []
sucrosecons = []
venticons = []

def wish(x):
    while x != "no":
        for i in range(1):
            if x == "yes":
                pull = pc[random.randint(0,80)]
                pull2 = "\n" + pull + "\n"
                print(pull2)
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
                        print("so is your wing glider license up to date?")
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
                    if len(diluccons) == 0:
                        print("I'm not saying he's Mondstadt Batman, but I've never seen him and Mondstadt Batman in the same room")
                        diluccons.append("*")
                    elif len(diluccons) == 1:
                        print("Birb man")
                        diluccons.append("*")
                    elif len(diluccons) == 2:
                        print("careful I hear a small cat child is trying to run you out of business")
                        diluccons.append("*")
                    elif len(diluccons) == 3:
                        print("I know you like birbs, but please leave the birb lady in Liyue alone.")
                        diluccons.append("*")
                    elif len(diluccons) == 4:
                        print("I'm sorry to tell you this homie, but a lot of people say you look weird \n\nI like your sense of style tho.")
                        diluccons.append("*")
                    elif len(diluccons) == 5:
                        print("Quick I hear Kaeya is having a good day. We can't have that now can we?")
                        diluccons.append("*")
                    elif len(diluccons) == 6:
                        print("come on we're friends by now with all the time we've spent together.\n\nYou can be honest with me\n\nYou got anything to do with Mondstadt Batman??")
                    x = input("do you want to do another?\n\n")
                elif pull == "Diona":
                    if len(dionacons) == 0:
                        print("she sniffin for alcohol on your breath")
                        dionacons.append("*")
                    elif len(dionacons) == 1:
                        print("you got alcyhols on your phone?")
                        dionacons.append("*")
                    elif len(dionacons) == 2:
                        print("How's your goal of getting rid of alcohol goin")
                        dionacons.append("*")
                    elif len(dionacons) == 3:
                        print("*pulls out a cat teaser*")
                        dionacons.append("*")
                    elif len(dionacons) == 4:
                        print("wild how you saved an oceanid, and now you can't make a bad drink... hmm")
                        dionacons.append("*")
                    elif len(dionacons) == 5:
                        print("I'm surprised you havent just tried to destroy the dawn winery plants")
                        dionacons.append("*")
                    elif len(dionacons) == 6:
                        print("ok fine I'll build you... but I ain't happy about it.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Eula":
                    if len(eulacons) == 0:
                        print("God she's hot")
                        eulacons.append("*")
                    elif len(eulacons) == 1:
                        print("I promise next time I will pull for you relentlessly")
                        eulacons.append("*")
                    elif len(eulacons) == 2:
                        print("I hate that people are mean to you bc of who your family is.")
                        eulacons.append("*")
                    elif len(eulacons) == 3:
                        print("Not gonna lie your theme is a bop")
                        eulacons.append("*")
                    elif len(eulacons) == 4:
                        print("Your fighting style is so gd graceful")
                        eulacons.append("*")
                    elif len(eulacons) == 5:
                        print("you can have revenge or anything else you got")
                        eulacons.append("*")
                    elif len(eulacons) == 6:
                        print("I made you some Jelly desserts ily")
                    x = input("do you want to do another?\n\n")
                elif pull == "Fischl":
                    if len(fischlcons) == 0:
                        print("she is O-fischl-y yours... ok I'll stop asking Cyno for jokes")
                        fischlcons.append("*")
                    elif len(fischlcons) == 1:
                        print("Do you go flex your talking lightning birb to Diluc a lot? you should.")
                        fischlcons.append("*")
                    elif len(fischlcons) == 2:
                        print("god you would love the internet.")
                        fischlcons.append("*")
                    elif len(fischlcons) == 3:
                        print("your bestie randomly got trapped in a domain again. he needs you rn")
                        fischlcons.append("*")
                    elif len(fischlcons) == 4:
                        print("you're giving real gamer energy")
                        fischlcons.append("*")
                    elif len(fischlcons) == 5:
                        print("you got some fun energy ily")
                        fischlcons.append("*")
                    elif len(fischlcons) == 6:
                        print("wait wasn't your ass in Honkai Impact 3rd?")
                    x = input("do you want to do another?\n\n")
                elif pull == "Jean":
                    if len(jeancons) == 0:
                        print("Sir put the work down")
                        jeancons.append("*")
                    elif len(jeancons) == 1:
                        print("go find your sister and flex your height on her")
                        jeancons.append("*")
                    elif len(jeancons) == 2:
                        print("your girlf- I mean your librarian wants to see you")
                        jeancons.append("*")
                    elif len(jeancons) == 3:
                        print("Klee is beelining for the lake again.")
                        jeancons.append("*")
                    elif len(jeancons) == 4:
                        print("why are your attack animations so stiff for??")
                        jeancons.append("*")
                    elif len(jeancons) == 5:
                        print("dropkick the actual grandmaster whenever you see them.")
                        jeancons.append("*")
                    elif len(jeancons) == 6:
                        print("Quickly a mandatory vacation is coming. run!")
                    x = input("do you want to do another?\n\n")
                elif pull == "Kaeya":
                    if len(kaeyacons) == 0:
                        print("Just waiting for the next Khaenri'ah lore dump funny immortal man")
                        kaeyacons.append("*")
                    elif len(kaeyacons) == 1:
                        print("inherited the eyepatch and hairstyle my ass")
                        kaeyacons.append("*")
                    elif len(kaeyacons) == 2:
                        print("Noelle is about to solo the dragon. Quickly Kaeya distract her!")
                        kaeyacons.append("*")
                    elif len(kaeyacons) == 3:
                        print("Go yoink some expensive wine from your brother's bar. It would be funni")
                        kaeyacons.append("*")
                    elif len(kaeyacons) == 4:
                        print("tbh you were the first free tall character, and that means your served an important exploring role.")
                        kaeyacons.append("*")
                    elif len(kaeyacons) == 5:
                        print("Maybe now you're strong enough to stand up to Jean when you slack off (lol no)")
                        kaeyacons.append("*")
                    elif len(kaeyacons) == 6:
                        print("lol 35 damage")
                    x = input("do you want to do another?\n\n")
                elif pull == "Klee":
                    if len(kleecons) == 0:
                        print("I'm scared of that thing")
                        kleecons.append("*")
                    elif len(kleecons) == 1:
                        print("You see those fish over there existing peacefully?\nI heard they talkin mad smack")
                        kleecons.append("*")
                    elif len(kleecons) == 2:
                        print("your mom got some fucked up ideas (I'll probably pull for her tho ngl)")
                        kleecons.append("*")
                    elif len(kleecons) == 3:
                        print("My god do you have an awesome childhood.")
                        kleecons.append("*")
                    elif len(kleecons) == 4:
                        print("Jean is distracted go teach those bitch ass fish a lesson.")
                        kleecons.append("*")
                    elif len(kleecons) == 5:
                        print("Is likely to terraform your lake if you're not careful")
                        kleecons.append("*")
                    elif len(kleecons) == 6:
                        print("I like your dodoco tho ngl")
                    x = input("do you want to do another?\n\n")
                elif pull == "Lisa":
                    if len(lisacons) == 0:
                        print("Lemme smash before you go")
                        lisacons.append("*")
                    elif len(lisacons) == 1:
                        print("Quite literally will be granted a vision for her convenience")
                        lisacons.append("*")
                    elif len(lisacons) == 2:
                        print("Hey I hear those hilichurls stole books from you\n get em")
                        lisacons.append("*")
                    elif len(lisacons) == 3:
                        print("I'm just waiting for you to accidentally give klee the knowledge to make a nuke.")
                        lisacons.append("*")
                    elif len(lisacons) == 4:
                        print("I love hearing about your time in Sumeru ngl")
                        lisacons.append("*")
                    elif len(lisacons) == 5:
                        print("You need to work your magic and help Jean relax more")
                        lisacons.append("*")
                    elif len(lisacons) == 6:
                        print("genuinely I hope you don't die before the story is over.")
                    x = input("do you want to do another?\n\n")
                elif pull == "Mika":
                    if len(mikacons) == 0:
                        print("you better take care of Noelle >:(")
                        mikacons.append("*")
                    elif len(mikacons) == 1:
                        print("I can respect you wanting to be a cartographer...\nIgnore the fact I have a self updating map of Teyvat")
                        mikacons.append("*")
                    elif len(mikacons) == 2:
                        print("I mean you're kinda just here ngl")
                        mikacons.append("*")
                    elif len(mikacons) == 3:
                        print("Don't let Huffman yuck your yum")
                        mikacons.append("*")
                    elif len(mikacons) == 4:
                        print("you should shoot shoot that crossbow at electro things to make things explode near some hilichurls")
                        mikacons.append("*")
                    elif len(mikacons) == 5:
                        print("you'd be a great camp guide I'm sure")
                        mikacons.append("*")
                    elif len(mikacons) == 6:
                        print("you are max stronk")
                    x = input("do you want to do another?\n\n")
                elif pull == "Mona":
                    if len(monacons) == 0:
                        print("No Mora Mona")
                        monacons.append("*")
                    elif len(monacons) == 1:
                        print("First water runny woman")
                        monacons.append("*")
                    elif len(monacons) == 2:
                        print("Lemme make you Mona")
                        monacons.append("*")
                    elif len(monacons) == 3:
                        print("I love how you decided to make one of your attacks just you essentially flipping off your enemies")
                        monacons.append("*")
                    elif len(monacons) == 4:
                        print("Don't think about how the sky is fake...")
                        monacons.append("*")
                    elif len(monacons) == 5:
                        print("Get the fuckin cat")
                        monacons.append("*")
                    elif len(monacons) == 6:
                        print("You'd think with this many constellations that one of them would give you the skill of responsible financial planning")
                    x = input("do you want to do another?\n\n")
                elif pull == "Noelle":
                    print("too precious for this world. Stop endagering yourself, and work as a team >:(")
                    x = input("do you want to do another?\n\n")
                elif pull == "Razor":
                    if len(razorcons) == 0:
                        print("Oh look prototype Cyno")
                        razorcons.append("*")
                    elif len(razorcons) == 1:
                        print("I hope those wolves taught you how to bathe")
                        razorcons.append("*")
                    elif len(razorcons) == 2:
                        print("You have simple enjoyments, I can respect that")
                        razorcons.append("*")
                    elif len(razorcons) == 3:
                        print("I hear you like potatoes")
                        razorcons.append("*")
                    elif len(razorcons) == 4:
                        print("I wanna meet you family and pet them ngl.")
                        razorcons.append("*")
                    elif len(razorcons) == 5:
                        print("I hope you never get into a fight with Cyno, even with all this stronk")
                        razorcons.append("*")
                    elif len(razorcons) == 6:
                        print("Make your guardian wolf thing flex their muscles. it would be funni")
                    x = input("do you want to do another?\n\n")
                elif pull == "Rosaria":
                    if len(rosariacons) == 0:
                        print("I support your devotion to not work")
                        rosariacons.append("*")
                    elif len(rosariacons) == 1:
                        print("I love how you and your potential girlfriend are working on your cat shelter together")
                        rosariacons.append("*")
                    elif len(rosariacons) == 2:
                        print("If you stand veeeeerrrryyy still then maybe the sisters won't see you and give you work")
                        rosariacons.append("*")
                    elif len(rosariacons) == 3:
                        print("Fuck they spotted you run!")
                        rosariacons.append("*")
                    elif len(rosariacons) == 4:
                        print("I'll give those treasure hoarders an extra stab for you I gotchu")
                        rosariacons.append("*")
                    elif len(rosariacons) == 5:
                        print("I wanna try some of that wild looking Sweet Madame you make.")
                        rosariacons.append("*")
                    elif len(rosariacons) == 6:
                        print("Ok I have nothing funny left to add here hot church lady")
                    x = input("do you want to do another?\n\n")
                elif pull == "Sucrose":
                    if len(sucrosecons) == 0:
                        print("Sweetest little baby in the room.")
                        sucrosecons.append("*")
                    elif len(sucrosecons) == 1:
                        print("I love how everything about you is related to sugar and sweetness")
                        sucrosecons.append("*")
                    elif len(sucrosecons) == 2:
                        print("*joins hilichurls in kicking the shit out of Pallad*")
                        sucrosecons.append("*")
                    elif len(sucrosecons) == 3:
                        print("Sucrose.. sweet babygirl your ex friends didn't deserve you")
                        sucrosecons.append("*")
                    elif len(sucrosecons) == 4:
                        print("you think I look smart with my glasses? Thanks! I had to fail a test to get them.")
                        sucrosecons.append("*")
                    elif len(sucrosecons) == 5:
                        print("I would kill for you")
                        sucrosecons.append("*")
                    elif len(sucrosecons) == 6:
                        print("Mr. Albedo check this shit out")
                    x = input("do you want to do another?\n\n")
                elif pull == "Venti":
                    if len(venticons) == 0:
                        print("I know you're hiding something you fucking twink")
                        venticons.append("*")
                    if len(venticons) == 1:
                        print("You terraformed so much of Mondstadt to where the highest peak is now the sea level... what are you hiding air twink")
                        venticons.append("*")
                    if len(venticons) == 2:
                        print("Anemo Elevator; and Air-levator if you will.")
                        venticons.append("*")
                    if len(venticons) == 3:
                        print("You only come back when you are needed so.. what the fuck is coming you scantily clad deity")
                        venticons.append("*")
                    if len(venticons) == 4:
                        print("I swear on your last banner you looked like Rice Cake's twink bf")
                        venticons.append("*")
                    if len(venticons) == 5:
                        print("Ngl you were adorable as a wind spirit")
                        venticons.append("*")
                    if len(venticons) == 6:
                        print("I hope you aren't on a banner with a cooler character bc I wanna complete my Archon collection")
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
def bonus(x):
    if x == "yes":
        print("Crease his Jordans Mr. Svarog\n\n")

bonus(input("would you like a secret bonus?\n\n"))

print("Ok have a nice day :)")
#print(len(pc))