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
    #decrypt method
    #Ask the user to input a message and key
    #print output with decor
    #program if you want to repeat it again