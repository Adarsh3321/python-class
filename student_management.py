'''
https://meet.google.com/ojc-fkoy-hpx


Program Description: 
School Management System
You are required to develop a School Management System that simulates the key functionalities of managing students, teachers, and courses. The system will use object-oriented programming principles to create models for Students, Teachers, and Courses, with well-defined relationships and functionalities.

Core Features:
User Types:
1. Staff
2. Student

User:
Each student will have:

A unique ID (validated to ensure no duplicates).
A name.
email
phone
address
A list of courses they are enrolled in. []
list of batches assign to the staff--> if the user is student then save this filed as None
A list of courses they teach.

Course Management:

Each course will have:
A unique course ID.
A course name.
course Description
An associated teacher.  []
USER can assign courses to students. [] this will have the list of id's of the student
ID Validation:

The system will validate all user and course IDs to ensure uniqueness before adding them to the database-->  [list of respective Objects].
Functionalities:

Add Users:

Add a new student or teacher to the system with all required details.
Search Users:

Search for a user (student or teacher) by their unique ID.
Assign Courses:

Assign a course to a student and ensure that only a valid teacher is associated with the course.
Display Data:

Show detailed information about a student, including their enrolled courses.
Show detailed information about a teacher, including the courses they teach and their assigned batches.
Classes and Relationships:
Class: Student

Attributes: studentID, name, listOfCourses
Methods: Add course, view courses.
Class: Teacher

Attributes: teacherID, name, listOfCourses, listOfBatches
Methods: Assign course, view courses and batches.
Class: Course

Attributes: courseID, courseName, teacher
Methods: Assign teacher, view course details.
Class: SchoolManagementSystem

Attributes: List of students, teachers, and courses.
Methods:
Add student, teacher, or course.
Validate IDs.
Search users.
Assign courses.
Display details.
Expected Workflow:
Add a teacher or student to the system with their respective details.
Create courses and assign them to teachers.
Enroll students in courses with validation.
Fetch details of a student or teacher using their unique ID.
'''




import random
from tabulate import tabulate



class user:
    def __init__(self,id,name,email,phone,add,list_of_courses,list_of_batches,user_type):
        self.id=id
        self.name=name
        self.email=email
        self.add=add
        self.phone=phone
        self.list_of_courses=list_of_courses
        self.list_of_batches=list_of_batches
        self.user_type=user_type




class course:

    def __init__(self,id,c_name,c_type,c_des):
        self.id=id
        self.c_name=c_name
        self.c_type=c_type
        self.c_des=c_des


class function:

    def __init__(self,list_user,list_courses):
        self.list_user=list_user
        self.list_courses=list_courses

    def gen_id(self,type_user):
        temp_id= type_user + str(random.randint(1,99999))
        if self.valid_id(type_user,temp_id):
            return temp_id
        self.gen_id(type_user)
    def gen_c_id(self):
        return "course" + str(random.randint(1,99999))


    def valid_id(self,type_user,id):
        if type_user.lower()=="staff" or type_user.lower()=="user":
            for d in list_user:
                if d.id==id:
                    return False
            return True
        else:
            for d in list_courses:
                if d.id==id:
                    return False
            return True
    def add_user(self):
        type_user=int(input("1. staff\n2. student"))

        users={
            1:"staff",
            2:"student"
        }
        
        user_obj=user(func.gen_id(users[type_user]),input("name: "),input("email :"),input("address :"),input("phone :"),None,None,users[type_user])

        
        

        list_user.append(user_obj)
        print("user added..... \nid :",user_obj.id)
        
    
    def add_course(self):
        course_obj=course(func.gen_c_id(),input("course name :"),input("course type :"),input("course description : "))

        list_courses.append(course_obj)
        print("course added..... \n id :",course_obj.id)

    def view_user(self):
        ss=input("1. for student\n2.for staff")
        if ss=='1':
            user_data=[{"user type":users.user_type,"ID":users.id, "name":users.name, "email":users.email, "add":users.add,"phone":users.phone,"course studing":users.list_of_courses} for users in self.list_user if users.user_type=="student"] 

            print(tabulate(user_data, headers="keys", tablefmt="pretty"))

        elif ss=='2':
            user_data=[{"user type":users.user_type,"ID":users.id, "name":users.name, "email":users.email, "add":users.add,"phone":users.phone,"course teaching":users.list_of_batches} for users in self.list_user if users.user_type=="staff"] 

            print(tabulate(user_data, headers="keys", tablefmt="pretty"))

        

    def view_course(self):
        course_data=[{"course id":cours.id,"course name":cours.c_name,"course type":cours.c_type,"course description":cours.c_des}for cours in self.list_courses]

        print(tabulate(course_data, headers="keys", tablefmt="pretty"))


    def search(self,id):
        for u in self.list_user:
            if u.id==id:
                user_data=[{"user type":u.user_type,"ID":u.id, "name":u.name, "email":u.email, "add":u.add,"phone":u.phone}]
                print(tabulate(user_data, headers="keys", tablefmt="pretty"))


    def assign(self):
        ac=input("1. to assign course to student\n2. to assign course to staff")
        if ac=='1':
            c=input("enter course id : ")
            for l in list_courses:
                if l.id==c:
                    print("course name : ",l.c_name)
            s=input("enter student id : ")
            for l in list_user:
                if l.id==s:
                    l.list_of_courses=c
                    print(l.name)

        elif ac=='2':
            c=input("enter course id : ")
            for l in list_courses:
                if l.id==c:
                    print("course name : ",l.c_name)
            s=input("enter staff id : ")
            for l in list_user:
                if l.id==s:
                    l.list_of_batches=c
                    print(l.name)


if __name__=='__main__':
    list_courses=list()
    list_user=list()

    func=function(list_user,list_courses)

    while True:
        choice=int(input(f"1. add user\n"
                     f"2. add course\n"
                     f"3. view user\n"
                     f"4. view course\n"
                     f"5. search user\n"
                     f"6. assign course\n"
                     f"7. exit program\n"))
        
        if choice==1:
            print("adding user....")
            func.add_user()
            
            

        elif choice==2:
            print("adding courses....")
            func.add_course()
        elif choice==3:
            func.view_user()
        elif choice==4:
            func.view_course()
        elif choice==5:
            i=input("enter id : ")
            func.search(i)
        elif choice==6:
            func.assign()
        elif choice == 7:
            print("BYE...BYE....")
            break
        else:
            print("choose valid option:(1 to 7)")
