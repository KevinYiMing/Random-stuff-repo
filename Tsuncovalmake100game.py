import random
options = [0,0,0,0]
selected = False
run = True
currentnumber = 0
while run:
    play = input("W-well, since you asked... m-make p-perfect 100! if you insist type: play... d-don't read into it!" + "\n").lower()
    if play == "quit" or play == "no":
        print("D-Don't get the wrong idea! h-hmmff f-f-f-fine I didn't want to play a-anyways... i-it's whatever.")
        run = False
    elif play !=  "play":
        print("Ugh, why haven't you typed 'play' yet, idiot?! It's not like I care or anything! I just thought it would be more fun if you did, okay?! D-Don't get the wrong idea!")
        play = input("D-Don't get the wrong idea! p-play game! if you i-insist type: play... n-not that I care or anything!"+ "\n").lower()
    else:
        while True:
            print("\nc-currently the number is on " + str(currentnumber) + "/100... n-not that I care or anything!" )
            for i in range (4):
                options[i] = random.randint(1,11)
            picked = input(str(options) + " Hmph! Fine! w-which number do you want to pick Hmph, it's not like I'm waiting!"+ "\n")
            for i in range (4):
                if str(options[i]) == picked:
                    currentnumber += int(picked)
                    break
            else:
                print("\nU-ugh! Seriously, you didn't even bother to pick an option, huh? Not that I care or anything! I just... I mean, whatever! Just don’t make me wait next time, okay?! It's not like I’m worried or anything... Hmph!")

            if currentnumber == 100:
                print("\nHmph! I-I guess you managed to win this time, but it’s not like I’m impressed or anything! D-Don’t get cocky, okay? It’s just a fluke!")
                break
            elif currentnumber > 100:
                print("\nW-What are you looking so smug for, idiot? It's not like it matters to me that you lost! I-I just didn’t want you to win anyway! Hmph!")
                break