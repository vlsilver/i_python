def mergeSort(arr):
	l = 0
	r = 0
	if len(arr) > 1:
		m = len(arr)//2
		L = arr[:m]
		R = arr[m:]
		mergeSort(L) # Khi gọi hàm như thê này thì id của arr và L giống nhau, sử dụng chung 1 ô dữ liệu khi kết quả trả về từ cuối function sẽ được tái sử dụng.
		mergeSort(R) # Khi gọi hàm như thê này thì id của arr và R giống nhau, sử dụng chung 1 ô dữ liệu khi kết quả trả về từ cuối function sẽ được tái sử dụng.
		i = 0
		j = 0
		k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			k += 1
			i += 1
		while j < len(R):			
			arr[k] = R[j]
			j += 1
			k += 1
		return arr
print(mergeSort([1,3,2,4,6,5]))
