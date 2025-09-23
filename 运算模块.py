def 创建矩阵(高,宽,值=0):
    return [[值 for _ in range(宽)] for _ in range(高)]
def 创建单位矩阵(高,宽):
    矩阵 = 创建矩阵(高,宽)
    for 索引 in range(min(高,宽)):
        矩阵[索引][索引] = 1
    return 矩阵


def 创建对角矩阵(高,宽,值=0):
    矩阵 = 创建矩阵(高,宽)
    for 索引 in range(min(高,宽)):
        矩阵[索引][索引] = 值
    return 矩阵


def 矩阵转置(矩阵):
    矩阵1高 = len(矩阵)
    矩阵1宽 = len(矩阵[0])
    转置矩阵 = [[0 for _ in range(矩阵1高)] for _ in range(矩阵1宽)]
    for 高 in range(矩阵1高):
        for 宽 in range(矩阵1宽):
            转置矩阵[宽][高] = 矩阵[高][宽]
    return 转置矩阵

def 矩阵加法(矩阵1, 矩阵2):
    矩阵1高 = len(矩阵1)
    矩阵1宽 = len(矩阵1[0])
    矩阵2高 = len(矩阵2)
    矩阵2宽 = len(矩阵2[0])
    if 矩阵1高 != 矩阵2高 or 矩阵1宽 != 矩阵2宽:
        print ("错误")
        return None
    结果矩阵 = [[0 for _ in range(矩阵1宽)] for _ in range(矩阵1高)]
    for 高 in range(矩阵1高):
        for 宽 in range(矩阵1宽):
            结果矩阵[高][宽] = 矩阵1[高][宽] + 矩阵2[高][宽]
    return 结果矩阵


def 矩阵乘法(矩阵1, 矩阵2):
    矩阵1高 = len(矩阵1)
    矩阵1宽 = len(矩阵1[0])
    矩阵2高 = len(矩阵2)
    矩阵2宽 = len(矩阵2[0])
    if 矩阵1宽 != 矩阵2高:
        print ("错误")
        return None
    结果矩阵 = [[0 for _ in range(矩阵2宽)] for _ in range(矩阵1高)]
    for 高 in range(矩阵1高):
        for 宽 in range(矩阵2宽):
            for 索引 in range(矩阵1宽):
                结果矩阵[高][宽] += 矩阵1[高][索引] * 矩阵2[索引][宽]
    return 结果矩阵



def 矩阵乘以标量(矩阵, 标量):
    矩阵高 = len(矩阵)
    矩阵宽 = len(矩阵[0])
    结果矩阵 = [[0 for _ in range(矩阵宽)] for _ in range(矩阵高)]
    for 高 in range(矩阵高):
        for 宽 in range(矩阵宽):
            结果矩阵[高][宽] = 矩阵[高][宽] * 标量
    return 结果矩阵

