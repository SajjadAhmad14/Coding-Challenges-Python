#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        sys.exit("Invalid input")

    if len(sys.argv) == 3:
        option = sys.argv[1]
        file = sys.argv[2]
        if option == "-c":
            bytes = count_bytes(file)
            print(bytes, file)
        elif option == "-l":
            lines = count_lines(file)
            print(lines, file)
        elif option == "-w":
            words = count_words(file)
            print(words, file)
        elif option == "-m":
            chars = count_chars(file)
            print(chars, file)
        else:
            print("Invalid option")
    else:
        if sys.stdin.isatty():
            file = sys.argv[1]
            lines = count_lines(file)
            words = count_words(file)
            bytes = count_bytes(file)
            print(lines, words, bytes, file)
        else:
          option = sys.argv[1]
          content = sys.stdin.read()
          if option == "-l":
            print(content.count('\n'))
          elif option == "-w":
            print(len(content.split()))
          elif option == "-c":
            print(len(content.encode()))
          elif option == "-m":
            print(len(content) + content.count('\n'))
          else:
            sys.exit("Invalid option.")

def count_bytes(f):
  with open(f, 'rb') as file:
    return len(file.read())

def count_lines(f):
  with open(f, 'r') as file:
    return sum(1 for _ in file)

def count_words(f):
  with open(f, 'r') as file:
    return sum(len(line.split()) for line in file)

def count_chars(f):
  with open(f, 'r') as file:
    content = file.read()
    return len(content) + content.count('\n')

if __name__ == "__main__":
    main()
