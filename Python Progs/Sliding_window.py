# Finding the Maximum Sum of a Subarray with Fixed Length k

def fn(arr, k):
    left = ans = curr = 0

    for right in range(len(arr)):
        # Add arr[right] to the current sum
        curr += arr[right]

        # If the window exceeds the desired length `k`, shrink from the left
        if right - left + 1 > k:
            curr -= arr[left]  # remove arr[left] from curr
            left += 1

        # Update ans to be the maximum sum found for any window of length `k`
        if right - left + 1 == k:
            ans = max(ans, curr)

    print(ans)


if __name__ == "__main__":
    fn(arr=[1,2,3,4,5], k=2)
