import turtle


def carre(n):
    # n représente 0 ou 1.
    if n == 0:
        tortue.fillcolor("red")
    elif n == 1:
        tortue.fillcolor("blue")
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(10)
        tortue.left(90)
    tortue.end_fill()


def dessine(nombre_ligne):
    ligne = []
    for i in range(nombre_ligne):
        prochaine_ligne = ligne + [1]
        for x in range(len(ligne) - 1):
            if (ligne[x] + ligne[x + 1]) % 2 == 0:
                prochaine_ligne[x + 1] = 0
            else:
                prochaine_ligne[x + 1] = 1
        ligne = prochaine_ligne
        cord_ligne_x = tortue.xcor()
        for y in ligne:
            carre(y)
            tortue.setx(tortue.xcor() + 10)
        tortue.penup()
        tortue.setx(cord_ligne_x - 5)
        tortue.sety(tortue.ycor() - 10)
        tortue.pendown()


if __name__ == '__main__':
    fen = turtle.Screen()
    tortue = turtle.Turtle()
    tortue.penup()
    tortue.sety(270)
    tortue.pendown()
    tortue.speed(1000)
    dessine(20)
    fen.exitonclick()