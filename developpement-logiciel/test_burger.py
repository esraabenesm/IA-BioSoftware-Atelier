import unittest
from unittest.mock import patch

from burger import (
    get_bun,
    get_bun_v2,
    get_meat,
    get_cheese,
    get_sauce,
    get_order_timestamp,
    calculate_burger_price,
    assemble_burger,
)

class TestBurgerFunctions(unittest.TestCase):
    @patch('builtins.input', return_value='brioche')
    def test_get_bun(self, mock_input):
        result = get_bun()
        self.assertEqual(result, 'brioche')

    @patch('builtins.input', return_value='sesame')
    def test_get_bun_v2(self, mock_input):
        result = get_bun_v2()
        self.assertEqual(result, 'sesame')

    @patch('builtins.input', return_value='beef')
    def test_get_meat(self, mock_input):
        result = get_meat()
        self.assertEqual(result, 'beef')

    @patch('builtins.input', return_value='cheddar')
    def test_get_cheese(self, mock_input):
        result = get_cheese()
        self.assertEqual(result, 'cheddar')

    def test_get_sauce(self):
        result = get_sauce()
        self.assertIn("and", result)  # juste pour vérifier que ça retourne quelque chose

    def test_get_order_timestamp(self):
        result = get_order_timestamp()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_calculate_burger_price(self):
        ingredients = ['bun', 'meat', 'cheese']
        price = calculate_burger_price(ingredients)
        self.assertGreater(price, 0)

    @patch('builtins.input', side_effect=['brioche', 'beef', 'cheddar'])
    def test_assemble_burger(self, mock_input):
        result = assemble_burger()
        self.assertIn('bun', result)   # va trouver "brioche bun"
        self.assertIn('beef', result)
        self.assertIn('cheddar', result)

if __name__ == "__main__":
    unittest.main()
