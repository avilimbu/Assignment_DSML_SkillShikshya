# Creating Strings 

word = "python"
sentence ="I love reading"
text = "very much"
order = "NICE"
string = "ram/hari/shyam/krishna"

# method 1 | upper()
print(f"{word} uppercase = {word.upper()}")

#  method 2 | lower ()
email = "ABC@gmail.com"
print(f"{email} lowercase = {email.lower()}")

# method 3 | title()
full_name = "hari chhetri"
print(f"title() eg {full_name} = {full_name.title()}")

#method 4 | replace()
rep = sentence.replace("I","Who?, you")
print(f"{sentence} after replace() ={rep}?") 

#method 5 | capitalizes()
print(f"captatilize {text} = {text.capitalize()}") 

#method 6 | split()
print(f"{sentence} after split() = {sentence.split()}")
print(f'{string} ater split("/") = {string.split("/")}')

#method 7 | slicing()
print(f"{word} after slicing[1:5] = word[1:5]")
print(f"{sentence} after slicing[0:12:2] = {sentence[0:12:2]}")

#method 8 | strip()
demo = "&&&Father&Mother"
print(f'{demo} after strip("&" = {demo.strip("&")}') 
demo1 ="   i am feeling wonderful  "
print(f"{demo1} after strip() = {demo1.strip()}")

#method 9 | len()
print(f"length of {string} = {len(string)}")
print(f"lenght of {word} = {len(word)}") 

#method 10 | join()
fruits = ["mango", "organge", "banana"]
print(f'{fruits} after "/".join(fruits) = {"/".join(fruits)}')

name = ["A","v","h","i"]
print(f"{name} after join() = {"".join(name)}")

#method 11 | find(sub)
Finding = word.find("y")
print(f"In {word} is there 'y' = {Finding}")

Finding = word.find("a")
print(f"In {word} is there 'a' = {Finding}") 

#method 12 | count(sub)
print(f"In {string} no of times 'a' comes = {string.count("a")}") 

#method 13 | startwith(sub)
print(f"Does {word} start with 'p'? = {word.startswith("p")}") 
print(f"Does {sentence} start with 'u'? = {word.startswith("u")}")

#method 14 | endswith9(sub)
print(f"Does {word} start with 'p'? = {word.endswith("p")}")

#method 15 | isalpha()
print(f"Is all the characters are alphabetic in {word}, {word.isalpha()}")





# OUTPUTS

# python uppercase = PYTHON
# ABC@gmail.com lowercase = abc@gmail.com
# title() eg hari chhetri = Hari Chhetri
# I love reading after replace() =Who?, you love reading?
# captatilize very much = Very much
# I love reading after split() = ['I', 'love', 'reading']
# ram/hari/shyam/krishna ater split("/") = ['ram', 'hari', 'shyam', 'krishna']
# python after slicing[1:5] = word[1:5]
# I love reading after slicing[0:12:2] = Ilv ed
# &&&Father&Mother after strip("&" = Father&Mother
#    i am feeling wonderful   after strip() = i am feeling wonderful
# length of ram/hari/shyam/krishna = 22
# lenght of python = 6
# ['mango', 'organge', 'banana'] after "/".join(fruits) = mango/organge/banana
# ['A', 'v', 'h', 'i'] after join() = Avhi
# In python is there 'y' = 1
# In python is there 'a' = -1
# In ram/hari/shyam/krishna no of times 'a' comes = 4
# Does python start with 'p'? = True
# Does I love reading start with 'u'? = False
# Does python start with 'p'? = False
# Is all the characters are alphabetic in python, True

