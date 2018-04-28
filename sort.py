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

def quick_sort(lst):
	'''
	快速排序采用分而治之的策略：
	- 选取基准值，然后将其与数组其他值比较，分为两个子数组；
	- 对子数组进行上述操作。
	- 快速排序在最佳情况下的时间复杂度为nlogn
	- 快速排序在最差情况下的时间复杂度为n^2
	'''
	if len(lst) < 2:
		return lst
	else:
		piovt = lst[0]
		left_lst = [i for i in lst[1:] if i <= piovt]
		right_lst = [i for i in lst[1:] if i > piovt]
		return quick_sort(left_lst) + [piovt] + quick_sort(right_lst)

def quick_sort_opt(lst):
	'''
	优化空间复杂度
	'''
	if len(lst) < 2:
		return lst
	else:
		piovt = lst[0]
		piovt_index = 0
		index = 1
		while index <= len(lst) - 1:
			if lst[index] <= piovt:
				lst.insert(0, lst.pop(index))
				piovt_index += 1
			index += 1
		return quick_sort_opt(lst[:piovt_index]) + [piovt] + quick_sort_opt(lst[piovt_index + 1:])


if __name__ == '__main__':
	test_lst = [1, 3, 2, 4]
	print(quick_sort_opt(test_lst))

