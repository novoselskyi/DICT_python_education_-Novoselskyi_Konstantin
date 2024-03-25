import argparse
import math
import sys

def calculate_n(principal, monthly_payment, interest):
    i = interest / (12 * 100)
    n = math.log((monthly_payment / (monthly_payment - i * principal)), 1 + i)
    return math.ceil(n)

def calculate_a(principal, periods, interest):
    i = interest / (12 * 100)
    annuity_payment = principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    return math.ceil(annuity_payment)

def calculate_p(annuity_payment, periods, interest):
    i = interest / (12 * 100)
    principal = annuity_payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    return round(principal)

def calculate_diff(principal, periods, interest):
    diff_payments = []
    i = interest / (12 * 100)
    for m in range(1, periods + 1):
        dm = principal / periods + i * (principal - (principal * (m - 1) / periods))
        diff_payments.append(math.ceil(dm))
    return diff_payments

def calculate_overpayment(payments, principal):
    return sum(payments) - principal

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: annuity or diff")
parser.add_argument("--principal", type=float, help="Principal amount of the loan")
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument("--periods", type=int, help="Number of periods (months)")
parser.add_argument("--interest", type=float, help="Annual interest rate")
args = parser.parse_args()

if not args.type:
    print("Incorrect parameters")
    sys.exit()

if args.type == "diff" and args.payment:
    print("Incorrect parameters")
    sys.exit()

if args.interest is None or any(v is None for v in [args.principal, args.periods]):
    print("Incorrect parameters")
    sys.exit()

if args.type == "annuity":
    if args.payment:
        annuity_payment = args.payment
        periods = args.periods
        interest = args.interest
        principal = calculate_p(annuity_payment, periods, interest)
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {calculate_overpayment([annuity_payment] * periods, principal)}")
    elif args.principal and args.periods:
        principal = args.principal
        periods = args.periods
        interest = args.interest
        annuity_payment = calculate_a(principal, periods, interest)
        print(f"Your annuity payment = {annuity_payment}!")
        print(f"Overpayment = {calculate_overpayment([annuity_payment] * periods, principal)}")
    elif args.payment and args.periods:
        print("Incorrect parameters")
    else:
        print("Incorrect parameters")

elif args.type == "diff":
    if args.principal and args.periods:
        principal = args.principal
        periods = args.periods
        interest = args.interest
        diff_payments = calculate_diff(principal, periods, interest)
        for m, payment in enumerate(diff_payments, start=1):
            print(f"Month {m}: payment is {payment}")
        print(f"Overpayment = {calculate_overpayment(diff_payments, principal)}")
    else:
        print("Incorrect parameters")
