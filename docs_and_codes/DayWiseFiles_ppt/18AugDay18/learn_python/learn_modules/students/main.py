import groups_opr
import students_opr as st

students = {} #Empty dictionary
groups = {} #empty dictionary
school = {}

def main_menu():
	print("1. Add student")
	print("2. Delete student")
	print("3. Search Student")
	print("4. Display all student")
	print("5. Change a student name in the list") 
	print("6. Manage All groups")
	print("7. exit")
	
def add_school():
	school["name"] = input("Enter school")
	school["email"] = input("Enter email")


while True:
	add_school()
	main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add student
		st.add_student()
	elif ch == 2:
		#Delete student
		st.delete_student()
	elif ch == 3:
		#Search student
		st.search_student()
	elif ch == 4:
		#Display student
		st.display_student()
	elif ch== 5:
		#Change a student name in the list
		st.change_student_name()
	elif ch == 6:
		#Manage team
		groups_opr.manage_all_groups()
	elif ch == 7:
		#Exit
		break;
	else:
		print("Invalid Choice")




"""
{"1":{student}, "2":{student}, "3":{student}, "4":{student}, "5":{student}}
teams={}

Storage:
{
	agri:["1","5"],
	rocket:["3","5"]
}

Fetch:
x = teams[agri]
students[x[0]]

Manage Groups:
	-Create group
	-Display groups
	-Manage group(Particular)
	-Delete group
"""




























