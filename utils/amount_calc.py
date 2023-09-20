def get_due_amount(days):
    print(days)
    if days <= 7:
        return 100 * days
    elif days <= 21:
        return 7*100 + (days-7)*200
    else:
        return 7*100 + 14*200 + (days - 21)*500
