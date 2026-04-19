
def count_vowels_constant(str):
    vowel=0
    consonant=0
    for char in str.lower():
        if char in 'aeiou':
            vowel+=1
        elif char.isalpha():
            consonant+=1
    print(f'In {str} number of vowels are {vowel} and constant are {consonant}')

if __name__ == "__main__":
    str=input('Enter a letter :')
    count_vowels_constant(str)
