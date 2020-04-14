import time
from dateutil.parser import parse
import datetime


t = '/Date(1581868800000)/'
 
print(time.ctime(1581868800.000))

s='1581868800.000'
timeArray = time.localtime(float(s))
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

# time_local = time.localtime('1581868800000')#格式化时间戳为本地时间
# time_YmdHMS = time.strftime("%Y%m%d_%H%M%S",time_local)#自定义时间格式

# h = parse(t)
# v = time.gmtime(t)

# x = time.strptime(t, '%Y-%m-%d %H:%M')

# print(x)


# import time
 
# timeStamp = 1557502800
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)

# 执行以上代码输出结果为：

# 2019-05-10 23:40:00

# 实例 4

 
timeStamp = 1581868800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)