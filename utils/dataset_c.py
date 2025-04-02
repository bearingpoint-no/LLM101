import pandas as pd


class FeedbackData:
    """
    Class containing fake datasets by us :)
    """

    # Load a DataFrame with a specific version of a CSV
    file_path = "./files/shuffled_df_LLM101_filtered.csv"
    df_o = pd.read_csv(file_path)

    enr_path = "./files/output_df.csv"
    df = pd.read_csv(enr_path)


# print(FeedbackData.df["Feedback"][0])
