stars = []
shine = []
def addstars(x):
    if len(x) < 6 :
        print("alright here is a mf star")
        x.append("*")
        print(x)
    else:
        print("alright you got enough stars damn")

while input("you want some fuckin stars?\n\n")!= "no":
    addstars(stars)
    
def ask():
    return input("do you want to check if you have stars or shine?")

question = ask()

def test(x):
    while x != "no":
        for i in range(1):
            if x == "yes":
                asking = (input("ok do you want stars or do you want shine??\n\n"))
                if asking == "stars":
                    print(stars)
                    x = input("do you want to check another?\n\n")
                elif asking == "shine":
                    print(shine)
                    x = input("do you want to check another?\n\n")
                else:
                    print("\nyeah I can't help you with that big homie")
                    x = input("do you want to check another?")
            elif x != "yes":
                print("I need a yes or a no lil homie")
                x = input("so yes or no?\n\n")
test(question)