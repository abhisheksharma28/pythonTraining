# open("employees.txt","r") #read
# open("employees.txt","w") #write
# open("employees.txt","a") #append
# open("employees.txt","r+") #readwrite both

employee_file = open("employees.txt","r")

# print(employee_file.read()) #true/false if readable then true else false
# print(employee_file.readlines()) #in list form
# print(employee_file.readline()) #for single line need to run it 4 different times
#print(employee_file.readlines()[1]) #in list form
for employee in employee_file.readlines():
    print(employee)
employee_file.close()