h_r = []
m_r = []
i = int(input())
while(i>0):
    h, m = map(int, input().split(':'))
    if(h==12 and 60-m==60):
        h_r.append(12)
        m_r.append(0)
    elif(60-m==60 and h!=12):
        h_r.append(12-h)
        m_r.append(0)
    elif(h==6 and 60-m==60):
        h_r.append(6)
        m_r.append(0)
    elif(h==6 and 60-m==30):
        h_r.append(6)
        m_r.append(30)
    elif(h==12 and 60-m==30):
        h_r.append(11)
        m_r.append(30)
    else:
        h_r.append(11-h)
        m_r.append(60-m)
    i-=1

for l in range(0, len(h_r)):
    print("%02d:%02d" % (h_r[l], m_r[l]))
'''
h_r = []
m_r = []
i = int(input())
while(i>0):
    h, m = map(int, input().split(':'))
    if(m==0 and (h==12 or h==6)):
        h_r.append(h)
        m_r.append(m)
    elif(m==0):
        h_r.append(12-h)
        m_r.append(m)
    else:
        h_r.append(11-h)
        m_r.append(60-m)
    i-=1

for l in range(0, len(h_r)):
    print("%02d:%02d" % (h_r[l], m_r[l]))
'''
# 12
# 12:00
# 1:00
# 1:30
# 2:00
# 2:25
# 3:00
# 3:15
# 3:30
# 6:00
# 9:30
# 11:50
# 7:45
# 
# 12:00
# 11:00
# 10:30
# 10:00
# 09:35
# 09:00
# 08:45
# 08:30
# 06:00
# 02:30
# 00:10
# 04:15