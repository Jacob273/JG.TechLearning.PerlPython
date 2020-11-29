import os.path
import hashlib

def searchDuplicates(foldersList):
    
    dictionaryWithSizes = {}

    # Step 1: 
    printStars()
    print("STEP 1: Building list of dictionaries with same sizes: { {size}, [ path1, path2, path3, path4 ]")
    printStars()
    for folder in foldersList:
        if os.path.exists(folder):
            sizeAndPathsDictionary = buildSizeAndPathsDictionary(folder)
            mergeValuesWithSameKeys(dictionaryWithSizes, sizeAndPathsDictionary)
        else:
            print('Given path is NOT VALID: <<%s>>' %folder)
            return None

    # Step 2: 
    printStars()
    print("STEP 2: Verification (all files with sizes)")
    printStars()
    for key, value in dictionaryWithSizes.items():
        print("<K, V[]>", end = "  ")  
        print("[<"+ str(key) + ">,   " + str(value))
    
    printStars()


    # Step 3:
    printStars()
    print("STEP 3: Verification (files with same sizes only)")
    printStars()
    for key, value in dictionaryWithSizes.items():
        if len(value) > 1:
            print("<K, V[]>", end = "  ")  
            print("[<"+ str(key) + ">,   " + str(value))
    
    printStars()

    # Step 4: If there are more files of given size, we calculate hash for them
    print("STEP 4: Calculating hash")
    finalDuplicates = {}
    for listOfDuplicatedSizes in dictionaryWithSizes.values():
        if len(listOfDuplicatedSizes) > 1:
            sameHashesDictionary = buildListOfFilesWithSameHashes(listOfDuplicatedSizes)
            mergeValuesWithSameKeys(finalDuplicates, sameHashesDictionary)


    return finalDuplicates


def mergeValuesWithSameKeys(first, second):
    for key in second.keys():
        if key in first:
            newValue = first[key] + second[key]
            first[key] = newValue
        else:
            first[key] = second[key]

def buildSizeAndPathsDictionary(parentDirectory):
    sizeAndPathsDictionary = {}

    # iteratively going through all files
    for directoryName, subDirectories, fileNamesList in os.walk(parentDirectory): # os.walk() generates the file names in a directory tree by walking the tree either top-down
        for filename in fileNamesList:
            path = os.path.join(directoryName, filename)
            if not os.path.exists(path):
                continue
            fileSize = os.path.getsize(path)
            if fileSize in sizeAndPathsDictionary:
                sizeAndPathsDictionary[fileSize].append(path)
            else:
                sizeAndPathsDictionary[fileSize] = [path]
    return sizeAndPathsDictionary

def printStars():
    for i in range(80):
        print("*", end ='')

    print();

def buildListOfFilesWithSameHashes(fileList):
    
    sameHashes = {}
    
    for path in fileList:
        fileHashMD5 = hashFileWithMD5(path)
        if fileHashMD5 in sameHashes:
            sameHashes[fileHashMD5].append(path)
        else:
            sameHashes[fileHashMD5] = [path]

    return sameHashes

def hashFileWithMD5(path):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read()
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read()
    afile.close()
    
    return hasher.hexdigest()

def printResults(dictionaryToPrint):
    results = list(filter(lambda x: len(x) > 1, dictionaryToPrint.values()))
    if len(results) > 0:
        printStars()
        print(':::::Duplicated:::::')
        printStars()
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            printStars()

    else:
        print('No duplicate files found.')

def main():
    printStars()
    printStars()

    foldersList = ["C:\StudiaRemote\semestr_7\programowanie_jezyki_skryptowe", "C:\StudiaRemote\semestr_7\programowanie_jezyki_skryptowe_inny_folder"]
    
    print("STEP 0: Executing program that does search for duplicates for following folders:\n")
    for folder in foldersList:
        print(folder)
    
    printStars()
    printStars()


    duplicates = searchDuplicates(foldersList)

    for key, value in duplicates.items():
             print("duplicated hashes: <<<" + str(key) + ">>>  " + str(value))

if __name__ == "__main__":
    main()
