
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
        self.len=0
        self.function=list()#used for nonlineer
class DynamicRules(Birey):
    def __init__(self):
        self.chromosome=list()
        self.numberOfrules=60
        print "DynamicRules.py"
    def CreateInitialPopulation(self):

        for i in range(0,self.numberOfrules):
            birey=Birey()
            birey.id=i
            terminalset=["p","P","DD","SLK","ODD","MODD","CR","CRODD","r","Re"]
            functionset=["+","-","*","/"]#used for nonlineer dynamic rules extracting
            chromosomelen=5*len(terminalset)#parameter
            birey.len=chromosomelen
            tempchromosome=list()
            tempfunction=list()

            count=0
            for j  in range (0,len(terminalset)):
                head=list()
                head.append(terminalset[count])
                head.append(">=")
                head.append("<=")
                a=random.random()
                b=random.random()
                if a<b:
                    head.append(a)
                    head.append(b)
                else:
                    head.append(b)
                    head.append(a)
                tempchromosome.append(head)
                count+=1
            for j in range(len(terminalset)-1):
                tempfunction.append(random.choice(functionset))

            birey.genotip=(tempchromosome)
            birey.function=tempfunction
            #birey.genotip=(sum(tempchromosome,[]))
            self.chromosome.append(birey)
        return self.chromosome

a=DynamicRules().CreateInitialPopulation()
abss=11

def mainGA(a):
    ngeneration=100
    nDR=60
    rOfElitizm=0.10
    rOfMutation=0.002
    Resultfilez = open("sumofresult.txt","a")
    for i in range(0,ngeneration):
        result=M.Main(a,extracting=1)
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
        Resultfilez.write(str(j.genotip)+ "\n")
        Resultfilez.write(str(j.function)+ "\n")

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
        tlist.append(chromosome[x].genotip)
        tfunctionlist.append(chromosome[x].function)


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
        functiona=chromosome[ebeveyn1[0]].function
        functionb=chromosome[ebeveyn2[0]].function
        ss=len(genoa)
        r=random.randint(0,len(genoa))
        child1=genoa[:r+1]+genob[r+1:]
        child2=genob[:r+1]+genoa[r+1:]
        c=r/5
        child1fun=functiona[:c+1]+functionb[c+1:]
        child2fun=functionb[:c+1]+functiona[c+1:]
        tlist.append(child1)
        tlist.append(child2)
        tfunctionlist.append(child1fun)
        tfunctionlist.append(child2fun)

    for i in tlist:#Mutasyon
        for j in i:
            for index,k in enumerate(j):
                rndm=random.random()
                if rndm<=(rOfMutation):
                    n=1
                    if index%5==0:
                        pass
                    elif index % 5==1 or index % 5==2 :
                        j=-1
                    elif index % 5==3:
                        k=random.uniform(0,j[4])
                    else:
                        k=random.uniform(j[3],1)


    for index,j in enumerate(tlist):
        chromosome[index].genotip=j
        chromosome[index].id=index
        chromosome[index].function=tfunctionlist[index]


vvv=mainGA(a)
