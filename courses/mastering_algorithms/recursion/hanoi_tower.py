def hanoi_tower(n, src, dst, tmp):
    if n > 0:
        hanoi_tower(n - 1, src, tmp, dst)
        print("Moving disk", n, "from", src, "to", dst)
        hanoi_tower(n-1, src,  tmp, dst)
    return


print(hanoi_tower(4, "A", "B", "C"))
