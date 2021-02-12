import random
import os
from mit_library.production import OR

def classifiy_intermediate_rules(rules_dict, tourist_name):
    intermediate_rules = {
        "blood_type": [],
        "nr_of_limbs": [],
        "body_specifics": []
    }
    intermediate_specific_rules = {}

    for rule_key, rules in rules_dict["intermediate_rules"].items():
        i = 0
        intermediate_specific_rules[rule_key] = []

        for rule in rules.antecedent():
            rule = rule.replace("(?x)", tourist_name)

            if i == 0:
                intermediate_rules["blood_type"].append(rule)
            elif i == 1:
                intermediate_rules["nr_of_limbs"].append(rule)
            elif i == 2:
                intermediate_rules["body_specifics"].append(rule)
            i = i + 1

            #other logic
            intermediate_specific_rules[rule_key].append(rule)


    return intermediate_rules, intermediate_specific_rules


def classifiy_species_rules(rules_dict, tourist_name, intermediate_result):
    intermediate_result = intermediate_result.replace(tourist_name, "(?x)")

    species_rules = {
        "pedal_type": [],
        "height": [],
        "skin_color": [],
        "extra": []
    }
    species_specific_rules = {}

    for rule_key, rules in rules_dict["species_rules"].items():
        i = 0

        if intermediate_result not in rules.antecedent():
            continue

        species_specific_rules[rule_key] = []

        for rule in rules.antecedent():
            if isinstance(rule, OR):
                or_rules = []
                for or_rule in rule:
                    or_rules.append(or_rule.replace("(?x)", tourist_name))
                rule = or_rules
            else:
                rule = rule.replace("(?x)", tourist_name)


            if i == 1:
                species_rules["pedal_type"].append(rule)
            elif i == 2:
                species_rules["height"].append(rule)
            elif i == 3:
                species_rules["skin_color"].append(rule)
            elif i == 4:
                species_rules["extra"].append(rule)

            i = i + 1

            #other logic
            species_specific_rules[rule_key].append(rule)

    return species_rules, species_specific_rules


def check_new_entry(data_list, rules, questions, old_data_list):
    verbose = bool(os.getenv("VERBOSE"))
    possible_cases = []
    new_questions = []
    print(f"OLD RULES:   {rules} \n") if verbose else None

    for data in data_list:
        if data in old_data_list:
            continue
        for rule_key, rule_value in rules.items():
            if isinstance(rule_value, list):
                if any(data in sl for sl in rule_value):
                    possible_cases.append(rule_key)
            else:
                if data in rule_value:
                    possible_cases.append(rule_key)
            print(f"Data: {data}") if VERBOSE else None
            print(f"Rule: {rule_value}") if VERBOSE else None
        print(f"POSSIBLE CASES: {possible_cases}") if VERBOSE else None

        #check finished
        possible_cases = remove_duplicated_questions(questions_list=possible_cases)
        new_rules = {}
        for case in possible_cases:
            new_rules[case] = rules[case]

        print(f"NEW RULES:   {new_rules} \n") if verbose else None
        print(f"OLD QUESTIONS:   {questions} \n") if verbose else None
        for new_rules_value in new_rules.values():
            for x in questions:
                if x in new_rules_value:
                    new_questions.append(x)

        print(f"NEW QUESTIONS:   {new_questions}") if verbose else None
        possible_cases = []
        rules = new_rules
        questions = new_questions

    return questions, rules




def remove_duplicated_questions(questions_list):
    seen = list()
    for x in questions_list:
        if isinstance(x, list):
            seen.append(x)
            continue
        elif x not in seen:
            seen.append(x)

    return seen


def ask_question(data_list, questions_list):
    new_questions_list = questions_list
    if questions_list == []:
        return data_list
    while True:
        question = random.choice(new_questions_list)
        if isinstance(question, list):
            index = 0
            print_str = "Choose the right answer: \n"
            answer_dict = {}
            for or_question in question:
                print_str += f"{index}: {or_question}? \n"
                answer_dict[index] = or_question
                index += 1
            print_str += f"{index}: None of those"

            print(print_str)

            inp = input()
            if inp == index:
                inp = "no"
            else:
                question = answer_dict.get(int(inp))
                inp = "yes"
        else:
            print(question + "?")
            inp = input()

        if inp == "yes":
            data_list.append(question)
            return data_list
        if inp == "no":
            if len(new_questions_list) == 1:
                print("[INFO] No more category questions exist. Please choose something from them!")
                new_questions_list = questions_list
            else:
                new_questions_list.remove(question)
        else:
            print("[INFO] Invalid answer. Answer should be 'yes' or 'no'!")

