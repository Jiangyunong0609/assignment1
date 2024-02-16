import pandas as pd
import sys
def clean_data(input1, input2, output):

    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged_df.dropna(inplace=True)
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    merged_df.drop(columns='id', inplace=True)
    merged_df.to_csv(output, index=False)
    print(merged_df.shape)


if __name__ == "__main__":

    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]
    clean_data(input1, input2, output)