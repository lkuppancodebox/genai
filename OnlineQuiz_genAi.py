import json
import re
import sys
import yaml
from bardapi import BardCookies

def send_query_to_ai (prompt):
    cookie_dict = {
        "__Secure-1PSID": "___enter_key__from__Cookie",
        "__Secure-1PSIDTS": "___enter_key__from__Cookie",
    }

    try:
        bard = BardCookies(cookie_dict=cookie_dict)
        response = bard.get_answer(prompt)
        return (response['content'])
    except:
        print("Cookie update required")
        return None

def gen_prompt(topic, n) :

    prompt_input = '''
    {} Quiz on the topic {}\n 
    ### 4 options required with a correct answer ### \n
    Required in YAML Format like below ###\n
    ---
    '1':
      question: ""
      options:
        a: ""
        b: ""
        c: ""
        d: ""
      answer: 
    '2':
    and so on.."" \n
    ### exclude ```yaml```
      '''.format(n, topic)

    return prompt_input

def get_quiz_dict(topic, count):
    prompt_input = gen_prompt(topic, count)
    while True:
        resp = send_query_to_ai(prompt_input)

        if not resp:
            sys.exit()

        try:
            quiz_dict = yaml.safe_load(resp)
            return quiz_dict
            break
        except:
            print("Retrying..")


if __name__ == '__main__':

    topic = input("Enter Topic: ")
    n = input("Number of questions: ")
    quiz_dict = get_quiz_dict(topic, n)

    print("----------------------------------------------------")
    print("\tOnline Quiz Started")
    print("----------------------------------------------------\n")

    score=0
    total_count=0

    for key, value in quiz_dict.items():
        total_count+=1
        print("\nquiz: {}".format(key))
        print(quiz_dict[key]["question"])

        for k, v in quiz_dict[key]["options"].items():
            print("{}: {}".format(k, v))

        ans = input("Enter Answer: (a/b/c/d): ")

        if quiz_dict[key]["answer"] == ans :
            print("[\u2713] CORRECT")
            score+=1
        else:
            print("[X] Wrong\n")
            print("Correct Answer is {}\n\n".format(quiz_dict[key]["answer"]))

    print("\n\n---------------------------")
    print("Your SCORE: {} %".format((score/total_count)*100))
    print("---------------------------")
