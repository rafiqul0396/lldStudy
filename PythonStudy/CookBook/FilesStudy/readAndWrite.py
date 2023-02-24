
# reading the files as single go file
with open("sample3.txt",'rt') as f:
    data=f.read()
    print(data)



print("_______________")
# Iterate over the lines of the file
with open('sample3.txt', 'rt') as f:
    for line in f:
        print(line)

# process line