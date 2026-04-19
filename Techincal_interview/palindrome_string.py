def is_palindrome(s):
    cleaned=' '.join(s.lower().split())
    # Two pointers :left from start, right from end
    left=0
    right=len(cleaned)-1
    # compare character untill pointers meet
    while left<right:
        if cleaned[left]!=cleaned[right]:
            return False
        left +=1
        right -=1
    return True

#  Driver code
if __name__ == "__main__":
     test_cases = [
        "racecar",                    # True - simple palindrome
        "hello",                      # False - not palindrome
        "madam",                      # True - palindrome
        "A man a plan a canal panama", # True - phrase palindrome
        "Never odd or even",          # True - phrase palindrome
        "12321",                      # True - numeric palindrome
        "12345",                      # False - not palindrome
        "a",                          # True - single character
    ]
for test in test_cases:
    result=is_palindrome(test)
    print(result)
