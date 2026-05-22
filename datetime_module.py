import datetime 
d= datetime.date(2025,2,1) #yyyy/mm/dd format
print(d)

today=datetime.date.today()
print(today)
print(today.year)
print(today.weekday()) #monday =0 and sunday=6
print(today.isoweekday()) #monday =1 and sunday=7

td= datetime.timedelta(days=7)#creates diff of days in bracket
print(today + td) #gives date of next 7 days
print(today - td)

bday=datetime.date(2027,2,1)
till_bday=bday-today
print("time till your b day is:", till_bday)
print("time till your b day is(in seconds):", till_bday.total_seconds())#gives total seconds

t=datetime.time(9,55,20,500)#hrs,min,sec,microsec format
print(t)
print(t.hour)
print(t.minute)
print(t.second)
c=datetime.datetime(2026,2,8,4,3,50)
print(c)
tt=datetime.datetime.today()
print(tt)
print(tt.date())
print(tt.time())
td2=datetime.timedelta(hours=5)
print(tt+td2)
dt_today=datetime.datetime.today() #gives current time with timezone set to none
dt_now=datetime.datetime.now() #gives opp top set time zone
dt_utcnow=datetime.datetime.utcnow()
print(dt_today)
print(dt_now) 
print(dt_utcnow) 