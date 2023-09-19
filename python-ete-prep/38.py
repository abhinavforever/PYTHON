# Write a user-defined function named Count() that will read the contents of text file
# named “Report.txt” and count the number of lines which starts with either “I‟ or “M‟ and
# displays the count.

def Count():
    with open("Report.txt","r") as f:
        count=0
        for line in f:
            line=line.upper()
            if line.startswith("I") or line.startswith("M"):
                count+=1
    return count
print(Count())