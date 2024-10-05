#!/usr/bin/env python3

import re

def remove_illegal_characters(text, illegal_chars):
    for char in illegal_chars:
        text = text.replace(char, '')
    return text

def main():
    text = input("Enter the text: ")
    
    # Check for illegal characters [a-f, 0-9]
    illegal_chars = re.findall(r'[^a-fA-F0-9]', text)
    if illegal_chars:
        print(f"Found {len(illegal_chars)} illegal characters: {', '.join(illegal_chars)}")
        choice = input("Do you want to delete them? (Y/N): ").lower()
        if choice == 'y':
            text = remove_illegal_characters(text, illegal_chars)
            print("Text after removing illegal characters:", text)

    # Check for [A-F] characters
    uppercase_chars = re.findall(r'[A-F]', text)
    if uppercase_chars:
        print(f"Found {len(uppercase_chars)} uppercase characters: {', '.join(uppercase_chars)}")
        choice = input("Do you want to delete them? (Y/N): ").lower()
        if choice == 'y':
            text = remove_illegal_characters(text, uppercase_chars)
            print("Text after removing uppercase characters:", text)
        else:
            choice = input("Do you want to convert uppercase to lowercase? (Y/N): ").lower()
            if choice == 'y':
                text = text.lower()
                print("Text converted to lowercase:", text)

if __name__ == "__main__":
    main()
