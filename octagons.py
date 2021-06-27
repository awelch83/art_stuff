import math

distance_initial = 100

x_outer_v1 = 585.79
y_outer_v1 = 2000
x_outer_v2 = 1414.21
y_outer_v2 = 2000
x_outer_v3 = 2000
y_outer_v3 = 1414.21
x_outer_v4 = 2000
y_outer_v4 = 585.79
x_outer_v5 = 1414.21
y_outer_v5 = 0
x_outer_v6 = 585.79
y_outer_v6 = 0
x_outer_v7 = 0
y_outer_v7 = 585.79
x_outer_v8 = 0
y_outer_v8 = 1414.21

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
    print("yt_3 =",yt_3,"\n")

    print("xt_4 =",xt_4)
    print("yt_4 =",yt_4,"\n")

    print("xt_5 =",xt_5)
    print("yt_5 =",yt_5,"\n")

    print("xt_6 =",xt_5)
    print("yt_6 =",yt_5,"\n")

    print("xt_7 =",xt_7)
    print("yt_7 =",yt_7,"\n")

    print("xt_8 =",xt_8)
    print("yt_8 =",yt_8)
    print("----------------")

    x_outer_v1 = xt_1
    x_outer_v2 = xt_2
    x_outer_v3 = xt_3
    x_outer_v4 = xt_4
    x_outer_v5 = xt_5
    x_outer_v6 = xt_6
    x_outer_v7 = xt_7
    x_outer_v8 = xt_8

    y_outer_v1 = yt_1
    y_outer_v2 = yt_2
    y_outer_v3 = yt_3
    y_outer_v4 = yt_4
    y_outer_v5 = yt_5
    y_outer_v6 = yt_6
    y_outer_v7 = yt_7
    y_outer_v8 = yt_8

    d_rotation = d_rotation * rotation_pct_inital
