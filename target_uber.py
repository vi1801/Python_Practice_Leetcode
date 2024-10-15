def maxtarget(target):
    # Initialize an empty list
    list1 = []

    # Append the first element (edge case)
    if len(target) > 0:
        list1.append(target[0])

    # Loop through the middle elements to find local maxima
    for i in range(1, len(target) - 1):
        if target[i] > target[i - 1] and target[i] > target[i + 1]:
            list1.append(target[i])

    # Append the last element (edge case)
    if len(target) > 1:
        list1.append(target[-1])

    return list1


# Test case
if __name__ == "__main__":
    target = [1, 3, 1, 3, 2]
    print(maxtarget(target))
