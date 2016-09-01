from __future__ import print_function
from ortools.linear_solver import pywraplp
import sys, random, itertools

def main():
  # Instantiate a Glop solver, naming it SolveSimpleSystem.
  solver = pywraplp.Solver('SolveSimpleSystem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  # [name, position, value, cost]
  c_data = [
    ['Buster Posey','C',434,29],
    ['Kyle Schwarber','C',405,14],
    ['Evan Gattis','C',339.5,13],
    ['Jonathan Lucroy','C',344,9],
    ['Salvador Perez','C',318.5,8],
    ['Brian McCann','C',332.5,9],
    ['Russell Martin','C',314.5,7],
    ['Stephen Vogt','C',297,4],
    ['Travis dArnaud','C',299.5,5],
    ['J.T. Realmuto','C',280,2],
    ['Nick Hundley','C',221,1],
    ['Yan Gomes','C',259,3],
    ['Derek Norris','C',276.5,2],
    ['Matt Wieters','C',256,1],
    ['Yadier Molina','C',255,1],
    ['Francisco Cervelli','C',239.5,1],
    ['Welington Castillo','C',242.5,1],
    ['Wilson Ramos','C',248.5,1],
    ['Blake Swihart','C',220,1],
    ['Devin Mesoraco','C',229.5,1],
    ['Yasmani Grandal','C',272,1],
    ['Clint Coulter','C',200,1],
    ['James McCann','C',211.5,1],
    ['Miguel Montero','C',234.5,1],
    ['A.J. Pierzynski','C',186,1],
    ['Dioner Navarro','C',174,1]
  ]

  first_base_data = [
    ['Paul Goldschmidt','1B',545.5,44],
    ['Miguel Cabrera','1B',492,35],
    ['Anthony Rizzo','1B',517,34],
    ['Jose Abreu','1B',464,32],
    ['Chris Davis','1B',451,31],
    ['Joey Votto','1B',481,23],
    ['Edwin Encarnacion','1B',475.5,27],
    ['Hanley Ramirez','1B',375.5,15],
    ['Freddie Freeman','1B',434.5,20],
    ['Eric Hosmer','1B',429.5,19],
    ['Adrian Gonzalez','1B',430.5,20],
    ['Brandon Belt','1B',359,12],
    ['Albert Pujols','1B',432,17],
    ['Matt Holliday','1B',357,7],
    ['Victor Martinez','1B',373,8],
    ['Byung-ho Park','1B',340.5,9],
    ['Lucas Duda','1B',369.5,8],
    ['Carlos Santana','1B',426.5,8],
    ['Justin Bour','1B',336.5,5],
    ['Adam Lind','1B',339,4],
    ['C.J. Cron','1B',316,3],
    ['Ryan Zimmerman','1B',321.5,3],
    ['Joe Mauer','1B',345.5,2],
    ['Mark Teixeira','1B',339,4],
    ['Mitch Moreland','1B',297.5,1],
    ['Ben Paulsen','1B',244,1],
    ['John Jaso','1B',250,1],
    ['Matt Adams','1B',236,1],
    ['Chris Carter','1B',300.5,1],
    ['Mike Napoli','1B',274,1],
    ['Yonder Alonso','1B',267.5,1],
    ['Brandon Moss','1B',239,1],
    ['A.J. Reed','1B',226.5,1],
    ['Logan Morrison','1B',270,1]
  ]

  third_base_data = [
    ['Kris Bryant','3B',479.5,37],
    ['Josh Donaldson','3B',511,35],
    ['Nolan Arenado','3B',483,30],
    ['Josh Harrison','3B',345.5,6],
    ['Todd Frazier','3B',437.5,20],
    ['Matt Duffy','3B',342.5,6],
    ['Adrian Beltre','3B',406,15],
    ['Kyle Seager','3B',441.5,18],
    ['Maikel Franco','3B',417.5,15],
    ['Justin Turner','3B',319,4],
    ['Evan Longoria','3B',402,12],
    ['Pedro Alvarez','3B',329.5,1],
    ['Danny Valencia','3B',290.5,2],
    ['Yasmany Tomas','3B',268.5,1],
    ['David Wright','3B',317,2],
    ['Trevor Plouffe','3B',352,3],
    ['Mike Moustakas','3B',361,4],
    ['Adonis Garcia','3B',249,2],
    ['Nick Castellanos','3B',336.5,2],
    ['Lonnie Chisenhall','3B',259.5,1],
    ['Yunel Escobar','3B',314.5,1],
    ['Chase Headley','3B',325.5,1],
    ['Jake Lamb','3B',290.5,1],
    ['Hector Olivera','3B',252.5,1],
    ['Cody Asche','3B',220,1],
    ['Travis Shaw','3B',267,1]
  ]

  second_base_data = [
    ['Jose Altuve','2B',498.5,35],
    ['Dee Gordon','2B',444.5,26],
    ['Robinson Cano','2B',439.5,21],
    ['Matt Carpenter','2B',446.5,19],
    ['Ian Kinsler','2B',428.5,16],
    ['Daniel Murphy','2B',394.5,12],
    ['Jason Kipnis','2B',409,13],
    ['DJ LeMahieu','2B',355.5,8],
    ['Rougned Odor','2B',393,12],
    ['Kolten Wong','2B',364,7],
    ['Brian Dozier','2B',439.5,16],
    ['Howie Kendrick','2B',327,4],
    ['Anthony Rendon','2B',392,11],
    ['Ben Zobrist','2B',364,8],
    ['Dustin Pedroia','2B',375.5,8],
    ['Brandon Phillips','2B',338.5,5],
    ['Neil Walker','2B',362.5,7],
    ['Joe Panik','2B',351.5,3],
    ['Cesar Hernandez','2B',273.5,1],
    ['Martin Prado','2B',331,2],
    ['Brett Lawrie','2B',312,2],
    ['Javier Baez','2B',216,1],
    ['Logan Forsythe','2B',323.5,2],
    ['Brock Holt','2B',258.5,1],
    ['Devon Travis','2B',254,1],
    ['Jonathan Schoop','2B',285,1],
    ['Scooter Gennett','2B',277.5,1],
    ['Cory Spangenberg','2B',268.5,1],
    ['Trea Turner','2B',209,1],
    ['Yangervis Solarte','2B',328.5,1],
    ['Johnny Giavotella','2B',284,1],
    ['Jace Peterson','2B',277.5,1],
    ['Jedd Gyorko','2B',190.5,1]
  ]

  ss_data = [
    ['Manny Machado','SS',490,32],
    ['Carlos Correa','SS',482.5,31],
    ['Xander Bogaerts','SS',407,18],
    ['Francisco Lindor','SS',413.5,15],
    ['Corey Seager','SS',389,12],
    ['Elvis Andrus','SS',378.5,6],
    ['Troy Tulowitzki','SS',358,11],
    ['Ketel Marte','SS',350.5,5],
    ['Jean Segura','SS',343,4],
    ['Erick Aybar','SS',347.5,3],
    ['Ian Desmond','SS',330.5,5],
    ['Alcides Escobar','SS',350,3],
    ['Marcus Semien','SS',367,6],
    ['Starlin Castro','SS',330.5,3],
    ['Jung-Ho Kang','SS',294,3],
    ['Brad Miller','SS',330,2],
    ['Addison Russell','SS',321,3],
    ['Alexei Ramirez','SS',336.5,1],
    ['Brandon Crawford','SS',332.5,2],
    ['Jose Iglesias','SS',272.5,1],
    ['Eugenio Suarez','SS',305.5,1],
    ['Jonathan Villar','SS',248,1],
    ['Jose Reyes','SS',220,1],
    ['Trevor Story','SS',258.5,1],
    ['Jose Peraza','SS',206,1],
    ['Asdrubal Cabrera','SS',307.5,1],
    ['Andrelton Simmons','SS',332.5,1],
    ['Eduardo Escobar','SS',271.5,1],
    ['Didi Gregorius','SS',302,1],
    ['Adeiny Hechavarria','SS',275,1],
    ['Jhonny Peralta','SS',226,1],
    ['Jed Lowrie','SS',285.5,1],
    ['Wilmer Flores','SS',218.5,1],
    ['Orlando Arcia','SS',197,1],
    ['Zack Cozart','SS',273,1],
    ['Freddy Galvis','SS',251,1],
    ['Jose Ramirez','SS',197,1],
    ['Jordy Mercer','SS',246,1],
    ['Danny Santana','SS',154.5,1]
  ]

  of_data = [
    ['Mike Trout','OF',578,56],
    ['Bryce Harper','OF',541,47],
    ['Mookie Betts','OF',516.5,36],
    ['Andrew McCutchen','OF',512.5,36],
    ['Starling Marte','OF',432,28],
    ['Giancarlo Stanton','OF',470.5,34],
    ['Charlie Blackmon','OF',446.5,25],
    ['J.D. Martinez','OF',435,30],
    ['Lorenzo Cain','OF',405,21],
    ['Ben Revere','OF',384.5,15],
    ['Jose Bautista','OF',508.5,31],
    ['Ryan Braun','OF',424,24],
    ['Justin Upton','OF',452,27],
    ['Nelson Cruz','OF',434.5,27],
    ['Adam Jones','OF',432.5,26],
    ['Jason Heyward','OF',445.5,21],
    ['Michael Brantley','OF',403.5,17],
    ['George Springer','OF',415,23],
    ['Yasiel Puig','OF',418.5,21],
    ['Carlos Gomez','OF',399.5,20],
    ['Yoenis Cespedes','OF',433,25],
    ['Billy Hamilton','OF',375,11],
    ['Carlos Gonzalez','OF',406.5,22],
    ['Christian Yelich','OF',402.5,16],
    ['David Peralta','OF',397,16],
    ['Miguel Sano','OF',416.5,23],
    ['Jacoby Ellsbury','OF',390.5,13],
    ['Adam Eaton','OF',407,15],
    ['Hunter Pence','OF',398,16],
    ['Matt Kemp','OF',388,17],
    ['Gregory Polanco','OF',411.5,14],
    ['Billy Burns','OF',372,9],
    ['Gerardo Parra','OF',363,11],
    ['Kevin Pillar','OF',372,10],
    ['Ender Inciarte','OF',359.5,8],
    ['Kole Calhoun','OF',394,15],
    ['Corey Dickerson','OF',343.5,10],
    ['Josh Reddick','OF',390.5,11],
    ['Denard Span','OF',354,5],
    ['Shin-Soo Choo','OF',385,12],
    ['Melky Cabrera','OF',374.5,9],
    ['Brett Gardner','OF',381,11],
    ['Alex Gordon','OF',374.5,9],
    ['Stephen Piscotty','OF',353.5,7],
    ['Jay Bruce','OF',391.5,12],
    ['Kevin Kiermaier','OF',347.5,5],
    ['Randal Grichuk','OF',339.5,9],
    ['Mark Trumbo','OF',337,8],
    ['Delino DeShields','OF',344,5],
    ['Odubel Herrera','OF',310.5,3],
    ['Curtis Granderson','OF',387.5,9],
    ['Byron Buxton','OF',308.5,3],
    ['Dexter Fowler','OF',362.5,6],
    ['Michael Conforto','OF',348.5,7],
    ['Marcell Ozuna','OF',331.5,6],
    ['Khris Davis','OF',342,7],
    ['Steven Souza','OF',311.5,5],
    ['Wil Myers','OF',335.5,1],
    ['Domingo Santana','OF',325.5,6],
    ['Jayson Werth','OF',319,4],
    ['Norichika Aoki','OF',319,1],
    ['Avisail Garcia','OF',288,1],
    ['Nick Markakis','OF',359,3],
    ['Eddie Rosario','OF',299.5,2],
    ['Rajai Davis','OF',244,1],
    ['Jarrod Dyson','OF',227,1],
    ['Chris Colabello','OF',256,1],
    ['Joc Pederson','OF',346.5,4],
    ['Carlos Beltran','OF',312.5,2],
    ['Austin Jackson','OF',288,1],
    ['Leonys Martin','OF',275,1],
    ['Jorge Soler','OF',257,1],
    ['Cameron Maybin','OF',259.5,1],
    ['A.J. Pollock','OF',207.5,1],
    ['Colby Rasmus','OF',293.5,2],
    ['Jackie Bradley','OF',300,1],
    ['Socrates Brito','OF',243.5,1],
    ['Angel Pagan','OF',249,1],
    ['Michael Taylor','OF',211.5,1],
    ['Chris Owings','OF',227.5,1],
    ['Chris Coghlan','OF',253.5,1],
    ['Anthony Gose','OF',203,1],
    ['Aaron Hicks','OF',227.5,1],
    ['Gregor Blanco','OF',198,1],
    ['Mark Canha','OF',214.5,1],
    ['Marlon Byrd','OF',202,1],
    ['Josh Hamilton','OF',189.5,1],
    ['Seth Smith','OF',262,1],
    ['Scott Schebler','OF',217.5,1],
    ['Dalton Pompey','OF',185,1],
    ['Michael Saunders','OF',202.5,1],
    ['Adam Duvall','OF',193.5,1],
    ['Jake Marisnick','OF',164,1],
    ['Tommy Pham','OF',174,1]
  ]

  dh_data = [
    ['Prince Fielder','DH',428.5,17],
    ['David Ortiz','DH',431.5,17],
    ['Kendrys Morales','DH',374,11]
  ]

  player_data = list(itertools.chain.from_iterable([c_data, first_base_data, third_base_data, second_base_data, ss_data, of_data, dh_data]))
  players = [[]] * len(player_data)

  # objective: maximize points
  objective = solver.Objective()
  for i in range(0, len(player_data)):
    players[i] = solver.IntVar(0.0, 1.0, player_data[i][0])
    objective.SetCoefficient(players[i], player_data[i][2])
  objective.SetMaximization()

  # total cost must be at most $190
  max_cost = solver.Constraint(0, 190)
  for j in range(0, len(players)):
    max_cost.SetCoefficient(players[j], player_data[j][3])

    ###
    # FIX! these indices rely on the order of the data definitions above
    ###
    c_index = 0
    first_base_index = c_index + len(c_data)
    third_base_index = first_base_index + len(first_base_data)
    second_base_index = third_base_index + len(third_base_data)
    ss_index = second_base_index + len(second_base_data)
    of_index = ss_index + len(ss_data)
    dh_index = of_index + len(of_data)

  # must have 1-2 C (C + DH)
  max_c = solver.Constraint(1,2)
  for j in range(c_index, c_index + len(c_data)):
    max_c.SetCoefficient(players[j], 1)

  # must have 1-3 1B (1B + CI + DH)
  max_1b = solver.Constraint(1,3)
  for j in range(first_base_index, first_base_index + len(first_base_data)):
    max_1b.SetCoefficient(players[j], 1)

  # must have 1-3 3B (3B + CI + DH)
  max_3b = solver.Constraint(1,3)
  for j in range(third_base_index, third_base_index + len(third_base_data)):
    max_3b.SetCoefficient(players[j], 1)

  # must have exactly 3 1B/3B (CI)
  max_ci = solver.Constraint(3,3)
  for j in range(first_base_index, first_base_index + len(first_base_data + third_base_data)):
    max_ci.SetCoefficient(players[j], 1)

  # must have 1-3 2B (2B + MI + DH)
  max_2b = solver.Constraint(1,3)
  for j in range(second_base_index, second_base_index + len(second_base_data)):
    max_2b.SetCoefficient(players[j], 1)

  # must have 1-3 SS (SS + MI + DH)
  max_ss = solver.Constraint(1,3)
  for j in range(ss_index, ss_index + len(ss_data)):
    max_ss.SetCoefficient(players[j], 1)

  # must have exactly 3 2B/SS (MI)
  max_mi = solver.Constraint(3,3)
  for j in range(second_base_index, second_base_index + len(second_base_data + ss_data)):
    max_mi.SetCoefficient(players[j], 1)

  # must have 5-6 OF (OF + DH)
  max_of = solver.Constraint(5,6)
  for j in range(of_index, of_index + len(of_data)):
    max_of.SetCoefficient(players[j], 1)

  # must have exactly 13 players (any position)
  max_players = solver.Constraint(13, 13)
  for j in range(0, len(players)):
    max_players.SetCoefficient(players[j], 1)

  # Solve the system.
  status = solver.Solve()
  total_value = 0
  cost = 0

  print("Optimal Lineup: ")
  for i in range(0, len(players)):
    if (players[i].solution_value() > 0):
      total_value += player_data[i][2]
      cost += player_data[i][3]
      print("{} {}, ${}".format(player_data[i][1], player_data[i][0],player_data[i][3]))

  print("\nTotal Pts: {}".format(total_value))
  print("Cost: {}".format(cost))
if __name__ == '__main__':
  main()