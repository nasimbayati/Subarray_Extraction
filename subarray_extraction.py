# Subarray Extraction and Modification Showcase
# Demonstrates extracting a subarray from a NumPy array as an independent array
# and modifying it without altering the original array.

import numpy as np

def extract_subarray(array):
    """
    Extracts a 3x2 subarray starting from row index 1 and column index 0.
    The subarray is a copy, so changes to it won't affect the original array.
    """
    return np.array(array[1:4, 0:2])

def modify_subarray(subarray):
    """
    Modifies specific elements in the subarray.
    This demonstrates that the extracted array is independent of the original.
    """
    subarray[0][0] = 'ww'
    subarray[2][1] = 'xx'
    return subarray

if __name__ == "__main__":
    # Create a 4x4 NumPy array
    my_array = np.array([
        ['00', '01', '02', '03'],
        ['10', '11', '12', '13'],
        ['20', '21', '22', '23'],
        ['30', '31', '32', '33']
    ])

    print("Original Array:")
    print(my_array)

    # Extract subarray
    sub_array = extract_subarray(my_array)
    print("\nExtracted Subarray:")
    print(sub_array)

    # Modify subarray
    modified_subarray = modify_subarray(sub_array)
    print("\nModified Subarray:")
    print(modified_subarray)

    # Verify original array remains unchanged
    print("\nOriginal Array After Modification Attempt:")
    print(my_array)
