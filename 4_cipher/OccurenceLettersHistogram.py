import sys


def printStars():
    for i in range(80):
        print("*", end ='')

    print();

def generateLettersAndZeroes():

    lettersToZeroesDict = {}
    for letter in getAlphabet():
        lettersToZeroesDict[letter] = 0
    return lettersToZeroesDict


def readContentFromFile(filePath):
    try:
        file = open(filePath)
        return file.read()
    except FileNotFoundError:
        printStars()
        print('ERROR: COULD NOT FIND FOLLOWING FILE <' + filePath + '>')
        printStars()
        return None

def getAlphabet():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'w', 'v', 'x', 'y', 'z']

def main():
    printStars()
    print('START: Generating histogram for letters a file: <<<' + sys.argv[1] + '>>>')
    printStars()

    fileContent = readContentFromFile(sys.argv[1])

    if fileContent is None or len(fileContent) == 0:
        printStars()
        print('File is empty! Cannot generate histogram!')
        printStars()
    else:
        lettersToValueDictionary = generateLettersAndZeroes()

        for character in fileContent:
            if character.lower() in lettersToValueDictionary:
                lettersToValueDictionary[character.lower()] += 1

        letterSum = sum(lettersToValueDictionary.values())
        
        printStars()
        print('DEBUG PURPOSES (letters count):')
        printStars()
        for key in lettersToValueDictionary.values():
            print(key)

        printStars()
        print('FINAL OUTPUT:')
        printStars()
        for keyLetter, value in lettersToValueDictionary.items():
            print("{}{:15d}  {:.2%}".format(keyLetter, value, value/letterSum))
        printStars()
        
if __name__ == "__main__":
    main()

