
def split_by_day(df):
    df['date'] = df['timestamp'].dt.date
    return dict(tuple(df.groupby('date')))