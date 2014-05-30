__author__ = 'dan'

import csv


class CSVParser:
    def __init__(self, file):
        self.file = file
        self.reader = csv.reader(file)



    def printFilesInCategory(self, category):

        rownum = 0
        files = []
        for row in self.reader:
            if rownum == 0:
                header = row
                header = header[0].replace('"','')
                header = header.split('\t')
                p = [i for i in range(len(header)) if header[i] == category]
                p = p[0]
            else:
                row = row[0].replace('"','')
                row = row.split('\t')
                if row[p] == '1':
                    files.append(row[-1])
            rownum += 1
        self.file.seek(0)
        return files


    def printCategoriesOfFile(self, filename):

        rownum = 0
        for row in self.reader:
            if rownum == 0:
                header = row
                header = header[0].replace('"','')
                header = header.split('\t')
            else:
                row = row[0].replace('"','')
                row = row.split('\t')

                if filename in row[-1]:
                    catList = []
                    for i in range(len(row)-1):
                        if row[i] == '1':
                            catList.append(header[i])
                    self.file.seek(0)
                    return catList

            rownum += 1
        self.file.seek(0)



if __name__ == '__main__':
	
	""" Path of annotations and database """
    filename = '/home/user/Magnatagtune/annotations_final.csv'
 
    file = open(filename, 'rb')
    mangaCSV = CSVParser(file)
    print 'Files with singer category'
    print mangaCSV.printFilesInCategory('singer')
    print 'Categories of burnshee_thornside-rock_this_moon-01-bad_bad_luck-117-146'
    print mangaCSV.printCategoriesOfFile('burnshee_thornside-rock_this_moon-01-bad_bad_luck-117-146')
