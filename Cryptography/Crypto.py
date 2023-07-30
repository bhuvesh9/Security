import sys

# Encryption Process
def hybrid_encryption(plain, keyword):
    key = vigenere_generate_key(keyword, len(plain))

    # Step 1 - Vigenere Encryption
    e_vigenere = vigenere_encryption(plain, key)

    # Step 2 - Polybius Encryption
    e_polybius= polybius_encryption(e_vigenere)
    printer(e_polybius)

# Descryption Process
def hybrid_decryption(cipher, keyword):
    cipher = list(cipher)
    ciphertext_list = list()
    for i in range(0,len(cipher),2):
        ciphertext_list.append(cipher[i]+cipher[i+1])
    key = vigenere_generate_key(keyword, len(cipher))

    # Step 1 - Polybius Decryption
    d_polybius, index= polybius_decryption(ciphertext_list)
   
    # Step 2 - Vigenere Decryption
    d_vigenere = vigenere_decryption(d_polybius, key)
    return d_vigenere

def vigenere_generate_key(key, length):
    key = list(key)
    for i in range(length):
        key.append(key[i % len(key)])
    return("".join(key))

# Ei = (Pi + Ki) mod 26 General Representation
def vigenere_encryption(string, key):
    encrypt_text = list()
    for i in range(len(string)):
        x = chr(((ord(string[i]) - ord('A')) + (ord(key[i]) - ord('A'))) % 26 + ord('A'))
        encrypt_text.append(x)
    return("".join(encrypt_text))

# Di = (Ei - Ki + 26) mod 26 General Representation
def vigenere_decryption(cipher_text, key):
    plain_text = list()
    for i in range(len(cipher_text)):
        x = chr((((ord(cipher_text[i]) - ord('A')) - ord(key[i]) - ord('A'))+ 26 ) % 26 + ord('A'))
        plain_text.append(x)
    return("".join(plain_text))

def polybius_encryption(plaintext):
    plain_table=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
          "R","S","T","U","V","W","X","Y","Z"," "]
    cipher_table=["11","12","13","14","15","21","22","23","24","26","25","31","32","33","34",
       "35","41","42","43","44","45","51","52","53","54","55"," "]
    cipher_table_index = list()
    cipher_text= list()
    for i in range(len(plaintext)):
        for j in range(len(plain_table)):
            if (plaintext[i] == " "):
                cipher_table_index.append(26)
                break
            if plain_table[j] == plaintext[i]:
                cipher_table_index.append(j)
    for k in range(len(cipher_table_index)):
        c = cipher_table[cipher_table_index[k]]
        cipher_text.append(c)
    return cipher_text

def polybius_decryption(cipher):
    plain_table=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
          "R","S","T","U","V","W","X","Y","Z"," "]
    cipher_table=["11","12","13","14","15","21","22","23","24","26","25","31","32","33","34",
          "35","41","42","43","44","45","51","52","53","54","55"," "]
    plain_table_index = list()
    plain_text= list()
    for i in range(len(cipher)):
        for j in range(len(cipher_table)):
            if (cipher[i] == " "):
                plain_table_index.append(26)
                break
            if cipher_table[j] == cipher[i]:
                plain_table_index.append(j)
    for k in range(len(plain_table_index)):
        p = plain_table[plain_table_index[k]]
        plain_text.append(p)
    return plain_text,plain_table_index

def printer(l):
    return print("".join(l))

def printer_decryption(l):
    plain_table=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
          "R","S","T","U","V","W","X","Y","Z"," "]
    for k in range(len(l)):
        print(plain_table[l[k]], end="")

if __name__ == "__main__":

    print("""What You Want To Do \n
                1. Encryption
                2. Decryption
                3. Exit
         """)
    choose = input("Choose: ")

    if (choose=="1"):
        message = input("Message you want to encrypt(captital letters & no space): ")
        keyword = input("PASSCODE(captital letters & no space): ")

        print("\n======== Encrypted Text ========")
        hybrid_encryption(message, keyword)
        print("\n")

    elif(choose=="2"):
        ciphertext = input("Text you want to decrypt(no sapce): ")
        keyword = input("PASSCODE(captital letters & no space): ")

        plaintext = hybrid_decryption(ciphertext, keyword)

        print("\n======== Decrypted Message ========")
        print(plaintext)
        print("\n")
    elif(choose=='3'):
        sys.exit("(: THANK YOU :) \n")
    else:
        sys.exit("!Please enter the correct choice!\n")