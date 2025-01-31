import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].value_counts()

colors_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [colors.Gray, colors.Cinnamon, colors.Black]
}

colors_data = pandas.DataFrame(colors_dict)
colors_data.to_csv("colors_data.csv", index=False)
