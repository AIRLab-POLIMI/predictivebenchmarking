# finds all .yaml, then adjusts file path
for f in `find . -name "*.yaml"`
do
    MY_PATH=$(awk -F": " '{print (NF>1)? $NF : "";exit;}' $f)
    DIR=$(dirname "${MY_PATH}")
    sed -i "s#${DIR}/#./#g" $f
done
