import pandas as pd
import numpy as np


def main():
    df = pd.DataFrame({'A': [2, 1, 2, 3, 3, 5, 4],
                       'B': [1, 2, 3, 5, 4, 2, 5],
                       'C': [5, 3, 4, 1, 1, 2, 3]})

    # sort the data in column A
    df = df.sort_values(by=['A'], ascending=[True])
    df = df.reset_index(drop=True)
    print(df)

    index = df.index.tolist()
    np.random.shuffle(index)
    df = df.loc[df.index[index]]
    df = df.reset_index(drop=True)
    print()
    print(df)


if __name__ == '__main__':
    main()
