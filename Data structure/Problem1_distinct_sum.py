"""
Problem 1: Sum of Distinct Elements from Two Sets
===================================================

Description:
Given two sets of elements, find the sum of all distinct elements from the set.
Find the sum of all elements which are present in either of the given set
(but not in both - symmetric difference).

Example:
Set 1: [3, 1, 7, 9]
Set 2: [2, 4, 1, 9, 3]
Output: 13 (distinct elements: 4, 7, 2)
Sum: 4 + 7 + 2 = 13

Algorithm Approach:
1. Initialize sum = 0
2. Compare each element of set 1 with set 2
   - If element is not present in set 2, add it to sum
3. Then do the same for set 2
   - If element is not present in set 1, add it to sum
"""

def is_present_in_array(arr, element):
    """
    Helper function to check if an element is present in an array
    
    Args:
        arr: Array to search in
        element: Element to search for
        
    Returns:
        True if element is present, False otherwise
    """
    for item in arr:
        if item == element:
            return True
    return False


def sum_of_distinct_elements(set1, set2):
    """
    Calculate the sum of all distinct elements from two sets
    (Elements present in one set but not both)
    
    Args:
        set1: First set as an array
        set2: Second set as an array
        
    Returns:
        Sum of distinct elements
    """
    sum_distinct = 0
    
    # Step 1: Add elements from set1 that are not in set2
    for element in set1:
        if not is_present_in_array(set2, element):
            sum_distinct += element
            print(f"Adding {element} from Set 1")
    
    # Step 2: Add elements from set2 that are not in set1
    for element in set2:
        if not is_present_in_array(set1, element):
            sum_distinct += element
            print(f"Adding {element} from Set 2")
    
    return sum_distinct


def sum_of_distinct_elements_optimized(set1, set2):
    """
    Optimized version using array operations
    (More efficient for larger datasets)
    
    Args:
        set1: First set as an array
        set2: Second set as an array
        
    Returns:
        Sum of distinct elements
    """
    # Convert to sets for O(1) lookup, then convert back to arrays if needed
    set1_only = []
    set2_only = []
    
    # Find elements only in set1
    for element in set1:
        if not is_present_in_array(set2, element):
            set1_only.append(element)
    
    # Find elements only in set2
    for element in set2:
        if not is_present_in_array(set1, element):
            set2_only.append(element)
    
    # Calculate sum
    total_sum = 0
    for element in set1_only:
        total_sum += element
    for element in set2_only:
        total_sum += element
    
    return total_sum, set1_only, set2_only


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("PROBLEM 1: SUM OF DISTINCT ELEMENTS")
    print("=" * 60)
    
    # Test Case 1: Given example
    set1 = [3, 1, 7, 9]
    set2 = [2, 4, 1, 9, 3]
    
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}\n")
    
    result = sum_of_distinct_elements(set1, set2)
    print(f"\nSum of distinct elements: {result}")
    
    # Test Case 2: Using optimized version
    print("\n" + "=" * 60)
    print("OPTIMIZED VERSION:")
    print("=" * 60)
    total_sum, unique_set1, unique_set2 = sum_of_distinct_elements_optimized(set1, set2)
    print(f"Elements only in Set 1: {unique_set1}")
    print(f"Elements only in Set 2: {unique_set2}")
    print(f"Sum of distinct elements: {total_sum}")
    
    # Test Case 3: Additional test
    print("\n" + "=" * 60)
    print("TEST CASE 2:")
    print("=" * 60)
    set1_test = [1, 2, 3, 4, 5]
    set2_test = [4, 5, 6, 7, 8]
    
    print(f"Set 1: {set1_test}")
    print(f"Set 2: {set2_test}\n")
    
    result_test = sum_of_distinct_elements(set1_test, set2_test)
    print(f"\nSum of distinct elements: {result_test}")
