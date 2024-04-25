

import sys
def Sort(elements):
    if len(elements) <=1:
        return elements

    pivot = elements.pop()
    lower_elements = [item for item in elements if item <= pivot]
    higher_elements = [item for item in elements if item > pivot]


    return Sort(lower_elements) + [pivot] + Sort(higher_elements)

if __name__ == "__main__":
    elements = [2, 3, 10, 4, 5, 6, 9, 8, 7, 1,3,5,7,2,5,63,4,6,24,6457,34,2,7657,24,46,84,2,658,452,23,5,86,35,46]
    print(f"Unsorted elements: {elements}")
    sorted_elements = Sort(elements)
    print(f"Sorted elements: {sorted_elements}")
    sys.exit()