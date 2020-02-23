import math
import random
import main as M
import timeit
start = timeit.default_timer()
class Birey:
    def __init__(self):
        self.id = 0
        self.genotip=list()
        self.fenotip=list()
        self.Cmax=0.0
        self.MeanTardiness=0.0
        self.MeanFlowTime=0.0
        self.FitnessValue=0.0
        self.headsize=0
class GenetikAlgoritma(Birey):
    def __init__(self):
        self.chromosome=list()

    def CreateInitialPopulation(self):
        for i in range(0,2):
            birey=Birey()
            birey.id=i
            headsize=5#parameter
            birey.headsize=headsize
            n=2#parameter
            tailsize=headsize*(n-1)+1
            dcsize=headsize
            genelength=headsize+tailsize+dcsize
            geneCount=1#parameter
            homeoticlength=5#parameter
            homeoticCount=0
            chromosomelength=geneCount*genelength+homeoticCount*homeoticlength
            functionset=["+","-","*","/"]
            terminalset=["SPT","LWKR","EDD","AT","TWORK","?","CR","SLK","ODD","CRODD","LnOps","SOP","SOPN","COVERT","LRnOps"]
            tempchromosome=list()
            head=list()
            tail=list()
            dcset=list()

            for j  in range (0,geneCount):
                for k in range(0,headsize):
                    a=random.randint(0,1)
                    #print a
                    if k==0:
                        head.append(random.choice(functionset))
                    else:
                        if a==0:
                            head.append(random.choice(functionset))
                        else:
                           head.append(random.choice(terminalset))
                    dcset.append(random.randrange(1,10))
                for h in range(0,tailsize):
                    tail.append(random.choice(terminalset))
                tempchromosome.append(head)
                tempchromosome.append(tail)
                tempchromosome.append(dcset)
            birey.genotip=(sum(tempchromosome,[]))
            codding=GenotipToFenotip(birey.genotip,headsize,tailsize)

            birey.fenotip=codding
            self.chromosome.append(birey)
        return self.chromosome,functionset,terminalset



def GenotipToFenotip(Genotip,hs,ts):
    codingArray=[[],[],[],[]]
    count=1
    countoperation=0
    countparameter=0
    functionset=["+","-","*","/"]
    for index,j in enumerate(Genotip):
        if index<hs:
                #if j[1] not in functioset and j[2] not in functioset:
                    #a=3
            if countparameter<=countoperation:#if countparameters are bigger than countoperations in any step, branching will finish
                if j in functionset:
                    codingArray[1].append(count)
                    codingArray[2].append(count+1)
                    codingArray[3].append(0)
                    count+=2
                    countoperation+=1
                else:
                    codingArray[1].append(0)
                    codingArray[2].append(0)
                    codingArray[3].append(0)
                    countparameter+=1
            else:
                break
        else:
            break
    for i in Genotip:
        codingArray[0].append(i)
    for i in range(len(codingArray[1])-1,-1,-1):
        if codingArray[1][i]==0:
            del codingArray[1][i]
            del codingArray[2][i]
            del codingArray[3][i]
        else:
            break

    countDcNumber=0
    for i in range(len(codingArray[1])-1,-1,-1):
        x=codingArray[1][i]
        y=codingArray[2][i]
        d=""
        if x!=0:
            if x>len(codingArray[1])-1:
                a=codingArray[0][x]
            else:
                a=codingArray[3][x]
            if y>len(codingArray[1])-1:
                b=codingArray[0][y]

            else:
                b=codingArray[3][y]
            c=codingArray[0][i]
            if a=="?":
                a=str(Genotip[countDcNumber+hs+ts])
                countDcNumber+=1
            if b=="?":
                b=str(Genotip[countDcNumber+hs+ts])
                countDcNumber+=1
            if a!=0 and b!=0:
                if c=="+":
                    d=a+"+"+b
                elif c=='-':
                    d=a+"-"+b
                elif c=="*":
                    d=a+"*"+b
                elif c=="/":
                    d=a+"/"+"("+b+"+"+"0.000000001"+")"
                else:
                    print "there is wrong something"

                codingArray[3][i]="("+d+")"
        else:
            codingArray[3][i]=codingArray[0][i]
    return codingArray


a=GenetikAlgoritma().CreateInitialPopulation()



