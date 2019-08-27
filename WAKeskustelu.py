import bokeh
from bokeh.plotting import figure, show
from bokeh.io.output import output_file
class Viestit:
    date=[]
    time=[]

    
def main():
    viestit=Viestit()

    data=open("WA Data.txt", "r", encoding="utf-8")
    reader=data.readlines()

    result_months=[]
    result_times=[]
    parseDates(reader, viestit)
    for month in range(1,13):
            month=str(month)
            count=viestit.date.count(month)
            result_months.append(count)
    parseTime(reader, viestit) 
    for hour in range(0,24):
        hour=str(hour)
        count=viestit.time.count(hour)
        result_times.append(count)    

    createFigures(result_months, result_times)
  
def createFigures(months, times):
    monthList=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    hourList=[]
    for hour in range(0,24):
        hour=str(hour)
        hourList.append(hour)
    figmonths=figure(x_range = monthList)
    figmonths.vbar(x= monthList, top=months, width=0.8)
    output_file("Frequency of messages.html")
    show(figmonths)
    figtimes=figure(x_range = hourList)
    figtimes.vbar(x= hourList, top=times, width=0.8)
    output_file("Times of messages.html")
    show(figtimes)
    
def parseDates(reader, viestit):

    for line in reader:
        try:
            line=line.split()
            line=line[0].split(".")
            viestit.date.append(line[1])
            
        except(IndexError):
            continue
        
            
def parseTime(reader, viestit):
    for line in reader:
        try:
            line=line.split()
            line=line[2].split(".")
            viestit.time.append(line[0])

            
        except(IndexError):
            continue

    
main()
