# Варіант 4
from pulp import *

pass_amount = [[320, 300, 190, 250],
               [200, 250, 170, 260],
               [225, 300, 200, 320]]

operational_expences = [[1200, 800, 1500, 1600],
                        [1400, 1500, 2000, 2900],
                        [1000, 1100, 1800, 1700]]

passangers_by_route = [40000, 50000, 40000, 30000]

ticket_cost_by_route = [200, 150, 180, 300]

amout_of_planes = [10, 25, 40]

prob1 = LpProblem("f1", LpMaximize)
prob2 = LpProblem("f2", LpMaximize)
prob3 = LpProblem("F", LpMinimize)

x111 = LpVariable("1 type of plane, 1 route", lowBound=0)
x112 = LpVariable("1 type of plane, 2 route", lowBound=0)
x113 = LpVariable("1 type of plane, 3 route", lowBound=0)
x114 = LpVariable("1 type of plane, 4 route", lowBound=0)
x121 = LpVariable("2 type of plane, 1 route", lowBound=0)
x122 = LpVariable("2 type of plane, 2 route", lowBound=0)
x123 = LpVariable("2 type of plane, 3 route", lowBound=0)
x124 = LpVariable("2 type of plane, 4 route", lowBound=0)
x131 = LpVariable("3 type of plane, 1 route", lowBound=0)
x132 = LpVariable("3 type of plane, 2 route", lowBound=0)
x133 = LpVariable("3 type of plane, 3 route", lowBound=0)
x134 = LpVariable("3 type of plane, 4 route", lowBound=0)

planes_by_route = [[x111, x112, x113, x114],
                   [x121, x122, x123, x124],
                   [x131, x132, x133, x134]]

for i in range(3):
    prob1 += planes_by_route[i][0] + planes_by_route[i][1] + planes_by_route[i][2] + planes_by_route[i][3] <= amout_of_planes[i]

for i in range(4):
    prob1 += planes_by_route[0][i]*pass_amount[0][i] + planes_by_route[1][i]*pass_amount[1][i] + planes_by_route[2][i]*pass_amount[2][i] <= passangers_by_route[i]

prob1 += (planes_by_route[0][0]*pass_amount[0][0] + planes_by_route[1][0]*pass_amount[1][0] + planes_by_route[2][0]*pass_amount[2][0])*ticket_cost_by_route[0] + (planes_by_route[0][1]*pass_amount[0][1] + planes_by_route[1][1]*pass_amount[1][1] + planes_by_route[2][1]*pass_amount[2][1])*ticket_cost_by_route[1] + (planes_by_route[0][2]*pass_amount[0][2] + planes_by_route[1][2]*pass_amount[1][2] + planes_by_route[2][2]*pass_amount[2][2])*ticket_cost_by_route[2] + (planes_by_route[0][3]*pass_amount[0][3] + planes_by_route[1][3]*pass_amount[1][3] + planes_by_route[2][3]*pass_amount[2][3])*ticket_cost_by_route[3]

prob1.solve()

print("Biggest income:", value(prob1.objective))
for v in prob1.variables():
    print(v.name, "=", v.varValue)  


x211 = LpVariable("1 type of plane, 1 route", lowBound=0)
x212 = LpVariable("1 type of plane, 2 route", lowBound=0)
x213 = LpVariable("1 type of plane, 3 route", lowBound=0)
x214 = LpVariable("1 type of plane, 4 route", lowBound=0)
x221 = LpVariable("2 type of plane, 1 route", lowBound=0)
x222 = LpVariable("2 type of plane, 2 route", lowBound=0)
x223 = LpVariable("2 type of plane, 3 route", lowBound=0)
x224 = LpVariable("2 type of plane, 4 route", lowBound=0)
x231 = LpVariable("3 type of plane, 1 route", lowBound=0)
x232 = LpVariable("3 type of plane, 2 route", lowBound=0)
x233 = LpVariable("3 type of plane, 3 route", lowBound=0)
x234 = LpVariable("3 type of plane, 4 route", lowBound=0)



