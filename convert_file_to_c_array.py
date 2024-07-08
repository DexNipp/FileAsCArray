import sys
import os
import argparse

def convert_bin_to_c_array(file_path, output_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
    except IOError as e:
        print(f"Error: Could not open file '{file_path}'")
        return False

    base_name = os.path.splitext(os.path.basename(file_path))[0]

    output = [f"unsigned char {base_name}[{len(data)}] = {{\n"]

    for i in range(len(data)):
        if i % 8 == 0:
            output.append("    ")

        output.append(f"0x{data[i]:02x}")

        if i + 1 != len(data):
            output.append(",")

        if (i + 1) % 8 == 0 or i + 1 == len(data):
            output.append("\n")
        else:
            output.append(" ")

    output.append("};\n")
    output.append(f"unsigned int {base_name}_len = {len(data)};")

    output_str = ''.join(output)

    if output_path:
        try:
            with open(output_path, "w") as output_file:
                output_file.write(output_str)
        except IOError as e:
            print(f"Error: Could not write to file '{output_path}'")
            return False
    else:
        print(output_str)

    return True


def main():
    parser = argparse.ArgumentParser(description="Convert a binary file to a C-style array.")
    parser.add_argument("file_path", help="Path to the binary file.")
    parser.add_argument("-o", "--output", help="Output file to write the C array (prints to console if not specified).")

    args = parser.parse_args()

    if not convert_bin_to_c_array(args.file_path, args.output):
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()