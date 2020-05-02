employee_file = open("employees.txt","a") #append
employee_file.write("Toby - Manager\n") #if append twice the entry is done twice
employee_file.write("kelly - Saleswoman")
employee_file.close()

employee_file1 = open("employees1.txt","w") #if done in existing file it rewrites the whole existing data
employee_file1.write("I'm best")
employee_file1.close()