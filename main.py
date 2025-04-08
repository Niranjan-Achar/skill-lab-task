def find_union_intersection(A, B):
    i = j = 0
    union = []
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            union.append(A[i])
            i += 1
        elif A[i] > B[j]:
            union.append(B[j])
            j += 1
        else:
            union.append(A[i])
            intersection.append(A[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < len(A):
        union.append(A[i])
        i += 1
    while j < len(B):
        union.append(B[j])
        j += 1

    # Remove duplicates from union
    union = sorted(set(union))

    return union, intersection

# Example usage
A = [1, 2, 4, 5, 6]
B = [2, 3, 5, 7]
union, intersection = find_union_intersection(A, B)

print("Union:", union)
print("Intersection:", intersection)
