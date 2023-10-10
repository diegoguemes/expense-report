from expense_report import DinnerExpense, ExpenseReportPrinter


if __name__ == '__main__':
    expense = DinnerExpense()
    expense.amount = 7500
    ExpenseReportPrinter().print_report([expense])