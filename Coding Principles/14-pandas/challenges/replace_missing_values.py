import pandas as pd
import numpy as np


def main():
    numbers = pd.Series([1, 12, 33, np.NaN, 45, 64, None, 34, 32, 11, 44, None, 324, np.NaN])

    print(numbers.fillna(int(numbers.mean())))
    print()
    print(numbers.dropna())


if __name__ == '__main__':
    main()
