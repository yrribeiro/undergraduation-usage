class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_node_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        prefix = ' ' * self.get_node_level( ) * 2 + ('|--' if self.parent else '')
        print(f"{prefix}{self.data['name']} ({self.data['desig']})")
        if self.children:
            for child in self.children:
                child.print_tree()

root = TreeNode({'name': 'Nilupul', 'desig': 'CEO'})
cto = TreeNode({'name': 'Chinmay', 'desig': 'CTO'})
hr = TreeNode({'name': 'Gels', 'desig': 'Head of HR'})


infra = TreeNode({'name': 'Vishwa', 'desig': 'Head of Infrastructure'})
appli = TreeNode({'name': 'Aamir', 'desig': 'Application Manager'})

cto.add_child(infra)
cto.add_child(appli)

recr = TreeNode({'name': 'Peter', 'desig': 'Recruitment Manager'})
pol = TreeNode({'name': 'Waqas', 'desig': 'Policy Manager'} )

hr.add_child(recr)
hr.add_child(pol)

cloud = TreeNode({'name': 'Daval', 'desig': 'Cloud Manager'})
app = TreeNode({'name': 'Abhijit', 'desig': 'App Manager'})
infra.add_child(cloud)
infra.add_child(app)

root.add_child(cto)
root.add_child(hr)
root.print_tree()
