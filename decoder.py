import sys
import time

def decod(filePath, outputFormat):
    with open(filePath) as file:
        code = file.read()

        code = code.replace("A", "00").replace("G", "10").replace("C", "01").replace("T", "11")     
        bytes = []
        baseIndex = 0
        while baseIndex < len(code):
            bytes.append(int(code[baseIndex:baseIndex + 8], 2).to_bytes((len(code[baseIndex:baseIndex + 8]) +7) // 8, byteorder=sys.byteorder))
            baseIndex += 8

        decodedFile = open(filePath.split(".")[0] + "_decoded" + outputFormat, 'wb')
        for byt in bytes:
            decodedFile.write(byt)

def main():
    start = time.time()
    decod("ressources/dataset_encoded.txt", ".mp3")
    end = time.time()
    print("running time : ", end - start)
    print("finit")


if __name__ == '__main__':
    main()