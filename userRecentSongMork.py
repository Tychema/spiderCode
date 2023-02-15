# 本脚本生产的所以数据均为虚假数据仅供测试


import datetime
import random
import time



#本地路径
userIDAddress="D:\\1论文\\爬虫\\data\\userID\\userID"
userDetailAddress="D:\\1论文\\爬虫\\data\\userDetail\\"
songsAddress="D:\\1论文\\爬虫\data\\songs\\"
#歌曲比例
#热门歌手热门歌曲（-1）占70%
#其他编号占1%左右
#每个编号共6w首随机
hotSongsRate=0.7
otherSonsRate=0.01
#生成随机时间戳
def strTimeProp(start, end, prop, frmt):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)

#生成随机时间戳
def randomTimestamp(start, end, frmt='%Y-%m-%d %H:%M:%S'):
    return strTimeProp(start, end, random.random(), frmt)

#随机生成数
def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

#获取用户ID
def getUserID(startNum):
    with open(userIDAddress +str(startNum)+".txt", "r") as f1:
        randomLine = random.randint(0,60000)
        for i in range(randomLine):
            line = f1.readline()
        if not line:
            return -1;
        myUserID = str(line.strip())
        return myUserID

def getSongsDetail(startChar):
    start_time = time.time()
    songsDetail=""
    with open(songsAddress + startChar + ".txt", "r",encoding="utf-8") as f1:
        randomLine = random.randint(0, 90000)
        for i in enumerate(f1):
            if list(i)[0]==randomLine:
                end_time = time.time()
                print("time cost:", float(end_time - start_time) * 1000.0, "ms")
                return list(i)[1]

startTime = '2022-01-01 12:12:12'
endTime = '2022-12-30 00:00:00'

#获取开始时间、结束时间和歌曲时长
def getStartTimeAndEndTime():
    # 时间戳生成时间
    playStartTime = randomTimestamp(startTime, endTime)
    rate = [50, 400, 400, 25, 1]
    RateTime = [120, 180, 240, 270, 300, 420]
    index1 = random_index(rate)
    dt = random.randint(RateTime[index1], RateTime[index1 + 1])
    listenRate = [10, 10, 100, 100]
    listenTime = [1, 60, 120, dt, dt]
    index2 = random_index(listenRate)
    if index2 != 4:
        playEndTime = playStartTime + random.randint(listenTime[index2], listenTime[index2 + 1])
    else:
        playEndTime = playStartTime + dt
    return [playStartTime,playEndTime,dt]

json = {'userId': '26159000', 'playStartTime': 1675662095361,'platEndTime':1675662095390, 'resourceType': 'SONG',
        'data': {'name': 'Moonlight', 'id': 26159000, 'pst': 0, 't': 0,
                 'ar': [{'id': 42898, 'name': 'Rameses B', 'tns': [], 'alias': []}], 'alia': [], 'pop': 95, 'st': 0,
                 'rt': '', 'fee': 8, 'v': 29, 'crbt': None, 'cf': '', 'al': {'id': 2400916, 'name': 'Inspire - EP',
                                                                             'tns': []}, 'dt': 343714,
                                                                             'a': None, 'cd': '1', 'no': 2,
                 'rtUrl': None, 'ftype': 0, 'rtUrls': [], 'djId': 0, 'copyright': 2, 's_id': 0, 'mark': 270464,
                 'originCoverType': 0, 'originSongSimpleData': None, 'single': 0, 'noCopyrightRcmd': None, 'mst': 9,
                 'cp': 743010, 'mv': 0, 'rtype': 0, 'rurl': None, 'publishTime': 1337702400007}, 'banned': False}


#userId 用户ID
#playStartTime 播放开始时间
#playStartTime 播放结束时间
#dt 歌曲长度
#data.name 歌曲名
#data.id 歌曲ID
#data.al.id
#data.al.name
if __name__ == '__main__':
    #参数是0-9用户ID是按这个划分的
    userID = getUserID(0)
    timeList=getStartTimeAndEndTime()
    # randomEndTime = randomTimestamp(startTime, endTime)
    # userID=getUserID(0)
    # songsDetail=getSongsDetail("-1")
    # songsDetailList=songsDetail.split(" ")
    # songsName=list(songsDetailList)[4]
    # json["data"]["name"]=list(songsDetailList)[4]
    # print(json["data"]["name"])
