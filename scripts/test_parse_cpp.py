import sys
import clang.cindex

def find_typerefs(node, typename):
    """Find all references to the type named 'typename'
    """
    if node.kind.is_reference():
        ref_node = node.get_definition()
        if ref_node.spelling == typename:
            print 'found %s [line=%s, col=%s]' % (
                typename, node.location.line, node.location.column
            )

    # recurse for children of this node
    for c in node.get_children():
        find_typerefs(c, typename)

if __name__=="__main__":
    index = clang.cindex.Index.create()
    tu = index.parse(sys.argv[1])
    print "Translation unit: ",  tu.spelling
    find_typerefs(tu.cursor, sys.argv[2])
