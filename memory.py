class Memory:
    
    def __init__(self):
        self.data = {}
        
    def save_memory(self, task, result):
        self.data[task] = result
        
    def get_all(self):
        return self.data