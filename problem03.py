# Welcome to problem 03!
# This time we are asked to make a vigenere cipher in Python.

# Like problem 02, we'll make it interactable.

# I want to make this an awesome project, so let's allow the option to encode and decode.

# declare the stop indicator:

user_stop = False

# greet the user
print("Welcome to the Vigenere Cipher maker!")


while user_stop == False:

    request_type = str(input("Indicate if this is to encode or decode, or 'stop' to stop the process: "))
    #check if it is to stop
    print(request_type)
    if request_type.lower() == 'stop':
        user_stop = True
        print("Stopping! See you soon!")
        break

    # We break things down into two: Encode and Decode.
    if request_type.lower() == "encode":
        # ask for the string

        message = str(input("Please state the message to encode, no spaces, all caps: "))
        #ask for the key
        key = str(input("Please state the key, no spaces, all caps: "))
    
        # remove spaces
        message_nospace = message.replace(" ", "")
        key_nospace = key.replace(" ", "")

        # all caps

        string_encode = message_nospace.upper()
        encode_key = key_nospace.upper()
        # begin encryption
        # define list of two, one for regenerating the key with the right conditions and the original message
        encrypted = []
        listkey = list(encode_key)
        # check if the key length matches the string, then encode
        if(len(string_encode) == len(encode_key)):
            # encode the message
            for i in range(len(string_encode)):
                compute = (ord(string_encode[i]) + ord(encode_key[i])) % 26
                compute += ord('A')
                encrypted.append(chr(compute))
            # print results
            print("Original Text: ", string_encode)
            print("Key: ", key)
            print("Encrypted text: ", "".join(encrypted))
        else:
            # repeat the key until it matches the string
            for i in range(len(string_encode) - len(encode_key)):
                listkey.append(encode_key[i % len(encode_key)])
            encode_key = "".join(listkey)
            # encode message
            for i in range(len(string_encode)):
                compute = (ord(string_encode[i]) + ord(encode_key[i])) % 26
                compute += ord('A')
                encrypted.append(chr(compute))
            print("Original Text: ", string_encode)
            print("Key: ", key)
            print("Encrypted text: ", "".join(encrypted))
    
    if request_type.lower() == "decode":
        # ask for the string

        message = str(input("Please state the message to decode, no spaces, all caps: "))
        #ask for the key
        key = str(input("Please state the key, no spaces, all caps: "))
    
        # remove spaces
        message_nospace = message.replace(" ", "")
        key_nospace = key.replace(" ", "")

        # all caps

        string_encode = message_nospace.upper()
        encode_key = key_nospace.upper()
        # begin decryption
        # define list of two, one for regenerating the key with the right conditions and the encrypted message
        encrypted = []
        listkey = list(encode_key)
        # check if the key length matches the string, then decode
        if(len(string_encode) == len(encode_key)):
            # decrypt message with key 
            for i in range(len(string_encode)):
                compute = (ord(string_encode[i]) - ord(encode_key[i] + 26)) % 26
                compute += ord('A')
                encrypted.append(chr(compute))
            # print results
            print("Encrypted Text: ", string_encode)
            print("Key: ", key)
            print("Original text: ", "".join(encrypted))   
        else:
            # repeat the key until it matches the string
            for i in range(len(string_encode) - len(encode_key)):
                listkey.append(encode_key[i % len(encode_key)])
            encode_key = "".join(listkey)
            # decrypt the message with the key
            for i in range(len(string_encode)):
                compute = (ord(string_encode[i]) - ord(encode_key[i]) + 26) % 26
                compute += ord('A')
                encrypted.append(chr(compute))
            # release results
            print("Encrypted Text: ", string_encode)
            print("Key: ", key)
            print("Original text: ", "".join(encrypted))