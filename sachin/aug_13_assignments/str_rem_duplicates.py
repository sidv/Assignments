#1.Write a python code to take string input from user and remove duplicate words.

user_str = input("Enter user string to remove delete duplicate words : ")
splited_str = user_str.split(" ")
print(splited_str)
rem_dub = set(splited_str)
con_ = str(rem_dub)
print("".join(con_))
 
