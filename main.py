import plotly.figure_factory as pff
import statistics
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
dataReadingTime = df["reading_time"].tolist()

fig = pff.create_distplot([dataReadingTime], ["reading_time"], show_hist=False)
fig.show()

populationMean = statistics.mean(dataReadingTime)
print("Population Mean:- {}".format(populationMean))

def randomSetsOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(dataReadingTime))
        value = dataReadingTime[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFig(meanList):
    dataFrame = meanList
    figure = pff.create_distplot([dataFrame], ["reading_time"], show_hist=False)
    figure.show()      

def main():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetsOfMean(10)
        meanList.append(setOfMeans)
    showFig(meanList)
    samplingMean = statistics.mean(meanList)
    print("Sampling Mean :- {}".format(samplingMean))    

main()    