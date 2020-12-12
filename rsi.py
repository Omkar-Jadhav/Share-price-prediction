def rsi(df):
    # Converting to a datetime object
    #df['Date'] = pd.to_datetime(df.Date, errors='coerce')

    #Copying the close and index-date to a new datafame
    # df1 = df[['Date', 'Close']].copy()
    df1 = df[['Close']].copy()
    # Dropping NaN rows
    df1 = df1.dropna()
    # Resetting index column if needed
    # df1 = df1.set_index('Date')

    # Adding extra columns
    df1["Gain"] = 0
    df1["Loss"] = 0
    df1["Avg gain"] = 0
    df1["Avg loss"] = 0
    df1["RS"] = 0
    df1["RSI"] = 0

    # Getting Gains and Losses
    for i in range(1, len(df1)):
        diff = df1.iloc[i, 0] - df1.iloc[i - 1, 0]
        # Gain
        if diff > 0:
            df1.iloc[i, 1] = diff
        # Loss
        elif diff < 0:
            df1.iloc[i, 2] = -1 * diff

    # Indexing in python starts from 0 and goes to (n-1)

    # First average Gain
    df1.iloc[14, 3] = df1.iloc[1:15, 1].mean(skipna=True)
    # First average Loss
    df1.iloc[14, 4] = df1.iloc[1:15, 2].mean(skipna=True)

    # Remaining Avg gains & Abg losses
    for i in range(15, len(df1)):
        # Avg gains
        df1.iloc[i, 3] = (df1.iloc[i - 1, 3] * 13 + df1.iloc[i, 1]) / 14
        # Avg losses
        df1.iloc[i, 4] = (df1.iloc[i - 1, 4] * 13 + df1.iloc[i, 2]) / 14

    # Calculating RS & RSI values
    for i in range(14, len(df1)):
        # RS
        df1.iloc[i, 5] = df1.iloc[i, 3] / df1.iloc[i, 4]
        # RSI
        df1.iloc[i, 6] = 100 - (100 / (1 + df1.iloc[i, 5]))

    #rsi_df=df1.apply(lambda x: pd.Series([1, 2,3,4,5,6], index=['Gain', 'Loss', 'Avg gain','Avg loss','RS', 'RSI']), axis=1)

    return df1
