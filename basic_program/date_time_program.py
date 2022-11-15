import  datetime
import time

# datatime_object = datetime.datetime.now()
# print(datatime_object)
# datatime=datetime.date.today()

# today =datetime.date.today()
# print("today:",today)
#
# set_date=datetime.date(2019,4,7)
# print(set_date)
#
# sets_date =datetime.date(2020,8,19)
# print(sets_date)

#
# timestamp =date.fromtimestamp(123344567)
# print("time stamp :",timestamp)
# from datetime import date
#
# data = date.today()
#
# print("get month,get year ,get days")
# print("get year ",data.year)
# print("get month :",data.month)
# print("get date :",data.day)

# Time object to represent time
# from  datetime import time

# a =time()
# print("Result is",a)
# b =time(12,23,44)
# print("get time its :",b)
#
# c=time(hour=20,minute=45,second=59,microsecond=1000)
# print(c)
#
# time=time(23,45,56,1000)
# print("get hours",time.hour)
# print("get min",time.minute)
# print("get second",time.second)
# print("gett microsecond",time.microsecond)

# from  datetime import  datetime
# data=datetime(2011,9,24)
# print(data)
#
# dataTime=datetime(2016,10,23,13,45,59,1000)
# print(dataTime)
# # print(
# dataTime.strftime("%y %m %d ,%H:%M:%S")
# print(dataTime)

from  datetime import  datetime

# data = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =",data.year)
# print("month =",data.month)
# print("days =",data.day)
# print("Hours =",data.hour)
# print("Minute =",data.minute)
# print("Second =",data.second)
# print("microsecond =",data.microsecond)
#
# data = datetime(2018,8,24,23,48,59,746764)
# print(data)
# print("year =",data.year)
# print("month=",data.month)
# print("days =",data.day)
# print("Hours =",data.hour)
# print("minutes =",data.minute)
# print("second =",data.second)
# print("microsecond =",data.microsecond)

#differences between two data and minutes
#
# from  datetime import  datetime, date
#
# # f1=datetime(year=2017, month=7,day=25,hour=19,minute=25,second=26,microsecond=535882)
# # f2=datetime(year=2018,month=8,day=20,hour=14,minute=28,second=30,microsecond=743333)
# # f3 = f2 -f1
# # print("F3",f3)
#
# data1=datetime(year=2018,month=9,day=29,hour=18,minute=45,second=45,microsecond=234885)
# data2=datetime(year=2019,month=7,day=20,hour=20,minute=55,second=57,microsecond=843843)
# data3=data2 -data1
# print("result is :",data3)

# from datetime import timedelta
#
# t1=timedelta(days=23,hours=23,minutes=43,seconds=45,microseconds=84644)
# print("duration of time =",t1.total_seconds())
# t2=timedelta(days=4,hours=23,minutes=55,seconds=45)
# print("duration of time :",t2.total_seconds())

# python datetime formating

# from  datetime import  datetime
#
# # dateForNow=datetime(year=2017,month=9,day=23,hour=18,minute=45,second=44)
# # print(dateForNow.strftime("%y %m %d  %H : %M :%S"))
#
# data1=datetime(year=2018, month=10,day=25,hour=7,minute=23,second=44)
# print(data1.strftime("%y %m %d %H : %M : %S"))

# using time moduls and use sleep function

# while True:
#     locale=time.localtime()
#     result=time.strftime("%y %m %d %H:%M:%S",locale)
#     print("display time show :",result)
#     time.sleep(1)

import  time
from  datetime import  datetime

datetime=time.time()
result = datetime.strftime("%y %m %d  %H:%M:%S")
print("display for  time :",result)
time.sleep(2)









# from  datetime import  date
#
# today= date.today()
# # print(today)
# d1=today.strftime("%y %m %d")
# d2=today.strftime("%m %d %y")
# d3=today.strftime("%d %m %y")
# print(d1)
# print("==========")
# print(d2)
# print("=============")
# print("b3",d3)
#
# d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)
#
# from  datetime import  datetime
#
# today = datetime.now()
# print(today)
# print("===============")
# str_date=today.strftime("%y %m %d , %H : %M : %S")
# print(str_date)