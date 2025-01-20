#!/usr/bin/env python3
import sys
import os
import chardet

def main():
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit()
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
      print("no")
  else:
    file = sys.argv[1]
    handle_default_option(file)




def count_bytes(f):
  file_path = f
  with open(file_path, 'rb') as f:
    file_content = f.read()
    file_size_bytes = len(file_content)
  return file_size_bytes

def count_lines(f):
  file_path = f
  lines = 0
  with open(file_path, "r") as f:
    for _ in f:
      lines = lines + 1
  return lines

def count_words(f):
  file_path = f
  with open(file_path, "r") as f:
    word_count = 0
    for line in f:
      words = line.split()
      word_count += len(words)
    return word_count

def count_chars(f):
  file_path = f
  with open(file_path, "r") as f:
    content = f.read()
    newline_count = content.count('\n')
  return len(content) + newline_count

def handle_default_option(f):
  print()

if __name__=="__main__":
  main()
