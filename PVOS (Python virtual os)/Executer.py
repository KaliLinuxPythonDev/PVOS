commands = ["exit"]

def execute_cmd(cmd):
    if cmd not in commands:
        print("Invalid Command!")

    elif cmd == "exit":
        exit()