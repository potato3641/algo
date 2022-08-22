w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())
y_val, x_val = 1, 1
distance = 1
p = (p+t)%(2*w)
q = (q+t)%(2*h)
p = p if p < w else 2*w-p
q = q if q < h else 2*h-q
print(p, q)
