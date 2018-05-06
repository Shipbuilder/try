myTree = ['a',
		 ['b', ['d', [], []],
		 	   ['e', [], []]],
		 ['c', ['f', [], []], 
		       []]
		 ]

def BinaryTree(r):
	return [r, [], []]

def insert_left(root, newBranch):
	t = root.pop(1)
	if len(t) > 0:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root

def insert_right(root, newBranch):
	t = root.pop(2)
	if len(t) > 0:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
	return root

def get_root_val(root):
	return root[0]

def set_root_val(root, newVal):
	root[0] = newVal

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]

