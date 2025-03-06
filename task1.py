import random

wordlist =  ["jungle", "castle", "tunnel", "breeze", "silver", "rocket"]

chosenword = random.choice(wordlist)

maxtry = 4

usedtry = 0

guessedletters = []

print("Welcome to Hangman game !!!!")

print("Try to guess the word one letter at a time.")

print("The word contains", len(chosenword), "letters.")

while usedtry < maxtry:
    worddisplay = ""
    for i in chosenword:
        if i in guessedletters:
            worddisplay+=i
        else:
            worddisplay+="_"
    print(f"\nWord:{worddisplay}")
    
    if "_" not in worddisplay:
        print(f"Congratulations! You guessed the word: {chosenword}")
        break
    
    guessletter =input("Enter a letter:").lower()
    
    if len(guessletter) != 1 or not guessletter.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
    
    if  guessletter in guessedletters:
        print("You've already guessed that letter. Try a different one.")
        continue
    
    guessedletters.append(guessletter)
    
    if guessletter not in chosenword:
        usedtry += 1
        print(f"Oops! '{guessletter}' is not in the word. You have {maxtry - usedtry} attempts left.")
    else:
        print(f"Nice! '{guessletter}' is in the word.")
                
if usedtry == maxtry:
    print(f"\nGame over! You're out of attempts. The word was: {chosenword}")

    
