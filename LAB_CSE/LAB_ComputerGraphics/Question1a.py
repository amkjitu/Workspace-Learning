def test(text):
    return ' '.join(sorted(text.split(), key=lambda c: c[0]))


#word = "Red Green Black White Pink"
word = input('Enter strings ')
print("Sort the said string based on its first character:")
print(test(word))

# word = "Calculate the sum of two said numbers given as strings."
# print("\nOriginal Word:", word)
# print("Sort the said string based on its first character:")
# print(test(word))

# word = "The quick brown fox jumps over the lazy dog."
# print("\nOriginal Word:", word)
# print("Sort the said string based on its first character:")
# print(test(word))