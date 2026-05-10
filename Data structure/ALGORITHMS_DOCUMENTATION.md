/*
===============================================================================
ALGORITHM DOCUMENTATION - DATA STRUCTURES ASSIGNMENT
===============================================================================

PROBLEM 1: SUM OF DISTINCT ELEMENTS FROM TWO SETS
===============================================================================

PROBLEM STATEMENT:
Given two sets of elements, find the sum of all distinct elements.
Find the sum of all elements which are present in either of the given set
(but not in both).

INPUT: 
- Set1: Array of integers [n1 elements]
- Set2: Array of integers [n2 elements]

OUTPUT: 
- Sum: Integer representing sum of distinct elements

ALGORITHM:
-----------

FUNCTION SumDistinctElements(Set1[], Set2[])
BEGIN
    sum_distinct ← 0
    i ← 0
    j ← 0
    
    // Step 1: Process elements from Set1
    FOR i = 0 TO length(Set1) - 1 DO
        found ← FALSE
        FOR j = 0 TO length(Set2) - 1 DO
            IF Set1[i] = Set2[j] THEN
                found ← TRUE
                EXIT INNER LOOP
            END IF
        END FOR
        
        IF found = FALSE THEN
            sum_distinct ← sum_distinct + Set1[i]
            PRINT "Adding ", Set1[i], " from Set1"
        END IF
    END FOR
    
    // Step 2: Process elements from Set2
    FOR j = 0 TO length(Set2) - 1 DO
        found ← FALSE
        FOR i = 0 TO length(Set1) - 1 DO
            IF Set2[j] = Set1[i] THEN
                found ← TRUE
                EXIT INNER LOOP
            END IF
        END FOR
        
        IF found = FALSE THEN
            sum_distinct ← sum_distinct + Set2[j]
            PRINT "Adding ", Set2[j], " from Set2"
        END IF
    END FOR
    
    RETURN sum_distinct
END

TIME COMPLEXITY: O(n * m) where n = length(Set1), m = length(Set2)
SPACE COMPLEXITY: O(1)


EXAMPLE TRACE:
==============
Set1 = [3, 1, 7, 9]
Set2 = [2, 4, 1, 9, 3]

Step 1: Check Set1 elements
- 3: Found in Set2 → SKIP
- 1: Found in Set2 → SKIP
- 7: Not found in Set2 → ADD (sum = 7)
- 9: Found in Set2 → SKIP

Step 2: Check Set2 elements
- 2: Not found in Set1 → ADD (sum = 9)
- 4: Not found in Set1 → ADD (sum = 13)
- 1: Found in Set1 → SKIP
- 9: Found in Set1 → SKIP
- 3: Found in Set1 → SKIP

RESULT: sum = 13 ✓


===============================================================================
PROBLEM 2: DOT PRODUCT AND ORTHOGONAL VECTORS
===============================================================================

PROBLEM STATEMENT:
1. Write a procedure DOT_PRODUCT to calculate the dot product of two vectors
2. Write an algorithm to check if n pairs of vectors are orthogonal
3. Modify using a function instead of a procedure

MATHEMATICAL DEFINITION:
For vectors v1 and v2 in R^n:
v1 · v2 = Σ(v1[i] * v2[i]) for i = 0 to n-1

ORTHOGONAL CONDITION:
Two vectors are orthogonal if their dot product = 0


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROCEDURE VERSION (Pass by Reference)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROCEDURE DotProduct(v1[], v2[], ps)
// ps is passed by reference and will be modified
BEGIN
    product_sum ← 0
    i ← 0
    
    FOR i = 0 TO length(v1) - 1 DO
        product_sum ← product_sum + (v1[i] * v2[i])
    END FOR
    
    ps ← product_sum  // Modifies the original variable
END

ALGORITHM CheckOrthogonalVectorsProcedure(vector_pairs[], n)
// n = number of vector pairs
BEGIN
    pair_index ← 0
    dot_result ← 0
    
    FOR pair_index = 0 TO n - 1 DO
        v1 ← vector_pairs[pair_index].first
        v2 ← vector_pairs[pair_index].second
        
        // Check dimension compatibility
        IF length(v1) ≠ length(v2) THEN
            PRINT "Pair ", pair_index + 1, ": Dimension mismatch"
            CONTINUE
        END IF
        
        // Call procedure with pass by reference
        CALL DotProduct(v1, v2, dot_result)
        
        // Check if orthogonal
        IF dot_result = 0 THEN
            PRINT "Pair ", pair_index + 1, ": ORTHOGONAL"
        ELSE
            PRINT "Pair ", pair_index + 1, ": NOT ORTHOGONAL"
        END IF
    END FOR
END


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FUNCTION VERSION (Pass by Value and Return)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FUNCTION DotProduct(v1[], v2[]) → INTEGER
// v1 and v2 are passed by value
// Returns the dot product
BEGIN
    product_sum ← 0
    i ← 0
    
    FOR i = 0 TO length(v1) - 1 DO
        product_sum ← product_sum + (v1[i] * v2[i])
    END FOR
    
    RETURN product_sum
END

ALGORITHM CheckOrthogonalVectorsFunction(vector_pairs[], n)
// n = number of vector pairs
BEGIN
    pair_index ← 0
    dot_result ← 0
    
    FOR pair_index = 0 TO n - 1 DO
        v1 ← vector_pairs[pair_index].first
        v2 ← vector_pairs[pair_index].second
        
        // Check dimension compatibility
        IF length(v1) ≠ length(v2) THEN
            PRINT "Pair ", pair_index + 1, ": Dimension mismatch"
            CONTINUE
        END IF
        
        // Call function and receive return value
        dot_result ← DotProduct(v1, v2)
        
        // Check if orthogonal
        IF dot_result = 0 THEN
            PRINT "Pair ", pair_index + 1, ": ORTHOGONAL"
        ELSE
            PRINT "Pair ", pair_index + 1, ": NOT ORTHOGONAL"
        END IF
    END FOR
END

TIME COMPLEXITY: O(n × m) where n = number of pairs, m = vector dimension
SPACE COMPLEXITY: O(1)


EXAMPLE TRACE:
==============

Test Case 1:
v1 = [1, 0]
v2 = [0, 1]

DotProduct(v1, v2):
  i=0: product_sum = 0 + (1 * 0) = 0
  i=1: product_sum = 0 + (0 * 1) = 0
  RETURN 0

Result: ORTHOGONAL ✓ (dot product = 0)


Test Case 2:
v1 = [1, 2, 3]
v2 = [4, 5, 6]

DotProduct(v1, v2):
  i=0: product_sum = 0 + (1 * 4) = 4
  i=1: product_sum = 4 + (2 * 5) = 14
  i=2: product_sum = 14 + (3 * 6) = 32
  RETURN 32

Result: NOT ORTHOGONAL (dot product = 32 ≠ 0)


KEY DIFFERENCES:
================

PROCEDURE (Pass by Reference):
✓ Modifies original variable directly
✓ No return statement needed
✓ Memory efficient (no copy of return value)
✗ Side effects on caller's variables
✗ Less predictable behavior

FUNCTION (Pass by Value and Return):
✓ Pure function - no side effects
✓ Predictable and safer
✓ Return value explicitly clear
✗ Creates copy of parameters
✗ Slightly more memory overhead

PARAMETER PASSING METHODS DEMONSTRATED:
========================================
1. Pass by Value: Copies of v1 and v2 are passed to function
2. Pass by Reference: Original ps variable is modified by procedure
3. Return Value: Dot product is returned and assigned to caller's variable
4. Array Parameters: Vectors represented as arrays
5. Nested Loops: Outer loop for pairs, inner loop for vector elements

*/
