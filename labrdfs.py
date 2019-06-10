import csv

with open("URIs.csv", newline="", encoding="utf-8") as a, open("RDF.nt","w", encoding="utf-8") as b:
    reader = csv.reader(a)

    for line in reader:
        s, p, o = line
       
        if "l:" in o:
            if "Ώρα" in o:
                b.write("_:" + s[2:] + " <" + p + "> " + '"' + o[2:] + ':00' + '" .\n')
            else:
                b.write("_:" + s[2:] + " <" + p + "> " + '"' + o[2:] + '" .\n')
        else:
            
            b.write("_:" + s[2:] + " <" + p + "> <" + o + "> .\n")