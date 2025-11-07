#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx


rules = [
    ([("problem","power_light_off")], ("solution","check_power_supply")),
    ([("problem","computer_not_starting")], ("solution","check_RAM")),
    ([("problem","blank_display")], ("solution","check_monitor_cable")),
    ([("problem","strange_beep")], ("solution","check_hard_disk"))
]

def forward_chain(facts, rules):
    inferred = set(facts)  # Start with known facts (user problems)
    changed = True    
    while changed: # Keep checking until no new facts found
        changed = False
        for p, c in rules:  # For each rule
            if all(x in inferred for x in p) and c not in inferred:
                inferred.add(c) # Add new conclusion
                changed = True
    return inferred

facts=[]
while True:
    s=input("Enter problem (done to stop): ").strip().lower()
    if s=="done": break
    facts.append(("problem",s))

res=forward_chain(facts,rules)
print("\nSuggested Solutions:")
for r in res:
    if r[0]=="solution": print("-",r[1])


 #Enter problem (done to stop): BLANK_DISPLAY
#Enter problem (done to stop): done

#Suggested Solutions:
#- check_monitor_cable   

'''
Forward chaining is a reasoning method that starts with the known facts and applies rules to infer (derive) new facts — until a goal is reached.
If it is raining → then the ground is wet.
If the ground is wet → then grass is slippery.

An Expert System is an AI program that uses human knowledge and reasoning rules to solve complex problems — just like a human expert in a specific field.
'''