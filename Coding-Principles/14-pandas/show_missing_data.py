import pandas as pd
import numpy as np


def main():
    s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])

    print(s.isnull())
    print()
    print(s[s.isnull()])


if __name__ == '__main__':
    main()
