#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx


class GoalStackPlanner:
    def __init__(self, init, goal, acts):
        self.state = set(init)
        self.goal = goal
        self.actions = acts
        self.stack = list(goal)
        self.plan = []

    def sat(self, f):
        return f in self.state

    def apply(self, a):
        [self.state.discard(x) for x in a["del"]]
        [self.state.add(x) for x in a["add"]]

    def plan_steps(self):
        while self.stack:
            t = self.stack.pop()
            if isinstance(t, str):  # it's a goal
                if not self.sat(t):
                    for a in self.actions:
                        if t in a["add"]:
                            self.stack.append(a)
                            self.stack.extend(a["pre"])
                            break
            else:  # it's an action
                if all(p in self.state for p in t["pre"]):
                    self.apply(t)
                    self.plan.append(t["name"])
        return self.plan


# ---------- USER INPUT ----------
init = input("Initial facts (comma separated): ").split(',')
goal = input("Goal facts (comma separated): ").split(',')
n = int(input("Number of actions: "))
acts = []

for i in range(n):
    print(f"\nAction {i+1}:")
    name = input(" Name: ")
    pre = input(" Preconditions (comma separated): ").split(',')
    add = input(" Add list (comma separated): ").split(',')
    dele = input(" Delete list (comma separated): ").split(',')
    acts.append({"name": name, "pre": pre, "add": add, "del": dele})

planner = GoalStackPlanner(init, goal, acts)
print("\nGenerated Plan:", planner.plan_steps())


#Initial facts (comma separated): A_on_Table,B_on_Table,Clear_A,Clear_B
#Goal facts (comma separated): A_on_B
#Number of actions: 1

#Action 1:
 #Name: Stack_A_on_B
 #Preconditions (comma separated): A_on_Table,Clear_A,Clear_B
 #Add list (comma separated): A_on_B
 #Delete list (comma separated): A_on_Table,Clear_B