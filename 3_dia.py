import json
import time
from config import X, N, M

with open("sample.dia") as dia:
    offsets = json.loads(dia.readline().strip())
    data = json.loads(dia.readline().strip())

num_diags = len(offsets)

print("开始计算:\n")

#---------------------------Sequential Execution---------------------------
t0 = time.time()
y0 = [0] * N

for idx in range(num_diags):
    k = offsets[idx]    #第几条对角线
    a = max(0, -k)      #当前对角线从第几行开始
    b = max(0, k)       #当前对角线从第几列开始
    c = min(M-a, N-b)   #当前对角线包含几个元素
    for idy in range(c):
        y0[a+idy] += data[a+idx][idy]*X[b+idy]

x1 = time.time() - t0



#---------------------------Parallel Execution---------------------------
from multiprocessing import Pool

y1 = [0] * N

def f(dx):
    k = offsets[dx]
    a = max(0, -k)
    b = max(0, k)
    c = min(M - a, N - b)
    for idy in range(c):
        y1[a + idy] += data[a + dx][idy] * X[b + idy]

p = Pool(16)

t0 = time.time()
p.map(f, range(num_diags))

x2 = time.time() - t0

print("串行耗时:%f"%x1)
print("并行耗时:%f"%x2)
print("加速度比：%f"%(x1/x2))
print("效率：%f"%(x1/x2/16))

