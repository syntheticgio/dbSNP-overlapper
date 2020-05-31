import csv
import vcf

vcf_reader = vcf.Reader(filename='00-common_all.vcf.gz', compressed=True, encoding='utf-8')

with open('universal_data.csv') as csvfile:
    windows = csv.reader(csvfile)
    j = 0
    for row in windows:
        if j == 0:
            j += 1
            continue
        i = 0
        for record in vcf_reader.fetch(row[0][3:], int(row[1]), int(row[2])):
            i += 1
        print("{},{},{},{}".format(row[0], row[1], row[2], i))
        
