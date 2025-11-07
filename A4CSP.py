# pip install python-constraint
#python.exe -m pip install --upgrade pip
#& "C:\Program Files\Python312\python.exe" -m pip install python-constraint
#& "C:\Program Files\Python312\python.exe" -m pip show python-constraint
#RERUN 
#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx



from constraint import Problem

teams = input("Enter team names (comma separated): ").split(',')
teams = [t.strip() for t in teams if t.strip()]  # clean spaces
slots = list(map(int, input("Enter slot numbers (comma separated): ").split(',')))
stadiums = input("Enter stadium names (comma separated): ").split(',')
stadiums = [s.strip() for s in stadiums if s.strip()]

matches = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i+1:]]

p = Problem()
p.addVariables(matches, [(s, st) for s in slots for st in stadiums])

# A team cannot play two matches in the same slot
for t in teams:
    team_matches = [m for m in matches if t in m]
    for i in range(len(team_matches)):
        for j in range(i+1, len(team_matches)):
            p.addConstraint(lambda a, b: a[0] != b[0], (team_matches[i], team_matches[j]))

# No two matches in same slot & stadium
for i in range(len(matches)):
    for j in range(i+1, len(matches)):
        p.addConstraint(lambda a, b: not (a[0] == b[0] and a[1] == b[1]), (matches[i], matches[j]))

# --- GET SOLUTIONS ---
sol = p.getSolutions()
print("\nTotal valid schedules:", len(sol))
if sol:
    print("Sample schedule:")
    for match, (slot, stadium) in sol[0].items():
        print(f"{match[0]} vs {match[1]} → Slot {slot}, Stadium {stadium}")
else:
    print("No valid schedules found.")



#OP
#Enter team names (comma separated): T1,T2,T3,T4
#Enter slot numbers (comma separated): 1,2,3
#Enter stadium names (comma separated): A,B
'''
Components of CSP
Variables:
The unknowns we need to assign values to.
Example: X, Y, Z.

Domain:
The set of possible values each variable can take.
Example: {Red, Green, Blue}.

Constraints:
The conditions that must be satisfied.
Example: X ≠ Y, Y ≠ Z, X ≠ Z.

Examples
Sudoku Puzzle
'''