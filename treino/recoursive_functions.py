# def bubble_sort(array):
#   if len(array) == 0:
#     return array

#   for idx in range(len(array) - 1):
#     if array[idx] > array[idx + 1]:
#       array[idx], array[idx + 1] = array[idx + 1], array[idx]

#   partial_list = array[:-1]
#   last_el = array[-1]

#   sorted_list = bubble_sort(partial_list)
#   sorted_list.append(last_el)
#   return sorted_list


# array = [4, 3, 6, 2, 7, 8, 2, 2, 1]
# print(bubble_sort(array))
def fatorial(num, fat):
  if fat == 1:
    return num
  
  calc = num * fat
  calc += fatorial(num, fat - 1)
  return calc


print(fatorial(3, 3))
