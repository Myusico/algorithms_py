def longest_inc_length(l):
    seq = []
    for n in l:
        size = len(seq)
        if size == 0 or n > seq[size-1]:
            seq.append(n)
        elif n < seq[0]:
            seq[0] = n
        else:
            left = 0
            right = size-1
            mid = (left+right)//2
            while left+1 < right:
                if n > seq[mid]:
                    left = mid
                else:
                    right = mid
                mid = (left+right)//2
            seq[right] = n
    return len(seq)


def main():
    l = [int(x) for x in input().split()]
    print(longest_inc_length(l))


if __name__ == "__main__":
    main()
