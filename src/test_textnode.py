import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_not_eq_text(self):
        node1 = TextNode("This is a not node", TextType.CODE)
        node2 = TextNode("This is a node", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_eq_with_link(self):
        node1 = TextNode("This is a node", TextType.CODE, "https")
        node2 = TextNode("This is a node", TextType.CODE, "https")
        self.assertEqual(node1, node2)

    def test_not_eq_with_link(self):
        node1 = TextNode("This is a node", TextType.LINK, "http2")
        node2 = TextNode("This is a node", TextType.LINK, "http3")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
