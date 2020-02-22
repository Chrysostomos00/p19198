#metatropi string se arithmo ascii
L=input("Insert a word: ")
def split(word): 
    return [char for char in word]  
  
word = list(L)
num=""
for i in list(map(str, map(ord, list(L)))): 
    print(i, end="") 
    num+=i
    
int_num=int(num)
prime=bool(False)

if int_num > 1:
  for i in range(2, int(int_num/2)):         
     if (int_num % i) == 0: 
       prime=bool(True)
       break

  
if prime == True: 
 print("  ",int_num, "is not a prime number")
else:
 print ("  ",int_num, "is a prime number")