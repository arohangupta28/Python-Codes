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

#How to find space in strings
st = "I hope this message finds you well  and in great spirits."

doublespace = st.find("  ")
print(doublespace)

#how to replace double spaces from single space
st = "I hope this  message finds you well  and in great  spirits."
replace = st.replace("  "," ")
print(replace)  
