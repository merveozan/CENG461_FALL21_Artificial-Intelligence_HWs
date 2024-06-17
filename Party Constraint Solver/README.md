# Party Constraint Solver

This repository contains a Python program designed to solve a Constraint Satisfaction Problem (CSP) using arc-consistency, Minimum Remaining Values (MRV), and Least Constraining Value (LCV) heuristics. The specific problem involves determining what each of Macy's friends brought to a surprise party and what time they arrived, based on a set of clues.

## Problem Description

Macy's friends threw her a surprise party. Using the clues provided, the goal is to determine what each friend brought and what time they arrived.

### Clues:
1. Of Brian and the party-goer who arrived at 4:40 pm, one brought the hummus and the other brought the fries.
2. Amber arrived 5 minutes before Brian.
3. Chris, the participant who brought the gingerbread, and the friend who arrived at 4:40 pm are all different people.
4. Diane arrived 5 minutes after the friend who brought the hummus.

## Solution

The solution is implemented in Python and involves the following components:

- **Arc Consistency**: Ensures that the domains of the variables are consistent with the binary constraints.
- **Minimum Remaining Values (MRV)**: Selects the variable with the fewest legal values left.
- **Least Constraining Value (LCV)**: Chooses the value that leaves the most options open for the remaining variables.

## Functions

- `apply_arc_consistency(lcv, index)`: Applies arc-consistency to a domain based on a list of constraints.
- `find_var_mrv(domain)`: Selects a variable using the MRV approach.
- `find_val_lcv(domain, min_variables, index)`: Selects a value for a variable using the LCV approach.
- `actual_value_assigment(lcv, index, domain)`: Assigns the actual value to a variable and updates the domains.
- `print_domain_list()`: Prints the current domains of the variables.
- `print_actual_values()`: Prints the current assignments of the variables.
- `assigment_check(i, domain)`: Checks the number of remaining values after an assignment.
- `copy_list(food_domain)`: Copies a list to preserve the original during manipulation.

## Usage

To run the program, execute the `main.py` script:

```bash
python main.py
```

The script will print the domains after each arc-consistency check and variable assignments, eventually arriving at the solution.

## Output

```
Domains
Food domains of party-goers:
Amber Domain List of Food :  ['eggroll', 'fries', 'gingerbread', 'hummus']
Brian Domain List of Food :  ['eggroll', 'fries', 'gingerbread', 'hummus']
Chris Domain List of Food :  ['eggroll', 'fries', 'gingerbread', 'hummus']
Diane Domain List of Food :  ['eggroll', 'fries', 'gingerbread', 'hummus']

Time domains of party-goers:
Amber Domain List of Time :  [4.3, 4.35, 4.4, 4.45]
Brian Domain List of Time :  [4.3, 4.35, 4.4, 4.45]
Chris Domain List of Time :  [4.3, 4.35, 4.4, 4.45]
Diane Domain List of Time :  [4.3, 4.35, 4.4, 4.45]

...

Variable-values assignment
Amber :  {'food': 'gingerbread', 'arrival_time': 4.3}
Brian :  {'food': 'hummus', 'arrival_time': 4.35}
Chris :  {'food': 'eggroll', 'arrival_time': 4.45}
Diane :  {'food': 'fries', 'arrival_time': 4.4}
```

