import re
pattern=r'^[a-zA-Z_][a-zA-Z0-9_]*'
string=input("Enter a string ")
if(re.search(pattern,string)):
    print("Valid Identifier")
else:
    print("Invalid idientifier")
