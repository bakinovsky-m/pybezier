def get_k(start_dot, control_start, t):
    k_x = start_dot.x + (control_start.x - start_dot.x)*t
    k_y = start_dot.y + (control_start.y - start_dot.y)*t

    k = Dot(k_x, k_y, "qwe", [])

    return k

def get_j(control_start, control_end, t):

    j_x = control_start.x + (control_end.x - control_start.x)*t #_!
    j_y = control_start.y + (control_end.y - control_start.y)*t #_!

    j = Dot(j_x, j_y, "qwe", []) #_!

    return j

def get_l(end_dot, control_end, t): #_!
    l_x = control_end.x + (end_dot.x - control_end.x)*t
    l_y = control_end.y + (end_dot.y - control_end.y)*t

    l = Dot(l_x, l_y, "qwe", [])

    return l  