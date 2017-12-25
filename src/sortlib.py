'''
sortlib.py

Sorting algorithms implemented in Python.
'''


def bubble_sort(seq):
    repeat = True
    while repeat:
        count = 0
        for i in range(0, len(seq) - 1):
            if seq[i] > seq[i + 1]:
                swap = seq[i]
                seq[i] = seq[i + 1]
                seq[i + 1] = swap
                repeat = True
                count = count + 1
        if count == 0:
            repeat = False
    return seq


def merge_sort(seq):
    def merge_lists(a, b):
        merged = []
        x, y = 0, 0
        while x < len(a) and y < len(b):
            if a[x] <= b[y]:
                merged.append(a[x])
                x += 1
            else:
                merged.append(b[y])
                y += 1
        merged += a[x:]
        merged += b[y:]
        return merged

    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge_lists(left, right)


if __name__ == '__main__':
    pass
