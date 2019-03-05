import re

# ss = '''I love #hackerrank
# I just scored 27 points in the Picking Cards challenge on #HackerRank
# I just signed up for summer cup @hackerrank
# interesting talk by hari, co-founder of hackerrank'''
#
# s_list = ss.split('\n')
# for s in s_list:
#     s = s.lower()
#     m = re.findall('hackerrank', s)
#     print(m)

num = 35
ss = '''1050:0:0:0:5:600:300c:326b
1050:0:0:0:5:600:300c:326a
1050:0:0:0:5:600:300c:326c
1051:0:0:0:5:600:300c:326b
22.231.113.64
22.231.113.164
255.231.111.64
253.231.111.64
1050:10:0:0:5:600:300c:326b
1050:10:0:0:5:600:300c:326a
1050:10:0:0:5:600:300c:326c
1051:10:0:0:5:600:300c:326b
22.21.113.61
22.21.113.162
255.21.111.63
253.21.111.69
1050:10:0:0:15:600:300c:326b
1050:10:0:10:5:600:300c:326a
1050:10:10:0:5:600:300c:326c
1051:110:0:0:5:600:300c:326b
22.211.113.64
22.212.113.164
255.213.111.64
253.214.111.64
1050:10:0:0:15:600:300c:326k
1050:10:0:0:15:600:300c:326g
1050:10:0:0:15:600:300c:326h
1050:10:0:0:15:600:300c:326i
22.211.113.364
22.212.113.3164
255.213.111.464
253.214.111.564
not an ip address
not an ipv4 Address
Not an IPv5 Address'''

s_list = ss.split('\n')
for t in s_list:
    ipv4_re = r'^\d+\.\d+\.\d+\.\d+$'
    ipv6_re = r'^([a-z0-9]+:){7}[a-z0-9]+$'
    if re.match(ipv4_re, t):
        t_list = t.split('.')
        if len([i for i in t_list if 0 <= int(i) <= 255]) == 4:
            print('IPv4')
        else:
            print('Neither')
    elif re.match(ipv6_re, t):
        t_list = t.split(':')
        try:
            print()
            ipv6_16 = [int(i, 16) for i in t_list]
        except:
            print('Neither')
    else:
        print('Neither')
