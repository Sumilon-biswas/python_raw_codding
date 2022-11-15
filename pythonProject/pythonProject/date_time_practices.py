# # import  datetime
# from  datetime import  date
# from  datetime import  time
# from  datetime import  datetime
# from  datetime import datetime,date
from  datetime import  timedelta

# date_time = datetime.datetime.now()
# print(date_time)

# date_time=datetime.datetime.today()
# print(date_time)
# print(dir(date_time))

# dateTime = datetime.date(2020,11,26)
# print(dateTime)

# dateTime = date.today()
# print(dateTime)
#
# data = date(2022,10,25)
# print("full result :",data)
# print("current date is :",data.year)
# print("current date is :",data.month)
# print("current date is :",data.min)

# timestmap=data.fromtimestamp(234445)
# print("this is get year of month :",timestmap)

# getTimeof = data.fromtimestamp(234335)
# print("this is finally result :",getTimeof)
#
# get_show_date= date.fromtimestamp(543627)
# print("get show year month and day :",get_show_date)

print("==================")

# today =data.today()
# print("full date time today",today)
# print("current of year :",today.year)
# print("current of month :",today.month)
# print("current of day :",today.day)

# data_show = date(2020,11,23)
# print("finally result is:",data_show)
# print("this is  year :",data_show.year)
# print("this is month :",data_show.month)
# print("this is day :",data_show.day)

# time = time(11,44,59)
# print("Total time is :",time)
# print(" hour of :",time.hour)
# print("mintue of :",time.minute)
# print("second of :",time.second)

# time = time(12,34,45,123232)
#
# print("total time is it :",time)
# print("hour of :",time.hour)
# print("minute of :",time.minute)
# print("second of  :",time.second)
# print("microsecond :",time.microsecond)

# print("=====================")
#
# a = time(11,34,56)
# print("full of hours",a)
# print("Hours",a.hour)
# print("minutes",a.minute)
# print("second ",a.second)

# datetime = datetime(2010,10,11,15,9,56,212321)
# a=datetime.fromtimestamp(datetime.microsecond)
#
# print("full time of :",datetime)
# print("date of year :",datetime.year)
# print("date of month :",datetime.month)
# print("date of days :",datetime.day)
# print("date of hours :",datetime.hour)
# print("date of minutes :",datetime.minute)
# print("date of second :",datetime.second)
# print("date of microsecond :",datetime.microsecond)
# print("total mintiues of :",a)

# datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =",datetime.year)
# print("month =",datetime.month)
# print("day =",datetime.day)
# print("Hours :",datetime.hour)
# print("minutes :",datetime.minute)
# print("Second :",datetime.second)
# # print("microsecond :",datetime.microsecond)
# print("timestamp ",datetime.timestamp())
#
# data =datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =",data.year)
# print("month =",data.month)
# print("day =",data.day)
# print("Hour =",data.hour)
# print("minutes =",data.minute)
# print("second =",data.second)
# print("microsecond =",data.microsecond)
# print("timestamp =",data.timestamp())
#
# time = data.timestamp()

# t1=date(year=2018,month=7,day=12)
# t2=date(year=2017,month=12,day=2)
# t3= t1-t2
# print("t3",t3)
#
# t4= datetime(year=2018, month=7,day=12,hour=7,minute=9,second=33)
# t5 = datetime(year=2017,month=6 ,day=10, hour=5, minute=55,second=33)
# t6=t5=t4
# print("total result ",t6)
#
# print("type of t3 :",type(t3))
# print("type of t6 :", type(t6))
#
# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print("t3 =", t3)
# print("type of t3",type(t3))

# t1 = date(year= 2019, month= 8, day= 12)
# # t2 = date(year= 2017,month= 10, day= 23)
# # t3 = t1 - t2
# # print(t3)

# t1 = datetime(year=2020, month = 8, day = 23, hour= 17,minute= 45 ,second= 33)
# t2 = datetime(year=2019,month=9, day=25, hour=6,minute=59, second=50)
# t3 = t1 -t2
# print(t3)
#
# t1 = date(year=2021, month=9, day=25)
# t2 = date(year= 2018,month=10,day=21)
# t3 = t1- t2
# print(t3)
# print("=======================")
#
# dt1 = datetime(year=2021,month=8, day=26, hour= 10,minute=45,second=47)
# dt2 =datetime(year= 2019,month= 9,day=25,hour=9,minute=45,second=35)
# dat3 = dt1 - dt2
#
# print(dat3)

# dt1= timedelta(weeks=2 ,days=5 ,hours=5,minutes=48,seconds=33)
# dt2 = timedelta(days=10,hours=20,minutes=50,seconds=45)
# dt3 = dt1- dt2
# print(dt3)
dt1 =timedelta(seconds=33)
dt2 =timedelta(seconds=45)
dt3 =dt1 -dt2
print(dt3)



