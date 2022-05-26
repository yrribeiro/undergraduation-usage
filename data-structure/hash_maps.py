class HashMap:
    def __init__(self, MAX):
        self.MAX = MAX
        self.arr = [[] for _ in range(self.MAX)]

    def get_idx(self, key):
        sum = 0
        for ch in key:
            sum = sum + ord(ch)

        return sum%self.MAX

    def __setitem__(self, key, value):
        idx = self.get_idx(key)
        # self.arr[idx] = value                         no collision treatment

        found = False
        for idy, element in enumerate(self.arr[idx]): # chaining method
            # breakpoint()
            if len(element) == 2 and element[0] == key:
                found = True
                self.arr[idx][idy] = (key, value)
                break

        if not found:
            self.arr[idx].append((key, value))

    def __getitem__(self, key):
        idx = self.get_idx(key)

        # return self.arr[idx]                    no collision treatment

        for element in self.arr[idx]: #           chaining method
            if len(element) == 2 and element[0] == key:
                return element[1]

    def __delitem__(self, key):
        idx = self.get_idx(key)
        # self.arr[idx] = None                    no collision treatment

        for idy, element in enumerate(self.arr[idx]): #           chaining method
            if len(element) == 2 and element[0] == key:
                del self.arr[idx][idy]
                break

if __name__ == '__main__':
    h = HashMap(12)

    h['richard grayson'] = 21
    h['wally west'] = 15
    h['kaldurahm'] = 410
    h['clark kent'] = 53
    # print(h.arr)
    # print('\n after deletion:')
    # del h['clark kent']

    h['drahcir nosyarg'] = 41
    h['yllaw tsew'] = 2
    h['mharudlak'] = 289

    for i in h.arr:
        print(i)
    print('\n after deletion:')
    del h['mharudlak']
    for i in h.arr:
        print(i)