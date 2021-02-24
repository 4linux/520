#!/bin/bash

OUTPUT="$(xrandr | grep -Eo '(.*) connected' | cut -d' ' -f1)"

RESOLUTIONS=''
while read RESOLUTION; do 
        RESOLUTIONS="$RESOLUTIONS      [exec] ($RESOLUTION) {xrandr --output $OUTPUT --mode $RESOLUTION}\n"
done <<< $(xrandr | grep -Eo '[0-9]{3,4}x[0-9]{3,4}' | sort -n -t x -r)

sed -E -i -z 's/\s*\[exec\] \([0-9]*x[0-9]*\) \{xrandr --output .* --mode [0-9]*x[0-9]*\}/\n#@#/' ~/.fluxbox/menu
sed -E -i -z 's/#@#\n/'"$RESOLUTIONS"'/' ~/.fluxbox/menu
