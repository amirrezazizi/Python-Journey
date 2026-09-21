class TodoManager():
    def __init__(self):
        self.task_dic = {}
        
    #methods
        
    def add_task(self,task):
        '''
        param = task [str]
        add to your manager.
           
        '''
        try:
            if len(task) == 0 or task == " " :
                raise ValueError("task must have at least one char  !!!")
            self.task_dic[task] = False
        except ValueError as e:
            print("ERROR" , e)
        
        
    def remove_task(self , task):
        '''
        param = task [str]
        remove your task.
        
        '''
        pass
    def complete_task(self, task):
        '''
        param = task [str]
        check your task as completed.
         
        '''
        pass
    def get_tasks(self):
        '''
        
        Show your active tasks.
         
        '''
        pass
    
pass