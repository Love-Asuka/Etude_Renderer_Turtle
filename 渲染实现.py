import turtle

屏幕 = None
笔 = None
帧缓存 = []

def 初始化窗口():
    global 屏幕, 笔
    if 屏幕 is None:
        屏幕 = turtle.Screen()
        屏幕.setup(800, 800)
        屏幕.setworldcoordinates(-1.0, -1.0, 1.0, 1.0)
        屏幕.tracer(False)  
    if 笔 is None:
        笔 = turtle.Turtle()
        笔.hideturtle()
        笔.penup()

def 添加到帧缓存(三维顶点):
    global 帧缓存
    帧缓存.append(三维顶点)

def 渲染帧():
    global 帧缓存
    初始化窗口()

    笔.clear()

    def 映射坐标(x, y):
        return x * 0.9, y * 0.9

    for 三维顶点 in 帧缓存:
        for 引索 in range(len(三维顶点)):
            try:
                x, y = 映射坐标(float(三维顶点[引索][0]), float(三维顶点[引索][1]))
                if 引索 == 0:
                    笔.goto(x, y)
                    笔.pendown()
                else:
                    笔.goto(x, y)
            except (ValueError, IndexError):
                continue
        if len(三维顶点) > 2:
            x0, y0 = 映射坐标(float(三维顶点[0][0]), float(三维顶点[0][1]))
            笔.goto(x0, y0)

        笔.penup()

    屏幕.update() 
    帧缓存 = []  
