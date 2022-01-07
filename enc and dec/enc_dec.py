inp = int(input("Enter the input --> 0 for encryption, 1 for decryption: "))

def encryption():
    enc_text = ""
    text = input("Enter the text: ")
    for i in range(len(text)):
        if(text[i] == "a"):
            enc_text = enc_text + "@"
        elif(text[i] == "b"):
            enc_text = enc_text + "!"
        elif(text[i] == "c"):
            enc_text = enc_text + "#"
        elif(text[i] == "d"):
            enc_text = enc_text + "%"
        elif(text[i] == "e"):
            enc_text = enc_text + "^"
    return enc_text

def decryption():
    dec_text = ""
    text = input("Enter the text: ")
    for i in range(len(text)):
        if(text[i] == "@"):
            dec_text = dec_text + "a"
        elif(text[i] == "!"):
           dec_text = dec_text + "b"
        elif(text[i] == "#"):
            dec_text = dec_text + "c"
        elif(text[i] == "%"):
           dec_text = dec_text + "d"
        elif(text[i] == "^"):
           dec_text = dec_text + "e"
    return dec_text


if(inp == 0):
    print(encryption())

elif(inp == 1):
    print(decryption())

else:
    print("Please give correct input")