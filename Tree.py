class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p=self.parent
        while p:
            p=p.parent
            level+=1
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces+"|---" if self.parent else ''
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def electronincs_tree():
    root = TreeNode('Electronics')
    
    laptops = TreeNode('Laptops')
    laptops.add_child(TreeNode('HP'))
    laptops.add_child(TreeNode('Mac'))
    laptops.add_child(TreeNode('Dell'))
    
    
    mobiles = TreeNode('Mobiles')
    mobiles.add_child(TreeNode('Motorola'))    
    mobiles.add_child(TreeNode('Apple'))
    mobiles.add_child(TreeNode('Nokia'))
    
    
    tvs = TreeNode('TVs')
    tvs.add_child(TreeNode('Reconnect'))    
    tvs.add_child(TreeNode('LG'))
    tvs.add_child(TreeNode('Samsung'))
    
    root.add_child(laptops)
    root.add_child(mobiles)    
    root.add_child(tvs)
    
    return root


root = electronincs_tree()

root.print_tree()