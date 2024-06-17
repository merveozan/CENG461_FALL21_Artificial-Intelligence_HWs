Amber_domain_list_of_food = ["eggroll","fries","gingerbread","hummus"]
Brian_domain_list_of_food = ["eggroll","fries","gingerbread","hummus"]
Chris_domain_list_of_food = ["eggroll","fries","gingerbread","hummus"]
Diane_domain_list_of_food = ["eggroll","fries","gingerbread","hummus"]

Amber_domain_list_of_time = [4.30,4.35,4.40,4.45]
Brian_domain_list_of_time = [4.30,4.35,4.40,4.45]
Chris_domain_list_of_time = [4.30,4.35,4.40,4.45]
Diane_domain_list_of_time = [4.30,4.35,4.40,4.45]

Amber = {"food": "",
         "arrival_time":0
         }
Brian = {"food": "",
         "arrival_time":0
         }
Chris = {"food": "",
         "arrival_time":0
         }
Diane = {"food": "",
         "arrival_time":0
         }
def actual_value_assigment(lcv,index,domain):
    if type(lcv) == str:
        if index==0 :
            Amber["food"] =lcv
        elif index == 1:
            Brian["food"] = lcv
        elif index == 2:
            Chris["food"] = lcv
        elif index == 3:
            Diane["food"] = lcv
        for i in range(len(domain)):
            if lcv in domain[i] and index != i:
                domain[i].remove(lcv)
        domain[index] = [""]

    elif type(lcv) == type(0.0) :
        if index==0 :
            Amber["arrival_time"] =lcv
        elif index == 1:
            Brian["arrival_time"] = lcv
        elif index == 2:
            Chris["arrival_time"] = lcv
        elif index == 3:
            Diane["arrival_time"] = lcv
        for i in range(len(domain)):
            if lcv in domain[i] and index != i:
                domain[i].remove(lcv)
        domain[index] = [""]


def apply_arc_consistency(lcv,index):
    if "gingerbread" in Chris_domain_list_of_food:
        Chris_domain_list_of_food.remove("gingerbread")

    if "hummus" in Diane_domain_list_of_food:
        Diane_domain_list_of_food.remove("hummus")

    for i in Brian_domain_list_of_food :
        if i != "fries" or i!="hummus":
            Brian_domain_list_of_food.remove(i)
        if "hummus" not in Brian_domain_list_of_food:
            Brian_domain_list_of_food.append("hummus")

    if index == 1 and lcv == 'hummus':
        Chris_domain_list_of_food.remove("fries")

    if 4.45 in Amber_domain_list_of_time:
        Amber_domain_list_of_time.remove(4.45)

    if 4.40 in Brian_domain_list_of_time:
        Brian_domain_list_of_time.remove(4.40)

    if 4.30 in Brian_domain_list_of_time:
        Brian_domain_list_of_time.remove(4.30)

    if 4.40 in Chris_domain_list_of_time:
        Chris_domain_list_of_time.remove(4.40)
    if 4.30 in Diane_domain_list_of_time:
        Diane_domain_list_of_time.remove(4.30)

    if Brian["food"]=="hummus" and 4.45 in Brian_domain_list_of_time :
        Brian_domain_list_of_time.remove(4.45)

    if Brian["arrival_time"] !=0 :
        for i in Amber_domain_list_of_time:
           if i != (Brian["arrival_time"]-0.05):
                Amber_domain_list_of_time.remove(i)

    if Brian["food"] == "hummus" and Amber["arrival_time"] == 4.30:
        if ("fries" in Amber_domain_list_of_food):
            Amber_domain_list_of_food.remove("fries")

    Domain_lists_of_time = []
    Domain_lists_of_time.append(Amber_domain_list_of_time)
    Domain_lists_of_time.append(Brian_domain_list_of_time)
    Domain_lists_of_time.append(Chris_domain_list_of_time)
    Domain_lists_of_time.append(Diane_domain_list_of_time)

    Domain_lists_of_food = []
    Domain_lists_of_food.append(Amber_domain_list_of_food)
    Domain_lists_of_food.append(Brian_domain_list_of_food)
    Domain_lists_of_food.append(Chris_domain_list_of_food)
    Domain_lists_of_food.append(Diane_domain_list_of_food)
    return Domain_lists_of_food,Domain_lists_of_time

