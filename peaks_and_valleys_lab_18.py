# peaks_and_valleys_lab_18.py
def peaks(heights):
    peaks = []
    for i in range(1, len(heights) - 1):
        left = heights[i - 1]
        mid = heights[i]
        right = heights[i + 1]
        # print(i - 1, i, i + 1)
        # print(left, mid, right)
        # lines 8 and 9 are for the developer to check what's happening
        if left < mid > right:
            peaks.append(i)
    return peaks


def valleys(heights):
    valleys = []
    for i in range(1, len(heights) - 1):
        left = heights[i + 1]
        mid = heights[i]
        right = heights[i - 1]
        # print(i - 1, i, i + 1)
        # print(left, mid, right)
        # lines 8 and 9 are for the developer to check what's happening
        if left > mid < right:
            valleys.append(i)
    return valleys


def peaks_and_valleys(heights):
    p = peaks(heights)
    v = valleys(heights)
    p_and_v = p + v
    p_and_v.sort()
    return p_and_v


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(len(data))
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
