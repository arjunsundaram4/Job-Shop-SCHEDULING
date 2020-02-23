import numpy as np
import jobSelection as JS
import TransformPermutaionToSolution as TS
import evaluation as EV
import nonDominatedSorting as NDS


class createSolution:

    def __init__(self, problem,solution,visitindex,GR,extraction):
        self.notReleasedOpSet = list()
        self.releasedOpSet = list()
        self.notFinishedOpSet = list()
        self.freeMahchinesSet = list()
        self.nextEventsSet = list()
       # self.EventsSet = list()
        self.machineWaitingList = list()
        self.machineEventSet = list()
        self.problem = problem
        self.solution=solution
        self.currentTime=0
        self.nextTime=0
        self.assignment=list()#it is necessary to hold assigned object
        self.lastAssigned=list()
        self.visitindex=visitindex
        self.GeneticRules=GR
        self.extraction=extraction
        print "createSolution.py"


    def initialization(self):

        for j in self.problem.jobs:
            for o in j.operations:
                self.notFinishedOpSet.append([j.id, o.id])
                if o.id!=0:
                    self.notReleasedOpSet.append([j.id, o.id])
        #self.notReleasedOpSet = self.notFinishedOpSet
        for m in range(self.problem.nm):
            self.freeMahchinesSet.append(m)#define machine as free
            #self.machineWaitingList.append([])

        for j in self.problem.jobs:
            self.nextEventsSet.append([j.id ,0,j.releaseTime,'r'])
        z= min(self.nextEventsSet, key=lambda tup: tup[2])
        #self.releasedOpSet.append([z[0],z[1],z[2]])
        self.currentTime=z[2]
        #self.releasedOpSet.sort(key=lambda tup: tup[2])
        # ilk released olan isi bul, ilgili operasyonu releasedOpSet'e ata



    def LeastWaitingTimeAssignment(self):
        self.lastAssigned=list()
        for j in self.releasedOpSet:
            minWm=1000000000
            mindex=0
            for m in self.problem.jobs[j[0]].operations[j[1]].machineSet:
                if m.id not in self.freeMahchinesSet:
                    wm1=self.solution.machines[m.id].mlft-self.currentTime
                else:
                    wm1=0
                wm2=self.solution.machines[m.id].mwlwm
                wm3=self.problem.jobs[j[0]].operations[j[1]].processingTimes[mindex]
                wm=wm1+wm2+wm3

                if wm<minWm:
                    minmid=m.id
                    minWm=wm
                    a=mindex
                mindex +=1
            self.solution.jobs[j[0]].operations[j[1]].machine.id=minmid
            self.solution.machines[minmid].mwlm.append([j[0],j[1]])
            self.solution.machines[minmid].mwlwm+=self.problem.jobs[j[0]].operations[j[1]].processingTimes[a]
            self.solution.machines[minmid].assigmentOperation.append([j[0],j[1]])
            self.lastAssigned.append([j[0],j[1],minmid])#hold last assigned operation and machine
            self.nextEventsSet.remove([j[0],j[1],self.currentTime,'r'])


    def update(self,assignment):#completed
        for j in assignment:
            self.solution.jobs[j[0]].operations[j[1]].ost=self.currentTime
            mid=j[2]
            for index,m in enumerate(self.problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:#find order machine id that given in machineSet
                    order=index
            self.solution.jobs[j[0]].operations[j[1]].oft=self.solution.jobs[j[0]].operations[j[1]].ost+self.problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            self.solution.jobs[j[0]].finishTime=self.solution.jobs[j[0]].operations[j[1]].oft
            self.nextEventsSet.append([j[0],j[1],self.solution.jobs[j[0]].operations[j[1]].oft,mid])
            if j[1]+1<self.problem.jobs[j[0]].nOfOperations:
                releaseTime=self.solution.jobs[j[0]].operations[j[1]].oft
                self.solution.jobs[j[0]].operations[j[1]+1].oreleaseTime=releaseTime
                self.nextEventsSet.append([j[0],j[1]+1,releaseTime,'r'])
            self.solution.machines[mid].mwlm.remove(j[:2])
            self.solution.jobs[j[0]].operations[j[1]].processingTime =self.problem.jobs[j[0]].operations[j[1]].processingTimes[order]#add workload to machine has mid
            self.solution.machines[mid].mlst=self.solution.jobs[j[0]].operations[j[1]].ost
            self.solution.machines[mid].mlft=self.solution.jobs[j[0]].operations[j[1]].oft
            self.freeMahchinesSet.remove(mid)
            #self.nextEventsSet.remove([j[0],j[1],self.nextTime,j[3]])
            #print self.solution.jobs[j[0]].id,self.solution.jobs[j[0]].operations[j[1]].id,self.solution.jobs[j[0]].operations[j[1]].machineId,self.solution.jobs[j[0]].operations[j[1]].ost,self.solution.jobs[j[0]].operations[j[1]].oft
            #print self.solution.machines[mid].mwlm,self.solution.machines[mid].mwlwm,self.solution.machines[mid].mlst,self.solution.machines[mid].mlft
            #print self.freeMahchinesSet
        #print self.nextEventsSet
    def findNextTimeandEvents(self):
        self.releasedOpSet=list()
        self.machineEventSet=list()
        if len(self.nextEventsSet):
            z= min(self.nextEventsSet, key=lambda tup: tup[2])
            self.nextTime=z[2]
        '''
        for j in self.nextEventsSet:
            if j[2]==self.nextTime:
                if j[3]=='r' :
                    self.releasedOpSet.append(j)
                    #self.notReleasedOpSet.remove(j[:2])
                else:
                    self.notFinishedOpSet.remove(j[:2])
                    self.nextEventsSet.remove(j)
                    self.solution.machines[j[3]].mwlwm-=self.solution.jobs[j[0]].operations[j[1]].processingTime
                    self.freeMahchinesSet.append(j[3])
                    self.machineEventSet.append(j)
                #self.notFinishedOpSet.remove()#how to delete a row.
                #self.freeMahchinesSet.append('machine.id')#is it True?
                #self.machineEventSet.append('machine.id')#is it True?
        '''
        if z[3]=='r':
            self.releasedOpSet.append(z)
            #self.notReleasedOpSet.remove(z[:2])
        else:
            self.notFinishedOpSet.remove(z[:2])
            self.nextEventsSet.remove(z)
            self.solution.machines[z[3]].mwlwm-=self.solution.jobs[z[0]].operations[z[1]].processingTime
            self.freeMahchinesSet.append(z[3])
            self.machineEventSet.append(z)

    def updateMachineSet(self,lastAssigned,machineEventSet,d):
        lastStarted=list()
        #if len(lastAssigned)>0:
        for j in lastAssigned:
            if j[2] in self.freeMahchinesSet:
                mindex=j[2]
                '''for index,m in enumerate(self.problem.jobs[j[0]].operations[j[1]].machineSet):
                    if m.id==mindex:#find order machine id that given in machineSet
                        order=index
                processingTime=self.problem.jobs[j[0]].operations[j[1]].processingTimes[order]
                self.solution.jobs[j[0]].operations[j[1]].ost=self.currentTime
                self.solution.jobs[j[0]].operations[j[1]].oft=self.currentTime+processingTime
                self.solution.machines[mindex].mlst=self.currentTime
                self.solution.machines[mindex].mlft=self.currentTime+processingTime
                self.solution.machines[mindex].mwlwm-=processingTime
                '''
                lastStarted.append([j[0],j[1],mindex])
                for i in self.nextEventsSet:
                    if i[0]==j[0] and i[1]==j[1] and i[3]=='r':

                        self.nextEventsSet.remove(i)
                #self.solution.machines[j[2]].mwlm.remove(j[:2])3
                #self.solution.machines[j[2]].mwlm.remove(j[:2])

        for i in machineEventSet:#used FIFO rule
            '''for l in lastStarted:
                if i[3]!=l[2] and len(self.solution.machines[i[3]].mwlm)>0 :
                    k = self.solution.machines[i[3]].mwlm
                    lastStarted.append([k[0][0],k[0][1],i[3]])
            '''
            #if len(lastStarted)<1:
            k = self.solution.machines[i[3]].mwlm
            if len(k)>0 :
                result=JS.dispatchingRules(k,self.solution,self.problem,i[3],d,self.currentTime,self.GeneticRules,self.extraction)
                #result=GEP.GeneExtraction(k,self.solution,self.problem,i[3],d,self.currentTime,self.visitindex)
                lastStarted.append(result[0])


        return lastStarted

    def simulatedSolution(self):
        nonDominated=list()
        Resultfile = open("result.txt","a")
        Result=[ [] for i in xrange(len(self.GeneticRules))]#it is depend on number of dispatching rules. GA kullaniliyor
        #Result=[ [] for i in xrange(14)]
        #Result[0].append(0)
        for dRulesID in range(len(self.GeneticRules)):
        #for dRulesID in range(14):
            #for h in range(10):
            self.__init__(self.problem,self.solution,self.visitindex,self.GeneticRules,self.extraction)
            self.initialization()
            self.nextTime=self.currentTime
            z= min(self.nextEventsSet, key=lambda tup: tup[2])#job in Evenset assigned to machines randomly
            lena=len(self.problem.jobs[z[0]].operations[z[1]].machineSet)
            a=np.random.randint(0,lena)

            assignedMachineId=self.problem.jobs[z[0]].operations[z[1]].machineSet[a].id
            self.assignment.append([z[0],z[1],assignedMachineId,'r'])
            self.solution.machines[assignedMachineId].assigmentOperation.append(z[:2])
            self.solution.machines[assignedMachineId].mwlm.append(z[:2])
            self.solution.machines[assignedMachineId].mwlwm+=self.problem.jobs[z[0]].operations[z[1]].processingTimes[a]
            #print self.solution.jobs[z[0]].id,self.solution.jobs[z[0]].operations[z[1]].id,self.solution.jobs[z[0]].operations[z[1]].machineId
            self.update(self.assignment)
            for i in self.nextEventsSet:
                if i[2]==self.currentTime:
                    self.nextEventsSet.remove(i)
            while len(self.notFinishedOpSet)>0:
                self.findNextTimeandEvents()
                self.currentTime=self.nextTime
                if len(self.releasedOpSet)>0:
                    self.LeastWaitingTimeAssignment()
                lastStarted=self.updateMachineSet(self.lastAssigned,self.machineEventSet,dRulesID)
                self.lastAssigned=list()
                if len(lastStarted)>0:
                    self.update(lastStarted)

                '''for i in self.nextEventsSet:
                    if i[2]==self.currentTime and i[3]=='r':
                        self.nextEventsSet.remove(i)
    '''
            #a=TS.tranformation(self.problem,self.solution)#used for draw gantt chart
            mal=EV.Evaluation(self.solution)


            Resultfile.write(str(dRulesID)+ "\t")
            Resultfile.write(str(mal[0])+ "\t")
            Resultfile.write(str(mal[1][0])+ "\t")
            Resultfile.write(str(mal[1][1])+ "\n")

            Result[dRulesID]+=[dRulesID,mal[0],mal[1][0],mal[1][1]] #GA kullanilir
            af=4
            #nonDominated.append([mal[0],mal[1][0],mal[1][1]])
        #print d,mal[0],mal[1][0],mal[1][1]
            #print nonDominated
        #nDominated=NDS.sorting(nonDominated)
        Resultfile.close()

        return Result #GA kullaniliyor
        #return self.solution








    def randomSolution(self, solution):
        allOperations = []  # define all operation set

        index = 0
        for job in self.problem.jobs:
            for o in job.operations:
                allOperations.append(
                    [job.id, 0, 0])  # add job id, operation id(default value=0) and machine id(default value=0)
                index += 1

        randomSolution = np.random.permutation(allOperations)  # convert allOperation set to numpy permutation

        for job in solution.jobs:
            for o in job.operations:
                jId = job.id
                oId = o.id
                numberOfMachine = len(self.problem.jobs[jId].operations[
                                          oId].machineSet)  # calculate assignable number of machine according to job id an opeation id
                index = np.random.randint(0,
                                          numberOfMachine)  # select random index between 0 and assignable number of machine
                o.machine.id = self.problem.jobs[jId].operations[oId].machineSet[
                    index].id  # assig m id that selects ramdomly assignable machine
                processingTime = self.problem.jobs[jId].operations[oId].processingTimes[
                    index]  # calculate operation process time on assigned  machine
                solution.jobs[jId].operations[oId].processingTime = processingTime  # assign this processing time to solution jobs set
                # print job.id,"\t", o.id, "\t", o.machineid

        processingTimes = []
        indexSet = np.zeros(self.problem.nj)  # define numpy zeros permutation whose lenght equals to number of jobs
        for o in randomSolution:  # generate job based permutation
            o[1] = indexSet[o[0]]
            indexSet[o[0]] = indexSet[o[0]] + 1
            o[2] = solution.jobs[o[0]].operations[o[1]].machine.id
            processingTimes.append(solution.jobs[o[0]].operations[o[1]].processingTime)

        sol = []
        for si, s in enumerate(randomSolution):  # add processing time to job based permutation
            sol.append([s[0], s[1], s[2], processingTimes[si]])

        solution.order = sol
        return solution  # assign sol set to solution set