def print_domain_list():
    print("\n")
    print("Domains")
    print("Food domains of party-goers:")
    print("Amber Domain List of Food : ", Amber_domain_list_of_food)
    print("Brian Domain List of Food : ", Brian_domain_list_of_food)
    print("Chris Domain List of Food : ", Chris_domain_list_of_food)
    print("Diane Domain List of Food : ", Diane_domain_list_of_food)
    print("\n")
    print("Time domains of party-goers:")
    print("Amber Domain List of Time : ", Amber_domain_list_of_time)
    print("Brian Domain List of Time : ", Brian_domain_list_of_time)
    print("Chris Domain List of Time : ", Chris_domain_list_of_time)
    print("Diane Domain List of Time : ", Diane_domain_list_of_time)



def print_actual_values():
    print("\n")
    print("Variable-values assigment ")
    print("Amber : ", Amber)
    print("Brian : ", Brian)
    print("Chris : ", Chris)
    print("Diane : ", Diane)
    print("\n")

def assigment_check(i,domain):
    count = 0
    new_list = copy_list(domain)
    for j in new_list:
        if i in j:
            j.remove(i)
    for k in new_list:
        count += len(k)
    return count

def copy_list(food_domain):
    new_list = []
    for i in food_domain:
        sub_list = []
        for j in i:
            sub_list.append(j)
        new_list.append(sub_list)

    return new_list

def find_var_mrv(domain):
    min_var = []
    min_len = 100
    for var in domain:
        if len(var) < min_len and var != [""] :
            min_len = len(var)
            min_var = var
    return min_var,domain.index(min_var)

def find_val_lcv(domain,min_variables,index):
    actual_count = 0
    lcv = ""
    temp = min_variables
    domain.remove(min_variables)

    for i in range(len(min_variables)):
        count =assigment_check(min_variables[i],domain)
        if count>actual_count:
            actual_count=count
            lcv = min_variables[i]

    domain.insert(index,temp)
    return lcv, index



food_domain,time_domain = apply_arc_consistency("",-1)
print_domain_list()
while(True):

    min_variables_food,index_food = find_var_mrv(food_domain)
    lcv_food,index_food = find_val_lcv(food_domain,min_variables_food,index_food)
    apply_arc_consistency(lcv_food,index_food)
    if Amber['food'] != "" and Brian['food'] != "" and Chris['food'] != "" and Diane['food'] != "" :
        if Amber['arrival_time'] !=0 and Brian['arrival_time'] !=0 and Chris['arrival_time'] !=0 and Diane['arrival_time'] !=0 :
            break
    print("Arc consistency is checked")
    print_domain_list()

    for i in food_domain:
        if len(i) == 1:
            actual_value_assigment(lcv_food,index_food,food_domain)
    print_domain_list()
    print_actual_values()
    if Amber['food'] != "" and Brian['food'] != "" and Chris['food'] != "" and Diane['food'] != "" :
        if Amber['arrival_time'] !=0 and Brian['arrival_time'] !=0 and Chris['arrival_time'] !=0 and Diane['arrival_time'] !=0 :
            break

    apply_arc_consistency([],-1)
    print("Arc consistency is checked")
    print_domain_list()

    if Amber['food'] != "" and Brian['food'] != "" and Chris['food'] != "" and Diane['food'] != "" :
        if Amber['arrival_time'] !=0 and Brian['arrival_time'] !=0 and Chris['arrival_time'] !=0 and Diane['arrival_time'] !=0 :
            break
    min_variables_time, index_time = find_var_mrv(time_domain)
    lcv_time, index_time = find_val_lcv(time_domain, min_variables_time, index_time)

    for i in time_domain:
        if len(i) == 1:
            actual_value_assigment(lcv_time,index_time,time_domain)

    apply_arc_consistency([], -1)
    print_domain_list()
    print_actual_values()
    if Amber['food'] != "" and Brian['food'] != "" and Chris['food'] != "" and Diane['food'] != "" :
        if Amber['arrival_time'] !=0 and Brian['arrival_time'] !=0 and Chris['arrival_time'] !=0 and Diane['arrival_time'] !=0 :
            break