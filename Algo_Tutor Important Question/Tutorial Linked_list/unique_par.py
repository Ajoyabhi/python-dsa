def unique_pair(arr):
    unique_pairs = set()
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            pair = tuple(sorted((arr[i], arr[j])))
            unique_pairs.add(pair)

    return unique_pairs, len(unique_pairs)



if __name__ == '__main__':
    x = int(input())
    while(x!=0):
        pairs, len_pair = unique_pair(list(map(int, input().split())))
        # print(pairs, end="\n")
        print(len_pair)
        x -= 1


