"""sklearn LinearRegression quick forecast demo"""

def main():
    try:
        import pandas as pd
    from sklearn.linear_model import LinearRegression
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    df = pd.DataFrame({"day":[1,2,3,4,5], "revenue":[10,11,13,16,18]})
    X = df[["day"]]; y = df["revenue"]
    model = LinearRegression().fit(X, y)
    next_day = [[df["day"].max() + 1]]
    print("next", float(model.predict(next_day)[0]))

if __name__ == "__main__":
    main()
