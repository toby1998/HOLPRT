nlayer=6
nlayer_ct=-2
State=47
for layer_ini in {1..6}
do 
   #echo $layer_ini
    layer_fnl=`echo "($layer_ini + $nlayer_ct) % $nlayer"|bc`
   #echo $layer_fnl
    if [ "$layer_fnl" -eq 0 ]; then
      layer_fnl=$nlayer
#     echo $layer_fnl
    fi
    if [ "$layer_fnl" -lt 0 ]; then
        layer_fnl=`echo "$layer_fnl + $nlayer"|bc -l`
	echo $layer_fnl
    fi
    State=`echo "$State + 1"|bc -l`
   #echo $layer_ini $layer_fnl $State
    cat ztemp|sed -e "s/State J/State $State/g"|sed -e "s/layerIni/layer$layer_ini/g"|sed -e "s/layerFnl/layer$layer_fnl/g"
    State=`echo "$State + 1"|bc -l`
    cat ztemp|sed -e "s/State J/State $State/g"|sed -e "s/layerIni/layer$layer_ini/g"|sed -e "s/layerFnl/layer$layer_fnl/g"|sed -e "s/_sym/_antisym/g"
done

