from multiprocessing import Queue, Manager, Process

class OutputQueue:
    def __init__(self):
        self.manager = Manager()
        self.queue = self.manager.Queue()
        self.listenerProcess = Process(target=outputListener,daemon=True)
        self.listenerProcess.start()

    def put(self,obj):
        self.queue.put(obj)

    def outputListener(self):
        while len(self.queue) == 0: pass
        for o in self.queue:
            print(o.get())
        self.outputListener()