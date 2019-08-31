
#### Practising basics from python crash course book
############## 7/22/2019
message="Hello world!!"
# print(message)
msg="the beginning!!!"
# print(f"{message }{  msg}")
###using the format function.
print("{}{}".format(msg,message))
### Python 3.6 offers similar function as F-strings
print(f"{msg}{message}")
print(msg,message)

#### whitespaces and tabs
print("My name is\t Abhi\naspiring to be\t a \ndeveloper")
# \t- tabs
# \n - next line 

### removing whitespeaces or trailing charcs
#rstrip()- removes whitespaces
#rstrip(char)- removes chars
#lstrip()- removes fro left side
#strip()- removes from both sides
name="www.google.com"
print(name.rstrip(".com"))
print(name.strip("w.com"))
### In real world, the whitespaces in user inputs are cleared using the strip() method

### If we want the value of a variable to be used the same throughout
### the program, then CAPITALISE the variable name
CONSTANT_NAME=5000
 
 #tips: Never stress urself to write perfect code. Write a code that works 
 # and iteratively improve its quality
 ##
 