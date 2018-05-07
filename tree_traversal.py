def preorder(t):
	'''前向遍历'''
    if t is None:
        return
    else:
        print(t.val)
        preorder(t.left)
        preorder(t.right)

def inorder(t):
	'''中序遍历'''
	if t is None:
		return
	else:
		inorder(t.left)
		print(t.val)
		inorder(t.right)

def postorder(t):
	'''后序遍历'''
	if t is None:
		return
	else:
		postorder(t.left)
		postorder(t.right)
		print(t.val)

def preorder_nonrec(t):
	'''前向非递归遍历'''
	stack = Stack()
	while t is not None or not stack.is_empty():
		while t is not None:
			print(t.val)
			stack.push(t.right) # 可以判断 t.right 是否为空优化空间复杂度 
			t = t.left
		t = stack.pop()

def inorder_nonrec(t):
	'''中向非递归遍历'''
	stack = Stack()
	while t is not None or not stack.is_empty():
		while t is not None:
			stack.push(t)
			t = t.left
		t = stack.pop()
		print(t.val)
		t = t.right

