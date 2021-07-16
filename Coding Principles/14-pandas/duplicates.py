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
    duplicate_rows_df = df_obj[df_obj.duplicated()]

    print('Duplicate Rows except the first occurrence based on all columns are:')
    print(duplicate_rows_df)


main()
