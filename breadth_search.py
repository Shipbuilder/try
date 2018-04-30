from collections import deque

def find_the_right_person(name):
	return name[-1] == 'm'

def breadh_search(name):
	'''
	从某人的社交网络中寻找关系最近的目标对象
	'''
	search_queue = deque()
	search_queue += gragh[name]
	searched = [] # 已查找的姓名名单,避免出现死循环
	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if find_the_right_person(person):
				print('Yes')
				return True
			else:
				search_queue += gragh[person]
				searched.append(person)
	print('No')
	return False
