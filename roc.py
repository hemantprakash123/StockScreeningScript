import pandas as pd

def filter1(currentCombined):

    magic_df = pd.DataFrame()
    temp_df = pd.DataFrame()
    temp_df["EBITDA"] = currentCombined.loc["EBITDA",:]
    temp_df["Depreciation & amortization"] = currentCombined.loc["Depreciation & amortization",:]
    temp_df["Total Current Assets"] = currentCombined.loc["Total Current Assets"]
    temp_df["Total Current Liabilities"] = currentCombined.loc["Total Current Liabilities"]
    temp_df["Net property, plant and equipment"] = currentCombined.loc["Net property, plant and equipment"]
    temp_df = temp_df.dropna()

    #ROC
    magic_df["Returns On Capital"] = (temp_df["EBITDA"] - temp_df["Depreciation & amortization"]) / (
            temp_df["Net property, plant and equipment"] + temp_df["Total Current Assets"] - temp_df["Total Current Liabilities"])
    magic_df["ROC Rank"] = magic_df["Returns On Capital"].rank(ascending=False,na_option='bottom')
    magic_df.sort_values(by=["ROC Rank"], inplace = True)
    print(magic_df.loc[:,["ROC Rank", "Returns On Capital"]])
    tickers = magic_df.index.values
    magic_df.drop(magic_df.index[len(tickers)//2:], inplace=True)
    tickers = tickers[:len(tickers) // 3]

    return magic_df, tickers
