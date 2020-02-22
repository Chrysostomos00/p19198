##askisi 5

with open('/home/chrysostomos/Desktop/P19198/ask5/test.txt') as f:
   words_list=[word for line in f for word in line.split()]
   print(words_list)
   
max="aaa"
for i in words_list:
    if len(i)>len(max):
       print(i[1:] +i[0]+ "ay")
    else: 
     print(i)
