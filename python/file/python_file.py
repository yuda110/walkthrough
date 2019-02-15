rf = open("input.txt", 'r')
lines = rf.read().splitlines()
formatted_lines = ['[test]{}[/test]'.format(i) for i in lines]

with open('output.txt', 'w') as wf:
    for l in formatted_lines:
        wf.write("{}\n".format(l))
