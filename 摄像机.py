import math
import time
from 运算模块 import 矩阵乘法, 矩阵转置, 创建单位矩阵

class 摄像机:
    def __init__(self, 位置=[0, 0, 5], 目标=[0, 0, 0], 上方向=[0, 1, 0]):
        self.位置 = 位置
        self.目标 = 目标
        self.上方向 = 上方向
        self.基础移动速度 = 0.1
        self.移动速度 = 0.0  # 当前移动速度（用于平滑加速）
        self.最大移动速度 = 0.1
        self.加速度 = 0.02
        self.减速度 = 0.03
        self.旋转速度 = 2.0  # 度
        self.上次更新时间 = time.time()
        

        self.正在向前移动 = False
        self.正在向后移动 = False
        self.正在向左移动 = False
        self.正在向右移动 = False
        self.正在向上移动 = False
        self.正在向下移动 = False
        

        self.正在左旋转 = False
        self.正在右旋转 = False
        self.正在向上看 = False
        self.正在向下看 = False
        

        self.视图矩阵 = self.计算视图矩阵()
    
    def 计算视图矩阵(self):
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        y轴 = self.叉乘(z轴, x轴)
        
        视图矩阵 = [
            [x轴[0], x轴[1], x轴[2], -self.点乘(x轴, self.位置)],
            [y轴[0], y轴[1], y轴[2], -self.点乘(y轴, self.位置)],
            [z轴[0], z轴[1], z轴[2], -self.点乘(z轴, self.位置)],
            [0, 0, 0, 1]
        ]
        
        return 视图矩阵
    
    def 归一化(self, 向量):
        长度 = math.sqrt(sum(分量 * 分量 for 分量 in 向量))
        if 长度 == 0:
            return 向量
        return [分量 / 长度 for 分量 in 向量]
    
    def 叉乘(self, a, b):
        return [
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        ]
    
    def 点乘(self, a, b):
        return sum(a[i] * b[i] for i in range(len(a)))
    
    def 向前移动(self):
        方向 = self.归一化([self.目标[0] - self.位置[0], 
                         self.目标[1] - self.位置[1], 
                         self.目标[2] - self.位置[2]])
        self.位置 = [self.位置[i] + 方向[i] * self.移动速度 for i in range(3)]
        self.目标 = [self.目标[i] + 方向[i] * self.移动速度 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 向后移动(self):
        方向 = self.归一化([self.目标[0] - self.位置[0], 
                         self.目标[1] - self.位置[1], 
                         self.目标[2] - self.位置[2]])
        self.位置 = [self.位置[i] - 方向[i] * self.移动速度 for i in range(3)]
        self.目标 = [self.目标[i] - 方向[i] * self.移动速度 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 向左移动(self):
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        self.位置 = [self.位置[i] - x轴[i] * self.移动速度 for i in range(3)]
        self.目标 = [self.目标[i] - x轴[i] * self.移动速度 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 向右移动(self):
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        self.位置 = [self.位置[i] + x轴[i] * self.移动速度 for i in range(3)]
        self.目标 = [self.目标[i] + x轴[i] * self.移动速度 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 向上移动(self):
        self.位置[1] += self.移动速度
        self.目标[1] += self.移动速度
        self.视图矩阵 = self.计算视图矩阵()
    
    def 向下移动(self):
        self.位置[1] -= self.移动速度
        self.目标[1] -= self.移动速度
        self.视图矩阵 = self.计算视图矩阵()
    
    def 左旋转(self):
        方向 = [self.目标[0] - self.位置[0], 
               self.目标[1] - self.位置[1], 
               self.目标[2] - self.位置[2]]
        
        角度 = math.radians(self.旋转速度)
        cosθ = math.cos(角度)
        sinθ = math.sin(角度)
        
        # 旋转方向向量
        新方向 = [
            方向[0] * cosθ + 方向[2] * sinθ,
            方向[1],
            -方向[0] * sinθ + 方向[2] * cosθ
        ]
        
        self.目标 = [self.位置[i] + 新方向[i] for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 右旋转(self):
        # 围绕上方向轴旋转
        方向 = [self.目标[0] - self.位置[0], 
               self.目标[1] - self.位置[1], 
               self.目标[2] - self.位置[2]]
        
        # 旋转矩阵 (绕Y轴)
        角度 = math.radians(-self.旋转速度)
        cosθ = math.cos(角度)
        sinθ = math.sin(角度)
        
        # 旋转方向向量
        新方向 = [
            方向[0] * cosθ + 方向[2] * sinθ,
            方向[1],
            -方向[0] * sinθ + 方向[2] * cosθ
        ]
        
        self.目标 = [self.位置[i] + 新方向[i] for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 开始左旋转(self):
        self.正在左旋转 = True
    
    def 停止左旋转(self):
        self.正在左旋转 = False
    
    def 开始右旋转(self):
        self.正在右旋转 = True
    
    def 停止右旋转(self):
        self.正在右旋转 = False
    
    def 开始向上看(self):
        self.正在向上看 = True
    
    def 停止向上看(self):
        self.正在向上看 = False
    
    def 开始向下看(self):
        self.正在向下看 = True
    
    def 停止向下看(self):
        self.正在向下看 = False
    
    def 向上看(self):
        """向上旋转摄像机视角"""
        # 计算当前方向向量
        方向 = [self.目标[0] - self.位置[0], 
               self.目标[1] - self.位置[1], 
               self.目标[2] - self.位置[2]]
        
        # 计算右向量（用于俯仰旋转的轴）
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        
        # 绕x轴旋转（俯仰）
        角度 = math.radians(self.旋转速度)
        cosθ = math.cos(角度)
        sinθ = math.sin(角度)
        
        # 旋转方向向量
        新方向 = [
            方向[0],
            方向[1] * cosθ - 方向[2] * sinθ,
            方向[1] * sinθ + 方向[2] * cosθ
        ]
        
        self.目标 = [self.位置[i] + 新方向[i] for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 向下看(self):
        """向下旋转摄像机视角"""
        # 计算当前方向向量
        方向 = [self.目标[0] - self.位置[0], 
               self.目标[1] - self.位置[1], 
               self.目标[2] - self.位置[2]]
        
        # 计算右向量（用于俯仰旋转的轴）
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        
        # 绕x轴旋转（俯仰）
        角度 = math.radians(-self.旋转速度)
        cosθ = math.cos(角度)
        sinθ = math.sin(角度)
        
        # 旋转方向向量
        新方向 = [
            方向[0],
            方向[1] * cosθ - 方向[2] * sinθ,
            方向[1] * sinθ + 方向[2] * cosθ
        ]
        
        self.目标 = [self.位置[i] + 新方向[i] for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def 获取视图矩阵(self):
        return self.视图矩阵
    
    def 设置移动速度(self, 速度):
        self.移动速度 = 速度
    
    def 设置旋转速度(self, 速度):
        self.旋转速度 = 速度
    
    def 获取位置(self):
        return self.位置
    
    def 获取目标(self):
        return self.目标
    
    def 设置位置(self, 新位置):
        """设置摄像机位置"""
        self.位置 = 新位置
        self.视图矩阵 = self.计算视图矩阵()
    
    def 设置目标(self, 新目标):
        """设置摄像机目标"""
        self.目标 = 新目标
        self.视图矩阵 = self.计算视图矩阵()
    
    def 开始向前移动(self):
        self.正在向前移动 = True
    
    def 停止向前移动(self):
        self.正在向前移动 = False
    
    def 开始向后移动(self):
        self.正在向后移动 = True
    
    def 停止向后移动(self):
        self.正在向后移动 = False
    
    def 开始向左移动(self):
        self.正在向左移动 = True
    
    def 停止向左移动(self):
        self.正在向左移动 = False
    
    def 开始向右移动(self):
        self.正在向右移动 = True
    
    def 停止向右移动(self):
        self.正在向右移动 = False
    
    def 开始向上移动(self):
        self.正在向上移动 = True
    
    def 停止向上移动(self):
        self.正在向上移动 = False
    
    def 开始向下移动(self):
        self.正在向下移动 = True
    
    def 停止向下移动(self):
        self.正在向下移动 = False
    
    def 更新移动(self):
        """基于时间的平滑移动和旋转更新"""
        当前时间 = time.time()
        时间差 = 当前时间 - self.上次更新时间
        self.上次更新时间 = 当前时间
        
        # 计算目标移动速度
        目标速度 = 0.0
        if (self.正在向前移动 or self.正在向后移动 or 
            self.正在向左移动 or self.正在向右移动 or
            self.正在向上移动 or self.正在向下移动):
            目标速度 = self.最大移动速度
        
        # 平滑加速/减速
        if self.移动速度 < 目标速度:
            self.移动速度 = min(self.移动速度 + self.加速度 * 时间差 * 60, 目标速度)
        elif self.移动速度 > 目标速度:
            self.移动速度 = max(self.移动速度 - self.减速度 * 时间差 * 60, 目标速度)
        
        # 应用移动
        if self.移动速度 > 0:
            if self.正在向前移动:
                self._平滑向前移动(时间差)
            if self.正在向后移动:
                self._平滑向后移动(时间差)
            if self.正在向左移动:
                self._平滑向左移动(时间差)
            if self.正在向右移动:
                self._平滑向右移动(时间差)
            if self.正在向上移动:
                self._平滑向上移动(时间差)
            if self.正在向下移动:
                self._平滑向下移动(时间差)
        
        # 应用旋转（不需要速度控制，直接应用）
        if self.正在左旋转:
            self.左旋转()
        if self.正在右旋转:
            self.右旋转()
        if self.正在向上看:
            self.向上看()
        if self.正在向下看:
            self.向下看()
    
    def _平滑向前移动(self, 时间差):
        方向 = self.归一化([self.目标[0] - self.位置[0], 
                         self.目标[1] - self.位置[1], 
                         self.目标[2] - self.位置[2]])
        移动量 = self.移动速度 * 时间差 * 60
        self.位置 = [self.位置[i] + 方向[i] * 移动量 for i in range(3)]
        self.目标 = [self.目标[i] + 方向[i] * 移动量 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def _平滑向后移动(self, 时间差):
        方向 = self.归一化([self.目标[0] - self.位置[0], 
                         self.目标[1] - self.位置[1], 
                         self.目标[2] - self.位置[2]])
        移动量 = self.移动速度 * 时间差 * 60
        self.位置 = [self.位置[i] - 方向[i] * 移动量 for i in range(3)]
        self.目标 = [self.目标[i] - 方向[i] * 移动量 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def _平滑向左移动(self, 时间差):
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        移动量 = self.移动速度 * 时间差 * 60
        self.位置 = [self.位置[i] - x轴[i] * 移动量 for i in range(3)]
        self.目标 = [self.目标[i] - x轴[i] * 移动量 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def _平滑向右移动(self, 时间差):
        z轴 = self.归一化([self.位置[0] - self.目标[0], 
                         self.位置[1] - self.目标[1], 
                         self.位置[2] - self.目标[2]])
        x轴 = self.归一化(self.叉乘(self.上方向, z轴))
        移动量 = self.移动速度 * 时间差 * 60
        self.位置 = [self.位置[i] + x轴[i] * 移动量 for i in range(3)]
        self.目标 = [self.目标[i] + x轴[i] * 移动量 for i in range(3)]
        self.视图矩阵 = self.计算视图矩阵()
    
    def _平滑向上移动(self, 时间差):
        移动量 = self.移动速度 * 时间差 * 60
        self.位置[1] += 移动量
        self.目标[1] += 移动量
        self.视图矩阵 = self.计算视图矩阵()
    
    def _平滑向下移动(self, 时间差):
        移动量 = self.移动速度 * 时间差 * 60
        self.位置[1] -= 移动量
        self.目标[1] -= 移动量
        self.视图矩阵 = self.计算视图矩阵()
    
    def 设置移动速度(self, 速度):
        self.基础移动速度 = 速度
        self.最大移动速度 = 速度 * 3  # 最大速度是基础速度的3倍