from multiprocessing import Pool, Process
import os

class ProcessPooler:
    def __init__(self,opqueue):
        self.opqueue = opqueue
        self.pool = Pool(1 if os.cpu_count==1 else os.cpu_count-1)
        self.results = []
        self.listenerProcess = Process(target=resultListener, daemon=True)
        self.listenerProcess.start()

    def addToPool(self,task,args):
        self.results.append(self.pool.apply_async(task,args))

    def resultListener(self):
        while len(self.results) == 0: pass 
        for r in self.results:
            self.opqueue.put(r.get())
        self.resultListener()