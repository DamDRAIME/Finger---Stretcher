# https://leetcode.com/problems/zigzag-conversion/

# Write the code that will take a string and make a zigzag conversion given a number of rows


def convert(s: str, numRows: int) -> str:
    d = numRows - 2
    m = [[] for _ in range(numRows)]
    i = 0
    for x in s:
        if i < numRows:
            m[i].append(x)
            i += 1
        elif i < numRows + d:
            m[numRows - (i - numRows + 2)].append(x)
            i += 1
        else:
            m[0].append(x)
            i = 1
    return "".join("".join(n) for n in m)
