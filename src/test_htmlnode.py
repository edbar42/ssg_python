import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node_with_all_params = HTMLNode(
            tag='div',
            value='content',
            children=[HTMLNode(tag='span', value='child')],
            props={'class': 'my-class', 'id': 'my-id'}
        )
        self.node_with_no_params = HTMLNode()
        self.node_with_some_params = HTMLNode(tag='p', value='text')

    def test_initialization_with_all_params(self):
        self.assertEqual(self.node_with_all_params.tag, 'div')
        self.assertEqual(self.node_with_all_params.value, 'content')
        self.assertEqual(len(self.node_with_all_params.children), 1)
        self.assertEqual(self.node_with_all_params.children[0].tag, 'span')
        self.assertEqual(self.node_with_all_params.props, {
                         'class': 'my-class', 'id': 'my-id'})

    def test_initialization_with_no_params(self):
        self.assertIsNone(self.node_with_no_params.tag)
        self.assertIsNone(self.node_with_no_params.value)
        self.assertIsNone(self.node_with_no_params.children)
        self.assertIsNone(self.node_with_no_params.props)

    def test_initialization_with_some_params(self):
        self.assertEqual(self.node_with_some_params.tag, 'p')
        self.assertEqual(self.node_with_some_params.value, 'text')
        self.assertIsNone(self.node_with_some_params.children)
        self.assertIsNone(self.node_with_some_params.props)

    def test_props_to_html(self):
        node = HTMLNode(props={'class': 'my-class', 'id': 'my-id'})
        expected_props_string = ' class="my-class" id="my-id" '
        self.assertEqual(node.props_to_html(node.props), expected_props_string)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        expected_props_string = ' '
        self.assertEqual(node.props_to_html(node.props), expected_props_string)

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        expected_props_string = ' '
        self.assertEqual(node.props_to_html(
            node.props or {}), expected_props_string)


if __name__ == '__main__':
    unittest.main()
