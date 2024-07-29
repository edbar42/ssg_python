import unittest

from htmlnodes import LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_leaf_node_no_value(self):
        """Test that LeafNode raises an error if no value is provided"""
        with self.assertRaises(ValueError):
            leaf = LeafNode(value=None, tag="p")
            leaf.to_html()

    def test_leaf_node_no_tag(self):
        """Test LeafNode correctly returns the value when no tag is provided"""
        leaf = LeafNode(value="Hello, World!")
        self.assertEqual(leaf.to_html(), "Hello, World!")

    def test_leaf_node_with_tag(self):
        """Test that LeafNode correctly formats HTML with a tag"""
        leaf = LeafNode(value="Hello, World!", tag="p", props={"class": "greeting"})
        self.assertEqual(leaf.to_html(), '<p class="greeting">Hello, World!</p>')

    def test_parent_node_no_tag(self):
        """Test that ParentNode raises an error if no tag is provided"""
        with self.assertRaises(ValueError):
            parent = ParentNode(tag=None, children=[LeafNode(value="Child")])
            parent.to_html()

    def test_parent_node_no_children(self):
        """Test that ParentNode raises an error if no children are provided"""
        with self.assertRaises(ValueError):
            parent = ParentNode(tag="div")
            parent.to_html()

    def test_parent_node_with_children(self):
        """Test that ParentNode correctly formats HTML with children"""
        child1 = LeafNode(value="Child 1")
        child2 = LeafNode(value="Child 2")
        parent = ParentNode(
            tag="div", children=[child1, child2], props={"id": "parent"}
        )
        expected_html = '<div id="parent">Child 1Child 2</div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_with_props(self):
        """Test that ParentNode correctly formats HTML with props"""
        child = LeafNode(value="Child", tag="span", props={"class": "child"})
        parent = ParentNode(tag="section", children=[child], props={"id": "section"})
        expected_html = (
            '<section id="section"><span class="child">Child</span></section>'
        )
        self.assertEqual(parent.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
