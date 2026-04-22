import time
userString = "" #I define the userString variable as nothing, which will be changed by the user, just for safekeeping.
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] #Here, I define what the vowels are in a list, which will be iterated through during the vowelNum function.
charNum = 0 #I define the charNum variable as "0", which will change during the character counter function. This was intended to solve a bug I found, but I ended up using a different method.

def main(): #I define the main variable here. This is the main control structure of the program, and includes calls of all the other functions at their respective choices.
    print("Welcome to the Word Toolkit!")
    print("")
    time.sleep(0.2)
    print("What string would you like to analyze today? ")
    while True:
        try:
            userString = input("Enter your string: ") #The user enters their string. I use a while loop as well as a try/except block for input validation, as this is the most important input of the program. If a user enters something that I've specified will not work, or a ValueError, it will tell them not to enter than and ask again, as opposed to ending the program or just crashing.
            if userString == "": #If the string entered is empty, it adds potential for crashes later, so it's safer to just make sure users cant enter it.
                print("Please enter a string with characters in it! Y'know, a string!")
            elif userString == " ": #This omits strings that are just one space, but is basically redundant as users can enter as many spaces they want as long as its more than one.
                print("Please enter a string with letters in it, so that it's an actual sentence!")
            else:
                break #If neither of the first two branches proc, it means the input is valid, and thus breaks the loop.
        except ValueError: #If there's a value error, it tells the user to enter a string and asks again.
            print("Please enter a string. I'm not playing anymore.")
    time.sleep(0.2)
    print("")
    print("What would you like to know?")
    while True: #Here's another while loop, which makes sure that if the user enters an option that isn't valid, the options will again be presented instead of a crash or exit.
        try:
            print("Enter the number that corresponds to your choice:")
            print("1. Character & Letter Counter") #I tell the user the options, as well as the number corresponding to it.
            print("2. Vowel Counter")
            print("3. Word Counter")
            print("4. Speaking/Typing Times")
            print("5. Commonality Checker")
            print("6. Analyze a Different String")
            print("7. Exit Program")
            choice = int(input("Enter your choice: "))
            if choice == 1:                                 #This is the if/else block responsible for calling the appropriate function for the user's choice.
                charCount(userString)                    #The function that corresponds to the number will be called, using the already inputted userString as a parameter to ensure that the functions work and can read the string in order to analyze it.
            elif choice == 2:
                vowelCount(userString)
            elif choice == 3:
                wordCounter(userString)
            elif choice == 4:
                readTypeTime(userString)
            elif choice == 5:
                commonCheck(userString)
            elif choice == 6:
                userString = newString(userString)
            elif choice == 7: #If they choose seven, I use the exit function to prematurely end the program.
                print("Thank you for using the Word Toolkit!")
                exit()
            else:
                print("Please enter a valid option! Thank you!") #If the user enters a number that isn't an option, it tells them to enter a valid one and asks the question again. I'm a big fan of while True.
        except ValueError:
            print("Please enter the number that corresponds with the choice! Thank you!") #If there's a value error, it tells the user to enter a number that corresponds to the choice, and enters again.

def wordCounter(userString):           #This is the wordCounter function, which uses userString as a parameter.
    numWords = len(userString.split()) #It creates a new variable, numWords, and sets it to the length of the splitted userString.
    words = userString.split()         #The other variable, words, is just the splitted userString.
    print("")                          #The program then 'thinks', and tells the user how many words there are, plus exactly what those words are.
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(f"There are {numWords} word(s) in that sentence!")
    print(f"The word(s) are: {words}!")
    print("")

def readTypeTime(userString):         #This is the readTypeTime function, which uses userString as a parameter.
    numWords = len(userString.split())#It uses another numWords variable, which also uses the length of the splitted userString.
    speakTimeMins = numWords / 150    #The function then uses very complex math to determine the speaking time and typing time in minutes of the userString, and multiplies those by 60 to find the seconds.
    typeTimeMins = numWords / 40      #The function then tells the user the answers, as well as how they were determined.
    speakTimeSecs = numWords / 150 * 60
    typeTimeSecs = numWords / 40 * 60

    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(
        f"Your sentence will take {speakTimeMins} minutes to speak, or {speakTimeSecs} seconds (Based on the average speaking time of 150 words per minute)!")
    print(
        f"Your sentence will take {typeTimeMins} minutes to type, or {typeTimeSecs} (Based on the average typing time of 50 words per minute)!")
    print("")

def charCount(userString):                           #This is the charCount function, which again uses userString as parameter.
    userStringNoSpaces = userString.replace(" ", "") #The function defines three variables; userStringNoSpaces, which is the user's string with all spaces removed,
    charNum = len(userString)
    charNumMinusSpaces = len(userStringNoSpaces)
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(f"There seem to be {charNum} characters in that string!")
    print(f"That's {charNumMinusSpaces} letters (the rest are spaces)! ")
    print("")


def vowelCount(userString):
    vowelNum = 0
    for letter in userString:
        if letter in vowel:
            vowelNum += 1
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print('')
    print(f"There are {vowelNum} vowels in that sentence!")



def commonCheck(userString):
    import pprint
    from collections import Counter
    common = Counter(userString)
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")

    print("The amount of times each letter appears in the string are as follows: ")

    pprint.pprint(dict(common), width=1)

def newString(userString):
    time.sleep(0.25)
    print("")
    newUserString = input("Enter your new string: ")
    return newUserString


main()
