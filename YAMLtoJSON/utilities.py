def convert_to_array():
    lines = []
    with open("temp.yaml", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            # line = line.strip() To be used only for v1
            lines.append(line)
    return lines

def count_leading_spaces_loop(line):
    count = 0
    for char in line:
        if char == ' ':
            count += 1
        else:
            break
    return count