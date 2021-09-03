import re
import nltk
from nltk.corpus import words, names
from nltk.corpus.reader import knbc

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()


'''''''''
Create an encrypt function that takes in a plain text phrase and a numeric shift.
'''''''''''

def encrypt(enc, k): 
    letters = ''
    # enc_len = len(enc)
    for T in enc:
    
        if T.isupper():
            num = ord( T ) - ord( 'A' )
            num_shift = ( num + k ) % 26 + ord( 'A' )
            new_num = chr( num_shift )
           

        elif T.islower(): 

            num = ord( T ) - ord( 'a' )
            num_shift = ( num + k ) % 26 + ord( 'a' )
            new_num = chr( num_shift )
            letters +=  new_num

        elif T.isdigit():

            new_numb = ( int( T ) + k ) % 10
            letters = letters + str( new_numb )

        else:

            letters += T

    

    return letters

'''''''''
Create a decrypt function that takes in encrypted text and numeric shift which will
'''''''''''
def decrypt(enc, k):
    return encrypt(enc, k)



def sum(T):
    word_sum = 0 
    words = T.split() 
    
    for j in words:
        word = re.sub(r'[^A-Za-z]+','', j)
        if word.lower() in word_list or word in name_list:
            word_sum += 1
    return word_sum
'''''''''
create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
'''''''''''
def crack(letters):
    for i in range (0,26):
        T = decrypt(letters,i)
        crack_pers = int(sum(T) / len(letters.split()) * 100)
        if crack_pers > 50:
            return T
'''''''''
In order to accomplish a certain task you’ll need access to a corpus of English words.

    A search on something like python list of english words should get you going.
decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
'''''''''''
if __name__ == "__main__":

    input = ['leen']
    actual = [encrypt(i,1) for i in input]
    expected = ['mffo']
    print(actual)
    actual2 = [decrypt(i,1) for i in input]
    # print('It was the best of times, it was the worst of times.')
    print(actual2)
     

    # word = 'It was the best of times, it was the worst of times.'
    # letters = encrypt(word, 26)
    # print(encrypt('casear', 10))
    # print('Leen',encrypt(word, 100))

    # print("the right decrypt is ", crack(letters))
    # word = 'casear'
    # print = encrypt('casear', 10)
    # print= decrypt(word, 10)
    # print  = crack(word)
    # print('Leen',encrypt(word, 100))