# Python-Codes
#first python practice code
letter = '''Dear <|Name|>,
Greeting from ABC company. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Mike
Date : <|Date|>
'''
name = input("Enter Your Name : ")
date = input("Enter Date : ")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)
