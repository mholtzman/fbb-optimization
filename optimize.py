from __future__ import print_function
from ortools.linear_solver import pywraplp
import random

def main():
  # Instantiate a Glop solver, naming it SolveSimpleSystem.
  solver = pywraplp.Solver('SolveSimpleSystem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  # [name, value, cost, is_ss, is_of]
  player_data = [
    ['ss1',22,80,1,0],
    ['ss2',11,50,1,0],
    ['ss3',50,100,1,0],
    ['of1',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of2',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of3',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of4',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of5',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of6',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of7',random.randrange(5, 50),random.randrange(10,40),0,1],
    ['of8',random.randrange(5, 50),random.randrange(10,40),0,1]
  ]

  players = [[]] * len(player_data)

  # objective: maximize points
  objective = solver.Objective()
  for i in range(0, len(player_data)):
    players[i] = solver.IntVar(0.0, 1.0, player_data[i][0])
    objective.SetCoefficient(players[i], player_data[i][1])
  objective.SetMaximization()

  # total cost must be at most $100
  max_cost = solver.Constraint(0, 100)
  for j in range(0, len(players)):
    max_cost.SetCoefficient(players[j], player_data[j][2])

  # must have exactly one SS
  max_ss = solver.Constraint(1,1)
  for j in range(0, 2):
    max_ss.SetCoefficient(players[j], player_data[j][3])

  # must have exactly three OF
  max_of = solver.Constraint(3,3)
  for k in range(2, len(players)):
    max_of.SetCoefficient(players[k], player_data[k][4])


  # Solve the system.
  status = solver.Solve()
  total_value = 0
  cost = 0

  print("Optimal Lineup: ")
  for i in range(0, len(players)):
    if (players[i].solution_value() > 0):
      total_value += player_data[i][1]
      cost += player_data[i][2]
      print("{}, ${}".format(player_data[i][0],player_data[i][2]))

  print("\nTotal Pts: {}".format(total_value))
  print("Cost: {}".format(cost))
if __name__ == '__main__':
  main()