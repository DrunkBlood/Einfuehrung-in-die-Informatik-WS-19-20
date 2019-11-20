big_tree= float(input("Groesster Baum: "))
def findSmallTree(tree):
    firstRule = tree - 34
    secondRule = (tree - 11) / 2.0
    if firstRule <= 0 and secondRule <= 0:
        return tree
    branch_1 = tree + 1
    branch_2 = tree + 1
    if firstRule > 0:
        branch_1 = findSmallTree(firstRule)
    if secondRule > 0:
        branch_2 = findSmallTree(secondRule)
    return min(branch_1,branch_2,tree)
print(findSmallTree(big_tree))