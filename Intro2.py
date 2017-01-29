run = True
def put():
    put = input("Continue (Yes/No): ").lower()
    print("\n")
    return put # most common input
def put2(): # inputs for broom closet
    put = input("Turn around and go to staircase? (Yes/No): ").lower()
    print("\n")
    return put
def put3(): # inputs for Coward
    put = input("Leave Room 427? (Yes/No): ").lower()
    print("\n")
    return put
def possible_exit(): #put3.5()
    put = input("End Game? (Yes/No): ")
    print("\n")
    return put
def start_over():
    for i in range(50):
        print("\n")

def Intro():
    print(" \'This is the story of a man named Stanley.\' ")
    inp = input("Continue? (Yes): ").lower()
    line = 0
    while True:
        if inp == "yes":
            if line == 0:
                print(" \'Stanley worked for a company in a big building where he was Employee #427. \n Employee #427's job was simple: he sat at his desk in room 427 and he pushed buttons on a keyboard. \n Orders came to him through a monitor on his desk, telling him what buttons to push, how long to push them, and in what order.\'")
            elif line == 1:
                print("\'This is what Employee #427 did every day of every month of every year, and although others might have considered it soul rending, \n Stanley relished every moment the orders came in, as though he had been made exactly for this job. And Stanley was happy.\' ")
            elif line == 2:
                print("\'And then one day, something very peculiar happened. \n Something that would forever change Stanley; something he would never quite forget.\n He had been at his desk for nearly an hour when he realized that not one single order had arrived on the monitor for him to follow.\' ")
            elif line == 3:
                print("\'No one had shown up to give him instructions, call a meeting, or even say \'hi.\' \n Never in all his years at the company had this happened, this complete isolation. \n Something was very clearly wrong.\' ")
            else:
                print("\'Shocked, frozen solid, Stanley found himself unable to move for the longest time. \n But as he came to his wits and regained his senses, he got up from his desk and stepped out of his office.\'")
                break
            line += 1
            inp = input("\nContinue? (Yes): ").lower()
        elif inp == "no":
            print(" \'But the game has just started!\'")
            inp = input("Continue? (Yes): ").lower()
        elif inp != "yes":
            print(" \'You must be mistaken, that is not a proper commmand\'")
            inp = input("Continue? (Yes): ").lower()
        else:
            while True:
                inp = possible_exit()
                if inp == "yes":
                    exit()
                else:
                    print("\'Well aren't you RUDE\'")
    inp = put3()
    while inp != "yes" and inp != "no":
        print("\'That's not a valid input!\'")
        inp = put3()
    if inp == "no":
        Coward()
    else:
        To_Doors()

def To_Doors():
    print1()
    door = Doors() # True is left door, False is right door
    if door == True:
        to_Boss()
        upstairs = Stairs() # True if going up, False if going down
        if upstairs == False:
            DownStairs()
        else:
            UpStairs()

def Coward():
    print("\n\'But Stanley simply couldn't handle the pressure. \n He re-entered his office and closed the door.\'")
    inp = put3()
    line = 0
    if inp == "no":
        while True:
            inp = put()
            if inp == "yes":
                if line == 0:
                    print("\'What if he had to make a decision? \n What if a crucial outcome fell under his responsibility? \n He had never been trained for that! \n No, this couldn't go any way except badly.\'")
                elif line == 1:
                    print("\'The right thing to do now, Stanley thought to himself, is to wait. \n Nothing will hurt me. \n Nothing will break me. \n  In here, I can be happy, forever. \n I will be happy.\'")
                elif line == 2:
                    print("\'Stanley waited. \nHours passed.\n Then days.\n Had years gone by? \nHe no longer had the ability to tell. \nBut the one thing he knew for sure, beyond any doubt, was that if he waited long enough, \nthe answers would come.\n Eventually, some day, they would arrive. \nSoon, very soon now, this will end. \nHe will be spoken to.\n He will be told what to do.\n Now it's just a little bit closer.\n\nNow it's even closer. \n\nHere it comes.\' ")
                    exit()
            elif inp != "no" and inp != "yes":
                print(" \'You must be mistaken, that is not a proper commmand \'")
                inp = put()
            else:
                print(" \'It's too late to stop Stanley. \nThis is happening \'")
            line += 1

    elif inp == "yes":
        print("\'Stanley stepped out of his office again\'")
        To_Doors()

def print1():
    print("\'All of his co-workers were gone.  What could it mean?\'")
    print(" \'Stanley decided to go to the meeting room; perhaps he had simply missed a memo. \'")
    print("\'When Stanley came to a set of 2 open doors, he entered the door on his left.\'")#All of his co-workers were gone...etc

