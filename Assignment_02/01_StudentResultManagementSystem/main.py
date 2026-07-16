# creating / defining a uer defined function
def student_result(): 
    names=[]
    marks=[]
    student_data = {}


    # Taking the name and mark of a five student
    for i in range(5):
        name = input("Enter the name: ").strip()
        mark = int(input("Enter the mark he/she obtained: "))
        marks.append(mark)
        
        #storing the student data in a dictionary
        student_data.update({name:mark})

    print("\n------ Student Result ------")    

    # Using the conditional statement to assign grade
    for name, mark in student_data.items():
        if (mark>=80):
            grade = "A"
        elif (mark>=60 and mark<80):
            grade = "B"
        elif(mark>=40 and mark<60):
            grade = "C"
        else:
            grade = "F"
 
       # Displaying the student data 
        print(f"Name:{name}")
        print(f"Mark: {mark}")
        print(f"Grade: {grade}")
        print("_"*15)
    
    #calculating hightest, lowest and average marks
    highest = max(marks)
    lowest = min(marks)
    Avg = sum(marks)/len(marks)
 
    #Displaying the highest, lowest and average marks
    print("Highest marks = ",highest)
    print("Lowest mark = ", lowest)
    print("Average marks = ",Avg)



# calling the function
student_result()