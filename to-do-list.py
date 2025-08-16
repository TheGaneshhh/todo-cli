
tasks = []

def add_task(t_list):
    
         
      str = input("\nEnter a new task name : ")
      
      if str :
          newT = str.upper() 
          t_list.append({"task" : newT, "done" : False}) 
          print("\nTask added successfully \n")
      else : 
          print("\nTask cannot be empty , Please try again \n")
    
    
def view_task(t_list):
            
        
        for i, t_list in enumerate(t_list,start=1) : 
    
            print("\n Task {} : {}\nCompleted : {} \n".format(i,t_list["task"],t_list["done"]))    
            
      
      
def mark_done(t_list):
      
      view_task(t_list)
           
      while True :
     
           raw =input("\nEnter the name of the task that you have completed ? or press q to quite : ").strip() 
           if not raw : 
               print("\nPlease enter a valid task name \n")
               continue
     
           stat = raw.upper()
         
           if stat.upper() == "Q" :  
                break 
                
           found = False 
           
           for task in t_list :
               if stat in task["task"]:    
                    task["done"] = True
                    found = True 
                
           if found == True: 
               print(f"Task '{stat}' marked as done!!\n ")
           else :
               print("\nTask not found!! \n ")
    
    
def remove_task(t_list):
     r_task = input("\nEnter the task you want to remove : \n ") 
     clock : False
     for i , j in enumerate(t_list, start=1) :
          if r_task.upper() == j["task"] : 
               t_list.pop(i-1)  
               print("\nTask removed successfully! \n")
               return 
          else :
               clock : False 
               
     if clock == False :
          print("\nTask not found!! \n")  
      
                
               
               
while True :
     print("------To-Do-List------")
     print("1. Add task")     
     print("2. View task")     
     print("3. Mark task as done")     
     print("4. Remove task") 
     print("q. Quite\n")
     
     opt = input("Enter your choice : ")
     
     if opt == "1" :
          add_task(tasks)
        
     elif opt == "2" :
          view_task(tasks)
          
     elif opt == "3" :
          mark_done(tasks)
          
     elif opt == "4" :
          remove_task(tasks)
          
     elif opt.lower() =="q" :
          break 
     
     else :
          print("Invalid Input!! \n") 
                
     

         
          
            
            
            