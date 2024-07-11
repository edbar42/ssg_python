import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = ("", "", None)
        node2 = ("", "", None)
        self.assertEqual(node1, node2)

        node3 = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "bold")
        self.assertEqual(node3, node4)

        node5 = TextNode("Check out boot.dev", "italic", "https://boot.dev")
        node6 = TextNode("Check out boot.dev", "italic", "https://boot.dev")
        self.assertEqual(node5, node6)


if __name__ == "__main__":
    unittest.main()
