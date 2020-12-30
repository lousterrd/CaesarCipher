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
            return False
    return True


def main(): 
    isBrute = False
    choice = raw_input("Would you like to encrypt (e) or decrypt (d)? ")

    print ("If you do not have a valid key and want to use a brute force approach, enter -1 as the key.")
    key = int(raw_input("Please enter a key between 1 and 26: "))

    if key > 26 or key < -1:
        print ("Sorry, you did not choose a valid option.")
    

    else:
        if key == -1:
            isBrute = True
        if choice == "encrypt" or choice == 'e':
            phrase = raw_input ("Please enter a phrase to encrypt: ")
            print (encrypt(phrase, key))
        elif choice == "decrypt" or choice == 'd':
            phrase = raw_input ("Please enter a phrase to decrypt: ")
            if isBrute:
                bruteforce(phrase)
            else:
                print (decrypt(phrase, key))
        else:
            print ("Sorry, you did not choose a valid option.")

