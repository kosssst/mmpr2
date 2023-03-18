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
prob2 = LpProblem("f2", LpMinimize)

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

planes_by_route = [[x211, x212, x213, x214],
                   [x221, x222, x223, x224],
                   [x231, x232, x233, x234]]

for i in range(3):
    prob2 += planes_by_route[i][0] + planes_by_route[i][1] + planes_by_route[i][2] + planes_by_route[i][3] <= amout_of_planes[i]

for i in range(4):
    prob2 += planes_by_route[0][i]*pass_amount[0][i] + planes_by_route[1][i]*pass_amount[1][i] + planes_by_route[2][i]*pass_amount[2][i] <= passangers_by_route[i]

prob2 += planes_by_route[0][0]*operational_expences[0][0] + planes_by_route[0][1]*operational_expences[0][1] + planes_by_route[0][2]*operational_expences[0][2] + planes_by_route[0][3]*operational_expences[0][3] + planes_by_route[1][0]*operational_expences[1][0] + planes_by_route[1][1]*operational_expences[1][1] + planes_by_route[1][2]*operational_expences[1][2] + planes_by_route[1][3]*operational_expences[1][3] + planes_by_route[2][0]*operational_expences[2][0] + planes_by_route[2][1]*operational_expences[2][1] + planes_by_route[2][2]*operational_expences[2][2] + planes_by_route[2][3]*operational_expences[2][3]

prob2.solve()

print("Smallest operational expences:", value(prob2.objective))
for v in prob2.variables():
    print(v.name, "=", v.varValue)  