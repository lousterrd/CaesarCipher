# Louis Doherty
# Import the enchant library which contains an english dictionary
# May need to type in the command line "pip install pyenchant"
import enchant

dict = enchant.Dict("en_US")

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(letters)

def encrypt(phrase, key):
    phrase = phrase.upper()

    translated = ''

    for letter in phrase:
        pos = letters.find(letter)
        if pos == -1:
            translated = translated + letter
        else:
            newpos = pos + key

            if newpos > length-1:
                newpos = newpos - length

            translated = translated + letters[newpos]

    return translated


def decrypt(phrase, key):
    phrase = phrase.upper()
    translated = ''

    for letter in phrase:
        pos = letters.find(letter)
        if pos == -1:
            translated = translated + letter
        else:
            newpos = pos - key

            if newpos < 0:
                newpos = newpos + length

            translated = translated + letters[newpos]

    return translated


def bruteforce(phrase):
    key = 0
    #phrase = input("Please enter a phrase to decrypt: ")
    while key < 26:
        decrypted = decrypt(phrase, key)
        if isPhrase(decrypted):
            print("Key: " + str(key) + "\nMessage: " + decrypted)
            break
        key += 1



def isPhrase(phrase):
    phrase = phrase.upper()
    phrase = phrase.split()
    for word in phrase:
        if not(dict.check(word)):
            #print ("not a phrase")
            return False
    #print("full english")
    return True




choice = input("Would you like to encrypt (e) or decrypt (d)? ")

key = int(input("Please enter a key between 1 and 26: "))

if key > 26 or key < 1:
    print ("Sorry, you did not choose a valid option.")

else:
    if choice == "encrypt" or choice == 'e':
        phrase = input ("Please enter a phrase to encrypt: ")
        print (encrypt(phrase, key))
    elif choice == "decrypt" or choice == 'd':
        phrase = input ("Please enter a phrase to decrypt: ")
        print (decrypt(phrase, key))
    else:
        print ("Sorry, you did not choose a valid option.")
