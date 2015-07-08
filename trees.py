
class Node(object):

	def __init__(self, value, left, right):
		self.left = left
		self.right = right
		self.value = value

	def iterator(self):
		return BstIterator(self)


class BstIterator(object):
	
	def __init__(self, root):
		self.stack = [root]

	def has_next(self):
		return len(self.stack)

	def next(self):
		ret = self._pop_stack()

		if ret.right:
			self._push_stack(ret.right)

		if ret.left:
			self._push_stack(ret.left)
		
		return ret

	def _pop_stack(self):
		tmp = self.stack[len(self.stack) - 1]
		del(self.stack[len(self.stack) - 1])
		return tmp

	def _push_stack(self, item):
		self.stack.append(item)


def in_order_print(node):
	if node.left:
		in_order_print(node.left)
	
	print node.value
	
	if node.right:
		in_order_print(node.right)

def pre_order_print(node):
	print node.value

	if node.left:
		pre_order_print(node.left)

	if node.right:
		pre_order_print(node.right)

def post_order_print(node):
	if node.left:
		post_order_print(node.left)

	if node.right:
		post_order_print(node.right)

	print node.value
