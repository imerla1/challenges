def missing_num(lst):
    new_list = sorted(lst)
    try:
        for i, miss in enumerate(new_list):
            if new_list[i+1] - miss != 1:
                return miss + 1
    except:
        pass

print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))
