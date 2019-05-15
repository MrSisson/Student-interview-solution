import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('csv_json.py -i <path to inputfile> -o <path to outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('csv_json.py -i <path to inputfile> -o <path to outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    read_csv(input_file, output_file)

#Read CSV File
def read_csv(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file)

#Convert csv data into json and write it
def write_json(data, json_file):
    print(json.dumps(data, indent=4, sort_keys=True))
    with open(json_file, "w") as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))
        #parsed = json.loads(f)
    #print(json.dumps(parsed, indent=4, sort_keys=True))

if __name__ == "__main__":
   main(sys.argv[1:])
