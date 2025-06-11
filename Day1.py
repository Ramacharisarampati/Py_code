def fatherfamily(savings, site):
    print("Savings:", savings, "Site Price:", site)

    if savings >= site:
        print("Buy")
    else:
        print("Family suggestion: Earn more money")


def closefriend(savings, site, location):
    print("Place:", location)

    if location == "airport road":
        print("Friend suggestion: Not a good place")
    elif location == "Sarjapur road":
        print("Friend suggestion: Good place")


def mysavings(earnings):
    savings = 1000000 + earnings
    site = 2500000
    location = "airport road"

    fatherfamily(savings, site)
    closefriend(savings, site, location)


def searchsite(location, pricing):
    sellingproperties = [
        {"airport road": "stree 123", "dim": "30*40", "pricing": 450000},
        {"airport road": "stree 124", "dim": "16*20", "pricing": 2500000}
    ]
    for i in sellingproperties:
        if i["pricing"] >= pricing:
            print(i)


def decidesite(khata, dim):
    documents = ["owner1", "owner2", "owner3", "owner4"]

    for i in documents:
        if i == "owner4":
            print(i)


# function calls
mysavings(earnings=1000000)
searchsite(location="airport road", pricing=2000000)
decidesite(khata="A", dim="30*40")
