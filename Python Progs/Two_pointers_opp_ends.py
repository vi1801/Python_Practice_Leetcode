def fn(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0

    while left < right:
        # Calculate the area formed between left and right pointers
        height = min(arr[left], arr[right])
        width = right - left
        area = height * width

        # Update the maximum area found
        max_area = max(max_area, area)

        # Move the pointers based on the condition
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    print(max_area)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    fn(arr)
