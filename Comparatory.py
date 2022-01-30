

import csv

def end():
    print("Mapping length doesn't match")

def compare(map1,map2):
    #remove spaces 
    map1 = map1.replace(' ','')
    map2 = map2.replace(' ','')
    # create mapping lists
    map1=list(map1)
    map2=list(map2)
    # turn values into integers
    mapping1 = [int(num) for num in map1]
    mapping2 = [int(num) for num in map2]
    # Hold Content
    fileContent1 = []
    filename = input("Enter file name: ")
    filename2 = input("Enter the second file name: ") 

    if len(mapping1) != len(mapping2):
        end()
        
    else:
        with open(filename,'r+')as file, open(filename2,'r+') as file2:
            csvfile = csv.reader(file, delimiter=',')
            csvfile2 = csv.reader(file2, delimiter=',')
            for row,row1 in zip(csvfile,csvfile2):
                count = 0
                for a, b in zip(mapping1,mapping2):
                    if len(row)-1 < a-1 or len(row1)-1 < b-1:
                        continue
                    if row[a-1] == row1[b-1]:
                        #print(row[a-1],row1[b-1])
                        count+= 1
                        if count == len(mapping1) - 1:
                            fileContent1.append(row)
                            count = 0
                        
               
                

    if fileContent1 == []:
        print("No Match")
    else:
        #print(fileContent1)
        with open('match.csv','w+') as file:
            for fileline in fileContent1:
                #print(fileline)
                line = ''
                for content in fileline:
                    line += content+','
                file.write(line+'\n')
        
    




compare('1 2 3 4','4 5 6 7')
