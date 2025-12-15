def Make_Key(msg,KEY):
    if len(msg) == len(KEY):
        return KEY
    else:
        for i in range(len(msg) - len(KEY)):
            KEY = KEY + KEY[i % len(KEY)]
            print(KEY)
        return"".join(KEY)

def Vigenere_Cipher(msg, KEY):
    encrypt = []
    KEY = Make_Key(msg, KEY)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(KEY[i]) - 2 * ord('A')) % 26 + ord('A'))
            print(encrypted_char)
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(KEY[i]) - 2 * ord('A')) % 26 + ord('a'))
            print(encrypted_char)
        #     awedh
        else:
            encrypted_char = char
        encrypt.append(encrypted_char)
    return "".join(encrypt)




msg = input(str("please input a word, a phrase, or sentence However you will need to avoid useing spaces: "))
KEY = input(str("please input a word or a phrase of letter for your key : "))

# ---To Do list----
# > Make cypher - COMPLETED -
# > add a way to prevent user from adding spaces
# > Allow the user a chance to add there newly made cyper to a file
# > Allow them the chance to decode from the file
# > Account for system error in the code and in the file

Excepted_Text = Vigenere_Cipher(msg, KEY)
print(Excepted_Text)
