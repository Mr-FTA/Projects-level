import os
import shutil

def path():
    return os.getcwd()

def storage():
    return os.listdir(os.getcwd())

def create(name):
    return open(name, "w").close()  

def create_f(name_k):
    return os.mkdir(name_k)
    
def delete(del_name):
    return os.remove(del_name)

def delete_f(del_name_f):
    return shutil.rmtree(del_name_f)

def rename(old,new):
    return os.renames(old, new)

def read(r_name):
    with open(r_name, "r") as file:
        content = file.read()
    return content

def write(w_name,new_text):
    with open(w_name, "w") as file:
        file.write(new_text)
        file.close()
        
def move_f(file,destination):
    return shutil.move(file, destination)

def search_file(filename, search_path):
    found_files = []  
    
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if filename.lower() in file.lower():  
                found_files.append(os.path.join(root, file))

    return found_files  