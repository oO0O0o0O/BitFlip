'''
Generates a copy of the input file with the bits flipped.
'''

from sys import argv

def main():
    # Load source data
    srcFile = open(argv[1], 'rb')
    data = bytearray(srcFile.read())

    # Flip Bits
    for i in range(len(data)):
        if (~data[i] < 0):
            data[i] = ~data[i] + 256
        else:
            data[i] = ~data[i]

    # Save output data
    outFile = open('out.txt', 'wb')
    outFile.write(data)

    # Cleanup
    srcFile.close()
    outFile.close()

main()
