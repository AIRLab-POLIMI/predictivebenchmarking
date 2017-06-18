# finds all .yaml, replaces extension with .png, then adjusts file path
for f in `find . -name "*.yaml"`
do
    sed -i 's/pgm/png/g' $f
    MY_PATH=$(awk -F": " '{print (NF>1)? $NF : "";exit;}' $f)
    DIR=$(dirname "${MY_PATH}")
    sed -i "s#${DIR}/#./#g" $f
done
