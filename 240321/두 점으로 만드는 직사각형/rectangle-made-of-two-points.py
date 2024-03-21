x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())
nx1,nx2 = min(x1,a1), max(x2,a2)
ny1,ny2 = min(y1,b1), max(y2,b2)

print((nx2-nx1) * (ny2-ny1))