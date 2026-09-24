import unittest
from Todo import TodoManager

class TestToDo(unittest.TestCase):
    def test_addtask(self):
        manager = TodoManager()
        task = "coding"
        manager.add_task(task)
        self.assertEqual(manager.task_dic[task],False)
    
    def test_addtask_type(self):
        manager = TodoManager()
        task = 1234
        self.assertRaises(TypeError , manager.add_task , task)
    
    def test_addtask_emtpystr(self):
        manager = TodoManager()
        task = " "
        self.assertRaises(ValueError, manager.add_task , task)
    
    def test_addtask_repetetive(self):
        manager = TodoManager()
        manager.add_task("coding")
        task = "coding"
        self.assertRaises(ValueError , manager.add_task , task)

if __name__== "__main__":
    unittest.main()