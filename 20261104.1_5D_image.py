import turtle
import math

# ---------------------- 5个维度数据，你可以自行修改 ----------------------
labels = ["V1", "V2", "V3", "V4", "V5"]
values = [0.7, 0.5, 0.9, 0.4, 0.6]
max_val = 1.0
num_dim = 5

# 画布设置
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.title("5D Radar Chart (Pure Python Turtle)")
screen.setup(600,600)

angle_step = 2 * math.pi / num_dim
radius = 200

# 画坐标轴+标签
for i in range(num_dim):
    ang = i * angle_step
    x = radius * math.cos(ang)
    y = radius * math.sin(ang)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.goto(x, y)
    t.penup()
    t.goto(x*1.15, y*1.15)
    t.write(labels[i], align="center", font=("Arial",12))

# 画多边形轮廓
t.penup()
for i in range(num_dim):
    ang = i * angle_step
    r = values[i] / max_val * radius
    x = r * math.cos(ang)
    y = r * math.sin(ang)
    t.goto(x,y)
    t.pendown()
t.goto(values[0]/max_val*radius * math.cos(0), values[0]/max_val*radius * math.sin(0))

# 填充颜色
t.fillcolor("lightblue")
t.begin_fill()
for i in range(num_dim):
    ang = i * angle_step
    r = values[i] / max_val * radius
    x = r * math.cos(ang)
    y = r * math.sin(ang)
    t.goto(x,y)
t.end_fill()

t.hideturtle()
turtle.done()