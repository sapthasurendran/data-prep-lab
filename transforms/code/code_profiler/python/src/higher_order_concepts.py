from UAST import *

def extract_ccr(uast):
    """
    Calculates the code to comment ratio given an UAST object as input
    """
    if uast is not None:
        total_comment_loc = 0
        for node_idx in uast.nodes:
            node = uast.get_node(node_idx)
            if node.node_type == 'uast_comment':
                total_comment_loc += node.metadata.get("loc_original_code", 0)
            elif node.node_type == 'uast_root':
                loc_snippet = node.metadata.get("loc_snippet", 0)
        if total_comment_loc > 0:
            return loc_snippet / total_comment_loc
        else:
            return None 
    return None