
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

def find_duplicate_keys(node, seen=None):
	if seen is None:
		seen = {}
	
	if not node.value in seen:
		seen[node.value] = 0

	seen[node.value] += 1

	if node.left:
		find_duplicate_keys(node.left, seen)
	
	if node.right:
		find_duplicate_keys(node.right, seen)

	k1 = None
	v1 = 0
	for k, v in seen.iteritems():
		if v > v1:
			k1 = k
			v1 = v
	return k1

if __name__ == '__main__':
	n1 = Node(5, None, None)
	n3 = Node(11, None, None)
	n2 = Node(10, None, n3)
	root = Node(5, n1, n2)

	print find_duplicate_keys(root)

