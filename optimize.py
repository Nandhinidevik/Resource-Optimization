Units = {"Large" : 10, "XLarge" : 20, "2XLarge" : 40 , "4XLarge" : 80, "8XLarge" : 160 , "10XLarge" : 320}
NewYork = {"Large" : 120, "XLarge" : 230, "2XLarge" :450 ,"4XLarge":774 , "8XLarge" : 1400, "10XLarge" : 2820 }
India = {"Large" : 140, "XLarge" : "null", "2XLarge" :413 ,"4XLarge":890 , "8XLarge" : 1300, "10XLarge" : 2970 }
China = {"Large" : 110, "XLarge" : 200, "2XLarge" :"null" ,"4XLarge":670 , "8XLarge" : 1180, "10XLarge" : "null" }

ActualCost = 0
TempMachineList = []
MachineList = []
Input = input()

def get_list(Value):
    return [d for d in Units.keys()  if Units[d] <= Value]
    
def get_cost(cost, AvailableUnit, RequiredUnit, Country, Hour):
    Value = RequiredUnit // Units[AvailableUnit]
    NewCost = cost + (Country[AvailableUnit] * Value * Hour)
    rem = RequiredUnit % Units[AvailableUnit]
    return NewCost, rem, Value
    
def process(cost, ActCost, Units, Country, Hour):
    global ActualCost
    global TempMachineList
    global MachineList
    ActualCost = ActCost
    List = get_list(Units)
    for i in List:
      if Country[i] != "null":
          NewCost, rem, Value= get_cost(cost, i, Units, Country, Hour)
          if rem == 0:
            if NewCost < ActualCost or ActualCost == 0:
                ActualCost = NewCost
                TempMachineList.append((i, Value))
                MachineList = TempMachineList
                TempMachineList = []
            else:
                TempMachineList = []
          else:
           TempMachineList.append((i, Value))
           process(NewCost, ActualCost, rem, Country, Hour)
           
def optimize(Input) :
    InputList = Input.split() 
    if len(InputList) == 5: 
        [TotalUnits, _, _, Hour, _] = InputList
        if int(TotalUnits) % 10 == 0 and int(Hour) > 0 :
            process(0,0,int(TotalUnits), NewYork, int(Hour))
            NewYorkRes = {"region":"New York","total_cost":"$"+str(ActualCost),"machines": MachineList}
            process(0,0,int(TotalUnits), India, int(Hour))
            IndiaRes = {"region":"India","total_cost":"$"+str(ActualCost),"machines": MachineList}
            process(0,0,int(TotalUnits), China, int(Hour))
            ChinaRes = {"region":"China","total_cost":"$"+str(ActualCost),"machines": MachineList}
            print({"Output":[NewYorkRes, IndiaRes, ChinaRes]})
        else: 
            print("Units should be multiple of 10 and the time in hour should be proper")
    else:
        print("Incorrect Input format")
        
optimize(Input)
