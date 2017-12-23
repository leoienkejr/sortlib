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


if __name__ == '__main__':
    pass
