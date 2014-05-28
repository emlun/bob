#/usr/bin/python3
# Outputs a Brainfuck program that outputs the input given on STDIN.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

import sys

WIDTH = 80

if len(sys.argv) > 1:
    WIDTH = int(sys.argv[1])

# Utility function for printing neatly aligned lines
output_lines = ['']
def output(s):
    output_lines[-1] += s
    while len(output_lines[-1]) >= WIDTH:
        output_lines.append(output_lines[-1][WIDTH:])
        output_lines[-2] = output_lines[-2][:WIDTH]


# Read STDIN into a list of character codes
desired_output_code_sequence = []
for line in sys.stdin:
    for c in line:
        desired_output_code_sequence.append(ord(c))


# Pre-initialize registers with character codes
output_language = list(set(desired_output_code_sequence))
output_language.sort()

prev_value = 0
for i in range(0, len(output_language)):
    output('+'*(output_language[i] - prev_value))
    # Add current to next
    output('[->+>+<<]>>[-<<+>>]<')
    prev_value = output_language[i]
output('<')


# Print the registers' values in the order specified by STDIN
current_register = len(output_language)-1
for i in desired_output_code_sequence:
    while i < output_language[current_register]:
        output('<')
        current_register -= 1
    while i > output_language[current_register]:
        output('>')
        current_register += 1
    output('.')


# Actually print stuff
for line in output_lines:
    print(line)
