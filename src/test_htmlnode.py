import unittest
from htmlnode import HTMLNode, LeafNode  # Update with your actual module name

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_repr(self):
        node = HTMLNode("div", "Hello, world!", [], {"class": "my-class"})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, world!, [], {'class': 'my-class'})")
    def test_htmlnode_props_to_html(self):
        node = HTMLNode("div", "Hello, world!", [], {"class": "my-class"})
        self.assertEqual(node.props_to_html(), ' class="my-class"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    # Add more test methods as requested in the assignment
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
    
    def test_leaf_to_html_empty_props(self):
        node = LeafNode("span", "Styled text", {})
        self.assertEqual(node.to_html(), "<span>Styled text</span>")

    def test_leaf_with_multiple_props(self):
        # Test a tag with multiple properties
        node = LeafNode("div", "Content", {"id": "main", "class": "container"})
        # The order of properties might vary, so we need to check parts
        html = node.to_html()
        self.assertTrue(html.startswith("<div"))
        self.assertTrue(' id="main"' in html)
        self.assertTrue(' class="container"' in html)
        self.assertTrue(">Content</div>" in html)
    
    def test_leaf_value_none_error(self):
        # Test that creating a LeafNode with None value raises ValueError
        with self.assertRaises(ValueError):
            LeafNode("p", None)    

if __name__ == "__main__":
    unittest.main()