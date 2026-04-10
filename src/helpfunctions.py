from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    

# create list of nodes to return
# loop over each of the nodes in old_nodes
#   if node is not PLAIN_TEXT type, append to return list and continue
#   use the .split() function to split the text of the node into a list on the delimeter argument and store into a new_list variable
#   loop over each item in the new_list
#       create TextNode instances for each item
#       if len(new_list) % 2 == 0, closing delimeter wasn't found - raise Exception("missing delimeter")
#       if string is empty, continue without creating a TextNode
#       else, it was surrounded by the delimeter and should be created as a TextNode with text_type argument type.
#       .append() the new TextNode to the return list
# return the list with all new TextNodes