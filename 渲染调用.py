import 模型数据
import 透视实现
import 渲染实现
import turtle

模型文件列表 = ['模型/场景.obj']

for 文件 in 模型文件列表:
    面顶点列表 = 模型数据.读取文件(文件)
    for 面顶点 in 面顶点列表:
        三维顶点 = 透视实现.透视(面顶点)
        渲染实现.渲染(三维顶点[:, :2])

turtle.mainloop()