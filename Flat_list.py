list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]

flat = [ele for sublist in list_of_lists for ele in sublist]

print("flattened list: ", flat)