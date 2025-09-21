import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
       md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

       node = markdown_to_html_node(md)
       html = node.to_html()
       self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
       md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

       node = markdown_to_html_node(md)
       html = node.to_html()
       self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_headings(self):
       md = """
# Heading 1

## Heading 2 **with bold**

##### Heading 5 `with code`

###### Heading 6 _with italics_

######## Fake heading paragraph
"""

       node = markdown_to_html_node(md)
       html = node.to_html()
       self.assertEqual(html, '<div><h1>Heading 1</h1><h2>Heading 2 <b>with bold</b></h2><h5>Heading 5 <code>with code</code></h5><h6>Heading 6 <i>with italics</i></h6><p>######## Fake heading paragraph</p></div>'
)

    def test_quotes(self):
       md = """
> First line

> `Some code`
> _some italics_
> **some bold**
"""

       node = markdown_to_html_node(md)
       html = node.to_html()
       self.assertEqual(html,
"<div><blockquote><p>First line</p></blockquote><blockquote><p><code>Some code</code> <i>some italics</i> <b>some bold</b></p></blockquote></div>")

    def test_unordered_lists(self):
       md = """
- First line
- Second line
- `Some code`
- _Some italics_
- **Some bold**
"""

       node = markdown_to_html_node(md)
       html = node.to_html()
       self.assertEqual(html,
"<div><ul><li>First line</li><li>Second line</li><li><code>Some code</code></li><li><i>Some italics</i></li><li><b>Some bold</b></li></ul></div>")

    def test_unordered_lists(self):
       md = """
1. First line
2. Second line
3. `Some code`
4. _Some italics_
5. **Some bold**
"""

       node = markdown_to_html_node(md)
       html = node.to_html()
       self.assertEqual(html,
"<div><ol><li>First line</li><li>Second line</li><li><code>Some code</code></li><li><i>Some italics</i></li><li><b>Some bold</b></li></ol></div>")

if __name__ == "__main__":
    unittest.main()
