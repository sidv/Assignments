     #87654321  Negative index Use -1,-2,-3 and so on
     #01234567  Postive index
name="Siddhant"
	# 10987654321   Negative index Use -1,-2,-3 and so on
	 # 0123456789    Positive index
full_name="Siddhant v"

print("_______Accessing index of string__________")
print(name[0]) #S
print(name[2]) #d
print(full_name[8]) # 
#print(name[11]) #Error: IndexError: string index out of range

print("______SLicing of string______________")
print(name[0:3]) #Sid  Syntax:name[startIndex:endindex+1] WHY? because endindex is excluded from output
print(name[2:5]) #ddh
print(name[4:7]) #han
print("name[4:15]",name[4:15])

print("_________Slicing shortcuts_________________")
print(name[:3]) #Sid   If index starts from 0,You dont need to mention it
print(name[4:]) #hant  If you want last part of string then dont need to mention closing  index
print(name[:])

print("______Negative index______________________")
print(name[-1]) #t
print(name[-8]) #S
#print(name[-9]) #Error : IndexError: string index out of range
print("name[-1:-4] =>",name[-1:-4]) # Nooutput
print("name[-4:-1] =>",name[-4:-1]) #han
print("name[:-1] => ",name[:-1]) #Siddhan
print("name[-5:] => ",name[-5:]) #dhant
print("name[7:4] =>",name[7:4]) # No output
print("name[2:-3] =>",name[2:-3]) #ddh
print("name[-6:5] =>",name[-6:5]) #ddh
print("name[-5:1] =>",name[-5:1]) #No output

print("__________Steps_______________________________")
alpha="abcdefghij"
      #0123456789 Positive index
     #10987654321 Negative index
print("name[0:6:1] =>",name[0:6:1])  #Siddha
print("name[0:6:2] =>",name[0:6:2])
print("alpha[0:9:2] =>",alpha[0:9:2]) #acegi
print("alpha[0:-5:4] =>",alpha[0:-5:2]) # 
print("alpha[1:6:-1] =>",alpha[1:6:-1]) #Negative step value will reverse the string. It'll fetch in reverse direction
print("alpha[4:1:-1] =>",alpha[4:1:-1]) #edc
print("alpha[6:2:-1] =>",alpha[6:2:-1]) #gfed
print("alpha[-4:1:-1] =>",alpha[-4:1:-1]) #gfedc
print("alpha[::-1] =>",alpha[::-1]) #Reverse the entire string
print("alpha[:3:-2] =>",alpha[:3:-2]) #jhf  
#In negative step value If start index is empty It consider that as a last index 
#And If endindex is empty is empty It'll conside that as a first index


