# Use the file name big.txt as the file name
fname = raw_input("Enter file name: ")  #use input("Enter file name: ") if u r using python3
fh = open(fname,'r')
count =0
total=0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue    
    num = line.split(" ")[1]

#taking floats from the file.

    for add in num:
        add = float(num)
        total = total +add
        count = count + 1
print "Average spam confidence:",total/count  #must use parenthesys if u r using python3
