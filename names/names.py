import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# MacBook Pro (15-inch, 2017): runtime: 8.966019868850708 seconds
# Two nested loops result in a time complexity of O(n ^ 2)

# Approach 1: Failed approach. just read we can't use set.
# set_of_names_1 = set(names_1)
# duplicates = [name for name in names_2 if name in set_of_names_1]
# runtime: 0.005300045013427734 seconds

# Approach 2:  Tried 1; there are a few others // https://www.geeksforgeeks.org/python-intersection-two-lists/ 
# duplicates = [value for value in names_1 if value in names_2] 
# runtime: 1.8755018711090088 seconds

# Approach 3: Binary Tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else: 
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True 
        else:
            if target >= self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
            else: 
                if self.left:
                    return self.left.contains(target)
                else:
                    return False

nameTree = BSTNode("N")
for name in names_1:
    nameTree.insert(name)

for name in names_2:
    if nameTree.contains(name):
        duplicates.append(name)

# This is a 0(log n) solution.
# runtime: 0.1528627872467041 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
