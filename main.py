# main.py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja

# csv読込
df = pd.read_csv("sales.csv")

# 日付を datetime 型に変換
df["date"] = pd.to_datetime(df["date"])

# 月ごとの列を作成
df["month"] = df["date"].dt.to_period("M")

# 月ごとの売り上げを集計
monthly_sales = df.groupby("month")["amount"].sum().reset_index()

# グラフサイズ指定（ここについては任意）
plt.figure(figsize=(8,4))

# 棒グラフ
plt.bar(monthly_sales["month"].astype(str), monthly_sales["amount"], color="skyblue")

# タイトルとラベル
plt.title("月別売上集計")
plt.xlabel("月")
plt.ylabel("売上（円）")

# 保存
plt.tight_layout()
# plt.show()
plt.savefig("monthly_sales.png")