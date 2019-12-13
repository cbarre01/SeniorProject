def getDates():

    years = range(2010,2020)
    months = range(4,10)
    days = range(1,31)

    thirtydays = [4,6,9,11]
    thirtyonedays = [1,3,5,7,8,10,12]

    dates = []

    for curYear in years:
        for curMonth in months:
            if curMonth in thirtydays:
                 for curDay in range(1,31):
                      if len(str(curDay)) == 1:
                          curDay = "0" + str(curDay)
                      if len(str(curMonth)) ==1:
                          curMonth = "0" + str(curMonth)
                      curDate = str(curYear) +str(curMonth) +  str(curDay) + ", "
                      dates.append(curDate)
            if curMonth in thirtyonedays:
                 for curDay in range(1,32):
                      if len(str(curDay)) == 1:
                          curDay = "0" + str(curDay)
                      if len(str(curMonth)) ==1:
                          curMonth = "0" + str(curMonth)
                      curDate = str(curYear)+ str(curMonth) + str(curDay) + ", "
                      dates.append(curDate)
            elif curMonth == 2:
                 for curDay in range(1,29):
                      if len(str(curDay)) == 1:
                          curDay = "0" + str(curDay)
                      if len(str(curMonth)) ==1:
                          curMonth = "0" + str(curMonth)
                      curDate = str(curYear) + str(curMonth) + str(curDay) + ", "
                      dates.append(curDate)

    return(dates)

def toFile(list1):
    outFile = open("dates.txt","w")
    for str1 in list1:
        outFile.write(str1)



def main():
    toFile(getDates())


if __name__ == "__main__":
    main()
