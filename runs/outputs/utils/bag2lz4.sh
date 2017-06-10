# finds all .bag files and recursively compresses them with LZ4 algorithm
for f in `find . -name "*.bag"`
do
    rosbag compress --lz4 $f
done

# then deletes them
for f in `find . -name "*.orig.bag"`
do
    rm $f
done


