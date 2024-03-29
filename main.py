from matplotlib import markers
import matplotlib
import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    # Algoritmo DDA

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx > dy:
        p = abs(dx)
    else:
        p = abs(dy)

    incremento_x = dx / p
    incremento_y = dy / p

    a = 0

    cord_x = []
    cord_y = []

    while a < p:
        a += 1
        x1 += incremento_x
        y1 += incremento_y

        print(f"x, y: ({int(x1)}, {int(y1)})")

        cord_x.append(x1)
        cord_y.append(y1)

    # Inicializacao do grafico
    plt.plot(cord_x, cord_y, color='red', marker='o')
    plt.get_current_fig_manager().canvas.manager.set_window_title('Algoritmo DDA')
    plt.xlabel("Eixo-x")
    plt.ylabel("Eixo-y")
    plt.title("Algoritmo DDA (6,9) - (11, 12)")
    plt.show()


def bresenham(x1, y1, x2, y2):
    # Algoritmo Bresenham

    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    incremento = dy/float(dx)

    if incremento > 1:
        dx, dy = dy, dx
        х, у = у, х
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx

    cord_x = [x]
    cord_y = [y]

    print(f'x, y: ({x}, {y})')

    for c in range(dx):
        if p > 0:
            if y < y2:
                y += 1
            else:
                y -= 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy
        if x < x2:
            x += 1
        else:
            x -= 1

        print(f'x, y: ({x}, {y})')

        cord_x.append(x)
        cord_y.append(y)

    # Inicializacao do grafico
    plt.plot(cord_x, cord_y, marker='o')
    plt.get_current_fig_manager().canvas.manager.set_window_title('Algoritmo Bresenham')
    plt.xlabel("Eixo-x")
    plt.ylabel("Eixo-y")
    plt.title("Algoritmo Bresenham (2, 2) - (7, 6)")
    plt.show()


def main():
    # Main
    print("1. para DDA")
    print("2. para Bresenham")

    op = int(input("Selecione o algoritmo: "))

    if op == 1:
        dda(5, 9, 11, 12)
    else:
        bresenham(2, 2, 7, 6)


if __name__ == '__main__':
    main()
