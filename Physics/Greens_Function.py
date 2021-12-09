import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random

L = 20

# The grid is n+1 points along x and y, including boundary points 0 and n
n = 10

Walks= 200#WALKS

# The grid spacing is L/n

# The number of iterations
nsteps = 200
# Set the boundary conditions








Convergce=[]
# checker=1: no checkboard, checker=2: checkerboard (note: n should be even)
checker = 1

# perform one step of relaxation
def relax(n,v):


    for check in range(0,1):

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

                Average=SUM/Walks

                v[x,y]=Average

        V_tot=607.5
        SUM=0

        for i in range(1,len(v)-1):
            for j in range(1,len(v[0])-1):
                SUM=SUM+v[i,j]

        Convergce.append(SUM/V_tot)
                            



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





Greens_0_y=[]
Greens_n_y=[]
Greens_x_0=[]
Greens_x_n=[]

for i in range(0,n+1):

    v=[]

    for j in range(0,n+1):

        

        if i==0 or i==n or j==0 or j==n:
            v = np.zeros((n+1, n+1))
            vnew = np.zeros((n+1, n+1))
            v[i,j] = 10

            v=relax(n,v)

            if i==0:

                Greens_0_y.append(v)

            if i==n:

                Greens_n_y.append(v)

            if j==0:

                Greens_x_0.append(v)

            if j==n:

                Greens_x_n.append(v)


Green_result=[Greens_x_0,Greens_x_n,Greens_0_y,Greens_n_y]

print(Green_result)






"""
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(v, cmap=None, interpolation='nearest')
fig.colorbar(im)


# we generate nsteps+1 frames, because frame=0 is skipped (see above)
anim = animation.FuncAnimation(fig, update, frames=nsteps+1, interval=200, blit=True, repeat=False)
plt.show()
"""










