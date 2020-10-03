from algorithms import Sorter
import random
import sys

FILENAME="merge_dupl.txt"

def main():
    results = []
    for i in range(7, 16):
        # for j in range(5):
        # array = [random.randint(-sys.maxsize, sys.maxsize) for x in range(2**i)]
        # array.sort()
        # array.sort(reverse=True)
        array = [random.randint(1, 3) for x in range(2**i)]
        size_results = ["size 2** " + str(i), ]
        sorter = Sorter()

        # sorter.selection_sort(array)
        # size_results.append(sorter.get_result())
        # sorter.insertion_sort(array)
        # size_results.append(sorter.get_result())
        sorter.merge_sort(array)
        size_results.append(sorter.get_result())
        # sorter.shell_sort(array)
        # size_results.append(sorter.get_result())

        results.append(size_results)

    for element in results:
        print(element)
    with open(FILENAME, "w") as f:
        for listitem in results:
            f.write('{}\n'.format(str(listitem)))


if __name__ == "__main__":
    main()
