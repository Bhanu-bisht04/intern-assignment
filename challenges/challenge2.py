def palindrome_check(s):
    formatted_str = s.replace(" ", "").lower()
    return formatted_str == formatted_str[::-1]

user_input = input("Enter a string")
print("The string", palindrome_check(user_input),"is a palindrome")