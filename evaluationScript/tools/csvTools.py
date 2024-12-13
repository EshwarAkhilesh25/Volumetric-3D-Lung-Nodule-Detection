import csv

def writeCSV(filename, lines):
    # with open(filename, "wb") as f:
    #     csvwriter = csv.writer(f)
    #     csvwriter.writerows(lines)
    with open(filename, "w", newline='', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(lines)

def readCSV(filename):
    lines = []
    # with open(filename, "rb") as f:
    #     csvreader = csv.reader(f)
    #     for line in csvreader:
    #         lines.append(line)
    with open(filename, "r", newline='', encoding='utf-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            lines.append(line)
    return lines



import csv


def tryFloat(value):
    try:
        value = float(value)
    except:
        value = value
    
    return value

def getColumn(lines, columnid, elementType=''):
    column = []
    for line in lines:
        try:
            value = line[columnid]
        except:
            continue
            
        if elementType == 'float':
            value = tryFloat(value)

        column.append(value)
    return column
