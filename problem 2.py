#Find the most frequent element in a list without using built-in dictionary or counter functions.
def most(List):
    return max(set(List), key=List.count)

List = [2, 1, 2, 2, 1, 3]
print(most(List))
