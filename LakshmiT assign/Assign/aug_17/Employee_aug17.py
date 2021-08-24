import organisation as org
import team
import employee as emp

def menu():
	print("1. Add organization Details")
	print("2. Edit Organization Details")
	print("3.View organisation Details")
	print("4. Add Employee")
	print("5. Delete Employee")
	print("6. Search Employee")
	print("7. Change employee data")
	print("\ta. Change Name")
	print("\tb. Change age")
	print("\tc. Change gender")
	print("\td. Change salary")
	print("8. Manage Team")
	print("9. Display")
	print("10. Exit")
def manage_gpmenu():
	print("\ta.Create Team")
	print("\tb.Display Teams")
	print("\tc.Manage Team(Particular)")
	team.manage_member_menu()
	print("\td.Delete Team")
	print("\te.Exit")

def manage_team():
	while True:
		manage_gpmenu()
		ch = input("\tEnter the choice")
		if ch == "a":
			#Create team
			team.create_team()
		elif ch == "b":
			#display teams
			team.display_teams()
		elif ch == "c":
			#Manage teams(Particular)
			team.manage_team_member()
		elif ch == "d":
			#Delete team
			team.delete_team()
		elif ch == "e":
			#exit
			break
		else:
			print("\tInvalid choice")	
def org_edit_menu():
	print("\t1. Edit Organisation name")	
	print("\t2. Edit email")	
	print("\t3. Edit phone number ")	
	print("\t4. Edit Website address")	
	print("\t5. Edit Organisation ID")
	print("\t6. Exit")	
	
def edit_organisation():
	while True:
		org_edit_menu()
		org_id = input("\t\tEnter your organisation ID")
		ch = int(input("\t\tEnter the choice"))
		if ch == 1:
			org.org_name_change(org_id)
		elif ch == 2:
			org.org_email_change(org_id)
		elif ch == 3:
			org.org_phno_change(org_id)
		elif ch == 4:
			org.org_website_change(org_id)
		elif ch == 5:
			print("")
		elif ch == 6:
				break
		else:
			print("Invalid Choice")
while True : 
	menu()
	ch = int(input("Enter the choice"))
	if ch is None:
		print("Enter valid choice ")
	elif ch == 1:
		org.add_organisation()
	elif ch == 2:
		edit_organisation()
	elif ch == 3:
		org.view_organisation()
	elif ch == 4:
		emp.add_employee()	
	elif ch == 5:
		emp.delete_employee()
	elif ch == 6:
		emp.search_employee_options()	
	elif ch == 7:
		emp.update_empoyee()
	elif ch == 8:
		manage_team()	
	elif ch == 9:
		emp.display_employee()
	elif ch == 10:
		break
	else:
		print("Invalid choice")
