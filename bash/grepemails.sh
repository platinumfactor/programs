for i in `grep -o "[[:graph:]]*@[[:graph:]]*" | sed -e s/,//g | sed -e s/\<//g | sed -e s/\>//g`; do 
	if [ "`dig mx +short $(echo $i | cut -d'@' -f2) | grep -i platinumfactor`" != "" ]; then 
		echo -n $i
	fi
done
