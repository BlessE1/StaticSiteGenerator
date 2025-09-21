class HTMLNode:
   def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props

   def to_html(self):
      raise NotImplementedError("to_html method not implemented")

   def props_to_html(self):
      if not self.props:
         return ''

      return ' '.join(f'{k}="{v}"' for k, v in self.props.items())

   def __repr__(self):
      return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
   def __init__(self, tag, value, props=None):
      super().__init__(tag=tag, value=value, props=props)

   def to_html(self):
      if self.value is None:
         raise ValueError(f"leaf node has no value: Tag->{self.tag}, Value->{self.value}, Props->{self.props}")

      if self.tag is None:
         return self.value

      props_string = self.props_to_html()
      return f"<{self.tag}{' '*bool(props_string)}{props_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
   def __init__(self, tag, children, props=None):
      super().__init__(tag=tag, children=children, props=props)

   def to_html(self):
      if self.tag is None:
         raise ValueError("parent node has no tag")

      if self.children is None:
         raise ValueError("parent node's children do not exist")

      inner_html = ""
      for child in self.children:
         inner_html += child.to_html()

      props_string = self.props_to_html()
      return f"<{self.tag}{' '*bool(props_string)}{props_string}>{inner_html}</{self.tag}>"

