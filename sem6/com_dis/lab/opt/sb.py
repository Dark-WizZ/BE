print("Recursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'/@\nT->FT'\nT'->*FT'/@\nF->(E)/i\n")
print("Enter the string want to be checked\n")
global s
s=list(input())
global i
i=0
def match(a):
    global s
    global i
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True
    else:
        return False
def F():
    return(
      (match("(") and E() and match(")"))
      or
      (match("i"))
    )

def Tx():
  return(
    (match("*") and F() and Tx())
    or
    (True)
  )
  
def T():
  return F() and Tx()
    
def Ex():
  return(
    (match("+") and T() and Ex())
    or
    (True)
  )
  
def E():
  return T() and Ex()



if(E()):
    if(i==len(s)): print("String is accepted")
    else: print("String is not accepted")
else: print("string is not accepted")
