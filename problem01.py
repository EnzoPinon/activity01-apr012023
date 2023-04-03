# this activity will encrypt a message with a set replacement for vowels.

# Let's make an interface that the user can still encrypt new sentences after
# their first encryption!

# define when to stop

user_stop = False

# simple greeting!
print("Hi there! I am a script that will encrypt messages.")

while user_stop == False:

    # ask user to input an encrypted statement.
    decrypted = input("Input a statement to encrypt, or say 'stop' to stop: ")

    # check if the user wanted to stop

    if decrypted.lower() == "stop":

        #set the initial variable to True to break the loop

        user_stop = True

        # say goodbye!
    
        print("Goodbye and hope to see you again!")

    else:    
        # attempt to replace every vowel with an appropriate equivalent.
        first_vowel = decrypted.replace('a', '*')
        second_vowel = first_vowel.replace('e', '&')
        third_vowel = second_vowel.replace('i', '#')
        fourth_vowel = third_vowel.replace('o', '#')
        encrypted = fourth_vowel.replace('u', '!')

        # print the encrypted message in low caps
        print("The encrypted message is: ", encrypted.lower())