# This activity will perform a similar function to Problem 01, but in reverse.

# define when to stop

user_stop = False

# simple greeting!
print("Hi there! I am a script that decrypts sentences already encrypted.")

while user_stop == False:

    # ask user to input an encrypted statement.
    encrypted = input("Input a statement that is already encrypted, or say 'stop' to stop: ")

    # check if the user wanted to stop

    if encrypted.lower() == "stop":

        #set the initial variable to True to break the loop

        user_stop = True

        # say goodbye!
    
        print("Goodbye and hope to see you again!")

    else:    
        # attempt to replace every encrypted symbol with an appropriate equivalent.
        first_vowel = encrypted.replace('*', 'a')
        second_vowel = first_vowel.replace('&', 'e')
        third_vowel = second_vowel.replace('#', 'i')
        fourth_vowel = third_vowel.replace('+', 'o')
        decrypted = fourth_vowel.replace('!', 'u')

        # print the decrypted message in low caps
        print("The decrypted message is: ", decrypted.lower())

