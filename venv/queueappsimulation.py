from datasection import queue
import random
class printer:
    def __init__(self,pages):
        self.pagerate=pages
        self.currentTask= None
        self.timeRemaining=0
    def tick(self):
        if self.currentTask != None :
            self.timeRemaining-=1
            if self.timeRemaining==0:
                self.currentTask=None
    def busy(self):
        return not self.currentTask==None
    def startNext(self,newTask):
        self.currentTask=newTask
        self.timeRemaining=newTask.get_pages()*60/self.pagerate
class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getstamp(self):
        return self.timestamp
    def get_pages(self):
        return self.pages
    def waitingtime(self,currenttime):
        return currenttime - self.timestamp
def simulation(numseconds,pagesperminute):
    labprinter=printer(pagesperminute)
    printqueue=queue()
    waitingtimes=[]
    for current in range(numseconds):
        if random.randrange(1,181)==180:
            task=Task(current)
            printqueue.enqueue(task)
        if (not labprinter.busy() )and (not printqueue.IsEmpty()):
            nexttask=printqueue.dequeue()
            waitingtimes.append(nexttask.waitingtime(current))
            labprinter.startNext(nexttask)
        labprinter.tick()
    print('avg',sum(waitingtimes)/len(waitingtimes),'remain tasks:',printqueue.size())
simulation(3600,20)
