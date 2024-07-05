with open('text.txt', 'r') as reader: # with, as will close the file after the work/execution for the file is done,
# no need to write open and close in different lines, w for write the file, r for reading

    content = reader.readlines()
    reversed(content)
    #r = reversed(content)
    with open('text1.txt', 'w') as writer:
        for line in reversed(content):
            #writer.write(str(r))
            writer.write(line)

