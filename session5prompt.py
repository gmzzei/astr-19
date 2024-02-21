# Write a Python program that writes out a table of the function sin(x) vs. x,
# where x is tabulated between 0 and 2 with a thousand entries.
# Follow the basic Python program structure, including a main program function.
import numpy as np
from tabulate import tabulate


def main():
    x = np.linspace(0, 2, 1000)
    y = np.sin(x)

    prompt_data = [(a, b) for a, b in zip(x, y)]
    headers = ["x", "sin(x)"]
    print(tabulate(prompt_data, tablefmt="grid", headers=headers, floatfmt=".3f"))


if __name__ == "__main__":
    main()