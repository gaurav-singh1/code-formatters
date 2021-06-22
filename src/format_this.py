import pandas as pd


def addOne(_ser):
    return _ser.map(lambda x: x + 1)


datesSeries = pd.Series(
    [
        "2019-01-01",
        "2013-01-09",
        "2016-01-01",
        "2003-01-09",
        "2010-01-01",
        "2010-11-09",
    ]
)


print(datesSeries.head())


toAddOne = pd.Series([1, 2, 3, 4])


addedOne = addOne(toAddOne)

print(addOne(toAddOne).tolist())
