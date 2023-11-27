filename = 'urls.txt'


def csv_reader(filename):
    file = open(filename, 'r')
    print(type(file))
    # print(file)
    # for row in file:
    #     print(row)
    result = file.read()
    # result = file.read().split("\n")
    print(type(result))
    return result


def my_gen(filename):
    with open(filename, 'r') as f:
        # breakpoint()
        for r in f:
            yield r
        #     print(r)

# print(type(my_gen(filename)))
# for line in my_gen(filename):
#     print(line)
# gen = my_gen(filename)
# try:
#     next.gen
# except StopIteration:
#     pass
file_list = csv_reader(filename)
print(file_list)
