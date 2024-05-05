import keyword
tokens=['']
ids=[]
key_words=keyword.kwlist
operators=['+','-','*','/','=','<']
punct=['(',')','{','}','[',']']

with open("a.txt") as t:
    a=t.readlines()
    for t in a:
        tokens=tokens+(t.split(" "))

print("id datatypes value rType NoArgs Targs")

for pos,t in enumerate(tokens):
    for k in key_words:
        if(t==k):
            ids.append(tokens[pos+1])
            if(tokens[pos+2]==','):
                print(tokens[pos+1]+" "+tokens[pos]+" "+"NULL")
                tokens.insert(pos+3,tokens[pos])                        
        elif(tokens[pos-1]=='('):
            continue;
        else:
            print(tokens[pos+1]+"   "+tokens[pos]+"    "+tokens[pos+3])
        
             
             

                 
             
             
             
                
            
