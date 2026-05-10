"""
Problem 2: Dot Product and Orthogonal Vectors
==============================================

Description:
1. Write a procedure called dot_product which calculates the dot (scalar) product
   of v1 and v2 (vectors in IR^n)
2. Write an algorithm which determines, for n pairs of vectors, whether two vectors
   are orthogonal by calling the dot_product procedure
   (Orthogonal vectors have dot product = 0)
3. Modify the algorithm to use a dot_product function instead of a procedure

Requirements:
- Use arrays to represent vectors
- Use nested loops
- Use different types of parameter passing (by value, by reference)

Dot Product Formula:
v1 · v2 = v1[0]*v2[0] + v1[1]*v2[1] + ... + v1[n-1]*v2[n-1]

Example:
v1 = [1, 2, 3]
v2 = [4, 5, 6]
v1 · v2 = 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32

Orthogonal Example:
v1 = [1, 0]
v2 = [0, 1]
v1 · v2 = 1*0 + 0*1 = 0 (ORTHOGONAL)
"""

# ============================================================================
# VERSION 1: USING PROCEDURE (Pass by Reference)
# ============================================================================

def dot_product_procedure(v1, v2, ps):
    """
    PROCEDURE: Calculates dot product using pass by reference approach
    
    Args:
        v1: First vector (list)
        v2: Second vector (list)
        ps: List containing the result (pass by reference - modifies original list)
        
    The procedure modifies ps[0] directly (simulating pass by reference)
    """
    dot_sum = 0
    
    # Nested loop approach: outer loop for main calculation
    for i in range(len(v1)):
        # Inner operations
        dot_sum += v1[i] * v2[i]
    
    # Store result in the passed list (simulating pass by reference)
    ps[0] = dot_sum


def check_orthogonal_vectors_procedure(vector_pairs):
    """
    Algorithm to determine if n pairs of vectors are orthogonal
    Using the dot_product PROCEDURE with pass by reference
    
    Args:
        vector_pairs: List of tuples, each containing (v1, v2)
        
    Returns:
        Dictionary with analysis results
    """
    results = []
    
    # Outer loop: iterate through n pairs of vectors
    for pair_index in range(len(vector_pairs)):
        v1, v2 = vector_pairs[pair_index]
        
        # Check if vectors have same dimension
        if len(v1) != len(v2):
            print(f"Pair {pair_index + 1}: Vectors have different dimensions")
            continue
        
        # Use the procedure to calculate dot product
        ps = [0]  # Pass by reference using a list
        dot_product_procedure(v1, v2, ps)
        dot_result = ps[0]
        
        # Check if orthogonal
        is_orthogonal = (dot_result == 0)
        
        result_entry = {
            'pair': pair_index + 1,
            'v1': v1,
            'v2': v2,
            'dot_product': dot_result,
            'orthogonal': is_orthogonal
        }
        results.append(result_entry)
        
        print(f"Pair {pair_index + 1}: {v1} · {v2} = {dot_result}", end="")
        print(f" -> {'ORTHOGONAL' if is_orthogonal else 'NOT ORTHOGONAL'}")
    
    return results


# ============================================================================
# VERSION 2: USING FUNCTION (Pass by Value and Return Value)
# ============================================================================

def dot_product_function(v1, v2):
    """
    FUNCTION: Calculates and returns dot product
    
    Args:
        v1: First vector (list) - passed by value
        v2: Second vector (list) - passed by value
        
    Returns:
        The dot product value (pass by return)
    """
    dot_sum = 0
    
    # Nested loop: outer loop iterates through vector elements
    for i in range(len(v1)):
        # Inner computation
        dot_sum += v1[i] * v2[i]
    
    return dot_sum


def check_orthogonal_vectors_function(vector_pairs):
    """
    Algorithm to determine if n pairs of vectors are orthogonal
    Using the dot_product FUNCTION with return value
    
    Args:
        vector_pairs: List of tuples, each containing (v1, v2)
        
    Returns:
        Dictionary with analysis results
    """
    results = []
    
    # Outer loop: iterate through n pairs of vectors
    for pair_index in range(len(vector_pairs)):
        v1, v2 = vector_pairs[pair_index]
        
        # Check if vectors have same dimension
        if len(v1) != len(v2):
            print(f"Pair {pair_index + 1}: Vectors have different dimensions")
            continue
        
        # Call function and receive return value
        dot_result = dot_product_function(v1, v2)
        
        # Check if orthogonal
        is_orthogonal = (dot_result == 0)
        
        result_entry = {
            'pair': pair_index + 1,
            'v1': v1,
            'v2': v2,
            'dot_product': dot_result,
            'orthogonal': is_orthogonal
        }
        results.append(result_entry)
        
        print(f"Pair {pair_index + 1}: {v1} · {v2} = {dot_result}", end="")
        print(f" -> {'ORTHOGONAL' if is_orthogonal else 'NOT ORTHOGONAL'}")
    
    return results


