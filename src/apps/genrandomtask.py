import sys
import yaml
import random
import json

def genrandomtask(data):
    template = random.choice(data['templates'])
    choices = {}
    mode = "task"
    for stream in template:
        out = ""
        buf = ""
        for char in stream:
            if char == "[":
                out += buf
                buf = ""
            elif char == ":":
                if mode == "task":
                    choice = random.choice(data[buf])
                    choices[buf] = choice
                elif mode == "solution":
                    choice = choices[buf]
                buf = ""
            elif char == "]":
                out += choice[buf]
                buf = ""
            else:
                buf += char
        out += buf
        if mode == "task":
           task = out[0].capitalize() + out[1:]
           mode = "solution"
        elif mode == "solution":
           solution = out[0].capitalize() + out[1:]

    return task, solution

def main(argv):
    if len(argv) != 2:
        print("Usage: {} data.yaml".format(argv[0]))
        exit(64)

    with open(argv[1], 'rt', encoding='utf8') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    task, solution = genrandomtask(data)
    print(json.dumps([task, solution]))
    

if __name__ == "__main__":
   main(sys.argv)
