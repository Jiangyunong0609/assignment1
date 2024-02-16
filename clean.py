
import pandas as pd
import sys

def clean_data(input1, input2, output):

    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')


    merged_df.drop('id', axis=1, inplace=True)


    merged_df.dropna(inplace=True)


    mask = merged_df['job'].str.contains('insurance', case=False, na=False)
    cleaned_df = merged_df[~mask]

    # Step 4: Save the cleaned data in the project folder.
    cleaned_df.to_csv(output, index=False)

    print(merged_df.shape)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean.py <input1> <input2> <output>")
        sys.exit(1)

    input1_path = sys.argv[1]
    input2_path = sys.argv[2]
    output_path = sys.argv[3]

    clean_data(input1_path, input2_path, output_path)
