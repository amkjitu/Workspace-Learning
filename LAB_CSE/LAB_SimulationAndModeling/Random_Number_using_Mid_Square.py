from matplotlib import pyplot as plt

seed_number = int(input("Please enter a four-digit number:\n[####] "))
number = seed_number
already_seen = set()
counter = 0
ss = []
while number not in already_seen:
    counter += 1
    already_seen.add(number)
    number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
    ss.append(number)
    print(f"#{counter}: {number}")


print(f"We began with {seed_number} and"
      f" have repeated ourselves after {counter} steps"
      f" with {number}.")


print(ss)
plt.scatter(range(counter),ss)
plt.grid()
plt.show()