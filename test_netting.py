import unittest

from netting import find_debt_cycle, calculate_cycle_netting


class NettingTests(unittest.TestCase):
    def test_three_company_cycle(self):
        debts = [
            {"from": "CompanyA", "to": "CompanyB", "amount": 100000},
            {"from": "CompanyB", "to": "CompanyC", "amount": 80000},
            {"from": "CompanyC", "to": "CompanyA", "amount": 70000},
        ]

        cycle = find_debt_cycle(debts)
        self.assertIsNotNone(cycle)

        result = calculate_cycle_netting(cycle)
        self.assertEqual(result["netting_amount_per_link"], 70000)
        self.assertEqual(result["total_before"], 250000)
        self.assertEqual(result["total_after"], 40000)
        self.assertEqual(result["debt_eliminated"], 210000)
        self.assertEqual(
            [d["after"] for d in result["residual_debts"]],
            [30000, 10000, 0],
        )

    def test_no_cycle(self):
        debts = [
            {"from": "CompanyA", "to": "CompanyB", "amount": 100000},
            {"from": "CompanyB", "to": "CompanyC", "amount": 80000},
        ]
        self.assertIsNone(find_debt_cycle(debts))

    def test_cycle_inside_longer_path(self):
        debts = [
            {"from": "Outside", "to": "CompanyA", "amount": 50000},
            {"from": "CompanyA", "to": "CompanyB", "amount": 40000},
            {"from": "CompanyB", "to": "CompanyA", "amount": 30000},
        ]
        cycle = find_debt_cycle(debts)
        self.assertEqual(len(cycle), 2)
        self.assertEqual(cycle[0]["from"], "CompanyA")
        self.assertEqual(cycle[1]["to"], "CompanyA")


if __name__ == "__main__":
    unittest.main()
