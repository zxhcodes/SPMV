import random
import json
from config import M, N

# 生成x向量
# with open("x.txt", "w") as w:
#     x = [random.randint(0, 9) for _ in range(10000)]
#     w.write(json.dumps(x))

# 生成随机稀疏矩阵
# mnz = 0
# with open("sample.mtx", "w") as w:
#     for _ in range(M):
#         data = []
#         for _ in range(N):
#             x = random.randint(1, 20)
#             if x < 5:
#                 data.append(random.randint(1, 9))
#                 mnz += 1
#             else:
#                 data.append(0)
#
#         w.write(json.dumps(data)+"\n")
#
# print(mnz)


# coo格式
# rows, cols, data = [], [], []
#
# with open("sample.mtx") as mtx:
#     for ridx, line in enumerate(mtx):
#         row_data = json.loads(line.strip())
#         for cidx, val in enumerate(row_data):
#             if val != 0:
#                 rows.append(ridx)
#                 cols.append(cidx)
#                 data.append(val)
#
# with open("sample.coo", "w") as w:
#     w.write(json.dumps(rows) + "\n")
#     w.write(json.dumps(cols) + "\n")
#     w.write(json.dumps(data) + "\n")


# csr格式
# from scipy.sparse import coo_matrix
# import numpy as np
# with open("sample.coo") as coo:
#     rows = np.array(json.loads(coo.readline().strip()))
#     cols = np.array(json.loads(coo.readline().strip()))
#     data = np.array(json.loads(coo.readline().strip()))
#
# mtx = coo_matrix((data, (rows, cols)), shape=(M, N))
#
# csr_mtx = mtx.tocsr()
# row_offsets = csr_mtx.indptr
# col_indexes = csr_mtx.indices
#
# with open("sample.csr", "w") as w:
#     w.write(json.dumps(csr_mtx.indptr.tolist())+"\n")
#     w.write(json.dumps(csr_mtx.indices.tolist())+"\n")
#     w.write(json.dumps(csr_mtx.data.tolist()))
#
#
# from scipy.sparse import coo_matrix
# import numpy as np
# with open("sample.coo") as coo:
#     rows = np.array(json.loads(coo.readline().strip()))
#     cols = np.array(json.loads(coo.readline().strip()))
#     data = np.array(json.loads(coo.readline().strip()))


#dia格式
# from scipy.sparse import coo_matrix
# import numpy as np
# with open("sample.coo") as coo:
#     rows = np.array(json.loads(coo.readline().strip()))
#     cols = np.array(json.loads(coo.readline().strip()))
#     data = np.array(json.loads(coo.readline().strip()))
#
# mtx = coo_matrix((data, (rows, cols)), shape=(M, N))
#
# dia_mtx = mtx.todia()
#
# with open("sample.dia", "w") as w:
#     w.write(json.dumps(dia_mtx.offsets.tolist())+"\n")
#     w.write(json.dumps(dia_mtx.data.tolist()))







