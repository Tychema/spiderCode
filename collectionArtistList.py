#抓取以a-z开头的所有歌手信息及其id
#-1代表热门0代表＃
import json
import threading
import urllib.request

url = "http://localhost:3000/"
functionUrl="artist/list?limit=1&type=-1&area=-1"
urlParameter1 ="&initial="      #startName
urlParameter2 ="&offset="     #offset
localDataAdd = "D:\\1论文\\爬虫\data\\artistCollection\\"
offsetNum=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
class myThread(threading.Thread):  # 继承父类threading.Thread
    myUserID=0;
    def __init__(self, threadID, name, counter,startName,offset):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.id =id                #唯一识别标识
        self.startName = startName #首字母
        self.offset = offset       #偏移量

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name +" "+str(self.offset))
        #print((url +functionUrl+urlParameter1 + self.startName +urlParameter2 + str(i)))
        #response = urllib.request.urlopen((url + functionUrl+urlParameter1 + self.startName +urlParameter2 + str(i)))
        for i in range(self.offset,self.offset+10000000,1):
            try:
                print(url+functionUrl+urlParameter1+self.startName+urlParameter2+str(i))
                response = urllib.request.urlopen(url+functionUrl+urlParameter1+self.startName+urlParameter2+str(i))
                # if content == json.loads(response.read().decode('utf-8'))['artists'][0] =='':
                #     break
                #content = json.loads(response.read().decode('utf-8'))['artists'][0]
            except:
                print("error:请求失败1")
                continue
            content = json.loads(response.read().decode('utf-8'))['artists'][0]
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
            print(content)
            try:
                try:
                    artistId_int = content["id"]
                    artistId = str(artistId_int)
                    print("artistId:"+artistId)
                except:
                    print("error：没找到artistId_int")
                    artistId = "无"
                try:
                    artistName = content["name"]
                    print("artistName:"+artistName)
                except:
                    print("error：没找到artistName")
                    artistName = "无"
                try:
                    musicSize = str(content["musicSize"])
                    print("musicSize:"+str(musicSize))
                except:
                    print("error：没找到musicSize")
                    musicSize = "无"
                try:
                    albumSize = str(content["albumSize"])
                    print("artistId:"+str(albumSize))
                except:
                    print("error：没找到artistId_int")
                    albumSize = "无"
                try:
                    fansCount = str(content["fansCount"])
                    print("fansCount:"+str(fansCount))
                except:
                    print("error：没找到fansCount")
                    fansCount = "无"
            except:
                print("error：没找到一个属性")
                continue
            #写入

            try:
                with open(localDataAdd + self.startName + ".txt", "a+", encoding='gbk') as f:
                    print(localDataAdd + self.startName + ".txt")
                    print(str(i) + " " + artistId + " " + artistName + " " + musicSize + " " + albumSize + " " + fansCount)
                    f.write("\n")
                    f.write((str(i) + " " + artistId + " " + artistName + " " + musicSize + " " + albumSize + " " + fansCount))
                with open(localDataAdd + self.startName + "Content" + ".txt", "a+", encoding='gbk') as f1:
                    f1.write("\n")
                    f1.write(json.dumps(content))
            except:
                print("error:写入失败")
                continue
        print("Exiting " + self.name)

if __name__ == '__main__':
    # 最后一行的offset
    # for i in range(26):
    #     try:
    #         with open(localDataAdd + str(i) + ".txt", "rb") as f:
    #             off = -50
    #             while True:
    #                 f.seek(off, 2)
    #                 lines = f.readlines()
    #                 if len(lines) >= 2:
    #                     last_line = lines[-1]
    #                     list=last_line.split()
    #                     offsetNum[i] = int(list[0])
    #                     break
    #                 off *= 2
    #     except:
    #         print("txtError")
    #thread0 = myThread(0, "Thread-0", 0, "a",offsetNum[0]);thread0.start()
    #thread1 = myThread(1, "Thread-1", 1, "b",offsetNum[1]);thread1.start()
    #thread2 = myThread(2, "Thread-2", 2, "c",offsetNum[2]);thread2.start()
    #thread3 = myThread(3, "Thread-3", 3, "d",offsetNum[3]);thread3.start()
    #thread4 = myThread(4, "Thread-4", 4, "e",offsetNum[4]);thread4.start()
    #thread5 = myThread(5, "Thread-5", 5, "f",offsetNum[5]);thread5.start()
    #thread6 = myThread(6, "Thread-6", 6, "g",offsetNum[6]);thread6.start()
    #thread7 = myThread(7, "Thread-7", 7, "h",offsetNum[7]);thread7.start()
    #thread8 = myThread(8, "Thread-8", 8, "i",offsetNum[8]);thread8.start()
    #thread9 = myThread(9, "Thread-9", 9, "j",offsetNum[9]);thread9.start()
    #thread10 = myThread(10, "Thread-10", 10 ,"k",offsetNum[10]);thread10.start()
    #thread11 = myThread(11, "Thread-11", 11, "l",offsetNum[11]);thread11.start()
    #thread12 = myThread(12, "Thread-12", 12, "m",offsetNum[12]);thread12.start()
    #thread13 = myThread(13, "Thread-13", 13, "n",offsetNum[13]);thread13.start()
    #thread14 = myThread(14, "Thread-14", 14, "o",offsetNum[14]);thread14.start()
    #thread15 = myThread(15, "Thread-15", 15, "p",offsetNum[15]);thread15.start()
    #thread16 = myThread(16, "Thread-16", 16, "q",offsetNum[16]);thread16.start()
    #thread17 = myThread(17, "Thread-17", 17, "r",offsetNum[17]);thread17.start()
    #thread18 = myThread(18, "Thread-18", 18, "s",offsetNum[18]);thread18.start()
    #thread19 = myThread(19, "Thread-19", 19, "t",offsetNum[19]);thread19.start()
    #thread20 = myThread(20, "Thread-20", 20 ,"u",offsetNum[20]);thread20.start()
    #thread21 = myThread(21, "Thread-21", 21, "v",offsetNum[21]);thread21.start()
    #thread22 = myThread(22, "Thread-22", 22, "w",offsetNum[22]);thread22.start()
    #thread23 = myThread(23, "Thread-23", 23, "x",offsetNum[23]);thread23.start()
    #thread24 = myThread(24, "Thread-24", 24, "y",offsetNum[24]);thread24.start()
    #thread25 = myThread(25, "Thread-25", 25, "z",offsetNum[25]);thread25.start()
    thread26 = myThread(26, "Thread-26", 26, "-1",offsetNum[26]);thread26.start()