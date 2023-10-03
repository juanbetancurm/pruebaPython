import statistics
from collections import Counter

def modeValue(parametros):
    messageMode = ""
    freq_dist = Counter(parametros)
    max_freq = max(freq_dist.values())
    modes = [value for value, freq in freq_dist.items() if freq == max_freq]
    if max_freq == 1:
        messageMode = "there is no mode"      
    else:
        if len(modes) == 1:
            messageMode = f"the mode is {modes[0]}, the frequency of this value is {max_freq}"
        else:
            messageMode = f"the modes are these values: {','.join(map(str, modes))}, and they have a frequency of {max_freq} each one"
    
        
    return messageMode

def menuCalc():

    print("Welcome, this is your statistics calculator.")
    
    numeros = input("Please, write your values separated by commas: ")
    
    parametrosStr = (numeros.split(","))
    parametros = [int(y) for y in parametrosStr]

    numberValues = len(parametros)
    values = ','.join(map(str, parametros))
    sortedVals = ','.join(map(str, sorted(parametros)))
    totalSum = sum(parametros)
    average = statistics.mean(parametros)
    median = statistics.median(parametros)
    mode = modeValue(parametros)
    maximum = max(parametros) if numberValues > 0 else None
    minimum = min(parametros) if numberValues > 0 else None
    rangeV = maximum - minimum if numberValues > 0 else None
    standardDev = statistics.stdev(parametros) if numberValues > 1 else None
    variance = statistics.variance(parametros) if numberValues > 1 else None
    geoMean = statistics.geometric_mean(parametros) if numberValues > 0 else None

    print(f'''
            -----------------------------------------------------------------------------
            Here you have the results for your values: 
            You entered {numberValues} values.
            They are: {values}.
            When sorted, they appear as: {sortedVals}.
            The sum of these values is {totalSum}.
            The media (average) is {average}, the median is {median}, and {mode}.
            The largest value is {maximum} and the smallest is {minimum}, so the range is {rangeV}.
            The standard deviation is {standardDev}, the variance is {variance}, and the geometric mean is {geoMean}.
            I hope this helps you.
            -----------------------------------------------------------------------------
            ''')

#parametros = [1,5,3,8,2,9,9,9,1,2]
menuCalc()
