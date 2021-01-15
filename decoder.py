import sys

def decod(filePath):
    with open(filePath) as file:
        code = file.read()
        # for line in file:
            # code += str(line)

        code = code.replace("A", "00").replace("G", "10").replace("C", "01").replace("T", "11")     
        # print(code)
        bytes = []
        baseIndex = 0
        while baseIndex < len(code):
            print(code[baseIndex:baseIndex + 8])
            bytes.append(int(code[baseIndex:baseIndex + 8], 2).to_bytes((len(code[baseIndex:baseIndex + 8]) +7) // 8, byteorder=sys.byteorder))
            baseIndex += 8

        decodedFile = open("decodedFile.txt", 'wb')
        for byt in bytes:
            decodedFile.write(byt)

def main():
            decod("encodedFile.txt")
            print("finit")


if __name__ == '__main__':
    main()