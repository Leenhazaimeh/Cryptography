import re
import string
import nltk
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)



word_list = words.words()
name_list = names.words()



def encrypt(plain, key): 
    encrypted_text = ""
    plain_len = len(plain)
    for k in range(plain_len):
        num = plain[k] 
        if  not(num.islower() or  num.isupper()):
            encrypted_text += num
            continue
        if num.islower():
            location = alephbet.index(num.upper()) 
            new_location = (location + key) % 26 
            encrypted_text += alephbet[new_location].lower()
        else:
            location = alephbet.index(num) 
            new_location = (location + key) % 26 
            encrypted_text += alephbet[new_location]

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key+1)

alephbet = string.ascii_uppercase 

def sum_words(text):

    candidate_words = text.split() 
    word_sum = 0 
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_sum += 1
    return word_sum

def crack(encrypted):
    percentage_init = 0
    for i in range(len(encrypted.split())*26):
        candidate_dec = decrypt(encrypted, i)
        word_sum = sum_words(candidate_dec)
        percentage = int(word_sum / len(candidate_dec.split()) * 100)
        if percentage > percentage_init:
            percentage_init = percentage 
            decrypt_word = candidate_dec
    return decrypt_word


if __name__ == "__main__":

    input = ['abc','zzz']
    actual = [encrypt(i,1) for i in input]
    expected = ['bcd','aaa']
    print(expected,actual)
    actual2 = [decrypt(i,1) for i in input]
    print(actual2)

    word = 'It was the best of times, it was the worst of times.'
    encrypted = encrypt(word, 50)
    print('en',encrypt(word, 50))

    print("the right decrypt is ", crack(encrypted))
