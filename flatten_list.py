def flatten_list(array):
  flat_list = []

  
  # iterate through the array given
  for el in array:
    if isinstance(el, list):
      flat_list += flatten_list(el)
    else:
      flat_list.append(el)

  return flat_list

print(flatten_list([1, [2, [3, 4], 5], 6]))



