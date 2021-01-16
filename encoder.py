import sys
import time


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
        encodedFile = open(filePath.split(".")[0] + "_encoded.txt", 'w')
        while byte:
            rl = bin(int.from_bytes(byte, byteorder=sys.byteorder))[2:]
            if len(rl) > 8:
                print("wesh soucis")

            if len(rl) < 8:
                while len(rl) < 8:
                    rl = "0" + rl
            baseIndex = 0
            while baseIndex < len(rl):
                encodedFile.write(getBaseFromByte(rl[baseIndex:baseIndex+2]))
                baseIndex += 2

            byte = file.read(1)


def main():
    start = time.time()
    encode("ressources/dataset.mp3")
    end = time.time()
    print("running time : ", end - start)
    print("finit")


if __name__ == '__main__':
    main()