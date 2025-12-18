

def Make_Key(msg,KEY):
    if len(msg) == len(KEY):
        return KEY
    else:
        for i in range(len(msg) - len(KEY)):
            KEY = KEY[i % len(KEY)]
            i += 1
            print(KEY)
        return"".join(KEY)

def Vigenere_Cipher(msg,KEY):
    Make_Key(msg, KEY)
    encrypt = []
    m = 0
    for i in range(len(msg)):
        char = msg[i]
        print(char, KEY[m % len(KEY)])
        if char.isalpha():
            if char.isupper():
                encode = (((ord(char) - ord('A')) + (ord(KEY[m % len(KEY)].upper()) - ord('A'))) % 26)
                encode_text = chr(encode + ord('A'))
                encrypt.append(encode_text)
            elif char.islower():
                encode = (((ord(char) - ord('a')) + (ord(KEY[m % len(KEY)].lower()) - ord('a'))) % 26)
                encode_text = chr(encode + ord('a'))
                encrypt.append(encode_text)
            # print(encode)
            # print(char)
            m += 1
        else:
            encode_text = char
            encrypt.append(encode_text)
    return "".join(encrypt)

# def Dedcode_Cipher(Excepted_Text, KEY):
#     Make_Key(msg, KEY)
#     decode = []
#     m = 0
#     for i in range(len(Excepted_Text)):
#         char = Excepted_Text[i]
#         print(char, KEY[m % len(KEY)])
#         if char.isalpha():
#             if char.isupper():
#                 decode = (((ord(char) + ord('A')) + (ord(KEY[m % len(KEY)].upper()) - ord('A'))) % 26)
#                 decode_text = chr(decode + ord('A'))
#                 print(decode_text)
#
#             elif char.islower():
#                 decode = (((ord(char) + ord('a')) + (ord(KEY[m % len(KEY)].lower()) - ord('a'))) % 26)
#                 decode_text = chr(decode + ord('a'))
#                 print(decode_text)
#
#             # print(encode)
#             # print(char)
#             m += 1
#         else:
#             decode_text = char
#             print(decode_text)
#         # decode.append(decode_text)
#     return "".join(decode)

# msg = input(str("please input a word, a phrase, mabye even a sentence : "))
# KEY = input(str("please input a word or a phrase of letter for your key : "))
#
# Excepted_Text = Vigenere_Cipher(msg, KEY)
# print("the encryted vesion of " +str(msg) + " is " + Excepted_Text)

# Decrypted_Text = Dedcode_Cipher(Excepted_Text, KEY)
# print(Decrypted_Text)
def main():

    while True:
        print("---------------Menu-------------------\n"
              "1. Make a cipher \n"
              "2. overwrite current file \n"
              "3. decode file content\n"
              "--------------------------------------")
        menu = int(input("What options would you like to choose: "))

        if menu == 1:
            msg = input(str("please input a word, a phrase, or sentence However you will need to avoid using spaces: "))
            KEY = input(str("please input a word or a phrase of letter for your key : "))
            Excepted_Text = Vigenere_Cipher(msg, KEY)
            Vigenere_Cipher(msg, KEY)
            print("the encryted vesion of " + str(msg) + " is " + Excepted_Text)
        elif menu == 2:
            print("In working progress")
        elif menu == 3:
            print("In working progress")
        else:
            print("please try selecting an available option")

if __name__ == "__main__":
    main()

# ---To Do list----
# > Make cypher - COMPLETED -
# > add a way to prevent user from adding spaces
# > Allow the user a chance to add there newly made cyper to a file
# > Allow them the chance to decode from the file
# > Account for system error in the code and in the file

# Excepted_Text = Vigenere_Cipher(msg, KEY)
# print(Excepted_Text)

# KEY = Make_Key(msg, KEY)
# for i in range(len(msg)):
#     char = msg[i]
#     if char.isupper():
#         encrypted_char = chr(((ord(char) - ord('A')) - ord(KEY[i % len(KEY)]) - ord('A')) % 26)
#         print(encrypted_char)
#     elif char.islower():
#         encrypted_char = chr((ord(char) - ord(KEY[i]) - ord('A')) % 26)
#         # if char.isupper():
#         #     encrypted_char = chr((ord(char) - ord(KEY[i]) - 2 * ord('A')) % 26 + ord('A'))
#         #     print(encrypted_char)
#         # elif char.islower():
#         #     encrypted_char = chr((ord(char) - ord(KEY[i]) - 2 * ord('A')) % 26 + ord('a'))
#         print(encrypted_char)
#     #     awedh
#     else:
#         encrypted_char = char
#     encrypt.append(encrypted_char)
# return "".join(encrypt)
