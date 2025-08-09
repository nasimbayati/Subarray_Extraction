# Subarray Extraction and Modification Showcase
# Demonstrates extracting a subarray from a NumPy array as an independent array
# and modifying it without altering the original array. Also saves a picture
# of the original array and modified subarray as output.png for README use.

import numpy as np
import matplotlib.pyplot as plt


def extract_subarray(array: np.ndarray) -> np.ndarray:
    """
    Extracts a 3x2 subarray starting from row index 1 and column index 0.
    Returns a COPY so changes won't affect the original array.
    """
    return array[1:4, 0:2].copy()


def modify_subarray(subarray: np.ndarray) -> np.ndarray:
    """
    Modifies specific elements in the subarray to demonstrate independence.
    """
    subarray[0, 0] = "ww"
    subarray[2, 1] = "xx"
    return subarray


def save_tables_as_image(original: np.ndarray, subarray: np.ndarray, path: str = "output.png") -> None:
    """
    Renders the original array and the modified subarray as tables and saves to an image.
    """
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))

    # Original Array Table
    axes[0].axis("off")
    axes[0].table(cellText=original, loc="center", cellLoc="center")
    axes[0].set_title("Original Array")

    # Modified Subarray Table
    axes[1].axis("off")
    axes[1].table(cellText=subarray, loc="center", cellLoc="center")
    axes[1].set_title("Modified Subarray")

    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    # Create a 4x4 NumPy array
    my_array = np.array([
        ["00", "01", "02", "03"],
        ["10", "11", "12", "13"],
        ["20", "21", "22", "23"],
        ["30", "31", "32", "33"]
    ])

    print("Original Array:")
    print(my_array)

    # Extract subarray (independent copy)
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

    # Save a picture for README output section
    save_tables_as_image(my_array, modified_subarray, path="output.png")
    print('\nSaved visualization to "output.png".')
