########### --- Exercise 6C --- #############
shopping_list = [
    "apple",
    "milk",
    "bread",
    "banana",
    "cheese",
    "avocado",
    "mango"
]

def find_long_items(shopping_list):
    new_shopping_list = []
    for item in shopping_list:
        if len(item) > 5:
            new_shopping_list.append(item)
    return new_shopping_list


new_shopping_list = find_long_items(shopping_list)
print(new_shopping_list)







#####################################
# Exercise: 6B

# shopping_list = [
#     "apple",
#     "milk",
#     "bread",
#     "banana",
#     "cheese",
#     "apple",
#     "milk"
# ]
#
# search_item = input("Enter item to search: ").lower()
#
#
# def analyzing_list(shopping_list, search_item):
#     count = 0
#
#     for item in shopping_list:
#             if item == search_item:
#                 count += 1
#     return count
#
#
# found = analyzing_list(shopping_list, search_item)
# count = analyzing_list(shopping_list, search_item)
#
# if count == 0:
#     print(f"{search_item} is not in the shopping list.")
# elif count == 1:
#     print(f"{search_item} appears 1 time.")
# else:
#     print(f"{search_item} appears {count} times.")


##############----Exercise6A----##########
# def analyze_list(shopping_list):
#     for item in shopping_list:
#        print(item)
#
#     if "milk" in shopping_list:
#         print("Milk is in the shopping list:")
#
#     count = len(shopping_list)
#     return count
#
# total_items = analyze_list(shopping_list)
# print(f"Total items: {total_items}")



