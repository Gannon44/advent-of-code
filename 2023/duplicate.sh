function ordinal () {
  case "$1" in
    *1[0-9] | *[04-9]) echo "$1"th;;
    *1) echo "$1"st;;
    *2) echo "$1"nd;;
    *3) echo "$1"rd;;
  esac
}
i=0
while (( i++ < 26 )); do
  cp -r ./0 "$(ordinal $i)"
done