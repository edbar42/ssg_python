class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self, props):
        props_string = " "
        for k, v in props.items():
            props_string += f'{k}=\"{v}\" '
        return props_string

    def __repr__(self):
        return f'''
        tag: {self.tag}
        value: {self.value}
        props: {self.props}
        children: {self.children}
        '''
