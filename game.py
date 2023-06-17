# Hungman
# These is the code for Hungman game in python, I have tried it works good...

# >>>>> Rules of Hungman.
# First wrong answer: Draw and upside-down "L." This is the post the man hangs from.
# Second: Draw a small circle for the "head" underneath the horizontal line of the "L."
# Third: Draw a line down from the bottom of the head for the "body."
# Fourth: Draw one arm out from the middle of his body for the "arm."
# Fifth: Draw the other arm.
# Sixth: Draw one diagonal line from the bottom of the body for the first "leg."
# Seventh: Draw the other leg.
# Eighth: Connect the head to the post with a "noose." Once you draw the noose the players have lost the game.

import random

# from getkey import getkey,key

def check(word_1,word_2):
    if(len(word_1)==len(word_2)):
        return 1
    else:
        return 0


def fails(val):
    if val==7:
        print("The line had dwawn like 'L'.....")
    elif val==6:
        print("The head is created....")
    elif val==5:
        print("The body is created....")
    elif val==4:
        print("The left arm is created....")
    elif val==3:
        print("The right arm is created....")
    elif val==2:
        print("The left leg is created....")
    elif val==1:
        print("The right leg is created....")
    else:
        print("The person is died..................................")

def game(random_word):
    random_word=random_word.upper()  # update word into upper case..
    random_word_duplicate=random_word # Create Duplicate word of random word
    random_word_size=len(random_word_duplicate) # store size of a word
    # print(random_word)
    wilo=8 # There are 8 chance to crack word..
    # yourword='____________________'   # make the space for your word .
    yourword="_"*(random_word_size)
    # yourword=yourword[:random_word_size]+'\0'+yourword[random_word_size+1:]
    print(yourword[:random_word_size]) # Display yourword upto real size...
    print(f"The numbers of letter of word {random_word_size}")  # Give hint to you the word size..
    temp_word="Error"
    while wilo!=0:  # Start the loop for upto 8 chance..
        if check(yourword,random_word)!=1:
            # your_new_word="_"*(random_word_size)
            your_new_word='_'+yourword[0:]
            yourword=your_new_word
            random_word=random_word[-1:0]+random_word_duplicate[0]+random_word[1:]
            yourword=yourword[-1:0]+temp_word[0]+yourword[1:]
            print(your_new_word)
            print(random_word)
        letter=input("Enter the letter or word that you think that it is in the word or that is word...\t")  # Take a letter or a word
        letter=letter.upper() #Make your word in upper case
        temp_word=yourword
        if letter in random_word or letter ==random_word_duplicate: # Check is your letter or word is equal the word or present in the word.
            t=random_word.find(letter)  # find your word position in the word
            random_word=random_word[:t]+'-'*len(letter)+random_word[t+len(letter):]    # update your random word to the replace with -
            yourword=yourword[:t]+letter+yourword[t+1:] # update your your word to the replace with letter or word
            if len(letter)!= 1:
                yourword=yourword[:random_word_size]
            if yourword[:random_word_size]==random_word_duplicate: # Check your word is equal to random word or not.
                print(f"The word is {yourword[:random_word_size]}")
                print("!!!!!!!!!!!!!!!!!!!!!!   HURRY, You have crack the word  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("You Have won the Game!!!!!!!!!!!!!!")
                break
            # print("ok running....")
            print(yourword[:random_word_size])  #Printing yourword.
        else:
            print("You Have choosen the wrong word letters............")
            print(yourword[:random_word_size])
            wilo=wilo-1 # Chance decreases 
            fails(wilo) # It is function define above in the program.and tell about What is staus of your hungsman.
        print("\n\n") #Give 2 line space for in every line
    else:
        # After the sucessfull complination of while loop it will execute.
        print(f"The word is wrong \nThe right word is {random_word_duplicate}")
        print("Game Over!!!!!!!!!!!!!!!!!!!!")     

words=['apple','Banana','mongo','pineapple','bike','laptop','bed','mobile','pillow','clothes','pen','charger',
        'flag','mouse','bedsheet','cover','potato','bottel','bowl','plate','movie','table','chair','fan',
        'socket','hanger','rice','wheat','mixer','iron','bank','locker','chips','pin','oil','photo','paper',
        'clothes','clip','light','gate','window','pencil','eraser','towel','mask','tent','newspaper','bill','lock','line',
        'circle','triangle','squre','doll','point','radius','angle','chord','tips','note','letter','word',
        'cable','leg','head','nose','arm','finger','thumb','eye','ear','food','heart','kidney','blood','dad','father','mother',
        'brother','sister','grandfather','grandmother','law','mouth','blank','rent','mixer','tap','water','fire','milk','copy',
        'tie','board','cardboard','air','land','monkey','name','god','life','paste','glue','wall','tree',
        'plant','land','water','machine','color','cool','hot','number','sign','motor','lunch','breakfast',
        'dinner','print','knife']
Total_words = len(words)
# print(Total_words)
j=random.randint(0,Total_words)  #Select the word index
game(words[j]) #Send the word to the function
# game('grandfather')




