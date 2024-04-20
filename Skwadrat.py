# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import turtle
import matplotlib.pyplot as plt
import matplotlib.patches as patches

print("Розрахуйте S площу квадрата")
print("Введіть розмір сторони у см ?")
a = float(input("a = "))
print("Площа S = a*a або а в квадраті.")
print("Площа = %.2f" % (a * a))
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, черепашка та matplotlib накреслили Вам ваш квадрат . Знайдіть їх у себе на моніторі.")
#turtle 
turtle.forward(a*37)
turtle.left(90)
turtle.forward(a*37)
turtle.left(90)
turtle.forward(a*37)
turtle.left(90)
turtle.forward(a*37)
turtle.hideturtle()
#Smatplotlib
fig, ax = plt.subplots()
square = patches.Rectangle((0, 0), a, a, edgecolor='grey', facecolor='none')
ax.add_patch(square)
plt.xlim(-1, a+2)
plt.ylim(-1, a+2)
plt.gca().set_aspect('equal', adjustable='box') 
plt.title('Ваш квадрат накреслений на координатній сітці')
plt.show()

