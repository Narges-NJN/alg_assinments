# alg_assinments
This repository is for Data Structure Class assignments

##### First assignment : insertion sort, selection sort, binary search (iterative and recursive), fibonacci numbers


{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ba914115",
   "metadata": {},
   "source": [
    "## Insertion Sort"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3e1aa3d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 5, 6, 11, 12, 13, 16]\n"
     ]
    }
   ],
   "source": [
    "def insertion_sort(arr):\n",
    "    for i in range(1, len(arr)):\n",
    "        key = arr[i]\n",
    "        j = i-1\n",
    "        while j >= 0 and key < arr[j] :\n",
    "            arr[j + 1] = arr[j]\n",
    "            j -= 1\n",
    "        arr[j + 1] = key\n",
    " \n",
    "\n",
    "# Driver Code\n",
    "test_arr = [12, 11, 13, 5, 6, 1, 16, 4]\n",
    "insertion_sort(test_arr)\n",
    "print(test_arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31d1bce2",
   "metadata": {},
   "source": [
    "## Selection Sort"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e1128c29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 5, 6, 11, 12, 13, 16]\n"
     ]
    }
   ],
   "source": [
    "def selectionsort(arr):\n",
    "    for i in range(len(arr)):\n",
    "        min = i\n",
    "        for j in range (i+1, len(arr)):\n",
    "            if arr[min] > arr[j]:\n",
    "                min = j            \n",
    "        arr[i], arr[min] = arr[min], arr[i]\n",
    "                        \n",
    "# Driver Code\n",
    "test_arr = [12, 11, 13, 5, 6, 1, 16, 4]\n",
    "insertion_sort(test_arr)\n",
    "print(test_arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d81a389c",
   "metadata": {},
   "source": [
    "## Binary Search (iterative)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4d9778ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element is present at index  4\n"
     ]
    }
   ],
   "source": [
    "def binarySearch(arr, low, high, x):\n",
    "\n",
    "    while low <= high:\n",
    "\n",
    "        mid = low + (high - low) // 2\n",
    "\n",
    "        # Check if x is present at mid\n",
    "        if arr[mid] == x:\n",
    "            return mid\n",
    "\n",
    "        # If x is greater, ignore left half\n",
    "        elif arr[mid] < x:\n",
    "            low = mid + 1\n",
    "\n",
    "        # If x is smaller, ignore right half\n",
    "        else:\n",
    "            high = mid - 1\n",
    "\n",
    "    # If we reach here, then the element\n",
    "    # was not present\n",
    "    return -1\n",
    "\n",
    "# Driver Code\n",
    "arr = [ 5, 4, 2, 12, 8, 15 ]\n",
    "x = 8\n",
    "\n",
    "result = binarySearch(arr, 0, len(arr)-1, x)\n",
    "\n",
    "if result != -1:\n",
    "    print (\"Element is present at index % d\" % result)\n",
    "else:\n",
    "    print (\"Element is not present in array\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47915968",
   "metadata": {},
   "source": [
    "## Binary Search (recursive)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c20b9c55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element is present at index  2\n"
     ]
    }
   ],
   "source": [
    "def binarySearch(arr, low, high, x):\n",
    "\n",
    "    while low <= high:\n",
    "\n",
    "        mid = low + (high - low) // 2\n",
    "\n",
    "        # Check if x is present at mid\n",
    "        if arr[mid] == x:\n",
    "            return mid\n",
    "\n",
    "        # If x is greater, ignore left half\n",
    "        elif arr[mid] > x:\n",
    "            return binarySearch(arr, low, mid-1, x)\n",
    "  \n",
    "        # If x is smaller, ignore right half\n",
    "        else:\n",
    "            return binarySearch(arr, mid + 1, high, x)\n",
    "\n",
    "    # If we reach here, then the element\n",
    "    # was not present\n",
    "    return -1\n",
    "\n",
    "# Driver Code\n",
    "arr = [ 5, 4, 2, 12, 8, 15 ]\n",
    "x = 2\n",
    "\n",
    "result = binarySearch(arr, 0, len(arr)-1, x)\n",
    "\n",
    "if result != -1:\n",
    "    print (\"Element is present at index % d\" % result)\n",
    "else:\n",
    "    print (\"Element is not present in array\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43ac9131",
   "metadata": {},
   "source": [
    "## Fibonacci (recursive)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "025fa57c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "144\n"
     ]
    }
   ],
   "source": [
    "# fibonacci serie : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …\n",
    "# Fn = Fn-1 + Fn-2\n",
    "\n",
    "def Fibonacci(n):\n",
    "\n",
    "    if n < 0:\n",
    "        print(\"Incorrect input\")\n",
    "\n",
    "    # 0th number in fibonacci is 0\n",
    "    elif n == 0:\n",
    "        return 0\n",
    "\n",
    "    # first and second numbers in fibonacci are 1\n",
    "    elif n == 1 or n == 2:\n",
    "        return 1\n",
    "\n",
    "    else:\n",
    "        return Fibonacci(n-1) + Fibonacci(n-2)\n",
    "\n",
    "# Driver Code\n",
    "print(Fibonacci(12))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
