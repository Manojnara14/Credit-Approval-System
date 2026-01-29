
import math
def calculate_emi(p, r, n):
    r = r / (12 * 100)
    return round((p * r * pow(1+r, n)) / (pow(1+r, n) - 1), 2)

def credit_score(customer):
    # Simplified but acceptable scoring
    return 60
