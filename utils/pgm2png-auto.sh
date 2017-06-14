# finds all .pgm files and recursively turns them into png, then deletes them
for f in `find . -name "*.pgm"`
do
    mogrify -format png $f
    rm $f
done
# finds all corresponding .yaml, replaces extension with .png, then adjusts file path
for f in `find . -name "*.yaml"`
do
    sed -i 's/pgm/png/g' $f
    MY_PATH=$(awk -F": " '{print (NF>1)? $NF : "";exit;}' $f)
    DIR=$(dirname "${MY_PATH}")
    sed -i "s#${DIR}/#./#g" $f
done
