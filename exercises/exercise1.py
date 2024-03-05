# How to use Conditionals

large_text = ["Line " + str(i+1) for i in range(1000)]
list_all = []
test_list = []

for index, line in enumerate(large_text):
    test_list.append(line)
    if ((index + 1) % 25 == 0):
    # List1 = test_list.copy()
        list_all.append(test_list)
        test_list = []
print(list_all)