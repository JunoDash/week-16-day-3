# Festival Inventory Disaster – Real‑World Python Collections Challenge
# Scenario
# You are hired as the Data Assistant for the Chicago Fall Music & Food Festival.
# The festival opens in 3 hours, but the digital system has scrambled the inventory lists, vendor data, and safety rules. Your job is to fix the data using Python lists, sets, and tuples.
# If you fail, the festival cannot legally open.

# Starting Data
foods = ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"]
stages = ("Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley")
restricted = {"glass bottles", "weapons", "alcohol", "alcohol"}
attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]

# Task 1 — Clean the Food Vendor List
    # 1. Remove duplicates while keeping only the first occurrence.
    # 2. Add "ramen" and "fried rice".
    # 3. Insert "smoothies" at index 2.
    # 4. Sort the list alphabetically.
    # 5. Print the final vendor list.
temp = []
for item in foods:
    if item not in temp:
        temp.append(item)
foods = temp

foods.append("ramen")
foods.append("fried rice")
foods.insert(2, "smoothies")
foods.sort()
print(foods)
#Task 1.5 
    # combine all the list into a nested list called festival_data
    #print out the new nested list(use a for loop to print each item on a new line)
festival_data = [foods, stages, attendance]
for i in festival_data:
    for x in i:
        print(x, end=" ")
# Task 2 — Stage Map
    # 1. Print the second stage
print(stages[1])
    # 2. Print the last two stages.
print(stages[-1], stages[-2])
    # 3. Convert the tuple into a list and add "Rock Arena".
stages = list(stages)
stages.append("Rock Arena")
    # 4. Convert it back into a tuple.
stages = tuple(stages)
# 5. Print the updated tuple.
print(stages)
# Task 3 — Restricted Items
    # 1. Add "fireworks".
restricted.add("fireworks")
    # 2. Try adding "weapons" again
restricted.add("weapons")
    # 3. Remove "alcohol".
restricted.discard("alcohol")
    # 4. Check if "glass bottles" is still restricted.
if "glass bottles" in restricted:
        print("Glass battles are still restricted.")
    # 5. Print the final restricted set.
print(restricted)
# Task 4 — Attendance Analysis
    # 1. Print the first three hours.
print(attendance[:3])
    # 2. Print the last hour.
print(attendance[-1])
    # 3. Print every 2nd hour.
print(attendance[::2])
    # 4. Remove the 5th hour using pop().
attendance.pop(4)
    # 5. Add five projected values using extend(range(...)).
attendance.extend(range(120, 125))
    # 6. Delete every 3rd value using del attendance[::3].
del attendance[::3]
    # 7. Print the length and cleaned list.
print(attendance)
# Task 5 — Festival Master List
    # 1. Convert vendors, restricted set, and stages into lists.
stages = list(stages)
restricted = list(restricted)
    # 2. Combine everything into festival_data.
festival_data = [foods, stages, restricted, attendance]
    # 3. Print: total items, first 10, last 10.
    # 4. Remove duplicates

    # 5. Print final cleaned festival_data.
print(festival_data)
# Extension
# Write a function festival_search(item) that returns True/False if item appears in festival_data.
