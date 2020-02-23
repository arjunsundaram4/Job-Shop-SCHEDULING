import random
def newdispatchingrules():
    
def dispatchingRules(k,solution,problem,mid,rid,currentTime,GRules,extraction):
    result=list()
    print "jobselection.py"
    '''
    result=list()
    dRules.append([0,"FIFO"])
    dRules.append([1,"SPT"])
    dRules.append([2,"EDD"])
    dRules.append([3,"(((SLK/((SLK/(SOPN+0.000000001))+0.000000001))+(LWKR-LWKR))*(SPT*(CR/(4+0.000000001))))"])
    dRules.append([4,"SPT+LWKR+SLK"])
    dRules.append([5,"(((SLK/((SLK/(SOPN+0.000000001))+0.000000001))+(LWKR-LWKR))*(LnOps*(TWORK*4)))"])
    dRules.append([6,"(SOP-((CR/(ODD+0.000000001))-(EDD+COVERT)))"])
    dRules.append([7,"(ODD+(((CRODD-LWKR)+LWKR)+1))"])
    dRules.append([8,"(ODD+LWKR)"])
    dRules.append([9,"(TWORK*LWKR)"])
    dRules.append([10,"((ODD-(CRODD*(CRODD*CRODD)))*LWKR)"])
    dRules.append([11,"((EDD-(CRODD*(CRODD*CRODD)))*LWKR)"])
    dRules.append([12,"(rTime+SPT+(2*TWORK))"])
    dRules.append(([13,"((7*TWORK)+(11*SPT)+12*(LnOps+rTime))"]))
    result=list()
    if rid==0:
        result.append([k[0][0],k[0][1],mid])
    if rid==1:
        oProccesingTime=list()
        for mindex,j in enumerate(k):
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            oProccesingTime.append([mindex,problem.jobs[j[0]].operations[j[1]].processingTimes[order]])
        z= min(oProccesingTime, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==2:
        duedate=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            duedate.append([mindex,dDate])
        z= min(duedate, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==3:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            pastProcessingTimes=0
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    pastProcessingTimes+=i.processingTime
            remainingProcessingTime=totalProcessingTime-pastProcessingTimes
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            a=max(rTime +((dDate-rTime)*remainingProcessingTime)/totalProcessingTime,operationProcessingTime+currentTime)
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==4:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            pastProcessingTimes=0
            totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    pastProcessingTimes+=i.processingTime
            remainingProcessingTime=totalProcessingTime-pastProcessingTimes
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            a=operationProcessingTime+remainingProcessingTime+(dDate-remainingProcessingTime-currentTime)#yanlis
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==5:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            pastProcessingTimes=0
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    pastProcessingTimes+=i.processingTime
            remainingProcessingTime=totalProcessingTime-pastProcessingTimes
            a=rTime +((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    ################################it is used for GA and DR
'''

    if extraction !=1:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            npastProcessingTimes=0
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    npastProcessingTimes+=i.processingTime
            remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
            LnOps=problem.jobs[j[0]].nOfOperations
            LRnOps=LnOps-j[1]
            TWORK=ntotalProcessingTime
            EDD=dDate
            AT=rTime
            LWKR=remainingProcessingTime
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
            CRODD=(ODD-currentTime)/ntotalProcessingTime
            SPT=operationProcessingTime
            SOP=(1-(SLK/LRnOps))/operationProcessingTime
            FIFO=mindex
            if SLK>=0:
                SOPN=SLK/LRnOps
            else:
                SOPN=SLK*LRnOps
            COVERT=max(1-(max(SLK,0)/2*remainingProcessingTime),0)/operationProcessingTime
            MODD=max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime)
            OOD=rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
            if extraction==0:
                a=eval(GRules[rid][1])
            else:
                a=eval(GRules[rid].fenotip[3][0])#it is worked with GA
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])

    ################## it is used for Dynamic rules
    elif extraction==1 or extraction==1.5:
        decisonList=list()
        tEDD=list()
        tr=list()
        tP=list()
        tp=list()
        tCR=list()
        tCRODD=list()
        tODD=list()
        tMODD=list()
        tSLK=list()
        tRe=list()
        for mindex,j in enumerate(k):

            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            npastProcessingTimes=0
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    npastProcessingTimes+=i.processingTime
            remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
            tRe.append(remainingProcessingTime)
            #LnOps=problem.jobs[j[0]].nOfOperations
            #LRnOps=LnOps-j[1]
            #TWORK=ntotalProcessingTime
            tEDD.append(dDate)
            #AT=rTime
            tr.append(rTime)
            tp.append(operationProcessingTime)
            tP.append(ntotalProcessingTime)
            #LWKR=remainingProcessingTime
            tSLK.append(dDate-currentTime-rTime)
            tCR.append((dDate-currentTime)/remainingProcessingTime)
            aODD=rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
            tODD.append(rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime)
            tCRODD.append((aODD-currentTime)/ntotalProcessingTime)
            #SPT=operationProcessingTime
            #SOP=(1-(SLK/LRnOps))/operationProcessingTime
            #FIFO=mindex

            #if SLK>=0:
                #SOPN=SLK/LRnOps
            #else:
               # SOPN=SLK*LRnOps

            #COVERT=max(1-(max(SLK,0)/2*remainingProcessingTime),0)/operationProcessingTime
            tMODD.append(max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime))
            #OOD=rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
        minDD=min(tEDD)
        maxDD=max(tEDD)
        minp=min(tp)
        maxp=max(tp)
        minP=min(tP)
        maxP=max(tP)
        minr=min(tr)
        maxr=max(tr)
        minCR=min(tCR)
        maxCR=max(tCR)
        maxCRODD=max(tCRODD)
        minCRODD=min(tCRODD)
        maxODD=max(tODD)
        minODD=min(tODD)
        maxMODD=max(tMODD)
        minMODD=min(tMODD)
        maxSLK=max(tSLK)
        minSLK=min(tSLK)
        maxRe=max(tRe)
        minRe=min(tRe)
        for mindex,j in enumerate(k):
            #a=eval(dRules[rid][1])#it is worked main promram
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            npastProcessingTimes=0
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    npastProcessingTimes+=i.processingTime
            remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
            xRe=remainingProcessingTime
            xSLK=(dDate-currentTime-rTime)
            xCR=((dDate-currentTime)/remainingProcessingTime)
            xODD=(rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime)
            xCRODD=(xODD-currentTime)/ntotalProcessingTime
            xMODD=(max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime))
            DD=(dDate-minDD)/(maxDD-minDD+0.00000001)
            p=(operationProcessingTime-minp)/(maxp-minp+0.00000001)
            P=(ntotalProcessingTime-minP)/(maxP-minP+0.00000001)
            r=(rTime-minr)/(maxr-minr+0.00000001)
            CR=(xCR-minCR)/(maxCR-minCR+0.00000001)
            CRODD=(xCRODD-minCRODD)/(maxCRODD-minCRODD+0.00000001)
            ODD=(xODD-minODD)/(maxODD-minODD+0.00000001)
            MODD=(xMODD-minMODD)/(maxMODD-minMODD+0.00000001)
            SLK=(xSLK-minSLK)/(maxSLK-minSLK+0.00000001)
            Re=(xRe-minRe)/(maxRe-minRe+0.00000001)
            if b==1:
                b=GRules[rid].genotip #it is used for extracing dynamic rules
            if b==1.5:
                b = GRules[rid][1]  # it is used for analysis of rules
            functionOfRule=GRules[rid].function
            #b= GRules[rid][1]#it is used for analysis of rules
            formule=""
            first=False
            for index,i in enumerate(b):
                x=eval(i[0])
                if i[1]!=-1:
                    up=True
                else:
                    up=False
                if i[2]!=-1:
                    down=True
                else:
                    down=False
                uplimit=i[4]
                downlimit=i[3]
                if up==True and down==True:
                    if downlimit<= x <=uplimit:
                        #formule+=i[0]+"+"
                        if index!=0 and first==True:
                            formule+=functionOfRule[index-1]+i[0]
                        else:
                            formule+=i[0]
                        first=True
                elif up==True and down==False:
                    if x<= uplimit:
                        if index!=0 and first==True:
                            formule+=functionOfRule[index-1]+i[0]
                        else:
                            formule+=i[0]
                        first=True
                elif up==False and down==True:
                    if x>=downlimit:
                        if index!=0 and first==True:
                            formule+=functionOfRule[index-1]+i[0]
                        else:
                            formule+=i[0]
                        first=True
                else:
                    if index!=0 and first==True:
                        formule+=functionOfRule[index-1]+i[0]
                    else:
                        formule+=i[0]
                    first=True

            DD=dDate
            p=operationProcessingTime
            P=ntotalProcessingTime
            r=rTime
            CR=xCR
            CRODD=xCRODD
            ODD=xODD
            MODD=xMODD
            SLK=xSLK
            Re=xRe
            if len(formule)<1:
                a=1000000000
            else:
                #formule=formule[:-1]
                a=eval(formule)
            #a=eval(GRules[rid].genotip)#it is worked with GA
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    else:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            #ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            npastProcessingTimes=0
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    npastProcessingTimes+=i.processingTime
            #remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
            #LnOps=problem.jobs[j[0]].nOfOperations
            #LRnOps=LnOps-j[1]
            #TWORK=ntotalProcessingTime
            EDD=dDate
            #AT=rTime
            #LWKR=remainingProcessingTime
            SLK=dDate-currentTime-rTime
            #CR=(dDate-currentTime)/remainingProcessingTime
            #ODD=rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
            #CRODD=(ODD-currentTime)/ntotalProcessingTime
            SPT=operationProcessingTime
            #SOP=(1-(SLK/LRnOps))/operationProcessingTime
            FIFO=mindex
            '''
            if SLK>=0:
                SOPN=SLK/LRnOps
            else:
                SOPN=SLK*LRnOps
            '''
            #COVERT=max(1-(max(SLK,0)/2*remainingProcessingTime),0)/operationProcessingTime
            #MODD=max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime)
            #OOD=rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
            rules=GRules[rid].rulesSet
            ql=GRules[rid].qlSet
            numberOfWaitingOperation=len(solution.machines[mid].mwlm)
            cumsum=0
            count=-1
            p=True
            #glList=list()
            for i in ql:
                cumsum+=i
                count+=1
                if numberOfWaitingOperation<=cumsum:
                    p=False
                    break
            if p == True :
                count+=1
            #glList.append(cumsum)
            #a=eval(GRules[rid][1])
            #a=eval(GRules[rid].fenotip[3][0])#it is worked with GA
            a=eval(rules[count])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])

    return result




