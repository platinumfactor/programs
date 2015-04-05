read -s -p "Enter sudo password: " PASS
for CLUSTER in 86 87 170 171 85; do
 for SERVER in {2..15}; do
        echo -e "\nChecking server: " s${SERVER}.c${CLUSTER} "\n"
        ssh -o stricthostkeychecking=no -q s${SERVER}.c${CLUSTER} "echo $PASS | sudo find /var/queue -type f -exec grep -lir platinumfactor {} \;"
 done
done
