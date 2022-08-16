# Input Parameter: a string x
# Return Value: True if x is a palindrome, False otherwise
def palindrome(string):
    reverse_string=''
    for i in string:
        reverse_string=i+reverse_string
    if string==reverse_string:
        return True
    else:
        return False

if __name__ == "__main__":
    print(palindrome("aba"))
    print(palindrome("a"))
    print(palindrome("abba"))
    print(palindrome("amanaplanacanalpanama"))
    print(palindrome("abca"))
    print(palindrome("ac"))
    print(palindrome("adabbba"))
    print(palindrome("amandaplanacanalpanama"))