def Doors():
    inp = input("Enter which door? (Left/Right): ").lower()
    if inp == "left":
        return True
    elif inp == "right":
        print("\n\'I said, Stanley entered the door on his left\'")
        inp = input("Enter which door? (Left/Right): ").lower()
        if inp == "left":
            return True
        elif inp == "right":
            print("\n\'I said left dammit!\'")
            inp = input("Enter which door? (Left/Right): ").lower()
            if inp == "left":
                return True
            elif inp == "right":
                print("\n\'Fine, have it your way\'")
                return False
            else:
                print("\'That's not a door, silly!\'")
                return Doors()
        else:
            print("\'That's not a door, silly!\'")
            return Doors()
    else:
        print("\'That's not a door, silly!\'")
        return Doors()

def to_Boss():
    print("\n\'Stanley entered the meeting room. \nYet there was not a single person here either. \nFeeling a wave of disbelief, Stanley decided to go up to his boss's office, hoping he might find an answer there.\'")
    inp = put()
    line = 0
    while True:
        if inp == "yes":
            if line == 0:
                print("\'Stanley entered the hallway that led to the staircase\'")
                line += 1
                inp = put()
            elif line == 1:
                print("\'Stanley saw a broom closet to his left, but walked right past it.\'\n")
                Broom_Closet()
                break
        elif inp == "no":
            print("\'Okay... I guess we can stay here.\'")
            inp = put()
        else:
            print("\'That's not a valid input!\'")
            inp = put()

def Broom_Closet():
    broom = input("Enter broom closet?: (Yes/No): ").lower()
    while broom != "yes" and broom != "no":
        print("\'That's not a valid input!\'")
        broom = input("Enter broom closet?: (Yes/No): ").lower()
    if broom == "yes":
        print("\'Stanley stepped into the broom closet, but there was nothing here, so he turned around and got back on track.\'")
        inp = put2()
        line = 0
        while inp != "yes":
            if line == 0:
                print("\'There was nothing here. \nNo choice to make. \nNo path to follow. \nJust an empty broom closet. \nNo reason to still be here.\'")
                inp = put2()
                line += 1
            elif line == 1:
                print("\'It was baffling that Stanley was still just sitting in the broom closet. \nHe wasn't even doing anything. \nAt least if there was something to interact with, he'd be justified in some way. \nAs it is, he's literally just standing there.\'")
                inp = put2()
                line += 1
            elif line == 2:
                print("\'Are you...\n Are you really still in the broom closet? \nStanding around doing nothing? \nWhy? \nPlease offer me some explanation here; \nI'm- I'm genuinely confused.\'")
                inp = put2()
                line += 1
            elif line == 3:
                print("\'You do realize there's no choice or anything in here right? \nThis closet, is of absolutely, no significance to the story, whatsoever.\'")
                inp = put2()
                line += 1
            elif line == 4:
                print("\'Maybe to you, this is somehow it's own branching path. \nMaybe, when you go talk about this with your friends, you'll say: \n\"OH! DID U GET THE BROOM CLOSET ENDING? THEB ROOM CLOSET ENDING WAS MY FAVRITE!1 XD\" \nI hope your friends find this concerning. \'")
                inp = put2()
                line += 1
            elif line == 5:
                print("\'Stanley was fat and ugly, and really, really stupid. \nHe probably only got the job because of a family connection; that's how stupid he is. \nThat, or with drug money. \nAlso, Stanley is addicted to drugs and hookers. \'")
                inp = put2()
                line += 1
            elif line == 6:
                print("\'Well, I've come to a very definite conclusion about what's going on right now. \nYou're dead. \nYou got to this broom closet, explored it a bit, \nand were just about to leave because there's nothing here, \nwhen a physical melody of some sort shut down your central nervous system and you collapsed on the keyboard, constantly typing \'No\'. \nWell, in a situation like this, \nthe responsible thing is to alert someone nearby so as to ensure that your body is taken care of, \nbefore it begins to decompose. \'")
                inp = put2()
                line += 1
            elif line == 7:
                print("\'HELLO!? ANYONE WHO HAPPENS TO BE NEARBY!! \nTHE PERSON AT THIS COMPUTER IS DEAD!! \nHE OR SHE HAS FALLEN PREY TO ANY NUMBER OF YOUR COUNTLESS HUMAN PHYSIOLOGICAL VULNERABILITIES. \nIT'S INDICATIVE OF THE LONG-TERM SUSTAINABILITY OF YOUR SPECIES. PLEASE REMOVE THEIR CORPSE FROM THE AREA AND INSTRUCT ANOTHER HUMAN TO TAKE THEIR PLACE AT THE COMPUTER, \nMAKING SURE THEY UNDERSTAND BASIC FIRST-PERSON VIDEO GAME MECHANICS, \nAND FILLING THEM IN ON THE HISTORY OF NARRATIVE TROPES IN VIDEO GAMING, \nSO THAT THE IRONY AND INSIGHTFUL COMMENTARY OF THIS GAME IS NOT LOST ON THEM. \'")
                inp = put2()
                line += 1
            else:
                print("\'Alright, I'm done, just step out into the hallway. \'")
                inp = put2()
        else:
            print("\'Good, that closet is a waste of time anyway.\n Plus I'm allergic to dust. And sponges\'")
    else:
        print("\'Good, that closet is a waste of time anyway.\n Plus I'm allergic to dust. And sponges\'")

