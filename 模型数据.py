import numpy as np

def 读取文件(路径):
    顶点数组 = []
    面索引 = []
    with open(路径, 'r', encoding='utf-8') as 文件:
        for 行 in 文件:
            if 行.startswith('v '):
                顶点 = list(map(float, 行.strip().split()[1:]))
                顶点数组.append(顶点)
            elif 行.startswith('f '):
                面 = [int(引索.split('/')[0]) - 1 for 引索 in 行.strip().split()[1:]]
                面索引.append(面)
    顶点数据 = np.array(顶点数组, dtype=np.float64)
    # 返回每个面的顶点数组
    
    面顶点列表 = [np.array([顶点数据[引索] for 引索 in 面], dtype=np.float64) for 面 in 面索引]
    print(f"加载的顶点数量: {len(顶点数据)}")
    print(f"加载的面数量: {len(面索引)}")
    return 面顶点列表
