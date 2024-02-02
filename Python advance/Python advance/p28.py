def getMonth():
    month=int(input("enter month number betn(1-12):"))
            if month<1 or month>12:
              raise ValueErrro("Invalid month value")
        return month
