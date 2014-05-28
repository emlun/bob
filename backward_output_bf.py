#/usr/bin/python3

# License: GNU General Public License, version 2 or later.
# Outputs a Brainfuck program that outputs the input given on STDIN.

import sys

width = 80

if len(sys.argv) > 1:
    width = int(sys.argv[1])

output_lines = ['']
def output(s):
    output_lines[-1] += s
    while len(output_lines[-1]) >= width:
        output_lines.append(output_lines[-1][width:])
        output_lines[-2] = output_lines[-2][:width]


desired_output_code_sequence = []
for line in sys.stdin:
    for c in line:
        desired_output_code_sequence.append(ord(c))

output_language = list(set(desired_output_code_sequence))
output_language.sort()

prev_value = 0
for i in range(0, len(output_language)):
    print('+'*(output_language[i] - prev_value))
    # Add current to next
    print('[->+>+<<]>>[-<<+>>]<')
    prev_value = output_language[i]
print('<')


current_register = len(output_language)-1
for i in desired_output_code_sequence:
    while i < output_language[current_register]:
        output('<')
        current_register -= 1
    while i > output_language[current_register]:
        output('>')
        current_register += 1
    output('.')

for line in output_lines:
    print(line)
