# Ping all servers in cluster to see if they're alive
for i in 134 139 140 169 173 174 184 186 195 208 217 33 57 78 79; do for x in `seq 1 15`; do ping -c1 s$x.c$i;done;done &>HI

# delete all blank lines
sed '/^$/d' filename

# to number all lines including blank lines:
nl -ba filename

# display the line number of where the pattern is
grep -n pattern filename

# find "string" and add "#" to the beginning of the line
sed -i '/string/s/^/#/' filename

# find "string" and add "#" to the end of the line
sed -i '/string/s/^/#/' filename

# insert "#" to the beginning of line "23"
sed -i '23 s/^/#/' some1

# read through file1 and delete
while read LINE ; do
let COUNTER=COUNTER+1
echo -e "\n Deleting file ${COUNTER} \n"
sudo rm -f $LINE
done < file1

