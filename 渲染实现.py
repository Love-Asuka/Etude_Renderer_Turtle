import turtle

屏幕 = None
笔 = None

def 初始化窗口():
    global 屏幕, 笔
    if 屏幕 is None:
        屏幕 = turtle.Screen()
        屏幕.setup(800, 800)
        屏幕.setworldcoordinates(-1.0, -1.0, 1.0, 1.0)
        屏幕.tracer(False)  # 禁用动画
    if 笔 is None:
        笔 = turtle.Turtle()
        笔.hideturtle()
        笔.penup()

def 渲染(三维顶点):
    初始化窗口()

    def 映射坐标(x, y):
        return x * 0.9, y * 0.9  

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

    # 闭合多边形
    if len(三维顶点) > 2:
        x0, y0 = 映射坐标(float(三维顶点[0][0]), float(三维顶点[0][1]))
        笔.goto(x0, y0)

    笔.penup()
    屏幕.update()  # 更新屏幕内容