def Stairs():
    print("\'\nComing to a staircase, Stanley walked upstairs to his boss's office.\'")
    inp = input("Walk upstairs or downstairs? (Up/Down): ").lower()
    if inp == "up":
        return True
    elif inp == "down":
        return False
    else:
        print("\'That's not a direction, silly!\'")
        return Stairs()

def DownStairs():
    print("\'But Stanley just couldn't do it.\'")
    inp = put()
    line = 0
    while True:
        if line == 0:
            print("\'He considered the possibility of facing his boss, \nadmitting he had left his post during work hours, \nhe might be fired for that. \nAnd in such a competitive economy, why had he taken that risk? \'")
            line += 1
            inp = put()
        elif line == 1:
            print("\'All because he believed everyone had vanished? \nHis boss would think he was crazy.\nAnd then something occurred to Stanley: Maybe, he thought to himself, maybe I am crazy. \nAll of my coworkers blinking mysteriously out of existence in a single moment for no reason at all? \'")
            line += 1
            inp = put()
        elif line == 2:
            print("\'For example, why couldn't he see his feet? \nOr his arms? \nOr feel his face? \nWas he even real? \nHe'd been walking downstairs for ages. \nWhere was this staircase even going?! \'")
            line += 1
            inp = put()
        elif line == 3:
            print("\'Why did he constantly feel like someone was asking him to Continue (Yes/No). \nHe was going to continue regardless of the answer. \nWhat does (Yes/No) even mean?!!? \'")
            line += 1
            inp = put()
        elif line == 4:
            print("\'\nAnd then perhaps the strangest question of them all entered Stanley's head, \none he was amazed he hadn't asked himself sooner: \nWhy is there a voice in my head, dictating everything that i'm doing and thinking? \'")
            line += 1
            inp = put()
        elif line == 5:
            print("\'No, Stanley said to himself, this is all too strange, this can't be real, \nand at last he came to the conclusion that had been on the tip of his tongue, \nhe just hadn't found the words for it. \nI'm dreaming! he yelled, \nThis is all a dream! \'")
            line += 1
            inp = put()
        elif line == 6:
            print("\'Now the voice was describing itself being considered by Stanley, \nwho found it particularly strange. \nI'm dreaming about a voice describing me thinking about how it's describing my thoughts, he thought! \nAnd while he thought it all very odd and wondered if this voice spoke to all people in their dreams, \nthe truth was that of course this was not a dream. \nHow could it be? \'")
            line += 1
            inp = put()
        elif line == 7:
            print("\'Stanley was still wakling down the godforsaken staircase! \nWhy hadn't he just chosen to go upstairs! \nWhy hadn't he followed the handsome voice's directions!  \'")
            line += 1
            inp = put()
        elif line == 8:
            print("\'He would prove it. \nHe would prove that he was in control, that this was a dream. \nSo he closed his eyes gently, and he invited himself to wake up. \'")
            line += 1
            inp = put()
        elif line == 9:
            start_over()
            line += 1
            inp = put()
        elif line == 10:
            print("\'Stanley opened his eyes. \nHe was still on the staircase! \nPlease just someone tell me i'm real! \nI must be real! \nI must be! \nCan anyone hear my voice?! \nWho am I? \n\nWho am I?!\'")
            line += 1
            inp = put()
        elif line == 11:
            start_over()
            line += 1
            inp = put()
        elif line == 12:
            print("\'This is the story of a woman named Mariella \'")
            line += 1
            inp = put()
        elif line == 13:
            print("\'Mariella woke up on a day like any other. \nShe arose, got dressed, gathered her belongings, and walked to her place of work. \'")
            line += 1
            inp = put()
        elif line == 14:
            print("\'But on this particular day, \nher walk was interrupted by the body of a man who had stumbled through town talking and screaming about a staircase \nand then collapsed dead on the sidewalk. \'")
            line += 1
            inp = put()
        elif line == 15:
            print("\'He was obviously crazy; this much she knew. \nEveryone knows what crazy people look like. \nAnd in that moment, she thought to herself how lucky she was to be normal. \'")
            line += 1
            inp = put()
        else:
            print("\'And then she turned and ran.\'")
            exit()

