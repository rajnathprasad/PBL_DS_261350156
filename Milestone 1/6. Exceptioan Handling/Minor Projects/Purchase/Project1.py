try:
    filename=input("Enter the file name: ")
    file=open(filename,"r")

    items=0
    free=0
    amount=0
    discount=0

    for line in file:
        line=line.strip()

        if line=="":
            continue

        data=line.split()

        if data[0].lower()=="discount":
            if len(data)>1:
                discount=int(data[1])
        elif data[1].lower()=="free":
            free+=1
        else:
            items+=1
            amount+=int(data[1])

    print("No of items purchased:",items)
    print("No of free items:",free)
    print("Amount to pay:",amount)
    print("Discount given:",discount)
    print("Final amount paid:",amount-discount)

    file.close()

except FileNotFoundError:
    print("File not found")
except Exception:
    print("Invalid data in file")