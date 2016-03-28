from eyetracking.models import GatheredData
import datetime

def countingPerMonth(usr):
    current_user = usr
    data = GatheredData.objects.filter(user = current_user)

    dataJanuary = data.filter(created_date__month = 1)
    totalJanuary = 0
    for gathereddata in dataJanuary:
        totalJanuary = totalJanuary + 1

    dataFebruary = data.filter(created_date__month = 2)
    totalFebruary = 0
    for gathereddata in dataFebruary:
        totalFebruary = totalFebruary + 1

    dataMarch = data.filter(created_date__month = 3)
    totalMarch = 0
    for gathereddata in dataMarch:
        totalMarch = totalMarch + 1

    dataApril = data.filter(created_date__month = 4)
    totalApril = 0
    for gathereddata in dataApril:
        totalApril = totalApril + 1

    dataMay = data.filter(created_date__month = 5)
    totalMay = 0
    for gathereddata in dataMay:
        totalMay = totalMay + 1

    dataJune = data.filter(created_date__month = 6)
    totalJune = 0
    for gathereddata in dataJune:
        totalJune = totalJune + 1

    dataJuly = data.filter(created_date__month = 7)
    totalJuly = 0
    for gathereddata in dataJuly:
        totalJuly = totalJuly + 1

    dataAugust = data.filter(created_date__month = 8)
    totalAugust = 0
    for gathereddata in dataAugust:
        totalAugust = totalAugust + 1

    dataSeptember = data.filter(created_date__month = 9)
    totalSeptember = 0
    for gathereddata in dataSeptember:
        totalSeptember = totalSeptember + 1

    dataOctober = data.filter(created_date__month = 10)
    totalOctober = 0
    for gathereddata in dataOctober:
        totalOctober = totalOctober + 1

    dataNovember = data.filter(created_date__month = 11)
    totalNovember = 0
    for gathereddata in dataNovember:
        totalNovember = totalNovember + 1

    dataDecember = data.filter(created_date__month = 12)
    totalDecember = 0
    for gathereddata in dataDecember:
        totalDecember = totalDecember + 1

	return(totalJanuary, totalFebruary, totalMarch, totalApril, totalMay, totalJune,
		   totalJuly, totalAugust, totalSeptember, totalOctober, totalNovember, totalDecember)
