import pandas as pd


def main():
    students = [
        ('Jack', 34, 'Sydney'),
        ('Riti', 30, 'Delhi'),
        ('Aadi', 16, 'New York'),
        ('Riti', 30, 'Delhi'),
        ('Riti', 30, 'Delhi'),
        ('Riti', 30, 'Mumbai'),
        ('Aadi', 40, 'London'),
        ('Sachin', 30, 'Delhi'),
    ]

    df_obj = pd.DataFrame(students, columns=['Name', 'Age', 'City'])

    print(df_obj.drop_duplicates())


main()
