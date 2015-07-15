import matplotlib.pyplot as plt

hit_location_y = [1 , 0.5 ]
Hit_location_z =  [1, 1.5 ] 

plt.axes()

#Create the target geometry
circle = plt.Circle((0, 0), radius=0.75, fc='y')
plt.gca().add_patch(circle)

line1 = plt.Line2D((-.5,.5), (0,0), lw=2.5, c='k')
plt.gca().add_line(line1)

line2 = plt.Line2D((0,0), (-.5,.5), lw=2.5, c='k')
plt.gca().add_line(line2)



plt.scatter(Hit_location_z, hit_location_y, s=20)



plt.axis('scaled')
plt.show()