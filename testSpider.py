import json
import time
import urllib.request
userIdNum=[300000000,310000000,320000000,330000000,340000000,350000000,360000000,370000000,380000000,390000000]
url = "http://localhost:3000"
functionUrl="artist/list?limit=1&type=-1&area=-1"
functionUrl2="/song/detail?ids=29850683"
functionUrl4="/user/playlist?uid=315759854"#用户歌单数据
functionUrl3="/playlist/track/all?limit=1000&offset=1&id=438858967&proxy="
#&proxy=
recentSongs="/record/recent/song"
urlParameter1 ="&initial="      #startName
urlParameter2 ="&offset="     #offset
# if __name__ == '__main__':
#     localDataAdd = "E:\\tychema\\1论文\\爬虫\\data\\userID\\userID"
#     with open(localDataAdd +"0"+ ".txt", "r", encoding='gbk') as f:
#         while True:
#             # Get next line from file
#             line = f.readline()
#             # If line is empty then end of file reached
#             if not line:
#                 break;
#             print(line.strip())
#             print(int(line.strip()))

            # Close Close

# if __name__ == '__main__':
#     with open(localDataAdd + "a" + ".txt", "a+", encoding='utf-8') as f:
#         print(localDataAdd + "a" + ".txt")
#         f.write("\n")
#         f.write("48683092"+" "+" Asher"+" "+"无"+" "+"无"+" "+"无")

#
# if __name__ == '__main__':
#     response1=urllib.request.urlopen(url + functionUrl4)
#     content1 = response1.read().decode('utf-8')
#     print(json.loads(content1))
#     response2 = urllib.request.urlopen(url + functionUrl3)
#     content2 = response2.read().decode('utf-8')
#     print(json.loads(content2))

if __name__ == '__main__':
    timeNow=1381419600
    timeArray = time.localtime(timeNow)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime[11:13])
