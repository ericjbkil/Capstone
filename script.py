
#read and print out to new file the outputs that have different chosen semantic fields 
#   i.e. signs and symptoms, disease or syndrome...

#### Patient DB ####
#for report.pdf
ff = open("reportoutput.txt", "w")

with open("reportpheno", "r") as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Disease or Syndrome" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 1" # print the current line (stripped off whitespace)
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Congenital Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 2"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Sign or Symptom" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 3"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Acquired Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 4"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        else:
            current_line = line.rstrip()  + " was not used from index: " + str(index)
            print(current_line)



ff.close()


# remove first column (index)
f = open("reportoutput.txt", "r")
g = open("reportfixed.txt", "w")

for line in f:
    g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()

# removing duplicate lines
lines_seen = set() # holds lines already seen
with open("reportclean.txt", "w") as output_file:
	for each_line in open("reportfixed.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)




#for summary.pdf
ff = open("summaryoutput.txt", "w")

with open("summarypheno", "r") as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Disease or Syndrome" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 1" # print the current line (stripped off whitespace)
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Congenital Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 2"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Sign or Symptom" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 3"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Acquired Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 4"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        else:
            current_line = line.rstrip()  + " was not used from index: " + str(index)
            print(current_line)



ff.close()


# remove first column (index)
f = open("summaryoutput.txt", "r")
g = open("summaryfixed.txt", "w")

for line in f:
    g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()

# removing duplicate lines
lines_seen = set() # holds lines already seen
with open("summaryclean.txt", "w") as output_file:
	for each_line in open("summaryfixed.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)




#for neurology.pdf
ff = open("neurologyoutput.txt", "w")

with open("neurologypheno", "r") as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Disease or Syndrome" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 1" # print the current line (stripped off whitespace)
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Congenital Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 2"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Sign or Symptom" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 3"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Acquired Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 4"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        else:
            current_line = line.rstrip()  + " was not used from index: " + str(index)
            print(current_line)



ff.close()


# remove first column (index)
f = open("neurologyoutput.txt", "r")
g = open("neurologyfixed.txt", "w")

for line in f:
    g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()

# removing duplicate lines
lines_seen = set() # holds lines already seen
with open("neurologyclean.txt", "w") as output_file:
	for each_line in open("neurologyfixed.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)



##### Patient TC #####
#for app.pdf
ff = open("appoutput.txt", "w")

with open("apppheno.txt", "r") as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Disease or Syndrome" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 1" # print the current line (stripped off whitespace)
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Congenital Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 2"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Sign or Symptom" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 3"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Acquired Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 4"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        elif "Finding" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 5"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        else:
            current_line = line.rstrip()  + " was not used from index: " + str(index)
            print(current_line)



ff.close()


# remove first column (index)
f = open("appoutput.txt", "r")
g = open("appfixed.txt", "w")

for line in f:
    g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()

# removing duplicate lines
lines_seen = set() # holds lines already seen
with open("appclean.txt", "w") as output_file:
	for each_line in open("appfixed.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)








##### Patient MB #####
#for app.pdf
#for app.pdf
ff = open("appoutput.txt", "w")

with open("apppheno.txt", "r") as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Disease or Syndrome" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 1" # print the current line (stripped off whitespace)
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Congenital Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 2"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Sign or Symptom" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 3"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Acquired Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 4"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        elif "Finding" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 5"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        else:
            current_line = line.rstrip()  + " was not used from index: " + str(index)
            print(current_line)



ff.close()


# remove first column (index)
f = open("appoutput.txt", "r")
g = open("appfixed.txt", "w")

for line in f:
    g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()

# removing duplicate lines
lines_seen = set() # holds lines already seen
with open("appclean.txt", "w") as output_file:
	for each_line in open("appfixed.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)


#for clinhist.pdf
ff = open("clinhistoutput.txt", "w")

with open("clinhistpheno.txt", "r") as f:
    lines = f.readlines()  # read all lines into a list

    for index, line in enumerate(lines):  # enumerate the list and loop through it
        if "Disease or Syndrome" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 1" # print the current line (stripped off whitespace)
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Congenital Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 2"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Sign or Symptom" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 3"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff)
        elif "Acquired Abnormality" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 4"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        elif "Finding" in line:  # check if the current line has your substring
            current_line = line.rstrip()  + "Case 5"
            print(current_line)
            print(current_line, file=ff)
            #print("".join(lines[max(0,index):index]), file=ff) 
        else:
            current_line = line.rstrip()  + " was not used from index: " + str(index)
            print(current_line)



ff.close()


# remove first column (index)
f = open("clinhistoutput.txt", "r")
g = open("clinhistfixed.txt", "w")

for line in f:
    g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()

# removing duplicate lines
lines_seen = set() # holds lines already seen
with open("clinhistclean.txt", "w") as output_file:
	for each_line in open("clinhistfixed.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)







# performing statistical analysis of results
import statistics

nlpgenerated = []


#DB - confusion matrix, ROC 
TPdb = 22
FPdb = 4
TNdb = 0
FNdb = 3

SensitivityDB = TPdb / (TPdb + FNdb)
SensitivityDB
SpecificityDB = TNdb / (TNdb + FPdb)
SpecificityDB

#TC - confusion matrix, ROC
TPtc = 32
FPtc = 1
TNtc = 0
FNtc = 6

SensitivityTC = TPtc / (TPtc + FNtc)
SensitivityTC #0.84%
SpecificityTC = TNtc / (TNtc + FPtc)
SpecificityTC #0%


