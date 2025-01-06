
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
dic={row.letter:row.code for (index,row) in data.iterrows()}
def phonetic_word():
        word = input("Enter a word:").upper()
        try:
            output = [dic[letter] for letter in word]
        except KeyError:
            print("Sorry,only letters in the alphabet Please..")
            phonetic_word()
        else:
            print(output)

phonetic_word()


