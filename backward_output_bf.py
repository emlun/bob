#/usr/bin/python3

# License: GNU General Public License, version 2 or later.
# Outputs a Brainfuck program that outputs the input given on STDIN.

import sys

width = 80

if len(sys.argv) > 1:
    width = int(sys.argv[1])

desired_output_code_sequence = []
for line in sys.stdin:
    for c in line:
        desired_output_code_sequence.append(ord(c))

output_language = list(set(desired_output_code_sequence))
output_language.sort()

for i in range(0, len(output_language)):
    print('+'*output_language[i], '>')

current_register = len(output_language)-1
print('<')
output_lines = ['']
def output(c):
    output_lines[-1] += c
    if len(output_lines[-1]) == width:
        output_lines.append('')


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
