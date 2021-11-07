import turtle as t
import random

tospik = t.Turtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
t.colormode(255)

# My method
tospik.penup()
going_up = -200
tospik.setposition(-200, -200)
tospik.speed('fastest')
tospik.hideturtle()

for _ in range(10):
    for _ in range(10):
        tospik.color(random.choice(color_list))
        tospik.begin_fill()
        tospik.circle(10)
        tospik.end_fill()
        tospik.forward(50)

    going_up += 50
    tospik.setposition(-200, going_up)


# Course method
# tospik.speed('fastest')
# tospik.setheading(225)
# tospik.penup()
# tospik.forward(300)
# tospik.setheading(0)
# number_of_dots = 100
# tospik.hideturtle()
#
# for dot_count in range(1, number_of_dots + 1):
#     tospik.color(random.choice(color_list))
#     tospik.dot(20, random.choice(color_list))
#     tospik.forward(50)
#
#     if dot_count % 10 == 0:
#         tospik.setheading(90)
#         tospik.forward(50)
#         tospik.setheading(180)
#         tospik.forward(500)
#         tospik.setheading(0)


screen = t.Screen()
screen.exitonclick()