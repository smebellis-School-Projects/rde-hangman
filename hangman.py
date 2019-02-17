# Hangman game
#

# -----------------------------------


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letters in secretWord:
        if letters not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for letters in secretWord:
        if letters in lettersGuessed:
            word = word + letters
        else:
            word = word + "_ "
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    
    for letters in lettersGuessed:
        try:
            alphabet.remove(letters)
        except ValueError:
            pass
    
        
    return ''.join(alphabet)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []
    
    print('Welcome to the game Hangman!')
    print( 'I am thinking of a word that is', len(secretWord),  'letters long')
    print('------------')    
    
    
    while guesses > 0: 
        # Checks to see if the word has been guessed.
        if isWordGuessed(secretWord, lettersGuessed) == True:
            
            print('Congratulations, you won!')
            break
        # Displays number of guesses remaining
        elif guesses >= 2:
            print('You have', guesses,  'guesses left.')
        elif guesses == 1:
            print('You have', guesses,  'guess left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        # Ask user for input
        user_guess = str(input('Please guess a letter: ')).lower()
        # Checks to see if user_guess is correct
        if user_guess in secretWord and user_guess not in lettersGuessed:
            lettersGuessed.append(user_guess)
            print('Good Guess:', getGuessedWord(secretWord, lettersGuessed))
            print('------------')
        # Checking to see if the user has already guessed letter
        elif user_guess in secretWord and user_guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', 
                  getGuessedWord(secretWord, lettersGuessed))
            print('------------')
        # Checks to see if the user guessed wrong letter
        elif user_guess not in secretWord and user_guess not in lettersGuessed:
            lettersGuessed.append(user_guess)
            print('Oops! That letter is not in my word: ', 
                  getGuessedWord(secretWord, lettersGuessed))
            print('------------')
            guesses -= 1 # Removes one guess from user
        # Another check to see if the user already guessed the letter
        elif user_guess not in secretWord and user_guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', 
                  getGuessedWord(secretWord, lettersGuessed))
            print('------------')
        
        # Checks guesses remaining if it is at zero the user looses the game        
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        else:
            continue
       

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
        

secretWord = # Choose your own secret word for testing                 
hangman(secretWord)
