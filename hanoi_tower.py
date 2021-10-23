def hanoi_tower(source, mid, dest, n):
    if n <= 0:
        return
    elif n == 1:
        print("Move Disk from", source, "to" , dest)
    else:
        hanoi_tower(source, dest, mid, n-1)
        print("Move Disk from", source, "to", dest)
        hanoi_tower(mid, source, dest, n-1)

# driver code
n = int(input("Enter the number of disks: "))
hanoi_tower('rod A','rod B','rod C',n)
