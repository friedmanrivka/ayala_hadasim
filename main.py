
from processing.cleaner import clean_dataframe
from processing.splitter import split_by_day
from processing.aggregator import hourly_averages
from utils.file_handler import load_file
import pandas as pd

def main():
   # df = load_file("data/time_series.parquet")  # או time_series.csv
    #df = load_file(r"C:\Users\USER\PycharmProjects\pythonProject3\data\time_series.xlsx")
    df = load_file("data/time_series.csv")
    print(df.columns)
    df = clean_dataframe(df)

    daily_splits = split_by_day(df)

    all_avgs = []
    for day_df in daily_splits.values():
        avg_df = hourly_averages(day_df)
        all_avgs.append(avg_df)

    final = pd.concat(all_avgs)
    final.to_csv("data/hourly_averages.csv", index=False)
    print("קובץ hourly_averages.csv נוצר בהצלחה.")

if __name__ == "__main__":
    main()
