for f in `find . -name "*.pgm"`
do
    mogrify -format png $f
done



