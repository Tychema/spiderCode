import json
import random
import threading
import time
import urllib.request
url = "http://localhost:3000"
functionUrl1=""
functionUrl2="/user/playlist?uid="#用户歌单数据
functionUrl3="/playlist/track/all?limit=80&offset=1&id="#歌单里面的歌曲
localDataAdd = "D:\\1论文\\爬虫\data\\userID\\userID"
userIDAddress="D:\\1论文\\爬虫\\data\\userID\\userID"
userDetailAddress="D:\\1论文\\爬虫\\data\\userDetail\\"

a=60
def writeText(writeContext,startName):
    with open(userDetailAddress+startName+".txt","a+",encoding='gbk') as f2:
        f2.write(writeContext+ "\n")

def getStartUserID()->int:
    try:
        with open(userDetailAddress + "0" + ".txt", "rb") as f:
            while True:
                line1=f.readline()
                if not line1:
                    print(line2.decode("gbk"))
                    print(int(line2.decode("gbk")[0:9]))
                    return int(line2.decode("gbk")[0:9])
                line2=line1
    except:
         print("txtError")
         return 300000000

class myThread(threading.Thread):  # 继承父类threading.Thread
    myUserID=0;
    def __init__(self, threadID, name, counter,startName,startUserID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.startName=startName
        self.startUserID = startUserID

    def run(self):  # 把要执行的userIDAddress代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        with open(userIDAddress +self.startName+".txt", "r") as f1:
            while True:
                #读取一行数据
                line = f1.readline()
                if not line:
                    break;
                #获取用户ID
                userID = str(line.strip())
                print(str(userID)+" "+str(int(self.startUserID or 0)))
                #从爬取过的用户ID之后开始爬取
                if int(userID)<=self.startUserID:
                    continue
                #获取用户的歌单信息
                try:
                    response1 = urllib.request.urlopen(url + functionUrl2 + userID)
                    content1 = response1.read().decode('utf-8')
                except Exception as e1:
                    print('错误明细1是', e1.__class__.__name__, e1)  # continue#jia
                    continue
                try:
                    playList = json.loads(content1)["playlist"]
                except Exception as e2:
                    print('错误明细2是', e2.__class__.__name__, e2)  # continue#jia
                    continue
                #playList[0]就是我最爱的歌单，通过这个歌单的ID请求这个歌单
                try:
                    # a=1
                    # time.sleep(random.uniform(1,a))
                    time.sleep(2)
                    response2 = urllib.request.urlopen(url + functionUrl3 + str(playList[0]["id"]))
                except Exception as e3:
                    print('错误明细3是', e3.__class__.__name__, e3)
                    if len(playList)==0:
                        time.sleep(2)
                    else:
                        time.sleep(60)
                    continue
                #遍历这个最喜欢的歌单
                #按行存储
                content2 = response2.read().decode('utf-8')
                songsList = json.loads(content2)["songs"]
                for k in range(0, len(songsList)):
                    # print(songsList[k])
                    try:
                        # 数据格式：用户ID+歌单ID+歌单名+歌曲id＋歌曲名+歌手id+歌手名+专辑ID＋专辑名+歌曲时间
                        writeContext = userID + " " + str(playList[0]["id"]) + " " + playList[0][
                            "name"] + " " + str(songsList[k]["id"]) + " " + songsList[k]["name"] + " " + str(
                            songsList[k]["ar"][0]["id"]) + " " + songsList[k]["ar"][0]["name"] + " " + str(
                            songsList[k]["al"]["id"]) + " " + songsList[k]["al"]["name"] + " " + str(
                            songsList[k]["dt"])
                        print(writeContext)
                        while True:
                            try:
                                time.sleep(0.5)
                                writeText(writeContext,self.startName)
                                break
                            except Exception as e4:
                                print('错误明细4是', e4.__class__.__name__, e4)
                            break
                    except Exception as e5:
                        print('错误明细5是', e5.__class__.__name__, e5)

if __name__ == '__main__':
    userID=getStartUserID()
    print(userID)
    thread0 = myThread(0, "Thread-0", 0 ,"0",userID);thread0.start()
    # thread1 = myThread(1, "Thread-1", 1, "1");thread1.start()
    # thread2 = myThread(2, "Thread-2", 2, "2");thread2.start()
    # thread3 = myThread(3, "Thread-3", 3, "3");thread3.start()
    # thread4 = myThread(4, "Thread-4", 4, "4");thread4.start()
    # thread5 = myThread(5, "Thread-5", 5, "5");thread5.start()
    # thread6 = myThread(6, "Thread-6", 6, "6");thread6.start()
    # thread7 = myThread(7, "Thread-7", 7, "7");thread7.start()
    # thread8 = myThread(8, "Thread-8", 8, "8");thread8.start()
    # thread9 = myThread(9, "Thread-9", 9, "9");thread9.start()

