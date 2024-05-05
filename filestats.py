def x(file_path):
    with open(file_path,'r') as file:
        text=file.read()
        char_count=len(text)
        line_count=text.count('\n')+1
        space_count=text.count(' ')
        word_count=len(text.split())
        return char_count,line_count,space_count,word_count
    
file_path='file.txt'

a,b,c,d=x(file_path)
print("character count = ",a)
print("line count = ",b)
print("space count = ",c)
print("word count = ",d)

