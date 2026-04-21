#Given a sentence (string of words), reverse the order of the words. The words themselves should remain unchanged, only their order should be reversed
def reverse_words(sentence):
    if not sentence :
        return ""
    # split into words
    words=[]
    current_word=""
    for char in sentence:
        if char==" ":
            if current_word:
                words.append(current_word)
                current_word=""
        else:
            current_word+=char

    # Adding last word
    if current_word:
        words.append(current_word)
    # reversing
    reversed_words=[]
    for i in range(len(words)-1,-1,-1):
        reversed_words.append(words[i])
    
    return ' '.join(reversed_words)

print (reverse_words("Hi this is hammad"))
