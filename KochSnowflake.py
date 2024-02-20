import sys
import turtle

DEFAULT_N    = 3
DEFAULT_SIZE = 300

def koch_snowflake(n=DEFAULT_N, l=DEFAULT_SIZE, funny:bool=False):
    def koch_curve(t, l, n):
        if n:
            for angle in [0, 60, -120, 60]:
                t.right(angle)
                koch_curve(t, l/3, n-1)
            return
        t.forward(l)

    t = turtle.Turtle()
    t.clear()
    t.speed(10)
    t.shape("classic")
    t.color('#285078')
    t.penup()
    t.goto(0, -l/2)
    t.pendown()
    t.left(60)
    while n >= 0:
        for _ in range(3):
            koch_curve(t, l, n)
            t.left(120)
        if not funny: break
        n -= 1


def main():
    n = DEFAULT_N if len(sys.argv) < 2 else int(sys.argv[1])
    l = DEFAULT_SIZE if len(sys.argv) < 3 else int(sys.argv[2])

    window = turtle.Screen()
    window.bgcolor("lightblue")

    koch_snowflake(n, l, funny=True)

    window.mainloop()


if __name__ == "__main__":
    main()
