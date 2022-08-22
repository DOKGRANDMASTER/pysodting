import operator


def arithmetic_arranfer(*args):
    ops = {"+": operator.add, "-": operator.sub}
    for oper in args[0]:
        s = oper.split()
        print(s[0] + "\n" + s[1] + " " + s[2] + '\n' + "-----")
        if args[1]:
            result = ops[s[1]](int(s[0]), int(s[2]))
            print(str(result) + "\n")


arithmetic_arranfer(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)


""" def arithmetic_arranfer(start, base=None):

    for name in start:
        name = name.split()
        print(f"  {name[0]}")
        print(name[1], name[2])
        print("-"*10)
        if base != None:
            if name[1] == "+":
                sum = int(name[0])+ int(name[2])
                print(sum)
                print("\n")
            elif name[1] == "-":
                sum_1 = int(name[0]) - int(name[2])
                print(sum_1)
                print("\n")


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) """



