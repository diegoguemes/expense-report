import locale
from enum import Enum, unique, auto
from datetime import datetime
from typing import Callable, List
import sys


class Expense:
    amount: int

class DinnerExpense(Expense):
    def name(self) -> str:
        return "Dinner"

    def is_over_expense(self):
        return self.amount > 5000
    
    def is_meal(self):
        return True

class BreakfastExpense(Expense):
    def name(self) -> str:
        return "Breakfast"

    def is_over_expense(self):
        return self.amount > 1000
    
    def is_meal(self):
        return True

class CarRentalExpense(Expense):
    def name(self) -> str:
        return "Car Rental"

    def is_over_expense(self):
        return False
    
    def is_meal(self):
        return False


class ExpenseReportPrinter:
    def __init__(self, file=sys.stdout):
        self.file = file

    def print_report(self, expenses: List[Expense], now: Callable=datetime.now):
        report = ExpenseReport(expenses)

        print("Expense Report", now(), file=self.file)

        for expense in report.expenses:
            meal_over_expenses_marker = "X" if expense.is_over_expense() else " "
            print(expense.name(), "\t", expense.amount, "\t", meal_over_expenses_marker, file=self.file)

        print("Meals:", report.calculate_meals_total(), file=self.file)
        print("Total:", report.calculate_total(), file=self.file)


class ExpenseReport():
    def __init__(self, expenses: List[Expense]) -> None:
        self.expenses = expenses

    def calculate_meals_total(self) -> int:
        return sum(e.amount for e in self.expenses if e.is_meal())

    def calculate_total(self) -> int:
        return sum(e.amount for e in self.expenses)