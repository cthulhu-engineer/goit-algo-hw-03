import turtle


def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)


def main():
    window = turtle.Screen()
    window.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)

    order = int(input("Enter the order of the Koch snowflake: "))

    for _ in range(3):
        koch_snowflake(snowflake_turtle, order, 300)
        snowflake_turtle.right(120)

    window.mainloop()


if __name__ == "__main__":
    main()
