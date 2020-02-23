
import random
import main as M
import timeit
start = timeit.default_timer()
print "dynamic selection of rules.py"
class Birey:
    def __init__(self):
        self.id = 0
        self.Cmax=0.0
        self.MeanTardiness=0.0
        self.MeanFlowTime=0.0
        self.FitnessValue=0.0
        self.len=0
        self.threshold=0
        self.rulesSet=list()
        self.qlSet=list()
class DynamicRules(Birey):
    def __init__(self):
        self.chromosome=list()
        self.numberOfrules=40
        self.tr=3
    def CreateInitialPopulation(self):

        for i in range(0,self.numberOfrules):
            birey=Birey()
            birey.id=i
            birey.threshold=self.tr
            terminalset=["FIFO","SPT","EDD","SLK"]
            #functionset=["+","-","*","/"]#used for nonlineer dynamic rules extracting
            chromosomelen=2*len(terminalset)-1#parameter
            birey.len=chromosomelen
            tail=list()
            head=list()
            for j  in range(self.tr + 1):

                head.append(random.choice(terminalset))

            for j in range(self.tr ):
                tail.append(int(random.uniform(1,5)))


            birey.rulesSet=(head)
            birey.qlSet = tail
            #birey.genotip=(sum(tempchromosome,[]))
            self.chromosome.append(birey)
        return self.chromosome

a=DynamicRules().CreateInitialPopulation()
abss=11

def mainGA(a):
    ngeneration=50
    nDR=40
    rOfElitizm=0.10
    rOfMutation=0.002
    Resultfilez = open("sumofresult.txt","a")
    for i in range(0,ngeneration):
        result=M.Main(a)
        print str(i)+" .iterasyon"

        Evaluate(result,a)
        GenetikOperations(a,rOfElitizm,rOfMutation,nDR)

        for k in a:
            Resultfilez.write(str(k.id)+ "\t")
            Resultfilez.write(str(k.Cmax)+ "\t")
            Resultfilez.write(str(k.MeanTardiness)+ "\t")
            Resultfilez.write(str(k.MeanFlowTime)+ "\t")
            Resultfilez.write(str(k.FitnessValue)+ "\n")

    for j in a:
        #print j.Cmax,"\t",j.MeanTardiness,"\t",j.MeanFlowTime,"\t",j.FitnessValue
        Resultfilez.write(str(j.id)+ "\t")
        Resultfilez.write(str(j.rulesSet)+ "\n")
        Resultfilez.write(str(j.qlSet)+ "\n")

    Resultfilez.write(str(ngeneration)+"\t"+str(nDR)+"\t"+str(rOfElitizm)+"\t"+str(rOfMutation)+ "\n")
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

def GenetikOperations(chromosome,rOfElitizm,rOfMutation,nDR):
    Fitness=list()
    Temp=list()
    tlist=list()
    tfunctionlist=list()
    for i in chromosome:
        Fitness.append([i.id,i.FitnessValue])
    #print Fitness
    SortedFitness=sorted(Fitness,key=lambda x: x[1])


    for i in range(0,int(nDR*rOfElitizm)):#Elitizm parametresi
        x=SortedFitness[i][0]
        #Temp.append(SortedFitness[i])
        tlist.append(chromosome[x].rulesSet)
        tfunctionlist.append(chromosome[x].qlSet)


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
        genoa=chromosome[ebeveyn1[0]].rulesSet
        genob=chromosome[ebeveyn2[0]].rulesSet
        functiona=chromosome[ebeveyn1[0]].qlSet
        functionb=chromosome[ebeveyn2[0]].qlSet
        ss=len(genoa)
        r=random.randint(0,len(genoa))
        child1=genoa[:r]+genob[r:]
        child2=genob[:r]+genoa[r:]
        child1fun=functiona[:r]+functionb[r:]
        child2fun=functionb[:r]+functiona[r:]
        tlist.append(child1)
        tlist.append(child2)
        tfunctionlist.append(child1fun)
        tfunctionlist.append(child2fun)

    for index1,i in enumerate(tlist):#Mutasyon
        for index2,j in enumerate(i):
            rndm=random.random()
            if rndm<=(rOfMutation):
                k=random.choice(["FIFO","SPT","EDD","SLK"])
                tlist[index1][index2]=k


    for index1,i in enumerate(tfunctionlist):#Mutasyon
        for index2,j in enumerate(i):
            rndm=random.random()
            if rndm<=(rOfMutation):
                h=int(random.uniform(1,5))
                tfunctionlist[index1][index2]=h


    for index,j in enumerate(tlist):
        chromosome[index].genotip=j
        chromosome[index].id=index
        chromosome[index].function=tfunctionlist[index]


vvv=mainGA(a)
