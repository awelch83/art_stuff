import math

distance_initial = 100

x_outer_v1 = 0
y_outer_v1 = 2000
x_outer_v2 = 1000
y_outer_v2 = 1000
x_outer_v3 = 0
y_outer_v3 = 0


d_rotation = 100
d_seg_init = math.sqrt(math.pow((x_outer_v2-x_outer_v1),2) + math.pow((y_outer_v2-y_outer_v1),2))
rotation_pct_inital = 1 - (d_rotation / d_seg_init)

while d_rotation > 2:
    d_segment = math.sqrt(math.pow((x_outer_v2-x_outer_v1),2) + math.pow((y_outer_v2-y_outer_v1),2))
    d_ratio = d_rotation / d_segment
    xt_1 = ((1 - d_ratio) * x_outer_v1 + d_ratio * x_outer_v2)
    yt_1 = ((1 - d_ratio) * y_outer_v1 + d_ratio * y_outer_v2)

    d_segment = math.sqrt(math.pow((x_outer_v3-x_outer_v2),2) + math.pow((y_outer_v3-y_outer_v2),2))
    d_ratio = d_rotation / d_segment
    xt_2 = ((1 - d_ratio) * x_outer_v2 + d_ratio * x_outer_v3)
    yt_2 = ((1 - d_ratio) * y_outer_v2 + d_ratio * y_outer_v3)

    d_segment = math.sqrt(math.pow((x_outer_v1-x_outer_v3),2) + math.pow((y_outer_v1-y_outer_v3),2))
    d_ratio = d_rotation / d_segment
    xt_3 = ((1 - d_ratio) * x_outer_v3 + d_ratio * x_outer_v1)
    yt_3 = ((1 - d_ratio) * y_outer_v3 + d_ratio * y_outer_v1)

    print("xt_1 =",xt_1)
    print("yt_1 =",yt_1,"\n")

    print("xt_2 =",xt_2)
    print("yt_2 =",yt_2,"\n")

    print("xt_3 =",xt_3)
    print("yt_3 =",yt_3,)
    print("----------------")

    x_outer_v1 = xt_1
    x_outer_v2 = xt_2
    x_outer_v3 = xt_3

    y_outer_v1 = yt_1
    y_outer_v2 = yt_2
    y_outer_v3 = yt_3

    d_rotation = d_rotation * rotation_pct_inital
