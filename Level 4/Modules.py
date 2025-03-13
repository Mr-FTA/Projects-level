import json
tasks = {}

with open('task_list.json','a') as f:
    pass

    

def add_task(task,category,due_date=None):
    global tasks
    try:
        with open('task_list.json','r') as f:
            data = f.read()
            if data:
                tasks = json.loads(data)
            else:
                tasks = {}
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = {}
        
    if category not in tasks:
        tasks[category] = []
        
    task_dict = {'task':task}
    
    if due_date and due_date.strip():
        task_dict['due_date'] = due_date.strip()
        
    tasks[category].append(task_dict)
        
    with open('task_list.json','w') as f:
        json.dump(tasks, f, indent=4)
    
    return "✅ Task added successfully! \n"
                
    
def view_task():  
    
    with open('task_list.json','r') as f:
        data=f.read().strip()
        if not data:
            return "No tasks available! \n"
    try:
        tasks = json.loads(data)  if data else {}
    except json.JSONDecodeError:
        tasks = {}
        
    l = 1
    task_formatted = []
    
    for category,tasks_in_category in tasks.items():
        if tasks_in_category:            
            for task in tasks_in_category:
                task_dscrp = task['task']
                due_date = task.get('due_date')
                if due_date:
                    task_formatted.append(f"{l}. {task_dscrp} ({category}) - Due: {due_date}   ")
                else:
                    task_formatted.append(f"{l}. {task_dscrp}   ({category}) ")
                l +=1
            
    return '\n'.join(task_formatted) if task_formatted else "No tasks available! \n"


def mark_task(mark):
    global tasks
    with open('task_list.json','r') as f:
        data = f.read().strip()
        if not data:
            return "No tasks available to mark \n"
    
    tasks = json.loads(data) if data else {}
    task_index=1
    found=False
    
    for category,task_list in tasks.items():
        for i in range(len(task_list)):
            if task_index == mark:
                if "✅" in task_list[i]['task']:
                    return "Task is already marked as complete! \n"
                task_list[i]['task'] = f"✅ {task_list[i]['task']}"
                found = True
                break
            task_index += 1 
        if found:
            break
        
    if not found:
        return "Invalid task number! \n"
    
    with open('task_list.json','w') as f:
        json.dump(tasks,f, indent=4)
    
    return  "✅ Task marked as complete!\n"



def remove_task(rmv_i):
    global tasks
    with open('task_list.json','r') as f:
        data = f.read().strip()
        if not data:
            return "No tasks available to remove! \n "
        
    tasks = json.loads(data) if data else {}
    task_index=1
    found=False
    
   
    for category,task_list in tasks.items():
        for i in range(len(task_list)):
            if task_index == rmv_i:
                if i < len(task_list):
                    del task_list[i]
                found = True
                break                         
                
            task_index += 1   
        if found:
            break
    if not found:
        return "❌ Task index not found. \n"
    
    with open('task_list.json', 'w') as f:
        json.dump(tasks, f, indent=4)
            
    return f"✅ Task {rmv_i} removed successfully! \n"


def view_c_task():
    global tasks
    with open('task_list.json','r') as f:
        data = f.read().strip()
        
    if not data:
        return 'There are no completed tasks ❌'
    
    tasks = json.loads(data) if data else {}
    completed_tasks = {}
    
    
    for category, task_list in tasks.items():
        completed = [task for task in task_list if "✅" in task['task']]
        if completed:
            completed_tasks[category] = completed
    if not completed_tasks:
        return 'There are no completed tasks ❌'
    
    result = "\n✅ Completed tasks ✅\n"
    for category, tasks_category in completed_tasks.items():
        result += f"\n{category}\n"
        for task in tasks_category:
            result += f" - {task['task']}\n"
    return result.strip()

def view_i_task():
    global tasks
    with open('task_list.json','r') as f:
        data = f.read().strip()
    
    if not data:
        return "There are no uncompleted tasks ❌"
       
    tasks = json.loads(data) if data else {}
    uncompleted_tasks = []
    task_index = 1
    
    for category, task_list in tasks.items():
        for task in task_list:
            task_desc = task['task']
            due_date = task.get('due_date')
            
            if "✅" not in task_desc:
                if due_date:
                    uncompleted_tasks.append(f"{task_index}. ❌ {task_desc} ({category}) - Due: {due_date}")
                else:
                    uncompleted_tasks.append(f"{task_index}. ❌ {task_desc} ({category})")
                task_index += 1
                
    return "\n".join(uncompleted_tasks) if uncompleted_tasks else "There are no uncompleted tasks ❌"

def sort_task():
    global tasks
    with open('task_list.json','r') as f:
        data = f.read().strip()
        if not data:
            return "No tasks available! \n"
              
    tasks = json.loads(data) if data else {}
    l=1
    sorted_tasks = []
    
    for category, tasks_in_category in sorted(tasks.items()):
        if tasks_in_category:
            sorted_tasks.append(f"\n--- {category} ---")
            
            for task in tasks_in_category:
                task_desc = task['task']
                due_date = task.get('due_date', 'No due date')
                
                sorted_tasks.append(f"{l}. {task_desc} - Due: {due_date}")
                l += 1
                
    return   '\n'.join(sorted_tasks) if sorted_tasks else "No tasks available! \n"




def edit_task(tsk_i,slc_i,nw_text=None,nw_category=None,nw_date=None):
    global tasks
    with open('task_list.json','r') as f:
        data = f.read().strip()
    
    tasks = json.loads(data) if data else {}
    task_index = 1
    found = False
    
    for category, tasks_in_category in tasks.items():
        for i in range(len(tasks_in_category)):
            if task_index==tsk_i:
                task_data = tasks_in_category[i]  

                if slc_i==1:
                    task_data['task'] = nw_text.strip()
                elif slc_i == 2 and nw_category:
                    
                    if nw_category not in tasks:
                        tasks[nw_category] = []
                    tasks[nw_category].append(task_data)
                    del tasks_in_category[i]
                elif slc_i == 3 and nw_date:
                    task_data['due_date'] = nw_date.strip()
                    
                found = True
                break
            task_index += 1
            
        if found:
            break
    if not found:
        return "❌ Task index not found. \n"
    
    with open('task_list.json','w') as f:
        json.dump(tasks, f, indent = 4 )
    
    return f"✅ Task {tsk_i} updated successfully! \n"
        
        
        


        