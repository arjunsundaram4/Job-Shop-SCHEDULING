import math

def Evaluation(solution):
    print "Evaluation.py"
    def MAL():
        mal=0
        for i in solution.jobs:
            duedate=i.dueDate
            finishedTime=i.operations[-1].oft
            mal+= abs(duedate-finishedTime)
        mal=mal/len(solution.jobs)
        return mal

    def MSL():
        msl=0
        for i in solution.jobs:
            duedate=i.dueDate
            finishedTime=i.operations[-1].oft
            msl+=math.pow((duedate-finishedTime),2)
        msl=msl/len(solution.jobs)
        return msl
    def Makespan():
        Cmax=0
        for j in solution.jobs:
            a=j.finishTime
            if a>Cmax:
                Cmax=a
        return Cmax
    def ML():
        ml=0
        mft=0
        for i in solution.jobs:
            duedate=i.dueDate
            start=i.operations[0].ost
            finishedTime=i.finishTime
            #if finishedTime>duedate:mutlak sapma yapildi
            ml+= abs(finishedTime-duedate)
            mft+=finishedTime-start
        ml=ml/len(solution.jobs)
        mft=mft/len(solution.jobs)

        return ml,mft
    def MFT():#Mean Flow Time

        pass
    a=MAL()
    b=MSL()
    c=Makespan()
    d=ML()
    return c,d