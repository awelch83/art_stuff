import math

theta_current = -20;
t_lt = 0;
t_gt = 0;

y_goal = 491.4075;

counter = 0;
x1 = ((1433.219-1000)*math.cos(math.radians(theta_current)))-((566.7671-1000)*math.sin(math.radians(theta_current)))+1000;
y1 = ((1433.219-1000)*math.sin(math.radians(theta_current)))+((566.7671-1000)*math.cos(math.radians(theta_current)))+1000;

while (abs(y_goal-y1) > .00000000000001):
    if y1 < y_goal:
        counter = counter + 1
        t_gt = theta_current
        theta_current = (t_lt+t_gt)/2
        x1 = ((1433.219-1000)*math.cos(math.radians(theta_current)))-((566.7671-1000)*math.sin(math.radians(theta_current)))+1000;
        y1 = ((1433.219-1000)*math.sin(math.radians(theta_current)))+((566.7671-1000)*math.cos(math.radians(theta_current)))+1000;
    elif y1 > y_goal:
        counter = counter + 1
        t_lt = theta_current
        theta_current = (t_lt+t_gt)/2
        x1 = ((1433.219-1000)*math.cos(math.radians(theta_current)))-((566.7671-1000)*math.sin(math.radians(theta_current)))+1000;
        y1 = ((1433.219-1000)*math.sin(math.radians(theta_current)))+((566.7671-1000)*math.cos(math.radians(theta_current)))+1000;
    elif y1 == y_goal:
        break

print(theta_current)
print(counter)
