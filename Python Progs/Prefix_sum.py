def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])

    print(prefix)


if __name__ == "__main__":
    fn(arr=[3,1,4,1,5])
