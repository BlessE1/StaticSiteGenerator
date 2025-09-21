import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
       child_node = LeafNode("span", "child")
       parent_node = ParentNode("div", [child_node])
       self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
       grandchild_node = LeafNode("b", "grandchild")
       child_node = ParentNode("span", [grandchild_node])
       parent_node = ParentNode("div", [child_node])
       self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_hmtl_with_no_children(self):
       parent_node = ParentNode("div", [])
       self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_no_value(self):
       child_node = LeafNode("span", "child")
       parent_node = ParentNode(None, [child_node])
       self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_props(self):
       child_node = LeafNode("span", "child", {"css":"good"})
       parent_node = ParentNode("div", [child_node], {"color":"red", "style":"ok"})
       self.assertEqual(parent_node.to_html(), '<div color="red" style="ok"><span css="good">child</span></div>')

if __name__ == "__main__":
    unittest.main()
