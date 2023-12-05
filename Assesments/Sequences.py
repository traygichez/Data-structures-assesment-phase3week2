def remove_duplicates(input_sequence):
    output = []
    for i in input_sequence:
        if i not in output:
            output.append(i)
    return output

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]