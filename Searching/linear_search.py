"""
This is an implementation of linear search
"""


class LinearSearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, search):
        found = False

        # Linear search performs linear scan of the data
        for element in self.arr:
            if element == search:
                print(f'Element {search} found in the array')
                found = True
                break

        if not found:
            print(f'Element {search} not found in the array')


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    search = 5

    ls = LinearSearch(arr)
    ls.search(search)

    search = 99  # not present
    ls.search(search)


