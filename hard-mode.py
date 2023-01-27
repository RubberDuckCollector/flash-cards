import re
import copy

# NOTICE: UNIT 3 NOR 5 HAVE BEEN COVERED YET

class Color:
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightPurple = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    Warn = "\033[93m"
    Underline = "\033[4m"
    Bold = "\033[1m"
    Hidden = "\033[8m"
    Blink = "\033[5m"
    Dim = "\033[2m"
    Reverse = "\033[7m"
    Reset = "\033[0m"

def main():

    while True:
        
        print(f"""Please enter the desired unit (enter the number of the unit, 1-6 inclusive) or otherwise.
    {Color.LightCyan}Other vocab{Color.Reset}:
        Body parts (Type: "{Color.LightCyan}body{Color.Reset}" to revise this")
        Countries in europe (Type: "{Color.LightCyan}europe{Color.Reset}" to revise this")
        Numbers (Type: "{Color.LightCyan}numbers{Color.Reset}" to revise this")""")
        set = input("> ").lower().replace(" ", "").replace("\t", "") # set means the set of flash cards the user chooses to do
        
        match set:
            case "1":
                filename = "unit1.txt"
                break
            case "2":
                filename = "unit2.txt"
                break
            case "3":
                filename = "unit3.txt"
                break
            case "4":
                filename = "unit4.txt"
                break
            case "5":
                filename = "unit5.txt"
                break
            case "6":
                filename = "unit6.txt"
                break
            case "body":
                filename = "body.txt"
                break
            case "europe":
                filename = "europe.txt"
                break
            case "numbers":
                filename = "numbers.txt"
                break
            case "test":
                filename = "test.txt"
                break
        
        if set != "1" or set != "2" or set != "3" or set != "4" or set != "5" or set != "6" or set != "body" or set != "europe" or set != "numbers" or set != "test":
            print("Unrecognised command. Please enter a valid card set to revise.")
            print(f"""Please enter the desired unit (enter the number of the unit, 1-6 inclusive) or otherwise.
    {Color.LightCyan}Other vocab{Color.Reset}:
        Body parts (Type: "{Color.LightCyan}body{Color.Reset}" to revise this)
        Countries in europe (Type: "{Color.LightCyan}europe{Color.Reset}" to revise this"
        Numbers (Type: "{Color.LightCyan}numbers{Color.Reset}" to revise this)""")
            set = input("> ").lower().replace(" ", "").replace("\t", "")
            
            match set:
                case "1":
                    filename = "unit1.txt"
                    break
                case "2":
                    filename = "unit2.txt"
                    break
                case "3":
                    filename = "unit3.txt"
                    break
                case "4":
                    filename = "unit4.txt"
                    break
                case "5":
                    filename = "unit5.txt"
                    break
                case "6":
                    filename = "unit6.txt"
                    break
                case "body":
                    filename = "body.txt"
                    break
                case "europe":
                    filename = "europe.txt"
                    break
                case "numbers":
                    filename = "numbers.txt"
                    break
                case "test":
                    filename = "test.txt"
                    break
        

    flashcards = []
    
    with open(filename) as f:
        words = f.read().splitlines()
    
        for i in range(len(words)):
            flashcards.append([words[i]])
    # use nested list comprehension to split the strings on every |
    flashcards = [[card.strip() for card in item.rsplit('|')] for sublist in flashcards for item in sublist]
    
    cards_no_brackets = copy.deepcopy(flashcards) # copy.deepcopy() makes it so the lists are truly different and they will not reference each other, so changing one won't change both
    
    indices = []
    
    pattern = re.compile(r'\(.*\)')
    
    for i, sublist in enumerate(cards_no_brackets): # [i][j]
        for j, item in enumerate(sublist):
            if j != 0: # this code is only performed on the spanish term, meaning that the index containing the english term in the flash card is untouched. i is each sublist (flash card) and j is each term in the flash card, j=0 means the english term, and j=1 is the spanish term of the flash card.
                original_card = item
                # Use the regular expression pattern to search for and remove brackets in the string
                item = re.sub(pattern, '', item).rstrip()
                # Check if any replacement was made
                if original_card != item:
                    # a list is appended every time the code finds a flash card with brackets
                    indices.append([i, j])
                # Update the modified string back into the cards_no_brackets list
                cards_no_brackets[i][j] = item
    
    
    def questions(card_set): # card_set is a list parameter
        correct = [] # list to store flashcards answered correctly
        incorrect = [] # list to store flashcards answered incorrectly

        for i in range(len(card_set)):
            answer = input(f"Write '{Color.Cyan}{card_set[i][0]}{Color.Reset}' in Spanish: ").lower()
            if answer == card_set[i][1].lower and [i, 1] in indices: # check if answer is correct but also show the content in brackets
                print(f"{Color.LightMagenta}Correct!{Color.Reset} Full answer: {flashcards[i][1]}")
                correct.append(card_set[i])
            elif answer == card_set[i][1].lower(): # check if answer is correct
                print(f"{Color.LightMagenta}Correct!{Color.Reset}")
                correct.append(card_set[i])
            else:
                print(f"{Color.LightYellow}Incorrect!{Color.Reset}")
                print(f"Correct answer: {Color.LightRed}{flashcards[i][1]}{Color.Reset}")
                # if user entered wrong answer by mistake, give them the option to report it as correct
                while True:
                    override = input(f"Were you actually correct? ({Color.LightYellow}y{Color.Reset}/{Color.LightYellow}n{Color.Reset}) ").lower().replace(" ", "").replace("\t", "")
                    if override == "y":
                        print(f"{Color.LightMagenta}Correct!{Color.Reset}")
                        correct.append(card_set[i])
                        break
                    elif override == "n":
                        print(f"{Color.LightYellow}Incorrect!{Color.Reset}")
                        incorrect.append(card_set[i])
                        break
                    else:
                        print(f"Please either input '{Color.LightYellow}y{Color.Reset}' or '{Color.LightYellow}n{Color.Reset}'.")
                        override = input(f"Were you actually corect? ({Color.LightYellow}y{Color.Reset}/{Color.LightYellow}n{Color.Reset}) ").lower().replace(" ", "").replace("\t", "")
                        if override == "y":
                            print(f"{Color.LightMagenta}Correct!{Color.Reset}")
                            correct.append(card_set[i])
                            break
                        elif override == "n":
                            print(f"{Color.LightYellow}Incorrect!{Color.Reset}")
                            incorrect.append(card_set[i])
                            break
        # Print number of correct and incorrect flashcards
        print(f"\n{Color.LightMagenta}Correct: ({len(correct)}){Color.Reset}")
        if len(correct) == 0: # if all of the user's answers were INCORRECT, a special message is printed
            print(f"{Color.LightRed}You didn't get anything correct. Don't worry! Your exam is soon!{Color.Reset}")
        else:
            for i in range(len(correct)):
                print(f"{Color.LightGreen}{correct[i][0]}: {correct[i][1]}{Color.LightGreen}")
        print()
        print(f"{Color.LightYellow}Incorrect: ({len(incorrect)}){Color.Reset}")
        if len(incorrect) == 0: # if all of the user's answers were CORRECT, a special message is printed
            print(f"{Color.LightGreen}You got everything right! Well done!{Color.Reset}")
        else:
            for i in range(len(incorrect)):
                print(f"{Color.LightRed}{incorrect[i][0]}: {incorrect[i][1]}{Color.Reset}")
        return incorrect
    
    incorrect = questions(cards_no_brackets)
    # print(indices)

if __name__ == '__main__':
    main()
   
