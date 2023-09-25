def calc(months, interest, total):
  monthly_Payment = total * ( interest / months)
  monthly_Payment = round(monthly_Payment, 2)
  return monthly_Payment