#!/usr/bin/env python3
import sys
import os
import chardet

def main():
  if len(sys.argv) < 3 or len(sys.argv) > 3:
    sys.exit()

  option = sys.argv[1]
  file = sys.argv[2]
  if option == "-c":
    count_bytes(option, file)
  if option == "-l":
    count_lines(option, file)
  if option == "-w":
    count_words(option, file)


def count_bytes(o, f):
  file_path = f
  with open(file_path, 'rb') as f:
    file_content = f.read()
    file_size_bytes = len(file_content)
  print(file_size_bytes, file_path)

def count_lines(o, f):
  file_path = f
  count = 0
  with open(file_path, "r") as f:
    for _ in f:
      count = count + 1
  print(count, file_path)

def count_words(o, f):
  file_path = f
  with open(file_path, "r") as f:
    word_count = 0
    for line in f:
      words = line.split()
      word_count += len(words)
    print(word_count, file_path)

if __name__=="__main__":
  main()
