# Given a string s and a character c, remove all occurrences of c from s and return the resulting string.

def remove_char(s,char_to_remove):
    result=""
    for char in s:
        if char != char_to_remove:
            result+=char
    return result
    
if __name__ == "__main__":
    print(remove_char('Banana','n'))
