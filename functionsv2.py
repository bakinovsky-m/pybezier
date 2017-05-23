def get_B(pushed_dot): #������� ����� �, ��� �� - ����� � ������� �������
	B = pushed_dot

	return B

def get_t(pushed_dot): #������� t 
    kurwa = pushed_dot.owners[1] #� ������� ��������� ��� ������ �� ����, ��� ����� ������� �����

    t = kurwa.dots.index(pushed_dot)/len(kurwa.dots)
	return t

def get_c(start_dot, end_dot, t): #������� C �� ������ ������ ������, ����� ������ � t(���� ����� ���� � ������ �� �������)
	u = (1 - t)**3/(t**3 + (1 - t)**3)

	C.x = u*start_dot.x + (1 - u)*end_dot.x;
	C.y = u*start_dot.y + (1 - u)*end_dot.y;

	return C

def ratio_t(t): #������� ����������� ��������� �� ������� ��� t

	return abs((t**3 + (1 - t)**3 - 1)/(t**3 + (1 - t)**3))

def get_a(B, C, ratio): #������� ����� �, ���� B, C � ����������� ���������
    A.x = B.x - (C.x - B.x)/ratio
    A.y = B.y - (C.y - B.y)/ratio 

    return A

def get_new_a(cur_dot, C, ratio): # ������ ������������ �������� A ��� �����, ���� ����������
    new_a.x = cur_dot.x - (C.x - cur_dot.x)/ratio
    new_a.y = cur_dot.y - (C.y - cur_dot.y)/ratio

    return new_a    

def get_e1(cur_dot, start_dot, old_control_start, A, B):  #������� e1, ��� ����� ����� ������ �����, �� �����-�����, ����� ��������� ����� �����
    k.x = start_dot.x + (old_control_start.x - start_dot.x)*t #����������� ����� �� ������
    k.y = start_dot.y + (old_control_start.y - start_dot.y)*t #���� ���������, ��� � ������ �������� ���� ������� �� t

    old_e1.x = k.x + (A.x - k.x)*t                            #� � ���������� ���� - ���������
    old_e1.y = k.y + (A.y - k.y)*t                            #������� ��������������� ��������� e1

    e1.x = old_e1.x + (cur_dot.x - B.x)                       #������������ �������
    e1.y = old_e1.y + (cur_dot.y - B.y)

    return e1

def get_e2(cur_dot, end_dot, old_control_end, A, B):      #�� �� �����
    k.x = old_control_end.x + (end_dot.x - old_control_end.x)*t
    k.y = old_control_end.y + (end_dot.y - old_control_end.y)*t

    old_e2.x = A.x + (k.x - A.x)*t
    old_e2.y = A.y + (k.y - A.y)*t

    e2.x = old_e2.x + (cur_dot.x - B.x)
    e2.y = old_e2.y + (cur_dot.y - B.y)

    return e2    

def get_c_start(start_dot, new_a, e1, t):  #�� �, ������� ���������� ����� ����������� �����, ������� ������ �������
    v.x = new_a.x + (e1.x - new_a.x)/t     #������ �� ��� � ������ ������ � �����
    v.y = new_a.y + (e1.y - new_a.y)/t

    control_start.x = v.x + (v.x - start_dot.x)/t
    control_start.y = v.y + (v.y - start_dot.y)/t

    return control_start 

def get_c_end(end_dot, new_a, e2, t):
    v.x = new_a.x + (e2.x - new_a.x)/t
    v.y = new_a.y + (e2.y - new_a.y)/t

    control_end.x = v.x + (v.x - end_dot.x)/t
    control_end.y = v.y + (v.y - end_dot.y)/t

    return control_end