import math


raw_input = list(map(int, input().strip().split()))
h_len = raw_input[0]
m_len = raw_input[1]
h = raw_input[2] / 12
m = raw_input[3] / 60
m_degree = 360 * m
h_degree = 360 * h + 30 * m
abs_degree = abs(m_degree - h_degree)
a_len = h_len ** 2 + m_len ** 2 - 2 * h_len * m_len * math.cos(math.radians(abs_degree))
print(math.sqrt(a_len))
