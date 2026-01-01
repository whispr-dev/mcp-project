"""polars quick dataframe demo"""

def main():
    try:
        import polars as pl
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    df = pl.DataFrame({"a":[1,2,3],"b":[10,20,30]})
    print(df.with_columns((pl.col("a")*pl.col("b")).alias("c")))

if __name__ == "__main__":
    main()
