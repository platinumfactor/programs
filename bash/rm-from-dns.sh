echo -e "Type 'os' to take clusters out of dns and 'is' to put back in dns" ; read resp

if [[ $resp == "os" ]]; then
        while read LINE ; do
        printf '%s\n' 'g/^cluster.*'"$LINE"'/s/^/;/\' '-s' w | ed -s dns-zone.platinumfactor.com && echo -e "\n $LINE is out of DNS."
        done < cluster.oos

elif [[ $resp == "is" ]]; then
        while read LINE ; do
        printf '%s\n' 'g/^\;cluster.*'"$LINE"'/s/^;//\' '-s' w | ed -s dns-zone.platinumfactor.com && echo -e "\n $LINE is back in DNS."
        done < cluster.oos
else
        echo "You chose an invalid option."
        exit 0
fi
