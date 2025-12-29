import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_random_walk(length=1000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    steps = np.random.choice([-1, 1], size=length)
    walk = np.cumsum(steps)
    return walk

if __name__ == "__main__":
    walk = generate_random_walk(length=1000, seed=42)
    plt.plot(walk)
    plt.title("Random Walk")
    plt.xlabel("Steps")
    plt.ylabel("Position")
    plt.show()