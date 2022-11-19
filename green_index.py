import pandas as pd

df = pd.read_csv("zero_tracker.csv")

cols = ["end_target_status", "gasses_coverage", "reporting_mechanism", "has_plan", "accountability"]

target = list(df["end_target_status"].unique())
t_values = [3, 5, 4, 7, 7, 0, 5, 10]
target_dict = {target[i] : t_values[i] for i in range(len(target))}

gas = list(df["gasses_coverage"].unique())
g_values = [0, 10, 5, 0]
gas_dict = {gas[i] : g_values[i] for i in range(len(gas))}

report = list(df["reporting_mechanism"].unique())
r_values = [2.5, 5, 0, 0]
report_dict = {report[i] : r_values[i] for i in range(len(report))}

plan = list(df["has_plan"].unique())
p_values = [0, 5, 0]
plan_dict = {plan[i] : p_values[i] for i in range(len(plan))}

acc = list(df["accountability"].unique())
a_values = [0, 0, 0, 5]
acc_dict = {acc[i] : a_values[i] for i in range(len(acc))}

df["green index"] = " "

for i in range(len(df)):
    a = list(df[cols].iloc[i])
    res = 0
    res = target_dict[a[0]] + gas_dict[a[1]] + report_dict[a[2]] + plan_dict[a[3]] + acc_dict[a[4]]
    df["green index"].iloc[i] = res

df.to_csv("zt_data_with_gi.csv")