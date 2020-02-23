import matplotlib.pyplot as plt
import matplotlib as mpl
import schedulingProblem as SP
import solution as SS
import numpy as np


class tranformation():
    def __init__(self,problem,solution):
        self.jobs = list()
        self.machineName=list()#machines name in the gantt chart
        self.startTime=list()#start time set
        self.finishTime=list()#finish time set
        self.names=list()#operation name set
        self.colors=list()#operation color
        preEndTime=0#finish time of previous operation in the permutation
        indexa=0
        cc=np.random.rand(problem.nj,3)
        '''
        for i in solution.order:
            job = i[0]#assign job to job id
            op = i[1]#assign op to operation id
            mak = i[2]#assign mak to machine id
            machineEndTime = solution.machines[mak].mlft#find machine latest finish time
            startTime = max(preEndTime,machineEndTime)#define current job start time
            preEndTime = startTime+i[3]#calculate current job finish time
            solution.machines[mak].mlft=preEndTime#update current machine last finis time
            solution.jobs[job].operations[op].ost = startTime#assign operation start time to solution jobs set
            solution.jobs[job].operations[op].oft = preEndTime#assign operation finish time to solution jobs set
            #print "bitis", solution.machines[mak].id, "\t",job,"\t",op,"\t",startTime,"\t",solution.machines[mak].mlft
            self.machineName.append(mak)#add machine id to machinename set
            self.startTime.append(startTime)#add operation start time to startTime set
            self.finishTime.append(preEndTime)#add operation finish time to finishTime set
            self.names.append([mak, startTime, preEndTime, "O_"+str(job)+str(op)])#add operation name to names set



            self.colors.append(cc[job])

            indexa=indexa+1
        '''
        for i in solution.jobs:
            for j in i.operations:
                job = i.id#assign job to job id
                op = j.id#assign op to operation id
                mak = j.machine.id#assign mak to machine id
                machineEndTime = j.oft #find machine latest finish time
                startTime = j.ost#define current job start time

                self.machineName.append(mak+1)#add machine id to machinename set
                self.startTime.append(startTime)#add operation start time to startTime set
                self.finishTime.append(machineEndTime)#add operation finish time to finishTime set
                self.names.append([mak+1, startTime, machineEndTime, "J"+str(job+1)+"O"+str(op+1)])#add operation name to names set



                self.colors.append(cc[job])

            indexa=indexa+1
        print "aa"
        #plt.rc('grid', linestyle="-", color='gray')

        #plt.grid(True)



        #plt.show()

        plt.hlines(self.machineName, 0,max(self.finishTime), color="gray", lw=44,linestyles=':')#define gantt chart interval
        plt.hlines(self.machineName, self.startTime, self.finishTime, colors=self.colors, lw=44)#draw Gantt Chart
        plt.margins(0.1)
        plt.ylabel("MACHINE",color='red',size='20')
        plt.xlabel("TIME",color='red',size='20')
        for i in self.names:
            plt.text(i[1], i[0], i[3],color='white',size='10')


        plt.show()
'''
        fig = plt.figure(figsize=(10,10))
        k=0

        cmaps  = ["Blues", "Greens", "Reds", "Purples", "Oranges", "Greens", "autumn"]

        for j in solution.machines:
            ax = fig.add_axes([0.05, 0.1 + k*0.12 , 0.9, 0.1])
            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)
            k += 1

        maxft = 3* max(self.finishTime)
        minst = min(self.startTime)
        range = maxft-minst
        k=0
        for j in solution.jobs:
            cmap = plt.get_cmap(cmaps[k])
            for o in j.operations:
                mid = o.machine.id
                nost = ((o.ost-minst) / range)      #normalized operatio start time
                noft = ((o.oft-minst) /range)       #normalized operation finis time
                ax = fig.add_axes([0.05+nost, 0.1 + 0.01 + mid * 0.12 , 0.05+noft, 0.08])
                cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                            orientation='vertical')
                ax.xaxis.set_visible(False)
                ax.yaxis.set_visible(False)

            k +=1
        plt.show()
'''
0