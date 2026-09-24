def log(f):
    def wrapper(*args , **kwargs):
        try:
            print(f'Calling {f.__name__}')
            return f(*args, **kwargs)
            
        except Exception as e :
            print(f'ERROR : {e}')
    return wrapper


class TodoManager():
    def __init__(self):
        self.task_dic = {}
        
    #methods
       
    @log 
    def add_task(self,task):
        '''
        param = task [str]
        add to your manager.
           
        '''
        if not isinstance(task , str):
            raise TypeError("task must be a string")
        if not task.strip():
            raise ValueError("task must have at least one char  !!!")
        if task in self.task_dic:
            raise ValueError("this task is repetitive")
        self.task_dic[task] = False
        
    @log
    def remove_task(self , task):
        '''
        param = task [str]
        remove your task.
        
        '''
        if task not in self.task_dic:
            raise ValueError("task not found.")
        self.task_dic.pop(task)

    @log     
    def complete_task(self, task):
        '''
        param = task [str]
        check your task as completed.
         
        '''
        if task in self.task_dic:
            self.task_dic[task] = True
        else:
            raise ValueError("task not found !!")
    
    @log   
    def get_tasks(self):
        '''
        
        Show your active tasks.
         
        '''
        return self.task_dic
    
pass


manager = TodoManager()

manager.add_task('learn python')
l = manager.get_tasks()
print(l)

manager.add_task("learn python")
manager.add_task(task="play music")
manager.add_task(1234)
# manager.add_task('play music')
# manager.add_task('swiming')
# manager.add_task('coding')

# manager.add_task(1234)
# manager.add_task('coding')
# manager.add_task(' ')

# manager.remove_task('ride')
# manager.remove_task("coding")
# manager.complete_task("coding")
# manager.get_tasks()