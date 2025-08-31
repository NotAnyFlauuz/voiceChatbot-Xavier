text = input("Enter a sentence: ").strip() 
words = text.split()  

if len(words) > 1: 
    result = ''.join(words[1:])  
else:
    result = ""

print(result)  

