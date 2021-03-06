import math

def factorial(n):
    r = 1
    for i in range (1, n + 1):
        r *= i
    return r

def get_perm(lst, perm):
    sz = len(lst)
    if sz == 1:
        return lst[0]
    fact = factorial(sz-1)
    if (perm >= fact*sz):
        perm -= sz
    first = math.floor(perm/fact)
    lstnew = lst[:]
    lstnew.remove(lstnew[first])
    if perm >= fact:
        perm -= fact
    return str(lst[first]) + str(get_perm(lstnew, perm))

def main():
    sz = int(input("Enter the size of the list: "))
    perm = int(input("Enter the permutation number: "))
    maxperm = factorial(sz)
    if perm > maxperm:
        print("The maximum permutation for a list of size", sz, "is", maxperm)

    numlist = list(range(1,sz+1))
    permstr = get_perm(numlist, perm)
    print("Permutation number", perm, "is", permstr)

if __name__ == "__main__":
    main()
