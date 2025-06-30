from src.counting_transactions import count_transactions
import unittest

class TestCountTransactions(unittest.TestCase):

    def test_empty_transactions(self):
        transactions = []
        result = count_transactions(transactions)
        self.assertEqual(result, {})

    def test_single_transaction(self):
        transactions = [{'description': 'deposit'}]
        result = count_transactions(transactions)
        self.assertEqual(result, {'deposit': 1})

    def test_multiple_transactions_same_description(self):
        transactions = [{'description': 'deposit'}, {'description': 'deposit'}]
        result = count_transactions(transactions)
        self.assertEqual(result, {'deposit': 2})

    def test_multiple_transactions_different_descriptions(self):
        transactions = [
            {'description': 'deposit'},
            {'description': 'withdraw'},
            {'description': 'transfer'}
        ]
        result = count_transactions(transactions)
        self.assertEqual(result, {'deposit': 1, 'withdraw': 1, 'transfer': 1})

    def test_transactions_with_same_and_different_descriptions(self):
        transactions = [
            {'description': 'deposit'},
            {'description': 'withdraw'},
            {'description': 'deposit'},
            {'description': 'transfer'},
            {'description': 'withdraw'}
        ]
        result = count_transactions(transactions)
        self.assertEqual(result, {'deposit': 2, 'withdraw': 2, 'transfer': 1})