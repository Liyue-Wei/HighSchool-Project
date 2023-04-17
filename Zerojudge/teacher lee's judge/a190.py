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