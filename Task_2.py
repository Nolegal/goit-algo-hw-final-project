import turtle

myTurtle=turtle.Turtle()
myTurtle.screen.bgcolor("white")
myTurtle.left(90)
myTurtle.speed('fastest')
myTurtle.color('red')
myTurtle.pensize(1)
myTurtle.screen.title("Pythagorean tree")


def drawFractalTree(blen):
    if blen<10:
        return
    else:
        myTurtle.forward(blen)
        myTurtle.left(45)
        drawFractalTree(3*blen/4)
        myTurtle.right(90)
        drawFractalTree(3*blen/4)
        myTurtle.left(45)
        myTurtle.backward(blen)
print('Оберіть рівень рекурсії для зручного вигляду дерева від 4 до 10,рівень7-8 відповідає малюнку в завданні.')
blen1=int(input())
drawFractalTree(blen1*10)
turtle.done()
 




































































































# # Draws a Pythagoras tree, which is another fractal tree,
# # using a recursive algorithm.
# # http://mathworld.wolfram.com/PythagorasTree.html

# import turtle
# import math

# screen = turtle.Screen()
# screen.bgcolor("skyblue")

# alan = turtle.Turtle()
# alan.shape("turtle")
# alan.color("green")
# alan.fillcolor("tan")
# alan.speed(9991010)

# # Draw a single square of the given size, and fill it in
# def drawSquare(t, size):
#   t.begin_fill()
#   for i in range(4):
#     t.forward(size)
#     t.left(90)
#   t.end_fill()
 
# # Draw a node at the given level, recursively drawing all
# # the smaller nodes
# def drawNode(t, size, level):
#   if (level < 1):
#     return
#   else:
#     drawSquare(t, size)
    
#     # Draw the left branch
#     leftSize = size * math.sqrt(3) / 2
#     t.forward(size)
#     t.left(90)
#     t.forward(size)
#     t.right(150)
#     t.forward(leftSize)
#     t.left(90)
#     drawNode(t, leftSize, level - 1)
    
#     # Draw the right branch
#     rightSize = size / 2
#     t.right(180)
#     t.forward(rightSize)
#     t.left(90)
#     drawNode(t, rightSize, level - 1)
#     t.left(60)
#     t.back(size)
  
# # Position the turtle, and start drawing!
# alan.penup()
# alan.goto(90, -150)
# alan.left(90)
# alan.pendown()

 
# # Note: 14 levels will take a while to draw!  You can try
# # a smaller number, but then the tree won't be as detailed.

# #  print("1 side:")
# #     order1=int(input())
# #     koch_snowflake(t, order1, size/2)

# print('Level of recursion:')
# level1=int(input())
# print('Tree size')
# size1=int(input())
# drawNode(alan,size1, level1)

# alan.hideturtle()

# screen.mainloop()
