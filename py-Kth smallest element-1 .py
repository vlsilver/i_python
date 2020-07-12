def get_top(lst,k):
   top_min = lst[0:k]
   i = k
   while i < len(lst):
      for n in range(len(top_min)-1,0,-1):
         if top_min[n] > top_min[n-1]:
            ch_ = top_min[n]
            top_min[n] = top_min[n-1]
            top_min[n-1] = ch_
         if lst[i] < top_min[0]:
            top_min[0] = lst[i]
   print(max(top_min))