for i in range(3):
    prob2 += planes_by_route[i][0] + planes_by_route[i][1] + planes_by_route[i][2] + planes_by_route[i][3] <= amout_of_planes[i]

for i in range(4):
    prob2 += planes_by_route[0][i]*pass_amount[0][i] + planes_by_route[1][i]*pass_amount[1][i] + planes_by_route[2][i]*pass_amount[2][i] <= passangers_by_route[i]

prob2 += planes_by_route[0][0]*pass_amount[0][0] + planes_by_route[0][1]*pass_amount[0][1] + planes_by_route[0][2]*pass_amount[0][2] + planes_by_route[0][3]*pass_amount[0][3] + planes_by_route[1][0]*pass_amount[1][0] + planes_by_route[1][1]*pass_amount[1][1] + planes_by_route[1][2]*pass_amount[1][2] + planes_by_route[1][3]*pass_amount[1][3] + planes_by_route[2][0]*pass_amount[2][0] + planes_by_route[2][1]*pass_amount[2][1] + planes_by_route[2][2]*pass_amount[2][2] + planes_by_route[2][3]*pass_amount[2][3]

prob2.solve()

print("Biggest pass amount:", value(prob2.objective))
for v in prob2.variables():
    print(v.name, "=", v.varValue)  

f1 = []
f2 = []

for i in range(3):
    for j in range(4):
        f1.append(-(pass_amount[i][j]*ticket_cost_by_route[j]) / value(prob1.objective))
        f2.append(-(pass_amount[i][j]) / value(prob2.objective))

f1.append(1)
f2.append(1)

print(f1)
print(f2)

F = []

for i in range(len(f1)):
    F.append((float(f1[i]) * 0.5) + (float(f2[i]) * 0.5))

print(F)

x11 = LpVariable("1 type of plane, 1 route", lowBound=0)
x12 = LpVariable("1 type of plane, 2 route", lowBound=0)
x13 = LpVariable("1 type of plane, 3 route", lowBound=0)
x14 = LpVariable("1 type of plane, 4 route", lowBound=0)
x21 = LpVariable("2 type of plane, 1 route", lowBound=0)
x22 = LpVariable("2 type of plane, 2 route", lowBound=0)
x23 = LpVariable("2 type of plane, 3 route", lowBound=0)
x24 = LpVariable("2 type of plane, 4 route", lowBound=0)
x31 = LpVariable("3 type of plane, 1 route", lowBound=0)
x32 = LpVariable("3 type of plane, 2 route", lowBound=0)
x33 = LpVariable("3 type of plane, 3 route", lowBound=0)
x34 = LpVariable("3 type of plane, 4 route", lowBound=0)

planes_by_route = [[x11, x12, x13, x14],
                   [x21, x22, x23, x24],
                   [x31, x32, x33, x34]]


for i in range(3):
    prob3 += planes_by_route[i][0] + planes_by_route[i][1] + planes_by_route[i][2] + planes_by_route[i][3] <= amout_of_planes[i]

for i in range(4):
    prob3 += planes_by_route[0][i]*pass_amount[0][i] + planes_by_route[1][i]*pass_amount[1][i] + planes_by_route[2][i]*pass_amount[2][i] <= passangers_by_route[i]

prob3 += planes_by_route[0][0]*F[0] + planes_by_route[0][1]*F[1] + planes_by_route[0][2]*F[2] + planes_by_route[0][3]*F[3] + planes_by_route[1][0]*F[4] + planes_by_route[1][1]*F[5] + planes_by_route[1][2]*F[6] + planes_by_route[1][3]*F[7] + planes_by_route[2][0]*F[8] + planes_by_route[2][1]*F[9] + planes_by_route[2][2]*F[10] + planes_by_route[2][3]*F[11] + F[12]

prob3.solve()

print("F:", value(prob3.objective))
for v in prob3.variables():
    print(v.name, "=", v.varValue) 