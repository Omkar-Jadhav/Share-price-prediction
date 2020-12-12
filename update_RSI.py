def update_rsi_df(df1, df1_rsi):
    # Price=sc1.inverse_transform(yhat)[0][0]
    diff = df1.iloc[-1, 0] - df1.iloc[-2, 0]  # Calculate the difference first

    ##Check if it is a gain or loss

    # Gain
    if diff > 0:
        Gain = diff
        Loss = 0
    # Loss

    elif diff < 0:
        Loss = -1 * diff
        Gain = 0
    else:
        Gain = 0
        Loss = 0

# Update the Avg gain and Avg loss using the previous Avg gain values and latest Gains
    Avg_gain = (df1_rsi.iloc[-1, 3] * 13 + Gain) / 14

    Avg_loss = (df1_rsi.iloc[-1, 4] * 13 + Loss) / 14

# Calculate Relative strength
    RS = Avg_gain / Avg_loss

# Calculate RSI
    RSI = 100 - (100 / (1 + RS))

# Add RSI to the data frame which has close values and RSI only
# df_temp=pd.DataFrame( {'Close':'NaN',
#                                                    'RSI':[RSI]}  )

# df1=df1.append(df_temp,ignore_index=True)
    df1.iloc[-1, 1] = RSI

# Append all the values to the data frame used for calculating RSI
# This updated dataframe will be used in next step
    df1_rsi = df1_rsi.append({'Close': Price, 'Gain': Gain, 'Loss': Loss, 'Avg gain': Avg_gain,
                          'Avg loss': Avg_loss, 'RS': RS, 'RSI': RSI}, ignore_index=True)
    return df1_rsi, RSI