fh, fm, fs = map(int,input().split(":"))
lh, lm, ls = map(int,input().split(":"))
first = fh*3600+fm*60+fs
last = lh*3600+lm*60+ls
if last > first:
    target = last-first
    print("{0:02d}:{1:02d}:{2:02d}".format(target//3600, (target%3600)//60, target%60))
else:
    target = 86400-first+last
    print("{0:02d}:{1:02d}:{2:02d}".format(target//3600, (target%3600)//60, target%60))
