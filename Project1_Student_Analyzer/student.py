marks=[]
passed=True
for i in range(5):
    mark=int(input(f"enter marks for subject{i+1}: "))
    marks.append(mark)
total=sum(marks)
avg=total/len(marks)
percentage=(total/500)*100
print("Total Marks:",total)
print("Average Marks:",avg)
print("Percentage:",percentage)
for mark in marks:
    if mark<40:
        passed=False
if passed:
    print("Result:Pass")
else:
    print("Result:Fail")
if avg>=90:
    print("Grade : A")
elif avg>=70:
    print("Grade : B")
elif avg>=55:
    print("Grade : C")
else:
    print("Grade : D")
highest=marks[0]
lowest=marks[0]
for mark in marks:
    if mark>highest:
        highest=mark
    if mark<lowest:
        lowest=mark
print("Highest:",highest)
print("Lowest:",lowest)