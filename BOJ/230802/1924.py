dates = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
dayes = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
M, D = map(int,input().split())
daycount = D
if M-1:
    daycount += sum(dayes[:M])
daycount %= 7
print(dates[daycount%7])
