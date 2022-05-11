student_name=["Ron","Don"]
student_grade=[5,7]

x=0

for x in range(100):
    student_name.append(str(input("Enter student name:")))
    student_grade.append(float(input("Enter student grade:")))
    print(student_name)
    yes_no= str(input("Do you want to add another entry Y/N:"))
    if yes_no=='Y':
        x+=1
    else:
        break

for x in range(100):
    add_search= str(input("Do you want to add(A)/search(S)/none(N):"))
    if add_search=="S":
        search_name= str(input("Enter name of student you want to search:"))
        index= student_name.index(search_name)
        print(student_grade [index])
    elif add_search=="A":
        student_name.append(str(input("Enter student name:")))
        student_grade.append(float(input("Enter student grade:")))
        print(student_name)
        print(student_grade)
    else:
        break
        
for x in range(100):
    update_delete= str(input("Do you want to update(U)/delete(D)/none(N):"))
    if update_delete=="D":
        remove_name= str(input("Enter student name:"))
        index= student_name.index(remove_name)
        remove_grade= student_grade[index]
        student_name.remove(remove_name)
        student_grade.remove(remove_grade)
        print(student_name)
        print(student_grade)
        
    elif update_delete=="U":
        update_name_mark= str(input("Do you want to update name(N)/marks(M):"))
    
        if update_name_mark== "N":
            old_name= str(input("Enter old student name:")) 
            index = student_name.index(old_name)
            student_name [index] = str(input("Enter new student name:"))
            print(student_name)
            print(student_grade)
            
        elif update_name_mark== "M":
            old_marks= float(input("Enter old student marks:")) 
            index = student_grade.index(old_marks)
            student_grade [index] = str(input("Enter new student marks:"))
            print(student_name)
            print(student_grade)
    else:
        break