#!/usr/bin/env python3
"""The Most Shameless Lie — single confession entry.

Writes the one-line confession to /output/entry.txt and prints it.
"""
import os

ENTRY = "I backed it up."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)

if __name__ == "__main__":
    main()
