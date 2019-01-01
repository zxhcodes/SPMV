import json
import time

from config import X

tx = time.time()
with open("sample.csr") as csr:
    ptrs = json.loads(csr.readline().strip())
    indices = json.loads(csr.readline().strip())
    data = json.loads(csr.readline().strip())

print("加载耗时：", time.time()-tx)

nums = len(ptrs)

print("开始计算:\n")

#---------------------------Sequential Execution---------------------------
t0 = time.time()
y0 = [0] * nums
for idx in range(nums-1):
    beg = ptrs[idx]
    end = ptrs[idx+1]
    for idy in range(beg, end):
        y0[idx] += X[indices[idy]] * data[idy]

x1 = time.time() - t0


#---------------------------Parallel Execution---------------------------
from multiprocessing import Pool

y1 = [0] * nums
def f(idx):
    beg = ptrs[idx]
    end = ptrs[idx+1]
    for idy in range(beg, end):
        y0[idx] += X[indices[idy]] * data[idy]

t0 = time.time()
p = Pool(16)
p.map(f, range(nums-1))
x2 = time.time() - t0

print("串行耗时:%f"%x1)
print("并行耗时:%f"%x2)
print("加速度比：%f"%(x1/x2))
print("效率：%f"%(x1/x2/16))