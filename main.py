from mit_library.production import forward_chain
from rules_base import TOURISTS_RULES_LIST, TOURISTS_RULES_DICT
from tools import classifiy_intermediate_rules, classifiy_species_rules, remove_duplicated_questions, ask_question, check_new_entry
import pprint
import os

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint

data_list = []
old_data_list = []

VERBOSE = os.getenv("VERBOSE")

intermediate_rules, intermediate_specific_rules = classifiy_intermediate_rules(
    rules_dict=TOURISTS_RULES_DICT,
    tourist_name="tourist_1"
)

#* Ask intermediate questions
for question_key, question_value in intermediate_rules.items():
    questions = intermediate_rules[question_key]
    questions = remove_duplicated_questions(questions_list=questions)

    questions, intermediate_specific_rules = check_new_entry(
        data_list=data_list,
        rules=intermediate_specific_rules,
        questions=questions,
        old_data_list=old_data_list
    )
    old_data_list.extend(data_list)

    data_list = ask_question(data_list=data_list, questions_list=questions)

# * Ask specific questions
*_, intermediate_result = forward_chain(rules=TOURISTS_RULES_LIST, data=data_list, verbose=True)

print(f"INTERMEDIATE RESULT:  {intermediate_result}") if VERBOSE else None
data_list = [intermediate_result]
old_data_list = []

species_rules, species_specific_rules = classifiy_species_rules(
    rules_dict=TOURISTS_RULES_DICT,
    tourist_name="tourist_1",
    intermediate_result=intermediate_result
)

for question_key, question_value in species_rules.items():
    questions = species_rules[question_key]
    questions = remove_duplicated_questions(questions_list=questions)
    print(f"\n\nQUESTIONS ASK LIST: {questions} \n \n") if VERBOSE else None

    questions, species_specific_rules = check_new_entry(
        data_list=data_list,
        rules=species_specific_rules,
        questions=questions,
        old_data_list=old_data_list
    )

    old_data_list.extend(data_list)

    data_list = ask_question(data_list=data_list, questions_list=questions)

pprint(forward_chain(rules=TOURISTS_RULES_LIST, data=data_list, verbose=True))

