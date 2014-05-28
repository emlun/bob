Backward Output Brainfuck
=========================

Nerd sniped myself after seeing [this Code Golf answer][codegolf]. This script
takes input on STDIN and outputs a [Brainfuck][bf] program that outputs the
input. It also accepts an optional command line argument that specifies the line
with of the output (default: 80).

Example:

    $ echo '      ++++         +++
        +[>++++    ++[>+<-][
       <]<  -]>   >++    +++
      +.-   ---   ---    ---
     --.+++++++         +++
            +++       .++
            +++      +.-
            ---    -----.--.' | python backward_output_bf.py

Output:

    ++++++++++[->+>+<<]>>[-<<+>>]<++++++++++++++++++++++[->+>+<<]>>[-<<+>>]<++++++++
    +++[->+>+<<]>>[-<<+>>]<++[->+>+<<]>>[-<<+>>]<+[->+>+<<]>>[-<<+>>]<++++++++++++++
    [->+>+<<]>>[-<<+>>]<++[->+>+<<]>>[-<<+>>]<+++++++++++++++++++++++++++++[->+>+<<]
    >>[-<<+>>]<++[->+>+<<]>>[-<<+>>]<<<<<<<<<......>....<.........>...<<.>....>.>>>>
    >.<.<<<<....<....>..>>>>>.<.<<<<.>>>.<<.>>>>>.<.<<<<<<<.>...>>>>.>>>.<<<.<<<<..>
    >.>>>>>.<<.<<<<<...>>>>>.<<<<..<....>...<<.>..>.>>.<.<<...>>...<<...>>...<<....>
    >...<<<.>.>>..>.<<.......<.........>...<<.>........>...<.......>>>.<<..<<.>.....
    ...>...<......>.>>.<.<<<.>........>>...<<....>>.....>.<..>.

Which in turn outputs:

          ++++         +++
        +[>++++    ++[>+<-][
       <]<  -]>   >++    +++
      +.-   ---   ---    ---
     --.+++++++         +++
            +++       .++
            +++      +.-
            ---    -----.--.


License
-------

[GNU General Public License][gpl], version 2 or later.

[codegolf]: http://codegolf.stackexchange.com/a/21857/15322
[bf]: http://esoteric.sange.fi/brainfuck/impl/interp/i.html
[gpl]: https://www.gnu.org/licenses/
