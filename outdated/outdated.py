def main():
    date = date_format()
    if int(date[0]) < 10:
        date[0] = (f"0{date[0]}")
    if int(date[1]) < 10:
        date[1] = (f"0{date[1]}")
    print(f"{date[2]}-{date[0]}-{date[1]}")





def date_format():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                listed = date.split("/")
            elif "-" in date:
                 listed = date.split("-")
            else:
                listed = date.split(" ")
            if listed[0].isalpha and "," in date:
                try:
                    listed[0] = (months.index(listed[0].capitalize()) + 1)
                    listed[1] = listed[1].replace(",","")
                    if  listed[0] <=12 and int(listed[1]) <=31:
                        return listed
                except:
                    pass
            elif listed[0].isnumeric():
                try:
                    if  int(listed[0]) <=12 and int(listed[1]) <=31:
                        return listed
                except:
                    pass
            else:
                pass
        except EOFError:
            break

main()