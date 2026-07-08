# Taking the input for the user
user_text = input("enter a full sentence:").strip()

print(f"Original sentence = {user_text}")

print("\n--Converting Case--\n")

print(f"Uppercase: {user_text.upper()}")
print(f"Lowercase: {user_text.lower()}")
print(f"Title: {user_text.title()}")
print(f"Capitalize: {user_text.capitalize()}")
print(f"Swap case: {user_text.swapcase()}")

print("\n--Counting words--")

words = user_text.split()
print(f"Total no of words = {len(words)}")

print("--checking Digits and Alphabets--")
print(f"Does all the sentence contains only alphabets: {user_text.isalpha()}")
print(f"Does all the sentence contains only digits: {user_text.isdigit()}")
print(f"Is alphanumeric: {user_text.isalnum()}")

print("\n----Replaicing a word:")
old_word = input("enter a word you want to replace:").strip()
new_word = input("enter a word you want to replace with:").strip()

print(f"Sentence after replacing '{old_word}' with '{new_word}' is: {user_text.replace(old_word,new_word)}")


#OUTPUT:

# enter a full sentence:I love doing Assignments given by my mentor.
# Original sentence = I love doing Assignments given by my mentor.

# --Converting Case--

# Uppercase: I LOVE DOING ASSIGNMENTS GIVEN BY MY MENTOR.
# Lowercase: i love doing assignments given by my mentor.
# Title: I Love Doing Assignments Given By My Mentor.
# Capitalize: I love doing assignments given by my mentor.
# Swap case: i LOVE DOING aSSIGNMENTS GIVEN BY MY MENTOR.

# --Counting words--
# Total no of words = 8
# --checking Digits and Alphabets--
# Does all the sentence contains only alphabets: False
# Does all the sentence contains only digits: False
# Is alphanumeric: False

# ----Replaicing a word:
# enter a word you want to replace:I
# enter a word you want to replace with:All
# Sentence after replacing 'I' with 'All' is: All love doing Assignments given by my mentor.