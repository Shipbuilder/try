def find_min_value(lst):
	small = lst[0]
	small_index = 0
	for i in range(1, len(lst)):
		if lst[i] < small:
			small = lst[i]
			small_index = i
	return small_index

def selection_sort(lst):
	'''
	简单排序采用最简单的策略：
	- 每次从数组中找出最小的元素
	- 循环遍历数组
	'''
	new = []
	for i in range(len(lst)):
		small_index = find_min_value(lst)
		new.append(lst.pop(small_index))
	return new


if __name__ == '__main__':
	print(selection_sort([1,3,2,4]))