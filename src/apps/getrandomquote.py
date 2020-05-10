import sys
import yaml
import random
import json

def main(argv):
    if len(argv) != 2:
        print("Usage: {} data.yaml".format(argv[0]))
        exit(64)

    with open(argv[1], 'rt', encoding='utf8') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    result = random.choice(data)
    print(json.dumps(result))
    

if __name__ == "__main__":
   main(sys.argv)
