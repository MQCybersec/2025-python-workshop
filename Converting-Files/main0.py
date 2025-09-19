# Slide 1 for Automation

def ReadTextFile(path):
    with open(path, "r") as f:
        lines = f.readlines()
        print(lines[0])
        print(lines[1])
        print(lines)

        # alternatively, we can also do:
        for line in lines:
            print(line.strip("\\\n")) 
            # using line.strip \\\n removes the '\n' from each line

ReadTextFile("./data.txt")