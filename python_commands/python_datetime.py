from datetime import datetime

a = 'Sun 10 May 2015 13:54:36 -0700'
b = 'Sun 10 May 2015 13:55:36 -0700'
c = 'Sat 02 May 2015 19:54:36 +0530'
d = 'Fri 01 May 2015 13:54:36 -0000'

def create_datetime(string):
	adate = datetime.strptime(string, '%a %d %b %Y %H:%M:%S %z')
	return adate

def time_diff(astring, bstring):
	atime = create_datetime(astring)
	btime = create_datetime(bstring)
	ellapsed = atime - btime
	return int(abs(ellapsed.total_seconds()))

# adatetime = create_datetime(a)
tdiff = time_diff(a, b)
print(tdiff)