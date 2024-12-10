"""
Unit tests
"""

import unittest
from script import generate_markdown_link


class TestGenerateMarkdownLink(unittest.TestCase):
    def test_custom_function_with_input(self):
        """
        Test custom_function with a specific input
        """
        input_value = "My Link Text"
        expected_output = "![Placeholder: My Link Text](https://placehold.co/600x400?text=Placeholder%3A+My+Link+Text)"
        self.assertEqual(generate_markdown_link(input_value), expected_output)


if __name__ == "__main__":
    unittest.main()
