import numpy as np

class Machine:
    def __init__(self):
        self.id = 0
        self.mlst=0
        self.mlft=0
        self.mwlm=list()
        self.mwlwm=0
        self.assigmentOperation=list()

class Operation:
    def __init__(self):
        self.id = 0
        self.machine = Machine()
        self.machineId = 0
        self.processingTime = 0.0
        self.oreleaseTime = 0
        self.ost = -1
        self.oft = 0

class Job:
    def __init__(self):
        self.id = 0
        self.operations = list()
        self.startTime = -1
        self.finishTime = 0
        self.dueDate=0


class Solution(Operation, Job, Machine):
    def __init__(self, problem):
        self.jobs = list()          #job set in solution
        self.order = list()      #solutin set in solution
        self.machines=list()        #machine set in solution
        for i in range(problem.nm):
            machine=Machine()       #define machine as class
            machine.id=i            #assign machine id
            machine.mlst=0          #machine last start time
            machine.mlft=0              #machine last finish time
            self.machines.append(machine)#add machine object to machines set
        '''for i in self.machines:
            print "machines \t", i.id,"\t",i.mlst,"\t",i.mlft'''
        totalNumberofOperations = 0
        for j in problem.jobs:
            sjob = Job()#define sjob as class
            sjob.id = j.id#assign job id
            sjob.dueDate=j.dueDate
            for o in j.operations:
                sop = Operation()#define sop as class
                sop.id = o.id#assign operation id
                m = Machine()
                sop.machine = m #define m as Solution Machine class
                sjob.operations.append(sop)#add operation object to sjob set
            totalNumberofOperations += len(sjob.operations)
            self.jobs.append(sjob)#add sjob set to solution jobs set










'''
def simulation(a, eList, ct, generation):
    notFinishO = list()
    AssignedOperation = list()
    eventlist = list()
    Mwlw = list()
    Amachine = list()
    for i in range(generation.nj):
        Amachine.append([i, 0])
    print Amachine
    for i in eList:
        eventlist.append(i)
    # eventList.sort(key=lambda tup: tup[2])
    print eventlist
    for i in a:
        for j in i.operations:
            notFinishO.append([i.id, j.id])
    preAllocation()
    # findNotFinishO(notFinishO,a,ct) is it necessary?

    while len(notFinishO) >= 1:
        ct = findNextTime(eventlist, AssignedOperation, ct)
        print "current time", ct
        LeastWaitingTimeAssignment(a, eventlist, ct, Amachine)
        break


def preAllocation():
    freeMachineSet = list()
    releasedOperationSet = list()


def findNotFinishO(notFO, a, ct):
    for i in notFO:
        pass


def findNextTime(a, AO, ct):
    y = min(a, key=lambda tup: tup[2])
    z = y[2]
    if z > ct:
        ct = z
        y[3] = ct
        AO.append(y)  # operasyonun atama zamani ct olarak degistirildi
    return ct


def findReleasedOperationSet(a):
    pass


def LeastWaitingTimeAssignment(a, eventlist, ct, Amachine):
    y = min(eventlist, key=lambda tup: tup[2])
    print "ilk eleman", y
    for i in a:
        if y[0] == i.id:
            for j in i.operations:
                if y[1] == j.id:
                    k = j.machineSet
                    x = 0  # index i tutabilmek icin
                    minp = 100000
                    for l in k:
                        if l.Mlft != 0:
                            wm1 = 1
                        else:
                            wm1 = 0
                        wm2 = l.Mwlwm
                        wm3 = j.processingTimes[x]
                        wm = wm1 + wm2 + wm3
                        print "makineid", l.id
                        x = x + 1
                        if wm < minp:
                            minp = wm
                            a = l.id

                        print "wm", wm
                    print "m.id", a
                    l.Mao.append([a, (str(i.id) + str(j.id))])
                    l.Mlst.append([a, y[3]])
                    print l.Mao, l.Mlst


ss = simulation(pr1.jobs, pr1.eventList, 0, pr1)
'''
