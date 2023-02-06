#正确的用户ID
import urllib.request
import json
import threading

# url
url = "http://localhost:3000/user/detail?uid="
# 本地路径
localDataAdd = "D:\\1论文\\爬虫\data\\userID\\userID"
#userID开始点
userIdNum=[300000000,310000000,320000000,330000000,340000000,350000000,360000000,370000000,380000000,390000000]
class myThread(threading.Thread):  # 继承父类threading.Thread
    myUserID=0;
    def __init__(self, threadID, name, counter,myUserID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.myUserID = myUserID

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name + str(userIdNum[self.threadID]))
        for i in range(self.myUserID,self.myUserID+10000000,1):
            try:
                print(url+str(i))
                response = urllib.request.urlopen(url+str(i))
            except:
                print("error:请求失败1")
                continue
            content = response.read().decode('utf-8')
            try:
                if response.code==200:
                    print(response.code)
                else:
                    print("error"+response.code)
                    continue
                # 字典查找+str转json（字典）
                # userID 用户ID
            except:
                print("error:请求代码错误")
            try:
                userID_int = json.loads(content)['userPoint']['userId']
                userID = str(userID_int)
                print(userID)
            except:
                print("error：没找到UserID")
                continue
            #写入
            try:
                # 数据类型 字典
                # print(type(json.loads(content)))
                with open(localDataAdd+str(self.threadID)+".txt", "a+") as f:
                    print(localDataAdd + str(self.threadID) + ".txt")
                    f.write("\n")
                    f.write(userID)
                userIdNum[self.threadID]=userID_int;
            except:
                print("error:写入失败")
                continue
        print("Exiting " + self.name)


if __name__ == '__main__':
    #最后一行的userID
    for i in range(10):
        try:
            with open(localDataAdd +str(i)+ ".txt", "rb") as f:
                off = -50
                while True:
                    f.seek(off,2)
                    lines = f.readlines()
                    if len(lines)>=2:
                        last_line = lines[-1]
                        userIdNum[i] = int(last_line)
                        break
                    off *= 2
        except:
            print("txtError")
    thread0 = myThread(0, "Thread-0", 0 ,userIdNum[0]+1);thread0.start()
    thread1 = myThread(1, "Thread-1", 1, userIdNum[1]+1);thread1.start()
    thread2 = myThread(2, "Thread-2", 2, userIdNum[2]+1);thread2.start()
    thread3 = myThread(3, "Thread-3", 3, userIdNum[3]+1);thread3.start()
    thread4 = myThread(4, "Thread-4", 4, userIdNum[4]+1);thread4.start()
    thread5 = myThread(5, "Thread-5", 5, userIdNum[5]+1);thread5.start()
    thread6 = myThread(6, "Thread-6", 6, userIdNum[6]+1);thread6.start()
    thread7 = myThread(7, "Thread-7", 7, userIdNum[7]+1);thread7.start()
    thread8 = myThread(8, "Thread-8", 8, userIdNum[8]+1);thread8.start()
    thread9 = myThread(9, "Thread-9", 9, userIdNum[9]+1);thread9.start()
