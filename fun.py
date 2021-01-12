from time import time

curr_time = int(time()) % 1000
a = 4353
c = 55
ans = ((curr_time * a ) + c ) % 100

print(ans)