N=input()
garden=input().split(" ")
popPlant=garden[0]

prevalence=garden.count(garden[0])
def compute(spikesPerPlant, curCount):
    global popPlant
    global prevalence
    popPlant=spikesPerPlant
    prevalence=curCount    
    
for spikesPerPlant in garden:
   
    curCount= garden.count(spikesPerPlant) 
    #print("spikes", spikesPerPlant, " prevalence ", curCount)
    if curCount > prevalence:
        compute(spikesPerPlant, curCount)
    elif curCount == prevalence and int(spikesPerPlant) < int(popPlant):
        compute(spikesPerPlant, curCount)

print(popPlant)
