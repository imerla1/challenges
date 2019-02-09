def find_max_on_array(array):
    counter = 0
    maxes = []
    while counter < len(array):
        is_max = max(array[counter])
        counter+=1
        maxes.append(is_max)
    return maxes

print(find_max_on_array(array=array))
