expenses=['400','500','800','900','1000']
total=0
for i in expenses:
    total+=int(i)
    average=total/len(expenses)
    print("total",total)
    print("Average",average)
