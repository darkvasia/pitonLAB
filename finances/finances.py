import csv
import datetime
from typing import List

class Transaction:
    def __init__(self, amount: float, description: str, date: datetime.date):
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.date.isoformat()}, {self.amount}, {self.description}"

class TransactionTracker:
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.balance = 0.0

    def add_transaction(self, transaction: Transaction):
        if transaction.amount < 0:
            print(f"Витрата: {transaction}")
        else:
            print(f"Дохід: {transaction}")

        self.transactions.append(transaction)
        self.balance += transaction.amount  

    def remove_transaction(self, index: int):
        if 0 <= index < len(self.transactions):
            self.balance -= self.transactions[index].amount
            del self.transactions[index]
        else:
            print("Не знайденно жодної транзакції")

    def get_balance(self):
        return self.balance

    def save_transactions_to_csv(self, file_path: str):
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Дата', 'Сцма', 'Опис'])
                for transaction in self.transactions:
                    writer.writerow([transaction.date, transaction.amount, transaction.description])
            print(f"Транзакція збережена до {file_path}")
        except Exception as e:
            print(f"Сталася помилка під час запису {e}")


tracker = TransactionTracker()


tracker.add_transaction(Transaction(100.0, 'Зарплата', datetime.date.today()))
tracker.add_transaction(Transaction(-50.0, 'Продукти', datetime.date.today()))


tracker.remove_transaction(0)

print(f"Поточний баланс: {tracker.get_balance()}")


tracker.save_transactions_to_csv('transactions.csv')
