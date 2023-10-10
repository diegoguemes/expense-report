import locale
from enum import Enum, unique, auto
from datetime import datetime
from typing import List


@unique
class ExpenseType(Enum):
    DINNER = auto()
    BREAKFAST = auto()
    CAR_RENTAL = auto()


class Expense:
    type: ExpenseType
    amount: int

    def name(self):
        name = ""
        if self.type == ExpenseType.DINNER:
            name = "Dinner"
        elif self.type == ExpenseType.BREAKFAST:
            name = "Breakfast"
        elif self.type == ExpenseType.CAR_RENTAL:
            name = "Car Rental"
        return name
    
    def is_over_expense(self):
        return self.type == ExpenseType.DINNER and self.amount > 5000 or self.type == ExpenseType.BREAKFAST and self.amount > 1000

    def is_meal(self):
        return self.type == ExpenseType.DINNER or self.type == ExpenseType.BREAKFAST

class ExpenseReport:
    def print_report(self, expenses: List[Expense]):
        total = 0
        meals = 0

        # TODO: Reemplazar con datetime.now()
        print("Expense Report", datetime(2023, 10, 3))

        for expense in expenses:
            if expense.is_meal():
                meals += expense.amount

            meal_over_expenses_marker = "X" if expense.is_over_expense() else " "
            print(expense.name(), "\t", expense.amount, "\t", meal_over_expenses_marker)
            total += expense.amount

        print("Meals:", meals)
        print("Total:", total)

