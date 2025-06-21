import unittest
import re
from src.bank_operations import search_transactions, count_transactions_by_category


class TestSearchTransactions(unittest.TestCase):

    def setUp(self):
        self.data = [
            {'id': 1, 'description': 'Payment for groceries'},
            {'id': 2, 'description': 'Payment for utilities'},
            {'id': 3, 'description': 'Refund for groceries'},
            {'id': 4, 'description': 'Dinner out'},
            {'id': 5, 'description': 'GROceries purchase'},
            {'id': 6, 'description': ''},
            {'id': 7, 'description': None},
            {'id': 8, 'amount': 100},
        ]

    def test_search_exact_match(self):
        result = search_transactions(self.data, 'groceries')
        expected = [
            {'id': 1, 'description': 'Payment for groceries'},
            {'id': 3, 'description': 'Refund for groceries'},
            {'id': 5, 'description': 'GROceries purchase'},
        ]
        self.assertEqual(result, expected)

    def test_search_partial_match(self):
        result = search_transactions(self.data, 'payment')
        expected = [
            {'id': 1, 'description': 'Payment for groceries'},
            {'id': 2, 'description': 'Payment for utilities'},
        ]
        self.assertEqual(result, expected)

    def test_search_case_insensitive(self):
        result = search_transactions(self.data, 'GROCERIES')
        expected = [
            {'id': 1, 'description': 'Payment for groceries'},
            {'id': 3, 'description': 'Refund for groceries'},
            {'id': 5, 'description': 'GROceries purchase'},
        ]
        self.assertEqual(result, expected)

    def test_search_no_matches(self):
        result = search_transactions(self.data, 'invalid search')
        expected = []
        self.assertEqual(result, expected)

    def test_search_with_non_string_descriptions(self):
        result = search_transactions(self.data, 'dinner')
        expected = [{'id': 4, 'description': 'Dinner out'}]
        self.assertEqual(result, expected)

    def test_search_on_nonexistent_key(self):
        result = search_transactions(self.data, 'amount')
        expected = []
        self.assertEqual(result, expected)


class TestCountTransactionsByCategory(unittest.TestCase):

    def test_empty_data(self):
        data = []
        categories = ['food', 'entertainment']
        result = count_transactions_by_category(data, categories)
        expected = {'food': 0, 'entertainment': 0}
        self.assertEqual(result, expected)

    def test_no_matching_categories(self):
        data = [{'description': 'shopping'}, {'description': 'travel'}]
        categories = ['food', 'entertainment']
        result = count_transactions_by_category(data, categories)
        expected = {'food': 0, 'entertainment': 0}
        self.assertEqual(result, expected)

    def test_some_matching_categories(self):
        data = [
            {'description': 'food'},
            {'description': 'entertainment'},
            {'description': 'food'},
            {'description': 'shopping'}
        ]
        categories = ['food', 'entertainment']
        result = count_transactions_by_category(data, categories)
        expected = {'food': 2, 'entertainment': 1}
        self.assertEqual(result, expected)

    def test_all_matching_categories(self):
        data = [
            {'description': 'food'},
            {'description': 'entertainment'},
            {'description': 'food'},
            {'description': 'entertainment'},
            {'description': 'entertainment'},
        ]
        categories = ['food', 'entertainment']
        result = count_transactions_by_category(data, categories)
        expected = {'food': 2, 'entertainment': 3}
        self.assertEqual(result, expected)

    def test_extra_categories(self):
        data = [{'description': 'food'}, {'description': 'entertainment'}]
        categories = ['food', 'entertainment', 'shopping']
        result = count_transactions_by_category(data, categories)
        expected = {'food': 1, 'entertainment': 1, 'shopping': 0}
        self.assertEqual(result, expected)
