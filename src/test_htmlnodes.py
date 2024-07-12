import unittest

from htmlnodes import HTMLNode


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
        expected_props_string = ' class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(node.props), expected_props_string)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        expected_props_string = ''
        self.assertEqual(node.props_to_html(node.props), expected_props_string)

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        expected_props_string = ''
        self.assertEqual(node.props_to_html(
            node.props or {}), expected_props_string)


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node has no value")
        if self.tag is None:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html(self.props)}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'''
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        '''


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.node_with_tag_and_value = LeafNode(
            value='Hello', tag='p', props={'class': 'greeting'})
        self.node_with_value_only = LeafNode(value='World')
        self.node_with_no_value = LeafNode(value=None, tag='div')

    def test_initialization(self):
        self.assertEqual(self.node_with_tag_and_value.tag, 'p')
        self.assertEqual(self.node_with_tag_and_value.value, 'Hello')
        self.assertEqual(self.node_with_tag_and_value.props,
                         {'class': 'greeting'})

        self.assertEqual(self.node_with_value_only.tag, None)
        self.assertEqual(self.node_with_value_only.value, 'World')
        self.assertEqual(self.node_with_value_only.props, None)

    def test_to_html(self):
        self.assertEqual(self.node_with_tag_and_value.to_html(),
                         '<p class="greeting">Hello</p>')

        self.assertEqual(self.node_with_value_only.to_html(), 'World')

    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            self.node_with_no_value.to_html()

    def test_repr(self):
        expected_repr_with_tag = '''
        tag: p
        value: Hello
        props: {'class': 'greeting'}
        '''
        expected_repr_with_value_only = '''
        tag: None
        value: World
        props: None
        '''
        self.assertEqual(repr(self.node_with_tag_and_value).strip(),
                         expected_repr_with_tag.strip())
        self.assertEqual(repr(self.node_with_value_only).strip(),
                         expected_repr_with_value_only.strip())


if __name__ == '__main__':
    unittest.main()
