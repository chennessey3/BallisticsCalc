# This is a program we will use to calculate balistics of various rounds
# Will serve as a platform that I will expand upon as time goes on
# Assume for now a spherical projectile with constant drag coefficient

#User entered constants:
vel_x_0 = 3200 #[fps]
mass_0 = 55 #[grains]
dist_to_target_x_dir = 3*600 #[ft]
bullet_dia = 0.223 #diameter of projectile [in]

drag_coefficient = 0.32
#form_factor = 1
atmospheric_density = 1.225 #[kg/m3] at sea level and 15 deg C

projectile_frontal_area = (bullet_dia/2)*(bullet_dia/2)*3.14159 

#Physical constants:
g_0 = 32.174 # standard gravity [ft/s^2]
speed_of_sound = 1126.0 #[ft/s] at sea level and 15 deg C


#Functions
def in_sq_to_m_sq(area_in_inch_sq):
    area_in_m_sq = 0.00064516*area_in_inch_sq
    return area_in_m_sq
    
def grains_to_kg(weight_in_grains):
    mass_in_kg = 6.479891E-5 * weight_in_grains
    return mass_in_kg    

def fps_to_mps(vel_in_fps):
    vel_in_mps = 0.3048 * vel_in_fps
    return vel_in_mps  

#Mach Number    
Mach_num =  (fps_to_mps(vel_x_0) / 343.2 )       
print 'Mach Number: ','{:+06.3f}'.format(Mach_num)
 
    
          
#now we want to calculate bullet drop

time_to_target = float(dist_to_target_x_dir)/float(vel_x_0)

print 'time to target: ','{:+06.5f}'.format(time_to_target), 'seconds'

bullet_drop = -0.5 * g_0 * time_to_target * time_to_target #[ft]

print 'bullet drop: ','{:+06.5f}'.format(bullet_drop*12), 'inch'


#calculate muzzle energy:

E_0 = (mass_0 * vel_x_0 * vel_x_0) / 450435 # muzzle energy in [ft*lbs] for mass in grains, vel in fps
print 'muzzle energy: ','{:+06.2f}'.format(E_0), 'ft*lbs'


#calculate energy at target:

#calculate sectional density:

sectional_density = mass_0 / (7000 * bullet_dia * bullet_dia)
print 'sectional density: ','{:+02.3f}'.format(sectional_density), 'units?'


#Calculate the initial drag force:

F_d_0 = - 0.5 * atmospheric_density * fps_to_mps(vel_x_0) * fps_to_mps(vel_x_0) * drag_coefficient * in_sq_to_m_sq(projectile_frontal_area)
print 'initial drag force: ','{:+02.3f}'.format(F_d_0), 'N'

#Calculate deceleration due to initial drag force:
a_d_0 = F_d_0 / grains_to_kg(mass_0)
print 'initial deceleration: ','{:+02.3f}'.format(a_d_0), 'm/s^2'


#Iterate to find the velocity as a function of time because fuck diff eqs
#We'll divide the total range to target and assume constant deceleration as
#the projectile traverses this distance for our first attempt

itterations =100000
counter = 0
time_inc = time_to_target/itterations
distance_traveled_x_dir = 0
vel_x = vel_x_0
a_d = a_d_0
while counter < itterations:
#    print counter
    counter = counter + 1
    dist_inc = fps_to_mps(vel_x)*time_inc + 0.5 * a_d * time_inc * time_inc
#    print dist_inc*3.28084 , 'ft'
    vel_x = vel_x + a_d * time_inc
    distance_traveled_x_dir = distance_traveled_x_dir + dist_inc
    #update drag force and acceleration of drag:
    F_d = - 0.5 * atmospheric_density * fps_to_mps(vel_x_0) * fps_to_mps(vel_x_0) * drag_coefficient * in_sq_to_m_sq(projectile_frontal_area)
    a_d = F_d / grains_to_kg(mass_0)
    #check for approach of transonic barrier
    if vel_x/speed_of_sound < 1.1:
       print "warning, transonic barrer encountered"
       break 
    #Increase itterations if needed
    if counter == (itterations - 1 )  and distance_traveled_x_dir < dist_to_target_x_dir:
        itterations = itterations + 1
    
print '\n', distance_traveled_x_dir*3.28084/3 , 'yrds'
print 'final_velocity', vel_x , 'ft/s'




