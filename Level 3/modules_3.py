import json
tasks = {}

with open('task_list.txt','a') as f:
    pass

    

def add_task(task,category):
    global tasks
    try:
        with open('task_list.txt','r') as f:
            data = f.read()
            if data:
                tasks = json.loads(data)
            else:
                tasks = {}
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = {}
        
    if category not in tasks:
        tasks[category] = []
    tasks[category].append(task)
        
    with open('task_list.txt','w') as f:
        json.dump(tasks, f, indent=4)
    
    return "✅ Task added successfully! \n"
                
    
def view_task():  
    
    with open('task_list.txt','r') as f:
        data=f.read()
        if not data:
            return "No tasks available! \n"
        
    tasks = json.loads(data)    
    l = 1
    task_formatted = []
    
    for category,tasks_in_category in tasks.items():
        if tasks_in_category:
            task_formatted.append(f"--- {category} ---")

            for task in tasks_in_category:
                task_formatted.append(f"{l}. {task}")
                l +=1
            
    return '\n'.join(task_formatted) if task_formatted else "No tasks available! \n"


def mark_task(mark):
    global tasks
    with open('task_list.txt','r') as f:
        data = f.read()
        if not data:
            return "No tasks available to mark \n"
    
    tasks = json.loads(data)
    task_index=1
    found=False
    
    for category,task_list in tasks.items():
        for i in range(len(task_list)):
            if task_index==mark:
                if "✅" in task_list[i]:
                    return "Task is already marked as complete! \n"
                task_list[i] = f"✅ {task_list[i]}"
                found = True
                break
            task_index += 1 
        if found:
            break
        
    if not found:
        return "Invalid task number! \n"
    
    with open('task_list.txt','w') as f:
        json.dump(tasks,f)
    
    return  "✅ Task marked as complete!\n"



def remove_task(rmv_i):
    global tasks
    with open('task_list.txt','r') as f:
        data = f.read()
        if not data:
            return "No tasks available to remove! \n "
        
    tasks = json.loads(data)
    task_index=1
    found=False
    
   
    for category,task_list in tasks.items():
        for i in range(len(task_list)):
            if task_index == rmv_i:
                del task_list[i]
                found = True
                break                         
                
            task_index += 1   
        if found:
            break
    if not found:
        return "❌ Task index not found. \n"
    
    with open('task_list.txt', 'w') as f:
        json.dump(tasks, f, indent=4)
            
    return f"✅ Task {rmv_i} removed successfully! \n"



        
    
        
        


        