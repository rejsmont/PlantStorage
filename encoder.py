import sys



def getBaseFromByte(byte):
    if byte == "00":
        return "A"
    elif byte == "10":
        return "G"
    elif byte == "01":
        return "C"
    elif byte == "11":
        return "T"

def encode(filePath):
    with open(filePath, 'rb') as file:
        byte = file.read(1)
        encodedFile = open("encodedFile.txt", 'w')
        sequence = ""
        while byte:
            rl = bin(int.from_bytes(byte, byteorder=sys.byteorder))[2:]
            if len(rl) % 2 == 1:
                # print("ça passe")
                rl = "0" + rl

            if len(rl) == 1:
                # print("soucis")
                rl = "0" + rl
                # print(rl)
            baseIndex = 0
            # print("byte value : " +  rl)
            while baseIndex < len(rl):
                # print(rl[baseIndex:baseIndex+2])
                # print(baseIndex)
                encodedFile.write(getBaseFromByte(rl[baseIndex:baseIndex+2]))
                baseIndex += 2

            byte = file.read(1)

        # encodedFile.write(sequence)

        # print(content)



def main():
    encode("test1.txt")
    print("finit")


if __name__ == '__main__':
    main()