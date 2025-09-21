import unittest
from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_not_heading(self):
        block = "########  This is not a heading"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code(self):
        block = "``` print(num) ```"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_not_code(self):
        block = "` `` not code `"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_quote(self):
        block = "> This\n>is \n> a quote "
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.QUOTE)

    def test_not_quote(self):
        block = "- This is\n>not a quote"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- this is\n- an unordered\n- list "
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_not_unordered_list(self):
        block = "- this is\n-not an unordered\n- list "
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. this is\n2. an ordered\n3. list "
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_not_ordered_list(self):
        block = "0. this is\n1. not an unordered\n2. list "
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is a paragraph"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
