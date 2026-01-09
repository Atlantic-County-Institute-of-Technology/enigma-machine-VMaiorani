
def Make_Key(msg,KEY):
    if len(msg) == len(KEY):
        return KEY
    else:
        for i in range(len(msg) - len(KEY)):
            KEY = KEY[i % len(KEY)]
            i += 1
        return"".join(KEY)

def Vigenere_Cipher(msg,KEY):
    Make_Key(msg, KEY)
    encrypt = ""
    m = 0
    for i in range(len(msg)):
        char = msg[i]
        if char.isalpha():
            if char.isupper():
                encode = (((ord(char) - ord('A')) + (ord(KEY[m % len(KEY)].upper()) - ord('A'))) % 26)
                encode_text = chr(encode + ord('A'))
                encrypt += encode_text
            elif char.islower():
                encode = (((ord(char) - ord('a')) + (ord(KEY[m % len(KEY)].lower()) - ord('a'))) % 26)
                encode_text = chr(encode + ord('a'))
                encrypt += encode_text
            # print(encode)
            # print(char)
            m += 1
        else:
            encode_text = char
            encrypt += encode_text
    return "".join(encrypt)

def write_file(e):
    message = e
    print(message)
    filename = input("What would you likw your filename to be: ")
    try:
        with open(filename, 'w') as file:
                file.write(message)
        print(f"\n You created a file '{filename}'.\n")

    except Exception as i:
        # if there is any issue, error out
        print(f"\ntheres seemed to be a problem!!! {i}\n")

def read_file():
    filename = input("Please type a file name in to select it to read from it: ")

    try:
        with open(filename, 'r') as file:
            message = file.read()
        print(f"\n The contents are : {message}")

    except FileNotFoundError:
        print("We couldn't find the file!!\n"
              "Check your spelling and other possible details")

    except Exception as i:
        print("there was an error")


# def contiue(param):
#     pass


def overwrite(e):
    while True:
        filename = input("Please type a file you would like to overwrite: ")
        confirmation = input("Are you positive you want to overwrite this file ('Y' - yes, 'N' - no): ")
        if confirmation == 'Y':
            try:
                f = open(filename)
            except FileNotFoundError:
                print("The file you wanted to overwrite was not found please try again!!!")
            else:
                print("File was found!!!")
                try:
                    message = e
                    with open(filename, 'w') as file:
                        file.write(message)
                    print(f"\n You created a file '{filename}'.\n")

                except Exception as i:
                    # if there is any issue, error out
                    print(f"\ntheres seemed to be a problem!!! {i}\n")
        elif confirmation == 'N':
            again = input("would you like to enter a different file or quit ('Y' - yes, 'N' - no): ")
            if again == 'N':
                break
            elif again == 'Y':
                print("You may try again")

def Dedcode_Cipher(Excepted_Text, KEY):
    Make_Key(Excepted_Text, KEY)
    decode = []
    m = 0
    for i in range(len(Excepted_Text)):
        char = Excepted_Text[i]
        print(char, KEY[m % len(KEY)])
        if char.isalpha():
            if char.isupper():
                decode = (((ord(char) + ord('A')) + (ord(KEY[m % len(KEY)].upper()) - ord('A'))) % 26)
                decode_text = chr(decode + ord('A'))
                print(decode_text)

            elif char.islower():
                decode = (((ord(char) + ord('a')) + (ord(KEY[m % len(KEY)].lower()) - ord('a'))) % 26)
                decode_text = chr(decode + ord('a'))
                print(decode_text)

            # print(encode)
            # print(char)
            m += 1
        else:
            decode_text = char
            print(decode_text)
        # decode.append(decode_text)
    return "".join(decode)

# msg = input(str("please input a word, a phrase, mabye even a sentence : "))
# KEY = input(str("please input a word or a phrase of letter for your key : "))
#
# Excepted_Text = Vigenere_Cipher(msg, KEY)
# print("the encryted vesion of " +str(msg) + " is " + Excepted_Text)
#
# Decrypted_Text = Dedcode_Cipher(Excepted_Text, KEY)
# print(Decrypted_Text)
def main():
    msg = input(str("please input a word, a phrase, or sentence(this would be your default): "))
    KEY = input(str("please input a word or a phrase of letter for your key(this would be your default): "))
    # Vigenere_Cipher(msg, KEY)

    while True:
        print("---------------Menu-------------------\n"
              "1. Cipher \n"
              "2. create a file \n"
              "3. read a file \n"
              "4. overwrite a file \n"
              "5. decode file content\n"
              "--------------------------------------")
        menu = int(input("What options would you like to choose: "))
        if menu == 1:
            # msg = input(str("please input a word, a phrase, or sentence However you will need to avoid using spaces: "))
            # KEY = input(str("please input a word or a phrase of letter for your key : "))
            Excepted_Text = Vigenere_Cipher(msg, KEY)
            # Vigenere_Cipher(msg, KEY)
            print("the encryted vesion of " + str(msg) + " is " + Excepted_Text)
        elif menu == 2:
            e = Vigenere_Cipher(msg,KEY)
            write_file(e)
        elif menu == 3:
            read_file()
        elif menu == 4:
            e = Vigenere_Cipher(msg, KEY)
            overwrite(e)
        elif menu == 5:
            Excepted_Text = Vigenere_Cipher(msg, KEY)
            decode = Dedcode_Cipher(Excepted_Text, KEY)
            print(decode)
        elif menu == 6:
            print("PROGRAM ENDING")
            break
        else:
            print("please input an available option!!!")
if __name__ == "__main__":
    main()
