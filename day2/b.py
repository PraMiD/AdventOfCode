from a import process_instrs

import copy

def diff(a, b):
    diffs = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs.append(i)

    return diffs

if __name__ == "__main__":
    with open("inputA.txt") as fp:
        instrs = [int(i) for i in fp.read().split(",")]

    original = copy.copy(instrs)

    for noun in range(100):
        for verb in range(100):
            instrs = copy.copy(original)
            instrs[1] = noun
            instrs[2] = verb

            try:
                if process_instrs(instrs)[0] == 19690720:
                    print(
                        "Noun: %d\nVerb: %d" % (
                            noun, verb
                        )
                    )
                    print("Solution: %d\n" % (noun * 100 + verb))
            except Exception:
                # invalid instruction generated
                pass
