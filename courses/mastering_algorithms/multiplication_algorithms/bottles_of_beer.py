def bottles_of_beer(n):
    for i in range(n, 0, -1):
        print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer,")
        print(
            "Take one down, pass it around, "
            + str(i - 1)
            + " bottles of beer on the wall"
        )
        print()
    print("No bottles of beer on the wall, no bottles of beer.")
    print("Go to the store, by some more, " + str(n) + " bottles of beer on the wall.")


print(bottles_of_beer(10))
