class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self, props):
        props_string = ""
        for k, v in props.items():
            props_string += f' {k}=\"{v}\"'
        return props_string

    def __repr__(self):
        return f'''
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        children: {self.children}
        '''


# Custom class for nodes with no children
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node has no value")
        if self.tag is None:
            return str(self.value)
        if self.props == " ":
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'''
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        '''
