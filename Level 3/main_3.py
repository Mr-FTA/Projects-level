import modules_3 as md

def main():
    print("=== To-Do List ===")
    print("""
1. View tasks
2. Add a task
3. Remove a task
4. Mark task as complete
5. Exit
          """)
    
      
    while True:
        try:
            n=int(input("Enter your choice: "))
            
            if n==1:
                print(md.view_task())
                print('\n')
                
                
            elif n==2:
                task=input("Enter task description: ")
                category=input("Enter task category (Work, Personal, etc.): ")
                print(md.add_task(task, category))
                       
            elif n==3:
                try:
                    rmv_i = int(input("Enter the task number to remove: "))
                    print(md.remove_task(rmv_i))
                except ValueError:
                    print("❌ Please enter a valid task number! \n")
            elif n==4:
                try:
                    mark=int(input("Enter task number to mark as complete: "))
                    print(md.mark_task(mark))
                    #print("✅ Task marked as complete! \n")
                except ValueError:
                    print("❌ Please enter the task number as a number! \n")
                
            elif n==5:
                print("Exiting To-Do List. Goodbye!")
                input()
                break
            
            else:
                print("❌ Invalid choice! Please choose between 1-5. \n")
        except ValueError:
            print("Please choose between 1-5! \n")
            
            
            
main()