def mainGA(a):
    ngeneration=500
    nDR=50
    rOfMutation=0.01
    rOfElitizm=0.10
    '''
    for j in a:
        print j.Cmax,"\t",j.MeanTardiness,"\t",j.MeanFlowTime,"\t",j.FitnessValue
    '''
    step=list()
    Resultfilez = open("sumofresult.txt","a")
    for i in range(0,ngeneration):
        print str(i)+" .iterasyon"
        result=M.Main(a[0],extracting=2)


        vbn=Evaluate(result,a[0])
        bcb=GenetikOperations(a[0],a[1],a[2],rOfElitizm,rOfMutation,nDR)
        step.append(bcb)

        for k in a[0]:
            Resultfilez.write(str(k.id)+ "\t")
            Resultfilez.write(str(k.Cmax)+ "\t")
            Resultfilez.write(str(k.MeanTardiness)+ "\t")
            Resultfilez.write(str(k.MeanFlowTime)+ "\t")
            Resultfilez.write(str(k.FitnessValue)+ "\n")

    for j in a[0]:
        #print j.Cmax,"\t",j.MeanTardiness,"\t",j.MeanFlowTime,"\t",j.FitnessValue
        Resultfilez.write(str(j.id)+ "\t")
        Resultfilez.write(str(j.fenotip[3][0])+ "\n")

    for i in step:
        print i
    Resultfilez.write(str(ngeneration)+"\t"+str(nDR)+"\t"+str(a[0][0].headsize)+"\t"+str(rOfElitizm)+"\t"+str(rOfMutation)+ "\n")
    stop = timeit.default_timer()
    print stop-start
    Resultfilez.write(str(stop-start)+"\n")
    Resultfilez.close()
def Evaluate(result,chromosome):

    #DrRules=[0 for i in xrange(len(result))]

    for j in result:
        chromosome[j[0]].Cmax=j[1]
        chromosome[j[0]].MeanTardiness=j[2]
        chromosome[j[0]].MeanFlowTime=j[3]
        chromosome[j[0]].FitnessValue=(chromosome[j[0]].Cmax/3)+(chromosome[j[0]].MeanTardiness/3)+(chromosome[j[0]].MeanFlowTime/3)
        '''
        for index,j in enumerate(i):
            DrRules[index]+=j

    for i in range(0,len(result[0])):
        DrRules[i]=DrRules[i]/len(result)
        '''

def GenetikOperations(chromosome,fset,tset,rOfElitizm,rOfMutation,nDR):
    Fitness=list()
    Temp=list()
    tlist=list()
    for i in chromosome:
        Fitness.append([i.id,i.FitnessValue])
    #print Fitness
    SortedFitness=sorted(Fitness,key=lambda x: x[1])


    for i in range(0,int(nDR*rOfElitizm)):#Elitizm parametresi
        x=SortedFitness[i][0]
        #Temp.append(SortedFitness[i])
        tlist.append(chromosome[x].genotip)

    for i in range(0,int(nDR*(1-rOfElitizm))):
        a=random.choice(Fitness)
        b=random.choice(Fitness)
        if a[1]<b[1]:
            x=1+random.randint(0,100)
            if x<=70:
                Temp.append(a)
            else:
                Temp.append(b)
        else:
            y=1+random.randint(0,100)
            if y<=70:
                Temp.append(b)
            else:
                Temp.append(a)


    for i in range(0,int((nDR*(1-rOfElitizm))/2)):#caprazlama
        ebeveyn1=random.choice(Temp)
        ebeveyn2=random.choice(Temp)
        genoa=chromosome[ebeveyn1[0]].genotip
        genob=chromosome[ebeveyn2[0]].genotip
        r=random.randint(1,2*(chromosome[ebeveyn1[0]].headsize))
        child1=genoa[:r+1]+genob[r+1:]
        child2=genob[:r+1]+genoa[r+1:]
        tlist.append(child1)
        tlist.append(child2)

    for i in tlist:#Mutasyon
        rndm=100*(random.random())+1
        if rndm<=(rOfMutation*100):
            x=random.randint(1,2*(chromosome[ebeveyn1[0]].headsize))
            if i[x] in fset:
                i[x]=random.choice(fset)
            else:
                i[x]=random.choice(tset)

    for index,j in enumerate(tlist):
        newfeno=GenotipToFenotip(j,chromosome[0].headsize,chromosome[0].headsize+1)
        chromosome[index].genotip=j
        chromosome[index].fenotip=newfeno
        chromosome[index].id=index

    return SortedFitness[0]
vvv=mainGA(a)