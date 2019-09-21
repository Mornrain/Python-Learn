#!/user/bin/python3

# 使用Threading模块创建两个时间线程

import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,delayTime):
        threading.Thread.__init__(self)
        self.threadId = threadID
        self.name = name
        self.delayTime=delayTime
    def run(self):
        print("开始线程： "+self.name)
        print_time(self.name,self.delayTime,5)
        print("结束线程： "+self.name)

def print_time(threadName,threadDelay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(threadDelay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新的线程
Thread1 = myThread(1,"myThread-1",3)
Thread2 = myThread(2,"myThread-2",7)

# 开启新的线程
Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print("退出全部线程")