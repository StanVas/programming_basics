deposit_amount = float(input())
deposit_time = int(input())
annual_rate = float(input())
interest = deposit_amount * (annual_rate / 100)
interest_per_month = interest / 12
total_amount = deposit_amount + (deposit_time * interest_per_month)
print(total_amount)
