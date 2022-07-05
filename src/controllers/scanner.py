def motor_run(motor,angle):
    ...

def ringlight(number,state):
    ...

def get_points(samples=1):
    from math import pi, sqrt, acos, atan2, cos, sin

    points = []
    phi = pi * (3. - sqrt(5.))
    for i in range(int(samples)):
        y = 1 - (i / float(samples - 1)) * 2
        radius = sqrt(1 - y * y)
        theta = phi * i
        x = cos(theta) * radius
        z = sin(theta) * radius
        r=sqrt(x*x+y*y+z*z)
        theta_neu=acos(z/r)*180/pi
        phi_neu=atan2(y,x)*180/pi
        points.append((theta_neu-90,phi_neu))
    points.sort()
    return points

def create_coordinates(angle_min, angle_max,point_count):
    point_count_final=point_count
    if angle_max < angle_min:
        a = angle_min
        angle_min = angle_max
        angle_max = a
    point_count=point_count*90/(angle_max-angle_min)
    actual_points=0
    while actual_points<point_count_final:
        points=get_points(point_count)
        filtered=[]
        for x,y in points:
            if x>angle_min and x<angle_max and len(filtered)<point_count_final:
                filtered.append((x,y))
        actual_points=len(filtered)

        if point_count-actual_points>20:
            point_count=point_count+3
        else:
            point_count=point_count+1
    return filtered