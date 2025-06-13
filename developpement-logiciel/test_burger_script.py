import unittest
from unittest.mock import patch

from burger import (
    get_bun,       # au lieu de GetBun
    get_meat,      # au lieu de getMeat
    get_sauce,     # au lieu de GET_SAUCE
    get_cheese,    # au lieu de get_cheese123
    assemble_burger,  # au lieu de AssembleBurger
    save_burger,      # au lieu de SaveBurger
    main
)


from datetime import datetime
import os


class TestBurgerFunctions(unittest.TestCase):

    def test_get_order_timestamp(self):
        """Should return a valid timestamp string."""
        timestamp = get_order_timestamp()
        try:
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid)

    @patch('builtins.input', return_value='brioche')
    def test_GetBun(self, mock_input):
        result = GetBun()
        self.assertEqual(result, 'brioche')

    @patch('builtins.input', return_value='sesame')
    def test_get_bun_v2(self, mock_input):
        result = get_bun_v2()
        self.assertEqual(result, 'sesame')

    def test_calculate_burger_price(self):
        ingredients = ['bun', 'beef', 'cheese']
        price = calculate_burger_price(ingredients)
        expected_base = 2.0 + 5.0 + 1.0  # = 8.0
        expected_price = expected_base * 1.1 * 1.1  # 2 taxes
        self.assertAlmostEqual(price, expected_price, places=2)

    @patch('builtins.input', return_value='beef')
    def test_getMeat(self, mock_input):
        result = getMeat()
        self.assertEqual(result, 'beef')

    def test_GET_SAUCE(self):
        result = GET_SAUCE()
        self.assertEqual(result, "ketchup and mustard")

    @patch('builtins.input', return_value='cheddar')
    def test_get_cheese123(self, mock_input):
        result = get_cheese123()
        self.assertEqual(result, 'cheddar')

    @patch('builtins.input', side_effect=['brioche', 'beef', 'cheddar'])
    def test_AssembleBurger(self, mock_input):
        # GET_SAUCE doesn't require input so only 3 needed
        burger = AssembleBurger()
        self.assertIn('brioche', burger)
        self.assertIn('beef', burger)
        self.assertIn('cheddar', burger)
        self.assertIn('ketchup', burger)

    @patch('builtins.input', side_effect=['brioche', 'beef', 'cheddar'])
    def test_SaveBurger(self, mock_input):
        burger = AssembleBurger()
        SaveBurger(burger)
        with open("/tmp/burger.txt", "r") as f:
            content = f.read()
        self.assertIn("brioche", content)
        with open("/tmp/burger_count.txt", "r") as f:
            count = int(f.read())
        self.assertGreaterEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
