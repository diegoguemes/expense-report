from datetime import datetime
from expense_report import BreakfastExpense, CarRentalExpense, DinnerExpense, ExpenseReportPrinter, ExpenseType
from io import StringIO
import sys

dinner = DinnerExpense()
dinner.amount = 7500

car_rental = CarRentalExpense()
car_rental.amount = 10000

breakfast = BreakfastExpense()
breakfast.type = ExpenseType.BREAKFAST
breakfast.amount = 1000

def dummy_now():
    return datetime(2023, 10, 3)

def test_empty_report():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([], now=dummy_now)
    
    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Meals: 0\n'
        'Total: 0\n'
    )

def test_one_dinner():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([dinner], now=dummy_now)

    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Dinner \t 7500 \t X\n'
        'Meals: 7500\n'
        'Total: 7500\n'
    )

def test_one_car_rental():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([car_rental], now=dummy_now)

    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Car Rental \t 10000 \t  \n'
        'Meals: 0\n'
        'Total: 10000\n'
    )

def test_multiple_expenses():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([breakfast, dinner, car_rental], now=dummy_now)

    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Breakfast \t 1000 \t  \n'
        'Dinner \t 7500 \t X\n'
        'Car Rental \t 10000 \t  \n'
        'Meals: 8500\n'
        'Total: 18500\n'
    )