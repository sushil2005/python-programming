score=int(input("enter your score:"))
if score>=90:
    grade='A+'
elif score>=85:
    grade='A-'
elif score>=80:
    grade='A'
elif score>=70:
        grade='B+'
elif score>=60:
    grade='b'
else:
    grade='F'
print(f"the students grade is:{grade}")