import requests


def byNewConfirmed_key(covid19):
    return covid19["NewConfirmed"]


URL = "https://api.covid19api.com/summary"
covid19 = requests.get(URL)
covid19 = covid19.json()["Countries"]
exit = False
while not exit:
    choise = int(input(
        "Select action:\n 1. Show COVID19 information\n 2. Sort by new confirmed\n 3. Show COVID19 information by country\n 0. Exit\n: -->> "))
    if choise == 1:
        for item in covid19:
            print(f'{item["Country"]}:\n\tNew Confirmed: {item["NewConfirmed"]}\n\tTotal Confirmed: {item["TotalConfirmed"]}\n\tNew Deaths: {item["NewDeaths"]}\n\tTotal Deaths: {item["TotalDeaths"]}\n\tNew Recovered: {item["NewRecovered"]}\n\tTotal Recovered: {item["TotalRecovered"]}\n')
    elif choise == 2:
        new_list = sorted(covid19, key=byNewConfirmed_key, reverse=True)
        for item in new_list:
            print(f'{item["Country"]}:\n\tNew Confirmed: {item["NewConfirmed"]}\n\tTotal Confirmed: {item["TotalConfirmed"]}\n\tNew Deaths: {item["NewDeaths"]}\n\tTotal Deaths: {item["TotalDeaths"]}\n\tNew Recovered: {item["NewRecovered"]}\n\tTotal Recovered: {item["TotalRecovered"]}\n')

    elif choise == 3:
        find = False
        country = input("Enter the name of the country: ")
        for item in covid19:
            if item["Country"] == country.capitalize():
                print(f'{item["Country"]}:\n\tNew Confirmed: {item["NewConfirmed"]}\n\tTotal Confirmed: {item["TotalConfirmed"]}\n\tNew Deaths: {item["NewDeaths"]}\n\tTotal Deaths: {item["TotalDeaths"]}\n\tNew Recovered: {item["NewRecovered"]}\n\tTotal Recovered: {item["TotalRecovered"]}\n')
                find = True
                break
        if not find:
            print("Error! Wrong name.")
    elif choise == 0:
        exit = True
        print("Bye!")
    else:
        print("Wrong choise")
