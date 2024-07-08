# FileAsCArray

FileAsCArray is a command-line tool designed to convert any file into a
C-style array, making it easier for developers to embed binary data directly into C or C++ source code.

## Usage

```
python file_as_c_array.py <file_path> [-o <output_path>]
```

* <file_path>: Path to the binary file to be converted.
* -o, --output (optional): Output file to write the C array. If not specified, the output will be printed to the console.