import csv

def main():
    with open('Beijing.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile) 
        for row in csvreader:
            print(row)

if __name__ == "__main__":
    main()
