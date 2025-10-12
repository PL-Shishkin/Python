text=input()
text1= text.lower()
words=text1.split()
count=0
for word in words:
    if word[0]=='е':
        count+=1
print(count)
print(f'слова: {words} список')
