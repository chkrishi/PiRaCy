def check_grammar(string):
    Print("S -> aSb | ε (epsilon represents empty string)")
    def is_valid(s):
        if len(s) == 0:
            return True
        elif s[0] == 'a' and s[-1] == 'b':
            return is_valid(s[1:-1])
        else:
            return False
    
    return is_valid(string)
string = input("Enter string :")

if check_grammar(string):
        print("In Grammar")
else:
        print("does not grammar.")   
