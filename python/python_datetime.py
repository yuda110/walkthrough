from datetime import datetime as dt

t1 = 'Wed 12 May 2269 23:22:15 -0500'
t2 = 'Tue 05 Oct 2269 02:12:07 -0200'

t1_dt = dt.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
t2_dt = dt.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
delta = abs(t1_dt-t2_dt)
print(int(delta.total_seconds()))


