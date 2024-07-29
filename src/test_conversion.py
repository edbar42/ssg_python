import unittest

from conversion import \
    text_node_to_html_node  # Replace with actual module name
from htmlnodes import LeafNode
from textnode import TextNode


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_valid_text_node(self):
        """Test conversion of plain text node."""
        text_node = TextNode("Welcome to Boot.dev!", "text")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Welcome to Boot.dev!")
        self.assertEqual(result, expected)

    def test_valid_bold_node(self):
        """Test conversion of bold text node."""
        text_node = TextNode("Bold Boot.dev", "bold")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="b", value="Bold Boot.dev")
        self.assertEqual(result, expected)

    def test_valid_italic_node(self):
        """Test conversion of italic text node."""
        text_node = TextNode("Italic Boot.dev", "italic")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="i", value="Italic Boot.dev")
        self.assertEqual(result, expected)

    def test_valid_code_node(self):
        """Test conversion of code text node."""
        text_node = TextNode("print('Hello, Boot.dev!')", "code")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="code", value="print('Hello, Boot.dev!')")
        self.assertEqual(result, expected)

    def test_valid_link_node(self):
        """Test conversion of link text node."""
        text_node = TextNode("Boot.dev Course", "link", "https://boot.dev")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(
            tag="a", value="Boot.dev Course", props={"href": "https://boot.dev"}
        )
        self.assertEqual(result, expected)

    def test_valid_image_node(self):
        """Test conversion of image text node."""
        text_node = TextNode("Boot.dev Logo", "image", "https://boot.dev/logo.png")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(
            tag="img",
            value="",
            props={"src": "https://boot.dev/logo.png", "alt": "Boot.dev Logo"},
        )
        self.assertEqual(result, expected)

    def test_invalid_text_node_type(self):
        """Test that an exception is raised for invalid text node type."""
        text_node = TextNode("Invalid Type", "invalid_type")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Invalid text node type")


if __name__ == "__main__":
    unittest.main()
