some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = []

for items in some_list:
  if some_list.count(items) > 1:
    if items not in duplicates:
      duplicates.append(items)
print(duplicates)






























# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)