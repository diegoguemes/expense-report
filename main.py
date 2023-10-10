from expense_report import ExpenseReportPrinter, Expense, ExpenseType


if __name__ == '__main__':
    expense = Expense()
    expense.type = ExpenseType.DINNER
    expense.amount = 7500
    ExpenseReportPrinter().print_report([expense])