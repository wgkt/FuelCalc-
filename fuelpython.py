def main():
    print('Fuel Efficiency Calculator - Meghan Cowan - COSC 420')
 
    try:
        #Get starting point of odometer
        while True:
            oStart = input('What\'s status of starting odometer: ')
             
            if oStart == '': oStart = 0
             
            
            oStart = float(oStart)
             
            if oStart < 0:
                    print('Error, correct your odometer.\n')
            else:
                break
         
        #oStart to find total MPG for trip
        oLast = oStart         
        gLast = 0              
        legCount = 1
        legMPG = []
         
        #Gather Leg info
        raw = input('\nLeg #{}, What is the new odometer status and  how much gas been used?\n'.format(legCount))
         
        while raw !='':
             #divide input on space
            oTotal,gTotal = raw.split()
            oTotal = float(oTotal)
            gTotal = float(gTotal)                          
             
            legMPG.append(round((oTotal-oLast)/(gTotal-gLast),1))
             
            oLast = oTotal
            gLast = gTotal
             #increment legCount
            legCount = legCount+1
             
            raw = input('\nLeg #{}, What is the new odometer status and  how much gas been used?\n'.format(legCount))
     
         
        if legCount > 1:
            print('\nYour fuel efficiency is:')
             
            #legCount must be at least 1
            for i in range(legCount-1):
                print('Leg#{} has {} MPG.'.format(i+1,legMPG[i]))
                 
            #at end, find MPG total
            print('\nYour total MPG is',round((oTotal-oStart)/gTotal,2))
        else:
            print('\nNo result.')
         
    except ValueError:
        print('\nPlease correct your input.')
    except:
        print('\nError! Please try again.')
    
if __name__ =='__main__': main()


def BusRoute():
    path = "C:\\"
    ext = ".txt"

    lines = ""
    miles = 0
    prevmiles = 0
    milest = 0
    fuel = 0.0
    mpg = 0.0
    i = 0

    filename = input("Please enter the file name (no extension)").strip()

    inFile = open(path + filename + ext, "r")

    prevmiles, fuel = inFile.readline().split()
    prevmiles = float(prevmiles)
    fuel = float(fuel)

    for lines in inFile:
        miles, fuel = lines.split(" ")

        miles = float(miles)
        fuel = float(fuel)

        milest = miles - prevmiles

        prevmiles = miles

        miles += 1

        print("Since last stop:", float(milest), "miles")