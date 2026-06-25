cost_per_hour=0.51

cost_per_day=cost_per_hour*24
cost_per_week=cost_per_day*7
cost_per_month=cost_per_day*30
days=918/cost_per_day

print("Cost per day: $",round(cost_per_day,2))
print("Cost per week: $",round(cost_per_week,2))
print("Cost per month: $",round(cost_per_month,2))
print("Days with $918:",round(days,2))