def UpStairs():
    print("\n\'Peering into his manager's office, Stanley was once again stunned to discover not an indication of any human life. \nShocked, unraveled, Stanley wondered in disbelief who orchestrated this. \nWhat dark secret was being held from him?  \'")
    inp = input("\nStep into the manager's office? (Yes/No): ").lower()
    if inp == "no":
        Escape_Pod()
    else:
        Manager_Office()

def Escape_Pod():
    print("\n\'Now why wouldn't you step into the manager's office?! \nThat's where the rest of the story is! \nSigh...\nLet's try this again\'")
    inp = input("Step into the manager's office? (Yes/No): ").lower()
    if inp == "yes":
        print("\n\'Thank you for being sensible.\'")
        Manager_Office()
    else:
        print("\n\'Fine, let just get going. \nStanley turned around and walked down the stairs.\'")
        inp = put()
        line = 0
        resp = 1
        while True:
            if inp == "yes":
                print(1)
            elif inp == "no":
                if resp == 0:
                    print("\'I DON'T CARE, THIS TIME WE'RE GOING IN THE DANG BROOM CLOSET\'")
                    resp += 1
                    inp = put()
            else:
                print("\n\'THAT'S NOT A VALID INPUT!!!!\'")
                inp = put()

def Manager_Office():
    print("\n\'Stepping into his manager's office, Stanley was once again stunned to discover not an indication of any human life. \nShocked, unraveled, Stanley wondered in disbelief who orchestrated this. What dark secret was being held from him? \nWhat he could not have known was that the keypad behind the boss's desk guarded the terrible truth that his boss had been keeping from him. \nAnd so the boss had assigned it an extra secret PIN #. 2845. \nBut of course, Stanley couldn't possibly have known this.\'")
    inp = input("Input PIN: ")
    line = 0
    while True:
        if inp == "2845":
            To_Mind_Control()
        else:
            if line == 0:
                print("\n\'Stanley began random codes into the keypad, knowing full well that the sheer statistical unlikelihood that this would result in a correct combination. \nIf he knew that the combo was 2-8-4-5, it would be another story entirely. \nBut no. No, this is what he's going to do instead. \'")
                inp = input("Input PIN: ")
                line += 1
            elif line == 1:
                print("\n\'Stanley just sat around twiddling his thumbs. \nTrying to input anything into the device was useless, \nsince he could never possibly know that the combination was 2-8-4-5. \'")
                inp = input("Input PIN: ")
                line += 1
            elif line == 2:
                print("\n\'2-8-4-5\'")
                inp = input("Input PIN: ")
                line += 1
            else:
                print("\n\'For god's- but it turns out that the panel's emergency override kicked in, \nand the door just opened all by itself, and Stanley just got the hell along with the story. \nWell woop-de-doo.\'")
                To_Mind_Control()

def To_Mind_Control():
    print("\n\'Yet incredibly, by simply pushing random buttons on the keypad, Stanley happened to input the correct code by sheer luck. \nAmazing. He stepped into the newly opened passageway.\'")
    inp = input("Continue? (Yes): ").lower()
    while True:
        if inp == "yes":
            print("\n\'Descending deeper into the building, Stanley realized he felt a bit peculiar. \nIt was a stirring of emotion in his chest, as though he felt more free to think for himself, to question the nature of his job. \nWhy did he feel this now, when for years it had never occurred to him? \n\nThis question would not go unanswered for long. \'")
            way = Escape_or_Mind_Control() #True for Mind Control, False for Escape
            if way == True:
                print(1)
                #Mind_Control_Facility():
            else:
                Escape_Hallway():
        else:
            print(" \'You must be mistaken, that is not a proper commmand\'")
            inp = input("Continue? (Yes): ").lower()

def Escape_or_Mind_Control():
    print("\n\'In front of Stanley was a large room labelled \"Mind Control Facility\"\nTo his left was a hallway labelled \"Escape\"\n \'")
    inp = input("Continue? (Yes): ").lower()
    while True:
        if inp != "yes":
            print ("\n\'That\'s not an option.")
        else:
            print("\n\'Stanley walked straight ahead through the large door that read Mind Control Facility.\'")
            break
    inp = input("Walk where? (Facility/Escape): ").lower()
    while True:
        if inp == "facility":
            return True
        elif inp == "escape":
            return False
        else:
            print ("\n\'That\'s not an option.")
            print("\n\'Stanley walked straight ahead through the large door that read Mind Control Facility.\'")
            inp = input("Walk where? (Facility/Escape): ").lower()

def Escape_Hallway():
    before = False
    print("\n\'Although this passageway had the word 'Escape' written on it, the truth was, \nthat at the end of this hall, Stanley would meet his violent death. \'")
    while True:
        inp = input("Turn Around? (Yes/No): ").lower()

while run == True:
    Intro()




if run == False:
    print("\'The game is over. Goodbye!\'")
