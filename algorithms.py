from time import time


class Sorter:
    def __init__(self):
        self.runtime = None
        self.comparison_num = 0
        self.type_of_last_result = None

    def selection_sort(self, array):
        print("Started selection sort")
        self.comparison_num = 0
        start = time()
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                if array[min] > array[j]:
                    min = j
                self.comparison_num += 1
            array[i], array[min] = array[min], array[i]
        self.runtime = time() - start
        self.type_of_last_result = "selection sort"
        return array

    def merge_sort(self, array):
        self.comparison_num = 0
        start = time()
        if len(array) > 1:
            half = len(array) // 2
            left_arr, right_arr = array[:half], array[half:]
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    array[k] = left_arr[i]
                    i += 1
                else:
                    array[k] = right_arr[j]
                    j += 1
                k += 1
            while i < len(left_arr):
                array[k] = left_arr[i]
                i, k = i + 1, k + 1
            while j < len(right_arr):
                array[k] = right_arr[j]
                j, k = j + 1, k + 1
        self.runtime = time() - start
        self.type_of_last_result = "merge sort"
        return array

    def insertion_sort(self, array):
        print("Started insertion sort")
        self.comparison_num = 0
        start = time()
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
                self.comparison_num += 1
            array[j + 1] = key
            self.comparison_num += 1
        self.runtime = time() - start
        self.type_of_last_result = "insertion sort"
        return array

    def shell_sort(self, array):
        print("Started shell sort")
        self.comparison_num = 0
        start = time()
        n = len(array)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while interval <= j and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                    self.comparison_num += 1
                self.comparison_num += 1
                array[j] = temp
            interval = interval // 2
        self.runtime = time() - start
        self.type_of_last_result = "shell sort"
        return array

    def get_result(self):
        return [self.type_of_last_result, self.runtime, self.comparison_num]

# "8128
# 32640
# 130816
# 523776
# 2096128
# 8386560
# 33550336
# 134209536
# 536854528
# null
# null"