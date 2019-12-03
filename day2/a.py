DEBUG = False

def process_instrs(instrs : list) -> list:
    ip = 0
    while(True):
        try:
            ip = process_instr(instrs, ip)
        except StopIteration:
            return instrs

def process_instr(instrs : list, ip : int) -> int:
    instr = instrs[ip]
    if instr in [1, 2]:
        posA = instrs[ip + 1]
        posB = instrs[ip + 2]
        st = instrs[ip + 3]
        op = (lambda x,y: x + y) if instr == 1 else (lambda x,y: x * y)
        instrs[st] = op(instrs[posA], instrs[posB])
    elif instr == 99:
        raise StopIteration()
    else:
        raise Exception("Unknown instruction %d" % instr)

    return ip + 4

def debug():
    inputs = {
        "1,0,0,0,99" : "2,0,0,0,99",
        "2,3,0,3,99" : "2,3,0,6,99",
        "2,4,4,5,99,0" : "2,4,4,5,99,9801",
        "1,1,1,4,99,5,6,0,99" : "30,1,1,4,2,5,6,0,99",
        "1,9,10,3,2,3,11,0,99,30,40,50" : "3500,9,10,70,2,3,11,0,99,30,40,50"
    }
    for i, (instrs, res) in enumerate(inputs.items()):
        result = process_instrs([int(i) for i in instrs.split(",")])

        if result != res.split(","):
            print("Test %d correct" % i)
        else:
            print("Test %d failed" % i)



if __name__ == "__main__":
    if DEBUG:
        debug()
    else:
        with open("inputA.txt") as fp:
            instrs = [int(i) for i in fp.read().split(",")]

        instrs[1] = 12
        instrs[2] = 2

        result = process_instrs(instrs)
        print(result)