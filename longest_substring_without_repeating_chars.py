# Author: Apache X692 Attack Helicopter
# Created on: 29/06/2024
def longest_substring(s):
    max_len = 0
    start = 0
    char_map = {}

    for end in range(len(s)):
        if s[end] in char_map:
            start = max(char_map[s[end]] + 1, start)

        char_map[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len

def main():
    s = input("Enter a string: ")
    length = longest_substring(s)

    print(f"The longest substring without repeating characters is: {length}")

if __name__ == "__main__":
    main()
