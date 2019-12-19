testFile = open('test.txt', 'r')
testFileContent = testFile.read() #returns a string
testFile.close()
print(testFileContent)