import json
import time
from config import M, MNZ, X

tx = time.time()
with open("sample.coo") as coo:
    rows = json.loads(coo.readline().strip())
    cols = json.loads(coo.readline().strip())
    data = json.loads(coo.readline().strip())

print("加载耗时：", time.time()-tx)

print("开始计算:\n")

#---------------------------Sequential Execution---------------------------
t0 = time.time()
y0 = [0]*M
for idx in range(MNZ):
    y0[rows[idx]] = data[idx]*X[cols[idx]]

x1 = time.time() - t0



#---------------------------Parallel Execution---------------------------
from multiprocessing import Pool

y1 = [0] * M

def f(idx):
    y1[rows[idx]] = data[idx] * X[cols[idx]]

t0 = time.time()

p = Pool(16)
p.map(f, range(MNZ))

x2 = time.time() - t0

print("串行耗时:%f"%x1)
print("并行耗时:%f"%x2)
print("加速度比：%f"%(x1/x2))
print("效率：%f"%(x1/x2/16))