def swappingFile(file1, file2):
    #Swapping File Started
    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1,'w') as c:
        c.write(data_b)

    with open(file2, 'w') as d:
        d.write(data_a)
    print("Swapped files succesfull, please check Thanks for using")


def inputBoxForSwap():
    file1Path = input("Please enter the name of you first file(Path):- ")
    file2Path = input("Please enter the name of your second file(Path):- ")
    swappingFile(file1Path, file2Path)
    print("Swapping files")

inputBoxForSwap()