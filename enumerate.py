# animals = ["cat", "dog", "pig", "scrim"]

# for index, animal in enumerate(animals, start=1):
#     # print(index)
#     print(f"{index}: {animal}")
    
# another example:
fruits = ["apple", "banana", "orange", "grape"]
# print(enumerate(fruits))
target = "orange"
for i, fruit in enumerate(fruits):
    if fruit == target:
        print(f"I found {target} at index {i}")
        print("I found", target, "at index", i)
        print("I found " + str(target) + " at index " + str(i))
        break