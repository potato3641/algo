D, H, W = map(int,input().split())
term1 = ((D*D*H*H)/(H*H+W*W))**0.5
term2 = term1*W/H
print(int(term1), int(term2))
