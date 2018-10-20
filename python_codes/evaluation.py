import numpy as np

def fitness_fx(x):
    x_np = np.array(x)
    sen_result = np.sin(10 * np.pi * x_np)
    fx = x_np * sen_result + 1

    return fx

if __name__ == '__main__':
    x = [1, 20, 50, 400]
    fx = fitness_fx(x)

    print(fx[1])