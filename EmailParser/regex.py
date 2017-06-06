import itertools
import re

def main():
    complete = 0
    user_dict = {}
    domain_dict = {}

    with open("mbox.txt", 'r') as hand:
        lines = hand.readlines()

    for line in lines:
        line = line.strip()
        # parse the info
        user = re.findall("^From ([^ ]*)@.*", line)
        domain = re.findall("^From .*@([^ ]*)", line)
        commit = re.findall("commit: r([0-9]*)", line)

        # if the user and domain name has been parsed, save the value from being overwritten
        if(user):
            u_name = user[0]
            d_name = domain[0]
            complete = 1

        # if all we need has been parsed, add it to the dict
        if(commit and complete == 1):
            c_num = commit[0]
            add_dict(user_dict, domain_dict, u_name, d_name, c_num)
            complete = 0

    # print the classified result
    print_dict(user_dict, domain_dict)


def add_dict(user_dict, domain_dict, u_name, d_name, c_num):
    # if the user / domain is not in the record, add it to the dict
    # and set its value as a list of commited versions
    if(u_name not in user_dict):
        user_dict[u_name] = list()
    user_dict[u_name].append(c_num)

    if(d_name not in domain_dict):
        domain_dict[d_name] = list()
    domain_dict[d_name].append(c_num)

def print_dict(user_dict, domain_dict):
    print("-" * 30)
    for key, value in user_dict.items():
        value.sort()
        print("User", key,"\ncommited versions:", " ".join((value)), '\n')
    print("-" * 30)
    for key, value in domain_dict.items():
        value.sort()
        print("Organization", key, "\ncommited versions:", " ".join((value)), '\n')

main()