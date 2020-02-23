import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS
import createSolution as CS
import timeit

#Your statements here
dRules=list()
nonDominated=list()
dRules.append([0,"FIFO"])
dRules.append([1,"SPT"])
dRules.append([2,"EDD"])
dRules.append([3,"ODD"])
dRules.append([4,"SPT+LWKR+SLK"])
#dRules.append([5,"CR"])
#dRules.append([6,"COVERT"])
#dRules.append([7,"CRODD"])
#dRules.append([8,"AT"])
#dRules.append([9,"(rTime+SPT+(2*TWORK))"])
#dRules.append(([10,"((7*TWORK)+(11*SPT)+12*(LnOps+rTime))"]))
#dRules.append(([11,"(((LRnOps*TWORK)+SPT)*LRnOps)"]))
#dRules.append(([12,"(LRnOps+((CRODD/(9+0.000000001))-(COVERT/(SPT+0.000000001))))"]))
#dRules.append(([13,"(TWORK/(((3+LnOps)-LRnOps)+0.000000001))"]))
#dRules.append(([14,"(LRnOps*LWKR)"]))
#dRules.append(([15,"((LRnOps+1)*LWKR)"]))
#dRules.append(([16,"((EDD+(((LRnOps+TWORK)/((LWKR-TWORK)+0.000000001))*LnOps))*LRnOps)"]))
#dRules.append(([17,"(LWKR+(((LRnOps*LRnOps)/((COVERT-COVERT)+0.000000001))-SOP))"]))
#dRules.append(([18,"(((LRnOps*LWKR)+LWKR)-(LRnOps*3))"]))
#dRules.append(([19,"(((CR/((ODD*3)+0.000000001))*CRODD)+ODD)"]))
#dRules.append(([20,"(ODD+(((CRODD-LWKR)+LWKR)+1))"]))
#dRules.append(([21,"(ODD+LWKR)"]))
#dRules.append(([22,"(TWORK*LWKR)"]))
#dRules.append(([23,"((ODD-(CRODD*(CRODD*CRODD)))*LWKR)"]))
#dRules.append(([24,"((EDD-(CRODD*(CRODD*CRODD)))*LWKR)"]))


def Main(GeneticRules,extracting=0):
    print "main"
    start = timeit.default_timer()
    #GeneticRules=[]

    #flexible=[0.2,0.5,1]
    flexible=[0.2]
    dueDateParameter=[1.2,1.5,2,0]
    #dueDateParameter=[1.2]
    jobAndMachine=[[10,5],[20,5],[50,5],[20,10],[50,10],[100,10],[50,15],[100,15],[200,15]]
    '''
    flexible=[0.5]
    dueDateParameter=[1.5]
    jobAndMachine=[[10,3]]
    '''
    data=[ [0,0,0,0] for i in xrange(len(GeneticRules))]

    repetition=1
    for h in range(0,repetition):
        for i in flexible:
            for j in dueDateParameter:
                for index,k in enumerate(jobAndMachine):
                    pr1 = SP.FJSSP(k[1], k[0], j, i)#generate problem
                    #pr1.printTable()#call print function from schedulingProblem file
                    s1 = SS.Solution(pr1)#call solution function from solution file
                    cs1 = CS.createSolution(pr1,s1,index,GeneticRules,extracting)
                    #s2 = cs1.randomSolution(s1)
                    #cs1.initialization()
                    Result=cs1.simulatedSolution()

                    for index,t in enumerate(data):
                        for l in range(0,4):
                            if l==0:
                                data[index][l]=Result[index][l]
                            else:
                                data[index][l]+=Result[index][l]

                    #a=TS.tranformation(pr1,ab)#call transformation function from TranformPermutationToSolution file
                    #print s1.order, "\n"#print solution
                #print timeit.default_timer()-start

    for index,t in enumerate(data):#it is used for calculate mean value of objectives
        for l in range(0,4):
            if l==0:
                data[index][l]=data[index][l]
            else:
                data[index][l]=data[index][l]/(len(flexible)*len(dueDateParameter)*len(jobAndMachine)*repetition)

    print data
   # print "oldu bu is"
    stop = timeit.default_timer()
    print stop-start
    return data
Main(dRules)