#The following code is tested in python version ---- Python v2.7.13

#Inputs to be used to find the optimization of the resources
Units = {"Large" : 10, "XLarge" : 20, "2XLarge" : 40 , "4XLarge" : 80, "8XLarge" : 160 , "10XLarge" : 320}
NewYork = {"Large" : 120, "XLarge" : 230, "2XLarge" :450 ,"4XLarge":774 , "8XLarge" : 1400, "10XLarge" : 2820 }
India = {"Large" : 140, "XLarge" : "null", "2XLarge" :413 ,"4XLarge":890 , "8XLarge" : 1300, "10XLarge" : 2970 }
China = {"Large" : 110, "XLarge" : 200, "2XLarge" :"null" ,"4XLarge":670 , "8XLarge" : 1180, "10XLarge" : "null" }

#Global variables 
ActualCost = 0
TempMachineList = []
MachineList = []

#sample input : "100 units for 5 hours"
Input = input()

#returns the list of machines capable of processing the given units
def get_list(Value):
    return [d for d in Units.keys()  if Units[d] <= Value]

#returns the cost and the number of machines required for a particular country and the remaining units to be processed by other machines
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
          #if there is no remaing units to be processed , checks if the cost is less than the previous set of machines
          if rem == 0:
            if NewCost < ActualCost or ActualCost == 0:
                ActualCost = NewCost
                TempMachineList.append((i, Value))
                MachineList = TempMachineList
                TempMachineList = []
            else:
                TempMachineList = []
          #if there is remaing units again repeats the process to find the optimized cost for the remaining units
          else:
           TempMachineList.append((i, Value))
           process(NewCost, ActualCost, rem, Country, Hour)
           
def optimize(Input) :
    InputList = Input.split() 
    if len(InputList) == 5: 
        [TotalUnits, _, _, Hour, _] = InputList
        #checks if the total unit given is multiple of 10 and the hour given is proper
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
