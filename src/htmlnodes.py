class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_string = ""
        for k, v in self.props.items():
            props_string += f' {k}="{v}"'
        return props_string

    def __repr__(self):
        return f"""
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        children: {self.children}
        """


# Custom class for nodes with no children
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node has no value")
        if self.tag is None:
            return str(self.value)

        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"""
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        """


# Custom class for nodes with children
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag associated with node")
        if self.children is None:
            raise ValueError("Parent node has no children")

        children_nodes = "".join([child.to_html() for child in self.children])

        props_string = self.props_to_html()

        return f"<{self.tag}{props_string}>{children_nodes}</{self.tag}>"
