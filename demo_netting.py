from netting import find_debt_cycle, calculate_cycle_netting

DEMO_DEBTS = [
    {"from": "Company A", "to": "Company B", "amount": 100000},
    {"from": "Company B", "to": "Company C", "amount": 80000},
    {"from": "Company C", "to": "Company A", "amount": 70000},
]

cycle = find_debt_cycle(DEMO_DEBTS)
result = calculate_cycle_netting(cycle)

print("DebtLoop circular debt demo")
print()
print("BEFORE NETTING")
for debt in cycle:
    print(f'{debt["from"]} -> {debt["to"]}: ${debt["amount"]:,}')

print(f'\nMaximum netting per link: ${result["netting_amount_per_link"]:,}')
print("\nAFTER NETTING")
for debt in result["residual_debts"]:
    print(f'{debt["from"]} -> {debt["to"]}: ${debt["after"]:,}')

print(f'\nGross obligations before: ${result["total_before"]:,}')
print(f'Gross obligations after: ${result["total_after"]:,}')
print(f'Debt eliminated: ${result["debt_eliminated"]:,}')
