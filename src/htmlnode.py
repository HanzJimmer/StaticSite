class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    #this string returns the props of a tag (e.g. href of a link)
    def props_to_html(self):
        temp_string = ""
        if self.props is None:
            return temp_string
        for prop in self.props:
            temp_string += f' {prop}="{self.props[prop]}"'

        return temp_string
    
    def __repr__(self):
        return f"Current Node:\ntag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props_to_html()}"


#this class is for the final nodes within a block of MD that has no additional internal HTML tags
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    #this function returns a string of HTML code
    def to_html(self):
        if self.value is None:
            raise ValueError("Missing node value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"Current Node:\ntag = {self.tag}\nvalue = {self.value}\nprops = {self.props_to_html()}"

#this class has children (or internal LeafNodes) that will be encapsulated in this Node's tag
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    #this function returns a string of HTML code including children nodes
    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag value")
        if not self.children:
            raise ValueError("Missing children!")
        full_string = f"<{self.tag}>"
        for child in self.children:
            full_string += child.to_html()

        full_string += f"</{self.tag}>"
        return full_string