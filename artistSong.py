#打开歌手信息，抓取该歌手的所有（上限200）歌曲信息
import json
import threading
import urllib.request
url = "http://localhost:3000"
functionUrl="/artist/songs?limit=200&order=hot&id="
localDataAdd = "D:\\1论文\\爬虫\data\\artistCollection\\"
localDataWriteAdd="D:\\1论文\\爬虫\data\\songs\\"
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
        with open(localDataAdd+self.startName+".txt","r",encoding='gbk') as f:
            for i in range(0,1000):
                f.readline(i)
        response = urllib.request.urlopen(url + functionUrl)
        content = response.read().decode('utf-8')



if __name__ == '__main__':
    k=0
    #读歌手ID
    with open(localDataAdd + "n" + ".txt", "r", encoding='gbk') as f:
         for i in range(1, 1000):
            a = f.readline()
            if a=="" or a=="\n" or a==" ":
                continue
            try:
                artistId=a.split()[1]
                artistName=a.split()[2]
            except:
                continue
            print(artistId)
            try:
                #请求该歌手全部歌曲
                response = urllib.request.urlopen(url+functionUrl+str(artistId))
                content = response.read().decode('utf-8')
                data = json.loads(content)["songs"]
            except:
                print("error:请求错误")
                continue
            try:
                #全部歌曲
                for j in data:
                    album =j["al"]
                    songID=j["id"]
                    songName=j["name"]
                    albumID=album["id"]
                    albumName=album["name"]
                    print(str(k)+" "+str(artistId)+" "+str(artistName)+" "+str(songID)+" "+songName+" "+str(j["id"])+" "+str(albumID)+" "+str(albumName))
                    print(str(k)+" "+str(songID)+" "+songName+" "+str(j)+"\n")
                    #with open(localDataWriteAdd+"z"+".txt","a+",encoding='utf-8') as f2:
                        #f2.write(str(k)+" "+str(artistId)+" "+str(artistName)+" "+str(songID)+" "+songName+" "+str(j["id"])+" "+str(albumID)+" "+str(albumName)+"\n")
                    with open(localDataWriteAdd+"n"+"context.txt","a+",encoding='utf-8') as f2:
                        f2.write(str(k)+" "+str(songID)+" "+songName+str(j)+"\n")
                    k=k+1
            except:
                print("error:写入错误")
                continue
