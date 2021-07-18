import pandas as pd


def main():
    exam_scores = {
        ('Coding Principles for Management', 4.0),
        ('Big Data Analytics', 4.0),
        ('Digital Business Strategy', 3.66),
        ('Digital Business Strategy', 3.66),
        ('Methodologies for Software projects', 3.33),
        ('Coding Principles for Management', 4.0),
    }

    df_obj = pd.DataFrame(exam_scores, columns=['Course Name', 'Score'])

    print(df_obj.drop_duplicates())


main()
