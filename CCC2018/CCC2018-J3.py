#CCC2018 J3
distances=input().split(" ")
#distance="3 10 12 5"
#distances=distance.split()
city=0
while city <5:
    output=""
    #calculate distance to first city
    loop=0
    while loop <= 4:
        
        if (city!=loop):
            if city < loop:
                counter=city
                total=0
                while counter <loop:
                    total+=int(distances[counter])
                    counter+=1
                output+=str(total)+" "
            else:
                counter=loop
                total=0
                while counter < city:
                    total+=int(distances[counter])
                    counter+=1
                output+=str(total)+" "
            
        else: 
            output+="0 "
        loop+=1
        #calculate distance to second city
    print(output[:len(output)-1])
    city+=1

    