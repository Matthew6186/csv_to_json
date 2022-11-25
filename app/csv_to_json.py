import os.path
import csv
import json
import argparse

FILENAME = './sample.csv'
ROWOFJSON = 4

def main(args):
    # csv2tsv_temperature()
    # csv2tsv_vital()
    csv2json(args)

def create_devidstr(head, row):
    tmpstr = ""
    tmparr = []

    for j in range(ROWOFJSON):
        tmparr.append(str(row[j].replace('"','')))

    for i, ihead in enumerate(head):
        tmpkey = str(ihead).replace('"', '')
        tmpvalue = str(tmparr[i]).replace('"', '')
        tmpstr += '"' + tmpkey + '":"' + tmpvalue + '",'
    tmpstr = tmpstr[:-1]

    return tmpstr

def jsonstr_clean(jsonstrarr):
    jsonstrarr = [ jarr.replace('"','') for jarr in jsonstrarr ]
    jsonstrarr = [ jarr.replace('{','') for jarr in jsonstrarr ]
    jsonstrarr = [ jarr.replace('}','') for jarr in jsonstrarr ]

    jsonstrarr = [ jarr.replace(':','":"') for jarr in jsonstrarr ]
    jsonstrarr = [ '"' + jarr for jarr in jsonstrarr ]
    jsonstrarr = [ jarr + '"' for jarr in jsonstrarr ]

    tmpjsonstr = '{'
    for jarr in jsonstrarr:
        tmpjsonstr = tmpjsonstr + str(jarr) + ','
    tmpjsonstr = tmpjsonstr[:-1] + '}'

    return tmpjsonstr

def csv2json(args):

    strarr = []
    with open(args.filename,"r") as f:
        reader = csv.reader(f)
        head = []
        for i, row in enumerate(reader):

            if i == 0:
                for j in range(ROWOFJSON):
                    tmphead = str(row[j]).replace('"','')
                    head.append(tmphead)
                strarr.append(head)
            else:
                tmpstr = ""

                tmpdevidstr = create_devidstr(head, row)

                jsonstrarr = row[ROWOFJSON:]
                tmpjsonstr = jsonstr_clean(jsonstrarr)

                tmpstr = '{' + tmpdevidstr + ',"data_json":' + tmpjsonstr + '}'

                strarr.append(json.loads(tmpstr))

    print(strarr[0])
    print(strarr[1:3])

    prop_name = os.path.basename(FILENAME)
    outjson = {}
    outjson[prop_name] = strarr[1:]

    with open('./outdata.json','w') as f:
        json.dump(outjson, f, indent=4)
    
    return outjson

def csv2tsv_vital():
    outarr = []
    strarr = []
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONE)
        head = []
        for i, row in enumerate(reader):
            tmparr = []
            tmpjson = []
            tmpstr = ""
            tmpdevidstr = ""
            tmparr.append(row[0])
            tmparr.append(row[1])
            tmparr.append(row[2])
            tmparr.append(row[3])
            tmparr.append(row[4:])
            outarr.append(tmparr)
                        
            tmpjson = row[4:]
            for item in tmpjson:
                tmpstr += str(item[:]) + ","
            tmpstr = tmpstr[:-1]
            if i == 0:
                # head = [row[0], row[1], row[2], row[3], row[4]]
                head = [row[0], row[1], row[2], row[3]]
                # head = row
                strarr.append(head)
            else:
                tmpdevidstr = create_devidstr(head, tmparr)
                # tmpdevidstr = "{" + tmpdevidstr + "}"
                # tmpjson0 = json.loads(tmpdevidstr)
                tmpstr = "{" + tmpdevidstr + ',"data_json":' + tmpstr + "}" 
                tmpjson = json.loads(tmpstr)
                strarr.append(json.loads(tmpstr))

    print(strarr[0])
    print(strarr[1:3])


    with open('./out.tsv', 'w', newline="") as f:
        writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(outarr)

    prop_name = os.path.basename(FILENAME)
    outjson = {}
    outjson[prop_name] = strarr[1:]

    with open('./outdata.json','w') as f:
        json.dump(outjson, f, indent=4)

def csv2tsv_temperature():
    outarr = []
    strarr = []
    with open('./iot_sample_data_from_db.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            tmparr = []
            tmpjson = []
            tmpstr = ""
            tmparr.append(row[0])
            tmparr.append(row[1])
            tmparr.append(row[2])
            tmparr.append(row[3])
            tmparr.append(row[4:])
            outarr.append(tmparr)
            tmpjson = row[4:]
            for item in tmpjson:
                tmpstr += str(item[:]) + ","
            tmpstr = tmpstr[:-1]
            if i == 0:
                strarr.append(tmpstr)
            else:
                strarr.append(json.loads(tmpstr))
    # print(outarr[0])
    # print(outarr[1])

    print(strarr[0])
    print(strarr[1:3])

    # d = json.loads(strarr[1])
    # pprint.pprint(d, width=40)

    outjson = {}
    outjson[strarr[0]] = strarr[1:]

    with open('./out.tsv', 'w', newline="") as f:
        writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(outarr)
        
    with open('./outdata.json','w') as f:
        json.dump(outjson, f, indent=4)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="convert csv file(includes json stirng) into complete json file")

    parser.add_argument('-n', '--filename', help='input csv filepath', type=str, required=True)

    args = parser.parse_args()

    main(args)