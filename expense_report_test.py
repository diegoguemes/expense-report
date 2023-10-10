from expense_report import Expense, ExpenseReportPrinter, ExpenseType
from io import StringIO
import sys

dinner = Expense()
dinner.type = ExpenseType.DINNER
dinner.amount = 7500

car_rental = Expense()
car_rental.type = ExpenseType.CAR_RENTAL
car_rental.amount = 10000

breakfast = Expense()
breakfast.type = ExpenseType.BREAKFAST
breakfast.amount = 1000

def test_empty_report():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([])
    
    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Meals: 0\n'
        'Total: 0\n'
    )

def test_one_dinner():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([dinner])

    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Dinner \t 7500 \t X\n'
        'Meals: 7500\n'
        'Total: 7500\n'
    )

def test_one_car_rental():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([car_rental])

    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Car Rental \t 10000 \t  \n'
        'Meals: 0\n'
        'Total: 10000\n'
    )

def test_multiple_expenses():
    out = StringIO()
    sys.stdout = out

    ExpenseReportPrinter().print_report([breakfast, dinner, car_rental])

    assert out.getvalue() == (
        'Expense Report 2023-10-03 00:00:00\n'
        'Breakfast \t 1000 \t  \n'
        'Dinner \t 7500 \t X\n'
        'Car Rental \t 10000 \t  \n'
        'Meals: 8500\n'
        'Total: 18500\n'
    )