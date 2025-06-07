import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m lolpython.main <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        sys.exit(1)

    print("File read successfully. Interpreter logic will be here.")

if __name__ == "__main__":
    main()