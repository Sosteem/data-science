import numpy as np
numP_Array=np.array([[1,2,3],[4,5,6]])#for aaray creation
NP1=np.array([[1,3],[4,5]]) #arrray create
NP2=np.array([[3,4],[5,7]])# create array
MNP=NP1@NP2 #MULTIPLICATION OF MATRIX 
MNP3=np.dot(NP1,NP2) #same as above //.dot is the class of numpy same result of multiplication
MNP2=NP1*NP2 #MULTIPLICATION OF SINGLE ELEMENTS OF THE ARRAY WITH ANOTHER ELEMENTS.
MNP4=np.multiply(NP1,NP2) #does same as *
#sum and substract
Sum1=NP1+NP2#sum
Sub1=NP1-NP2#substract
Sub2=np.subtract(NP1,NP2)#substract
El_Sum=np.sum(NP1)#sum between the arrays
Broad_Num=NP1+3 #adding 3 on every number
NP3=np.array([[3,4]])
NP1+NP3
D=np.divide(NP1,NP2)
E=np.divide([5,10,15],5)
F=np.floor_divide([6,10,15],5)
np.math.sqrt(10)
ND=np.random.standard_normal((2,2))
UD=np.random.uniform(1,12,(3,4))
Random_Ar=np.random.randint(1,50,(2,5))#this is for int number generation
np.random.rand(1.5,25.5,(2,2))#this is for float number generation
Ze=np.zeros((2,2))
ones=np.ones((3,5))
Filter_Ar=np.logical_and(Random_Ar>30,Random_Ar<50)
F_Random_Ar=Random_Ar[Filter_Ar]
Data_N=np.array([1,2,3,4,5])
Mean_N=np.mean(Data_N)#mean
Median_N=np.median(Data_N)#median
Var_N=np.var(Data_N)#varience 
SD_N=np.std(Data_N)#standard deviation
numP_Array=np.array([[1,2,3],[4,5,6]])
Var_Nump=np.var(numP_Array,axis=1) #for row gives varience for rows,specifying for the rows
Var_Nump1=np.var(numP_Array,axis=0)#for column gives varience for coloumn  