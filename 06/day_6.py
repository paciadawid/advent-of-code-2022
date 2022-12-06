with open("input.txt", "r") as f:
    datastream = f.read().strip()


def find_marker(sequence_length):
    for i, _ in enumerate(datastream[:-sequence_length]):
        if len(set(datastream[i:i + sequence_length])) == sequence_length:
            return i + sequence_length
    return False


# part 1
print(find_marker(4))

# part 2
print(find_marker(14))
