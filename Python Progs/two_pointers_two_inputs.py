def fn(arr1, arr2):
    i = j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # Append remaining elements from arr1 if any
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # Append remaining elements from arr2 if any
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    print(ans)


if __name__ == '__main__':
    arr1 = [1,3,5,7]
    arr2 = [2,4,6,8]
    fn(arr1, arr2)
