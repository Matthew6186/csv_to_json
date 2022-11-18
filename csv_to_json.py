import os.path
import csv
import json

FILENAME = './sample.csv'

def main():
    # csv2tsv_temperature()
    # csv2tsv_vital()
    csv2json_air()

def add_devid(head, tmparr):
    tmpstr = ""
    for i, ihead in enumerate(head):
        # tmpstr += "'" + str(ihead) + "':'" + str(tmparr[i]) + "',"
        # tmpstr += '"' + str(ihead) + '":"' + str(tmparr[i]) + '",'
        tmpstr += str(ihead) + ':' + str(tmparr[i]) + ','
        # tmpstr += str(ihead) + ':"' + str(tmparr[i]) + '",'
    tmpstr = tmpstr[:-1]

    return tmpstr

def csv2json_air():
    outarr = []
    strarr = []
    with open(FILENAME,"r") as f:
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
            # tmpstr = tmpstr[:-1]
            tmpstr = tmpstr[1:-2]
            if i == 0:
                # head = [row[0], row[1], row[2], row[3], row[4]]
                head = [row[0], row[1], row[2], row[3]]
                # head = [row[0][1:-1], row[1][1:-1], row[2][1:-1], row[3][1:-1]]
                # head = row
                strarr.append(head)
            else:
                tmpdevidstr = add_devid(head, tmparr)
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
                tmpdevidstr = add_devid(head, tmparr)
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
    main()