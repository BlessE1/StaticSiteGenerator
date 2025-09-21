import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
       node = TextNode("This is a text node", TextType.TEXT)
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, None)
       self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
       node = TextNode("This is a bold text node", TextType.BOLD)
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, "b")
       self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
       node = TextNode("This is an italic text node", TextType.ITALIC)
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, "i")
       self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
       node = TextNode("This is a code text node", TextType.CODE)
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, "code")
       self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
       node = TextNode("This is a link (anchor) text node", TextType.LINK, "https")
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, "a")
       self.assertEqual(html_node.value, "This is a link (anchor) text node")
       self.assertEqual(html_node.props, {"href": "https"})

    def test_image(self):
       node = TextNode("This is a image (alt) text node", TextType.IMAGE, "http")
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, "img")
       self.assertEqual(html_node.value, "")
       self.assertEqual(html_node.props, {"src": "http", "alt":"This is a image (alt) text node"})

    def test_not_valid_text_type(self):
       node = TextNode("This is not a text node", "o")
       self.assertRaises(Exception, text_node_to_html_node, node)

if __name__ == "__main__":
    unittest.main()
