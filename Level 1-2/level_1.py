import modules_1 as md
def main():
    print("=== Simple File Manager ===")

    options =  """
    1. List files and folders
    2. Create a file
    3. Create a folder
    4. Delete a file
    5. Delete a folder
    6. Rename a file/folder
    7. Read a file
    8. Write to a file
    9. Move a file
    10. Search for a file
    11. Exit
           """
    print(options)
    while True:
        try:
            n=int(input("Enter your choice: "))
            if n==1:
                a=md.storage()
                print(f"Files and folders in {md.path()}: \n")
                for i in a:
                    print(i)
                    
            
                
            elif n==2:
                name = input("Enter file name: ")
                md.create(name)
                print(f"✅ File {name} created successfully! \n")
            
            elif n==3:
                name_k = input("Enter folder name: ")
                md.create_f(name_k)
                print(f"✅ Folder {name_k} created successfully! \n")
            
            elif n==4:
                try:
                    del_name = input("Enter the file name you want to delete: ")
                    md.delete(del_name)
                    print(f"✅ File {del_name} deleted successfully! \n")
                
                except FileNotFoundError:
                    print(f"❌ Could not find the file named {del_name} \n" )
                
            elif n==5:
                try:
                    del_name_f = input("Enter the Folder name you want to delete: ")
                    md.delete_f(del_name_f)
                    print(f"✅ File {del_name_f} deleted successfully! \n")
                
                except FileNotFoundError:
                    print(f"❌ Could not find the Folder named {del_name_f} \n" )
                
                except PermissionError:
                    print("😕 You don’t have permission to delete this folder! \n")
                
                except Exception as e:  
                    print(f"An unexpected error occurred: {e} \n")
                
            elif n==6:
            
                try:
                    old = input("Enter the file name you want to change: ")
                    new = input("Enter the new name: ")
                    md.rename(old, new)
                    print(f"✅ File/Folder {old} changed to {new} \n")
                
                except FileNotFoundError:
                    print(f"❌ Could not find the Folder/File named {old} \n" )
                             
            elif n==7:
                try:    
                    r_name = input("Enter the name of the file you want to read: ")
                    print(md.read(r_name))
                    
                
                except FileNotFoundError:
                    print(f"❌ Could not find the File you want to read \n" )
                    
                except PermissionError:
                    print("😕 You don’t have permission to read this file! \n")

                
            elif n==8:
                w_name = input("Enter the file name: ")
                new_text = input("Enter text to write: ")
                md.write(w_name, new_text)
                print("✅ File updated successfully! \n")
            
            elif n==9:
                try:
                    file = input("Enter the file name: ")
                    destination = input("Enter file destination: ")
                    md.move_f(file, destination)         
                    print("✅ File updated successfully! \n")
                
                except Exception as d:
                    print(f"Please check again: {d} \n")
                
            elif n==10:
                file_name = input("Enter file name to search: ")
                search_path = input("Enter the folder to search in (e.g., C:/Users/Documents): ")
                results = md.search_file(file_name, search_path)
  
                if results:
                    print("\n🔎 Found:")
                    for f in results:
                        print(f"📂 {f} \n")
                    
                else:
                    print(f"❌ No file named '{file_name}' found in '{search_path}'. \n")
                
            elif n==11:
                print("Goodbye!")
                input()
                break
            else:
                print("Please enter 1-11! \n")
                
        
        
        
                
        except ValueError:
            print("Please enter a valid number")



main()