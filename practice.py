# name = input("Enter your name : ")
# print("Good Afternoon",name)

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