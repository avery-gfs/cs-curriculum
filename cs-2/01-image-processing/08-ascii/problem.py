# Oeeeccccceeeeeeeeeec<++<<c<+:<eOeeeeeeeeOOOOOOOOOE  ```````````````````'--''`'-~'` ````````
# eecccccccceeeee+-               `<eeeeeeeeeOOOOOOO ```````````````-+OEEEEEEEEEEEEEEe'`````````
# cccccccccccec~`                    -eeeeeeeeeeeOOO `````````````:eOEEEEEOOOOOOOOOOEEEE+```````````
# ccccccccccc~`      ` `-~~::~-``      <OeeOeOOeOOOO ```````````:eOEEEEOeOc+::~~:+ceOOOOEO' `` `  `
# ccccccccc<`        `~+<<<<<<<<<<~`   'eeeOOOOOOOOO `````````'eEEEEEEEOe:-'''''''''':cOOO<```
# cccccccc+         `-:::+<<<cccc<<<+:'`+eeeOOOOOOOO ````````-OEEEEEEEOc+~~~-'''````'''-~<e-```
# ccccccc:         ``'-~:++<ccccc<<<<++~'eeeeeeOOOOO ```````~EEEEEEEEEec<+:~--'`````''''--:<``````
# cccccc'          '~~::::+<<c<<<<<+++::-<eeeeeOOOOO ``````<EEEEEEEEEO<::~~~~-''`'''''---~~+'`````
# ccccc`  `''    `'-~::~~--'`-:+<<<+++:~'`<eeeeOOOOO `````cEEe<<OEOOe<+:~~::++<c+~-'''---~:<c'````
# cccc' `:-' ':```-~~~~-'--~~+- `':+::+:~+eeOOOOOOOE ````<Ee~+<O<~ccc+::::+<++::-+Oe<~-~~-~:-``
# ccc<` `+~:+`'` '-::+:--```:+`-'`~~~'```<OOOOOOOEEE ```'eEe-:~-c<eO<+~~-~++cce~-e+<c:::<cec'
# ccc<`  -:+~-<~`''-:++<c+--~::~:+<' `'--eOOOOOOEEEE ```'eEE+~-:+':e<<+~--'`-++:~~:~-'<Oc<++`
# cc<cc- `~-:-~-''``-~::cc<+::<<+:<:``+~OOOOEEEEEEEE ``'``+Ee:+~+:+<<cc+:~~``'-~~''-~'~cc-:
# ccc<- `` ~++:''-'`'-~~:+<cee<+++c:-'<EOOOEEEEEEEEE ```'+OecO:--~<<+<c<+::~-'```'---`~+<'
# '`     `~`` ``'---'-~:~:<<+::+:<c:~~OOOOOEEOOEEEEE <eOEOOEc:ceOec<+++<+:~:~''-~~-~'`~::
#        `':<' `'-~----~:~~+c-   -~~-cOOOEOcOEEEEEEE OOOOOOOe<~'<Oc<+:++++:~::-`+OOO+::+`     `
#        -:'+-  `'-~~~::~'``-::'  `'cOOOecOEEEEEEEEE OOOOOOE+~<-+OOe<+:::~~:<ee+~~<EEc<`   ``
#         <:-:    '-~~:::~-`  '~` 'cc<cOEEEEEEEEEEEE OOOOOOOO'~+~OEEO<+::~~~:+cOO<:eO<``'`
#         `e~-`    `''-~::~-~~~' `cOOOOEEEEEEEEEEEEE OOOOOOOOe`:+cOEEOe<<+:~~:+:::<Oe`
#          ~O~`       `~:++<+~```<OOOOEEEEEEEEEEEEEE OOOOOOOOE: :cOEEEEEOc:~--'-:cec'
#           cO-         ``-~~~-~eOOOOOEEEEEEEEEEEEEE OOOOOOOOOO` +OEEEEEEEEec+:::+:`
#           ~ec'         '-~-~cOOOOOOOOOOOEEEEEEEEEE OOOOOOOOOE:``<EEEEEEEEO<+:+:`
#           `c<~     `<eeeeeOOOOOOOOOOOOOOEEEEEEEEEE OOOOOOOOOEc`':OEEEEc'`````
#            ::~` `<eeeeeeeeeOOOOOOOOOOOOEEEEEEEEEEE OOOEOOOOOOO~~:eEe'`````````
#            -c<-  :`-eeeeeeeeeeOOOOOOOOOOOOEEEEEEEE OOOEOOOOOOE+`'+OO~c+``````````
#            'c~     <eeeeeeeeeeeeOOOOOOOOOOOEEEEEEE OOOEOOOOOOE<`:OEEEO'````````````
#              `    'eceeeeeeeeeeeeOOOOOOOOOOOEEEEEE OOOEOOOOOOOOOeEEEE<``````````````
# :           ``    +ecccccceeeeeeeeeeOOOOOOOOOEEEEE ~OOEOOOOOOOOeeEEEO-`````````````````

from PIL import Image

im = Image.open("dali.png")

invert = False  # Set to True for dark-on-light color scheme
symbols = "   ``'-~:+<ceOEB"

if invert:
    symbols = symbols[::-1]  # Reverse symbols

# Your code goes here
