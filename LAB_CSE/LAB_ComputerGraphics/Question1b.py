def test(text):
  result = []
  for x in text:
    if not result or result[-1] != x:
      result.append(x)
  return ''.join(result)


#text = "Yellowwooddoor"
text = input('Enter the text: ')
print("Remove repeated consecutive characters and replace with the single letters:")
print(test(text))
