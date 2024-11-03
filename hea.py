def heapify(A, n, i):
  """
  Heapify the subtree rooted at index i.

  Args:
      A: The array to heapify.
      n: The size of the array.
      i: The index of the root of the subtree to heapify.
  """
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  # If left child is larger than root
  if l < n and A[l] > A[largest]:
    largest = l

  # If right child is larger than largest so far
  if r < n and A[r] > A[largest]:
    largest = r

  # If largest is not root
  if largest != i:
    # Swap root with largest
    A[i], A[largest] = A[largest], A[i]

    # Recursively heapify the affected subtree
    heapify(A, n, largest)


def build_max_heap(A, n):
  """
  Build a max heap from the given array.

  Args:
      A: The array to build the max heap from.
      n: The size of the array.
  """
  # Start from the last non-leaf node and heapify all subtrees
  for i in range(n // 2 - 1, -1, -1):
    heapify(A, n, i)


def heap_sort(A, n):
  """
  Sort the given array in ascending order using heap sort.

  Args:
      A: The array to sort.
      n: The size of the array.
  """
  # Build a max heap from the array
  build_max_heap(A, n)

  # Extract elements from the heap one by one
  for i in range(n - 1, 0, -1):
    # Swap the root with the last element
    A[i], A[0] = A[0], A[i]

    # Heapify the reduced heap
    heapify(A, i, 0)

# Example usage
A = [5, 12, 3, 10, 1, 6, 2, 9]