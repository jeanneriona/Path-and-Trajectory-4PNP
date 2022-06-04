import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib.pyplot as plt

### create model
a1 = float(input("a1 = ")) # FT 150
a2 = float(input("a2 = ")) #FT 80
a3 = float(input("a3 = ")) #FT 70


def mm_to_meter(a):
    m = 1000
    return a/m

a1 = mm_to_meter (a1)
a2 = mm_to_meter (a2)
a3 = mm_to_meter (a3)


lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)


# create Links
# [Robot variable] = DHRevolute(d,r/a,alpha,offset)
Arti_Elbow = DHRobot([
    RevoluteDH(a1,0,(90.0/180.0)*np.pi,0,qlim=[(-90.0/180.0)*np.pi,(90.0/180.0)*np.pi]),
    RevoluteDH(0,a2,0,0,qlim=[(-20.0/180.0)*np.pi,(90.0/180.0)*np.pi]),
    RevoluteDH(0,a3,0,0,qlim=[(-90.0/180.0)*np.pi,(90.0/180.0)*np.pi]),
    ], name='Articulated-Elbow')

def deg_to_rad(T):
    return (T/180)*np.pi

q0  = np.array([0,0,0])

q1  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q2  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q3  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q4  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q5  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q6  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q7  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q8  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q9  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q10  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q11  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

q12  = np.array(([deg_to_rad(float(input("T1 = "))),
                 deg_to_rad(float(input("T2 = "))),
                 deg_to_rad(float(input("T3 = ")))]))

traj1 = rtb.jtraj (q0,q1,10)
traj2 = rtb.jtraj (q1,q2,10)
traj3 = rtb.jtraj (q2,q3,10)
traj4 = rtb.jtraj (q3,q4,10)
traj5 = rtb.jtraj (q4,q5,10)
traj6 = rtb.jtraj (q5,q6,10)
traj7 = rtb.jtraj (q6,q7,10)
traj8 = rtb.jtraj (q7,q8,10)
traj9 = rtb.jtraj (q8,q9,10)
traj10 = rtb.jtraj (q9,q10,10)
traj11 = rtb.jtraj (q10,q11,10)
traj12 = rtb.jtraj (q11,q12,10)


# plot scale limits
x1 = -0.1
x2 = 0.1
y1 = -0.1
y2 = 0.1
z1 = -0.1
z2 = 0.1

# for Joint Variable vs Time(s) table
rtb.qplot(traj1.q)
rtb.qplot(traj2.q)
rtb.qplot(traj3.q)
rtb.qplot(traj4.q)
rtb.qplot(traj5.q)
rtb.qplot(traj6.q)
rtb.qplot(traj7.q)
rtb.qplot(traj8.q)
rtb.qplot(traj9.q)
rtb.qplot(traj10.q)
rtb.qplot(traj11.q)
rtb.qplot(traj12.q)


#plot for trajectory
Arti_Elbow.plot(traj1.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj2.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj3.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj4.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj5.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj6.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj7.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj8.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj9.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj10.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj11.q, limits=[x1, x2, y1, y2, z1, z2])
Arti_Elbow.plot(traj12.q, limits=[x1, x2, y1, y2, z1, z2], block=True)


print(Arti_Elbow)
#Arti_Elbow.teach(jointlabels=1)
