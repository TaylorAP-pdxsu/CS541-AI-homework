import random
import numpy as np

def main():
    

    n = [0.1, 0.01, 0.001]
    vectors = [[]]

    for i in range(3):
        vectors.append([])
        for trial in range(10):
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            for _ in range(500):
                x = f_dx(n[i], x)
                y = f_dy(n[i], y)
            vectors[i].append((n[i], round(x, 4), round(y, 4)))

    for i in range(3):
        for j in range(10):
            print(vectors[i][j])
            

def f_dx(n, x):
    return x - n * (10 * x + 40)

def f_dy(n, y):
    return y - n * (2 * y - 12)

if __name__ == "__main__":
    main()