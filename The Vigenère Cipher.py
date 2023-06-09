#Michael Angelo P. Biag
#BSCOE 1-4
#Problem number 3 The Vigenère Cipher  (50 points)
def main():
    #implementing keypadding method
    def _pad_key(plaintext, key):
        padded_key = ''
        i = 0

    #loop over the characters of the plain text
        for char in plaintext:
            if char.isalpha():
                padded_key += key[i % len(key)]
                i += 1
            else:
                padded_key += ' '
        return padded_key

    #implementing the encrtypt and decrypt method
    def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):
        if plaintext_char.isalpha():
            if plaintext_char.isupper():
                first_alphabet_letter = 'A'

    #subctracting the position of the first alphabet letter from the position of the plain text character
            old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
            key_char_position = ord(key_char.lower()) - ord('a')

            if mode == 'encrypt':
                new_char_position = (old_char_position + key_char_position) % 26
            else:
                new_char_position = (old_char_position - key_char_position + 26) % 26
            return chr(new_char_position + ord(first_alphabet_letter))
        return plaintext_char

    #encrypt method
    def encrypt(plaintext, key):
        ciphertext = ''
        padded_key = _pad_key(plaintext, key)
        for plaintext_char, key_char in zip(plaintext, padded_key):
            ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
        return ciphertext

    #decrypt method
    def decrypt(ciphertext, key):
        plaintext = ''
        padded_key = _pad_key(ciphertext, key)
        for ciphertext_char, key_char in zip(ciphertext, padded_key):
            plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode='decrypt')
        return plaintext

    #Ask the user to input a message and key
    plain_text = input('Enter a message (all uppercase letters, no spaces): ')
    key = input('Enter a key (all uppercase letters): ')

    ciphertext = encrypt(plain_text, key)
    decrypted_plaintext = decrypt(ciphertext, key)

    #print output with decor
    print("\033[1;36m" +"=" * 20)
    print(f'Encrypted message: {ciphertext}')
    print(f'Decrypted message: {decrypted_plaintext}')
    print("=" * 20)
    
 #program if you want to repeat it again
    Repeat = input("Would you like to try again? (YES/NO) : ").upper()
    if Repeat == "YES":
            main()
    else:
            print("Thank you!!")
            exit()
main()
