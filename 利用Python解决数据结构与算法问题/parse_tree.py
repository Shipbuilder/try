from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def buildParseTree(expr):
	expr = expr.split()
	binaryTree = BinaryTree('')
	stack = Stack()
	stack.push(binaryTree) # 避免空栈弹出时报错
	currentTree = binaryTree
	for i in expr:
		if i == '(':
			currentTree.insertLeft('')
			stack.push(currentTree)
			currentTree = binaryTree.getLeftChild()
		elif i not in ['+', '-', '*', '/', ')']:
			currentTree.setRootVal(int(i)) # 非数字int()就会报错
			currentTree = stack.pop()
		elif i in ['+', '-', '*', '/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			stack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = stack.pop()
		else:
			raise ValueError
	return binaryTree

def evaluate(parseTree):
	oper = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.turediv}
	leftChild = parseTree.getLeftChild()
	rightChild = parseTree.getRightChild()
	if leftChild and rightChild: # 解析树只存在都有值或都为None
		fn = oper[parseTree.getRootVal()]
		return fn(evaluate(leftChild), evaluate(rightChild))
	else:
		return parseTree.getRootVal()

