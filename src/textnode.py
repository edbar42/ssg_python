class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text_type = text_type
        self.text = text
        self.url = url

    def __eq__(self, text_node):
        match_tt = self.text_type == text_node.text_type
        match_text = self.text == text_node.text
        match_url = self.url == text_node.url
        return match_tt and match_text and match_url

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
