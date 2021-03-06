from dot import Dot

def get_B(pushed_dot):  # Вычисление точки B для нажатой точки на кривой 
	B = Dot(pushed_dot.x, pushed_dot.y, "qwe", [])

	return B

def get_t(pushed_dot):  # Вычисление значения t для нажатой точки на кривой 
    kurwa = pushed_dot.owners

    t = kurwa.dots.index(pushed_dot)/len(kurwa.dots)
    return t

def get_c(start_dot, end_dot, t):   # Вычисление C по точкам начала кривой, конца кривой и t
    u = (1 - t)**3/(t**3 + (1 - t)**3)

    c_x = u*start_dot.x + (1 - u)*end_dot.x
    c_y = u*start_dot.y + (1 - u)*end_dot.y
    c = Dot(c_x, c_y, "qwe", [])

    return c

def ratio_t(t):   # Вычисление константного отношения по формуле для t

    return abs((t**3 + (1 - t)**3 - 1)/(t**3 + (1 - t)**3))

def get_a(B, C, ratio):     # Вычисление точек А, по B, C и константному отношению
    a_x = B.x - (C.x - B.x)/ratio
    a_y = B.y - (C.y - B.y)/ratio 

    a = Dot(a_x, a_y, "qwe", [])

    return a

def get_old_e1(start_dot, old_control_start, old_control_end, t): # Находим точки второй итерации алгоритма де Кастельжо 
    k_x = start_dot.x + (old_control_start.x - start_dot.x)*t
    k_y = start_dot.y + (old_control_start.y - start_dot.y)*t

    k = Dot(k_x, k_y, "qwe", [])

    j_x = old_control_start.x + (old_control_end.x - old_control_start.x)*t
    j_y = old_control_start.y + (old_control_end.y - old_control_start.y)*t

    j = Dot(j_x, j_y, "qwe", []) 

    old_e1_x = k.x + (j.x - k.x)*t
    old_e1_y = k.y + (j.y - k.y)*t

    old_e1 = Dot(old_e1_x, old_e1_y, "qwe", [])

    return old_e1


def get_old_e2(end_dot, old_control_end, old_control_start, t): # Вычисление точек второй итерации алгоритма де Кастельжо
    k_x = old_control_end.x + (end_dot.x - old_control_end.x)*t
    k_y = old_control_end.y + (end_dot.y - old_control_end.y)*t

    k = Dot(k_x, k_y, "qwe", [])

    j_x = old_control_start.x + (old_control_end.x - old_control_start.x)*t
    j_y = old_control_start.y + (old_control_end.y - old_control_start.y)*t

    j = Dot(j_x, j_y, "qwe", [])

    old_e2_x = j.x + (k.x - j.x)*t
    old_e2_y = j.y + (k.y - j.y)*t 

    old_e2 = Dot(old_e2_x, old_e2_y, "qwe", [])

    return old_e2

def get_new_a(cur_dot, C, ratio): # Пересчет значения A для нового положения точки кривой 
    new_a_x = cur_dot.x - (C.x - cur_dot.x)/ratio
    new_a_y = cur_dot.y - (C.y - cur_dot.y)/ratio

    new_a = Dot(new_a_x, new_a_y, "qwe", [])

    return new_a    

def get_e1(cur_dot, old_e1, B):  # Пересчет точек второй итерации алгоритма де Кастельжо           
    e1_x = old_e1.x + (cur_dot.x - B.x)
    e1_y = old_e1.y + (cur_dot.y - B.y)

    e1 = Dot(e1_x, e1_y, "qwe", [])

    return e1

def get_e2(cur_dot, old_e2, B):  # Пересчет точек второй итерации алгоритма де Кастельжо     
    e2_x = old_e2.x + (cur_dot.x - B.x)
    e2_y = old_e2.y + (cur_dot.y - B.y)

    e2 = Dot(e2_x, e2_y, "qwe", [])

    return e2  

def get_c_start(start_dot, new_a, e1, t):  # Пересчёт координат точек-рычагов
    v_x = new_a.x + (e1.x - new_a.x)/(1-t) 
    v_y = new_a.y + (e1.y - new_a.y)/(1-t)

    v = Dot(v_x, v_y, "qwe", [])

    control_start_x = start_dot.x + (v.x - start_dot.x)/t 
    control_start_y = start_dot.y + (v.y - start_dot.y)/t

    control_start = Dot(control_start_x, control_start_y, "lever", [])

    return control_start 


def get_c_end(end_dot, new_a, e2, t):  # Пересчёт координат точек-рычагов
    v_x = new_a.x + (e2.x - new_a.x)/t
    v_y = new_a.y + (e2.y - new_a.y)/t

    v = Dot(v_x, v_y, "qwe", [])

    control_end_x = end_dot.x + (v.x - end_dot.x)/(1-t)
    control_end_y = end_dot.y + (v.y - end_dot.y)/(1-t) 

    control_end = Dot(control_end_x, control_end_y, "lever", [])

    return control_end


def get_k(start_dot, control_start, t):   # Вычисление точек второй итерации алгоритма де Кастельжо для визуализации
    k_x = start_dot.x + (control_start.x - start_dot.x)*t
    k_y = start_dot.y + (control_start.y - start_dot.y)*t

    k = Dot(k_x, k_y, "qwe", [])

    return k

def get_j(control_start, control_end, t):  # Вычисление точек второй итерации алгоритма де Кастельжо для визуализации

    j_x = control_start.x + (control_end.x - control_start.x)*t #_!
    j_y = control_start.y + (control_end.y - control_start.y)*t #_!

    j = Dot(j_x, j_y, "qwe", []) #_!

    return j

def get_l(end_dot, control_end, t):  # Вычисление точек второй итерации алгоритма де Кастельжо для визуализации
    l_x = control_end.x + (end_dot.x - control_end.x)*t
    l_y = control_end.y + (end_dot.y - control_end.y)*t

    l = Dot(l_x, l_y, "qwe", [])

    return l 

class Point:  # Класс для локальных нужд
    def __init__(self,x,y):
        self.x = x
        self.y = y

def ccw(A,B,C):  # Служебная функция
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def line_intersection(A,B,C,D):  # Проверка пересечения двух отрезков
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def point_sort_to_poligon(p1, p2, p3, p4):  # создание выпуклого четырехуголика из набора точек
    poligon = []
    a = Point(p1[0], p1[1])
    b = Point(p2[0], p2[1])
    c = Point(p3[0], p3[1])
    d = Point(p4[0], p4[1])

    if line_intersection(a, b, c, d) == True:
        poligon.append(p1)
        poligon.append(p3)
        poligon.append(p2)
        poligon.append(p4)
        return poligon
    if line_intersection(a, d, c, b) == True:
        poligon.append(p1)
        poligon.append(p2)
        poligon.append(p4)
        poligon.append(p3)
        return poligon
    else:
        poligon.append(p1)
        poligon.append(p2)
        poligon.append(p3)
        poligon.append(p4)
    
    return poligon

def calculateLever(b1, b2):  # 
    mid = ((b1.x + b2.x)/2, (b1.y + b2.y)/2)
    coords = (mid[0], mid[1])
    return Dot(coords[0], coords[1], "lever", [])

# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.

def point_inside_polygon(x, y, poly):  # Определение попадения точки в четырехугольник

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n + 1):
        p2x,p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside 

