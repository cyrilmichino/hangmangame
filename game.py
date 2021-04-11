import string
import random

def guessletter(letter_lst):
    
    #Allow users to make a hangman letter guess
    letter = input("Enter the letter: ").lower()

    #Make sure the input is valid and fits all set parameters for the hangman game
    if len(letter) == 1 and letter not in letter_lst and letter in string.ascii_lowercase:
        letter_lst.append(letter)
        return letter

    #Assk user to guess letter again if initial input was not right
    else:
        print("Invalid Input!")
        
        if len(letter) != 1:
            print("Choose only 1 letter.")
            return guessletter(letter_lst)
        elif letter in letter_lst:
            print("You have already chosen that letter.")
            return guessletter(letter_lst)
        else:
            print("Choose a letter of the alphabet.")
            return guessletter(letter_lst)


def playhangman(words):
    
    #Choose a random word and print out the slots
    word = random.choice(words)
    
    #Set default word list and fail count
    guessed_letters = list()
    fail_count = 0

    while fail_count < 6:

        dashes = len(word)

        #Show the hangman challenge word to user
        for char in word:

            #Replace dash with letter if already guessed
            if char in guessed_letters:
                print(char, end = " ")
                dashes -= 1
            #Maintain dash if letter is not yet guessed
            else:
                print("_", end=" ")

        #Stop the loop if user fills all dashes
        if dashes == 0:
            print("Congrats! You have won the game.")
            break

        #Allow the user to make letter guesses
        letter = guessletter(guessed_letters)
        guessed_letters.append(letter)

        #Check if the letter guess is wrong or right
        ##Append letter to word list if letter is correct
        if letter in word:
            pass
        
        ##Adjust fail count if letter guess is wrong
        else:
            fail_count += 1

            ###Check whether user has exhausted attempts and print notice
            if fail_count == 6:
                print(f"Sorry, that's 6 failed attempts. The right word is {word}.")
            else:
                print(f"Wrong Attempt. You have {6-fail_count} failed attempts left. Try again!")


if __name__ == "__main__":
    words = ["abruptly", "bandwagon", "buzzwords"] #List out the words to be used for the hangman game
    playhangman(words) #Execute and run the game using a random word from the word list