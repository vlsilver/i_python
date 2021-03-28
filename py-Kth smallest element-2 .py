def get_top(lst):
   k = 3
   if k > (len(lst)/2):
      top_min = lst[0:k]
      for i in range(k,len(lst)):
         for n in range(len(top_min)-1,0,-1):
            if top_min[n] > top_min[n-1]:
               ch_ = top_min[n]
               top_min[n] = top_min[n-1]
               top_min[n-1] = ch_
         if lst[i] < top_min[0]:
            top_min[0] = lst[i]
      return max(top_min)
   else:
      k = len(lst) - k + 1
      top_max = lst[0:k]
      for i in range(k,len(lst)):
         for n in range(len(top_max)-1,0,-1):
            if top_max[n] < top_max[n-1]:
               ch_ = top_max[n]
               top_max[n] = top_max[n-1]
               top_max[n-1] = ch_
         if lst[i] > top_max[0]:
            top_max[0] = lst[i]
      return min(top_max)     

print(get_top([73,188,894,915,940,616,900,548]))