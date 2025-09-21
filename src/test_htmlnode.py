import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_node1(self):
        node1 = HTMLNode("p", "Here is some text", None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        html_props = node1.props_to_html()
        self.assertEqual(html_props,  'href="https://www.google.com" target="_blank"')

    def test_node2(self):
        node2 = HTMLNode(None, "Here is some text", None, {
    "href": "https://www.google.com"})
        html_props = node2.props_to_html()
        self.assertEqual(html_props,  'href="https://www.google.com"')

    def test_node3(self):
        node3 = HTMLNode(None, None, None, {})
        html_props = node3.props_to_html()
        self.assertEqual(html_props, '')

if __name__ == "__main__":
    unittest.main()
