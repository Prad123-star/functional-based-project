db={1:{"name":"pradip","city":"nashik","passing_year":2024,"percentage":78,"course":"python"}}
print("-"*100)
print(f"{' '*35}the kiran academy")
print("-"*100)
def dash_board():
   print( """           1.add details
                  2.display student details
                   3.update student details
                   4.delete student details
                   5.filter
                   """)


def add_student(rno,name,city,passing_year,percentage,course):
   
    db[rno]={"name":name,"city":city,"passing_year":passing_year,"percentage":percentage,"course":course}
    print('_'*120)
    
def display_student():
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("rno","name","city","passing_year","percentage","course"))

    for rno in db:
        print("-"*120)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(rno,db[rno]["name"],db[rno]["city"],db[rno]["passing_year"],db[rno]["percentage"],db[rno]["course"]))    
    print("-"*120) 

        
def update_student():
       rno=eval(input("enter a rno whose details you want to update:"))
       print("""
                    1.name     
                    2.city
                    3.percentage
                    4.passing_year
                    5.course""")
       choice=int(input("enter a choice:"))
       if choice==1:
                  if rno in db:
                        name=input("enter a name:")
                        db[rno]["name"]=name
                        print("update successfully........")
                  elif choice==2:
                      if rno in db:
                        city=input("enter a city name:")
                        db[rno]["city"]=city
                        print("update sucessfully")
                  elif choice==3:
                      if rno in db:
                         passing_year=int(input("enter a passing_year"))
                         db[rno]["passing_year"]=passing_year
                         print("updated successfully")
                  elif choice==3: 
                       if rno in db:
                         percentage=int(input("enter a percentage:"))
                         db[rno]["percentage"]=percentage
                         print("update successfully")
                  elif choice==4 :
                        if rno in db:
                          course=input("enter a course:")
                          db[rno]["course"]=course
                          print("updated successfully")


def delete_student():
     rno=int(input("enter your roll number who was deleted:"))
     del db[rno]
     print("deleted successfully:")
 
def filter(name,city,passing_year,percentage,course):
     print(""" 
              1.name
              2.city
              3.passing_year
              4.percentage
              5.course  
           """)
     choice=input("enter your choice:")
     if choice==1:
          print("-"*150)
          print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format("rno","name","city","passing_year","percentage","course"))
          print("-"*150)
          for i in db:
                if db[i]['name']==name:
                  print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(i,db[i]["name"],db[i]["city"],db[i]["passing_year"],db[i]["percentage"],db[i]["course"]))
                  print("-"*150)
     elif choice==2:
          print("-"*150)
          print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format("rno","name","city","passing_year","percentage","course"))
          print("-"*150)
          for i in db:
               if db[i]["city"]==city:
                    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(i,db[i]["name"],db[i]["city"],db[i]["passing_year"],db[i]["percentage"],db[i]["course"]))
                    print("-"*150)
     elif choice==3:
          print("-"*150)
          print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format("rno","name","city","passing_year","percentage","course"))
          print("-"*150)
          for i in db:
               if db[i]["passing_year"]==passing_year:
                    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(i,db[i]["name"],db[i]["city"],db[i]["passing_year"],db[i]["percentage"],db[i]["course"]))
                    print("-"*150)
     elif choice==4:
          print("-"*150)
          print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format("rno","name","city","passing_year","percentage","course"))
          print("-"*150)
          for i in db:
               if db[i]["percentage"]==percentage:
                    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(i,db[i]["name"],db[i]["city"],db[i]["passing_year"],db[i]["percentage"],db[i]["course"]))
                    print("-"*150)
     elif choice==5:
          print("-"*150)
          print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format("rno","name","city","passing_year","percentage","course"))
          print("-"*150)
          for i in db:
               if db[i]["course"]==course:
                    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(i,db[i]["name"],db[i]["city"],db[i]["passing_year"],db[i]["percentage"],db[i]["course"]))
                    print("-"*150)

                    
while True:
     dash_board()
     ch=int(input("enter your choice:"))
     if ch==1:
          rno=int(input("enter a roll no:"))
          name=input("enter a name:")
          city=input("enter a city")
          passing_year=int(input("enter a passing_year"))
          percentage=eval(input("enter a percentage"))
          course=input("enter a course:")
          print(add_student(rno,name,city,passing_year,percentage,course))
     elif ch==2:
          display_student()
     elif ch==3:
          roll=eval(input("enter a roll number:"))
          print(update_student())
     elif ch==4:
          print(delete_student()) 
     elif ch==5:
        #   name=input("enter a filter name:")
        #   city=input("enter a filter city:")
        #   passing_year=int(input("enter a filter year:") )
        #   percentage=int(input("enter a percentage:"))
        #   course=input("enter a filter course:")
          print(filter(name,city,passing_year,percentage,course))
     else:
          print("invalid information")     










