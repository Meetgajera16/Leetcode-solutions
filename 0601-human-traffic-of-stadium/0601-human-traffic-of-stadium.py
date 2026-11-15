import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium[stadium["people"] >= 100].copy()

    df["grp"] = df["id"] - range(1, len(df)+1)

    df["count"] = df.groupby("grp")["id"].transform("count")

    result = df[df["count"] >= 3]

    return result[["id", "visit_date", "people"]].sort_values("visit_date")