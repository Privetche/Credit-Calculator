import sys
import math
import argparse


def calculate_annuity_period(principal, monthly_payment, credit_interest):
    credit_interest = credit_interest / 1200
    result = math.ceil(
        math.log((monthly_payment / (monthly_payment - credit_interest * principal)), 1 + credit_interest))
    if result == 1:
        print("1 month")
    elif result < 12:
        print(str(result) + " months")
    else:
        if result == 1:
            print("1 year")
        elif result % 12 == 0:
            print(str(result // 12) + " years")
        else:
            print(str(result // 12) + " years and " + str(result % 12) + " months")
    print("Overpayment = " + str(monthly_payment * result - principal))

def calculate_annuity_principal(monthly_payment, count_of_periods, credit_interest):
    credit_interest = credit_interest / 1200
    result = monthly_payment * ((1 + credit_interest) ** count_of_periods - 1) / (
                credit_interest * ((1 + credit_interest) ** count_of_periods))
    print("Your credit principal = " + str(result) + "!")
    print("Overpayment = " + str(monthly_payment * count_of_periods - result))


def calculate_annuity_payment(principal, count_of_periods, credit_interest):
    credit_interest = credit_interest / 1200
    result = math.ceil(principal * credit_interest * ((credit_interest + 1) ** count_of_periods) / (
                ((1 + credit_interest) ** count_of_periods) - 1))
    print("Your annuity payment = " + str(result) + "!")

def calculate_diff_payment(principal, periods, interest):
    interest = interest / 1200
    current_period = 1
    total = 0
    while current_period < periods + 1:
        result = principal / periods + interest * (principal - (principal * (current_period - 1) / periods))
        print("Month " + str(current_period) + " paid out " + str(math.ceil(result)))
        total = total + math.ceil(result)
        current_period += 1
    total = int(total - principal)
    print("""
Overpayment = """ + str(total))

parser = argparse.ArgumentParser()
arguments = ["--type", "--payment", "--principal", "--periods", "--interest"]
for argument in arguments:
    parser.add_argument(argument)
args = parser.parse_args()

if len(sys.argv) != 5:
    print("Incorrect parameters")
else:
    if args.type == "annuity":
        if not args.payment:
            calculate_annuity_payment(float(args.principal), float(args.periods), float(args.interest))
        elif not args.principal:
            calculate_annuity_principal(float(args.payment), float(args.periods), float(args.interest))
        elif not args.periods:
            calculate_annuity_period(float(args.principal), float(args.payment), float(args.interest))
        else:
            print("Incorrect parameters")

    elif args.type == "diff":
        if not args.payment:
            calculate_diff_payment(float(args.principal), float(args.periods), float(args.interest))
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
