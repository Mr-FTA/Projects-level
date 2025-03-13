import Modules as md

def main():
    print("=== To-Do List ===")
    commands = """
0. See the list of commands
1. View all tasks
2. View incomplete tasks
3. View completed tasks
4. Add a task
5. Edit a task
6. Remove a task
7. Mark task as complete
8. Sort tasks by category
9. Exit    
          """
    print(commands)
      
    while True:
        try:
            n=int(input("Enter your choice: "))
            if n==0:
                print(commands)
                
                
            elif n==1:
                print(md.view_task())
                print('\n')
                
                
            elif n == 4:
    
                try:
                    task = input("Enter task description: ")
                    if not task.strip():
                        raise ValueError("Task description cannot be empty. Please enter a valid task.")

                    category = input("Enter task category (Work, Personal, etc.): ")
                    if not category.strip():
                        raise ValueError("Category cannot be empty. Please provide a valid category.")

                    due_date = input("Enter due date (YYYY-MM-DD) [Optional]: ").strip()
                  
                    print(md.add_task(task, category, due_date))
                    
                except ValueError as e:
                        print(f"❌ Error: {e}")
            
                except Exception as e:
                    print(f"❌ Unexpected error: {e}")                              
           
            elif n==6:
                print(md.view_task(),'\n')
                try:
                    rmv_i = int(input("Enter the task number to remove: "))
                    print(md.remove_task(rmv_i))
                except ValueError:
                    print("❌ Please enter a valid task number! \n")
            elif n==7:
                print(md.view_task(),'\n')
                try:
                    mark=int(input("Enter task number to mark as complete: "))
                    print(md.mark_task(mark))
                    #print("✅ Task marked as complete! \n")
                except ValueError:
                    print("❌ Please enter the task number as a number! \n")
                
            elif n==9:
                print("Exiting To-Do List. Goodbye!")
                
                break
            elif n==3:
                print(md.view_c_task())
                print('\n')
            elif n==2:
                print(md.view_i_task())
                print('\n')
            elif n==5:
                print(md.view_task(),'\n')

                try:
                    tsk_i = int(input("Enter task number to edit: "))
                    slc_i = int(input("What do you want to edit? (1: Task Name, 2: Category, 3: Due Date): "))
                    if slc_i == 1:
                        nw_text = input("Enter new task name: ")
                        print(md.edit_task(tsk_i, slc_i, nw_text=nw_text))
                    elif slc_i == 2:
                        nw_category = input("Enter the new category name: ")
                        print(md.edit_task(tsk_i, slc_i, nw_category=nw_category))
                    elif slc_i == 3:
                        nw_date = input("Enter new due date: ")
                        print(md.edit_task(tsk_i, slc_i, nw_date=nw_date))
                except ValueError:
                    print("❌ Please enter valid task numbers and selection options.")

            elif n==8:
                print(md.sort_task())
                print('\n')
            
            else:
                print("❌ Invalid choice! Please choose between 1-5. \n")
        except ValueError:
            print("Please choose between 0-9! \n")
            
            
            
main()