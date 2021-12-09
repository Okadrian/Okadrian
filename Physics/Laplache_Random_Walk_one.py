import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random

L = 20

# The grid is n+1 points along x and y, including boundary points 0 and n
n = 10




v_correct=[[0,10,10,10,10,10.
,10,10,10,10,0,]
,[0,5,6.95783874,7.83135496,8.22657404,8.34226793
,8.22657404,7.83135496,6.95783874,5,0]
,[0,3.04216126,5,6.14100706,6.73267327,6.91592364
,6.73267327,6.14100706,5,3.04216126,0]
,[0,2.16864504,3.85899294,5,5.64718834,5.85608008
,5.64718834,5,3.85899294,2.16864504,0]
,[0,1.77342596,3.26732673,4.35281166,5,5.21402002
,5,4.35281166,3.26732673,1.77342596,0]
,[0,1.65773207,3.08407636,4.14391992,4.78597998,5.
,4.78597998,4.14391992,3.08407636,1.65773207,0]
,[0,1.77342596,3.26732673,4.35281166,5,5.21402002
,5,4.35281166,3.26732673,1.77342596,0]
,[0,2.16864504,3.85899294,5,5.64718834,5.85608008
,5.64718834,5,3.85899294,2.16864504,0]
,[0,3.04216126,5,6.14100706,6.73267327,6.91592364
,6.73267327,6.14100706,5,3.04216126,0]
,[0,5,6.95783874,7.83135496,8.22657404,8.34226793
,8.22657404,7.83135496,6.95783874,5,0]
,[0,10,10,10,10,10.
,10,10,10,10,0]]



# The grid spacing is L/n

# The number of iterations
nsteps = 200
# Initialize the grid to 0
v = np.zeros((n+1, n+1))
vnew = np.zeros((n+1, n+1))

for l in range(0,20):
    print(l)
    Break=0
    V_tot=250
    for i in range(1,n):
        v[0,i] = 10
        v[n,i] = 10
        v[i,0] = 0
        v[i,n] = 0

# Set the interior points

# Set center potential






fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(v, cmap=None, interpolation='nearest')
fig.colorbar(im)

Convergce=[]
# checker=1: no checkboard, checker=2: checkerboard (note: n should be even)
checker = 1

# perform one step of relaxation
def relax(n, v):

    for x in range(1,n):
        for y in range(1,n):

            SUM=0
            
            for w in range(0,Walks):

                Hit=0
                A,B=x,y

                while Hit==0:

                    RN=random.random()
                    RN=RN*4

                    if RN<1:

                        A=A+1

                    elif RN<2:

                        A=A-1

                    elif RN<3:

                        B=B+1

                    else:

                        B=B-1


                    if A==0 or A==n or B==0 or B==n:

                        SUM=SUM+v[A,B]

                        Hit=1

            v[x,y]=SUM/Walks

    return v
def update(step):

    global n, v, checker

    # FuncAnimation calls update several times with step=0,
    # so we needs to skip the update with step=0 to get
    # the correct number of steps 
    if step > 0:
        relax(n, v, checker)

    im.set_array(v)
    #print(im)
    return im,

print(v)

K=[]
normalize=10
Step=[]

for j in range(0,11):

    K.append([])

    K[0].append(v_correct[5][j])


for i in range (1,11,3):

    Walks=i*100
    v=relax(n, v)
    print(Walks)


    for j in range(0,11):

        K[i].append(v[5][j])




    




plt.figure()
plt.plot(K[0])
for i in range(1,11,3):
    plt.plot(K[i])
plt.xlabel("Position on horisonta")
plt.ylabel("Potential on the middel of the figure along the horisontal")
plt.title("Potential in middel: Boundary 10-10-0-0")
plt.legend(["Correct potential","Walks=100","Walks=400","Walks=700","Walks=1000"])
plt.show()