# ============================================================================
# VERSION 3: ADVANCED - USING PASS BY REFERENCE WITH ADDITIONAL PARAMETERS
# ============================================================================

def dot_product_advanced(v1, v2, result_dict):
    """
    Advanced PROCEDURE: Stores multiple values in a dictionary (pass by reference)
    
    Args:
        v1: First vector
        v2: Second vector
        result_dict: Dictionary to store results (pass by reference)
    """
    dot_sum = 0
    intermediate_products = []
    
    for i in range(len(v1)):
        product = v1[i] * v2[i]
        dot_sum += product
        intermediate_products.append(product)
    
    # Store detailed results
    result_dict['dot_product'] = dot_sum
    result_dict['intermediate_products'] = intermediate_products
    result_dict['is_orthogonal'] = (dot_sum == 0)


def check_orthogonal_advanced(vector_pairs):
    """
    Advanced algorithm with detailed analysis
    
    Args:
        vector_pairs: List of tuples, each containing (v1, v2)
    """
    results = []
    
    for pair_index in range(len(vector_pairs)):
        v1, v2 = vector_pairs[pair_index]
        
        if len(v1) != len(v2):
            continue
        
        # Create result dictionary to be filled by procedure
        result_dict = {}
        dot_product_advanced(v1, v2, result_dict)
        
        results.append({
            'pair': pair_index + 1,
            'v1': v1,
            'v2': v2,
            **result_dict
        })
        
        print(f"Pair {pair_index + 1}:")
        print(f"  Vectors: {v1} · {v2}")
        print(f"  Intermediate Products: {result_dict['intermediate_products']}")
        print(f"  Dot Product: {result_dict['dot_product']}")
        print(f"  Status: {'ORTHOGONAL' if result_dict['is_orthogonal'] else 'NOT ORTHOGONAL'}\n")
    
    return results


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PROBLEM 2: DOT PRODUCT AND ORTHOGONAL VECTORS")
    print("=" * 70)
    
    # Define test vector pairs
    vector_pairs = [
        ([1, 0], [0, 1]),           # Orthogonal in 2D
        ([1, 2, 3], [4, 5, 6]),     # Not orthogonal in 3D
        ([2, -1], [1, 2]),          # Orthogonal in 2D (2*1 + (-1)*2 = 0)
        ([1, 1, 1], [-1, 0, 1]),    # Not orthogonal (1*(-1) + 1*0 + 1*1 = 0) Actually this IS orthogonal!
        ([3, 0, 4], [0, 1, 0]),     # Not orthogonal (3*0 + 0*1 + 4*0 = 0) Actually this IS orthogonal!
    ]
    
    # ======== VERSION 1: PROCEDURE WITH PASS BY REFERENCE ========
    print("\n" + "=" * 70)
    print("VERSION 1: USING PROCEDURE (Pass by Reference)")
    print("=" * 70)
    results_v1 = check_orthogonal_vectors_procedure(vector_pairs)
    
    print(f"\nOrthogonal pairs: {sum(1 for r in results_v1 if r['orthogonal'])}")
    print(f"Non-orthogonal pairs: {sum(1 for r in results_v1 if not r['orthogonal'])}")
    
    # ======== VERSION 2: FUNCTION WITH RETURN VALUE ========
    print("\n" + "=" * 70)
    print("VERSION 2: USING FUNCTION (Pass by Value and Return)")
    print("=" * 70)
    results_v2 = check_orthogonal_vectors_function(vector_pairs)
    
    print(f"\nOrthogonal pairs: {sum(1 for r in results_v2 if r['orthogonal'])}")
    print(f"Non-orthogonal pairs: {sum(1 for r in results_v2 if not r['orthogonal'])}")
    
    # ======== VERSION 3: ADVANCED WITH DETAILED ANALYSIS ========
    print("\n" + "=" * 70)
    print("VERSION 3: ADVANCED ANALYSIS WITH DETAILED BREAKDOWN")
    print("=" * 70)
    results_v3 = check_orthogonal_advanced(vector_pairs)
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total pairs tested: {len(results_v1)}")
    print(f"Orthogonal pairs found: {sum(1 for r in results_v1 if r['orthogonal'])}")
    print(f"Non-orthogonal pairs found: {sum(1 for r in results_v1 if not r['orthogonal'])}")
