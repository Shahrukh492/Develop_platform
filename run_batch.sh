while true
do
~/goldeneye/bin/python3 /home/centos/goldeneye/uploads/9db593a8/vids_move.py
echo "Video transfer " >> /home/centos/video.out
~/goldeneye/bin/python3 /home/centos/goldeneye/uploads/9db593a8/processing/face_dect.py
echo "face detection" >> /home/centos/face.out
~/goldeneye/bin/python3 /home/centos/goldeneye/uploads/9db593a8/processing/img_compare.py
echo "image compare" >> /home/centos/image.out
~/goldeneye/bin/python3 /home/centos/goldeneye/uploads/9db593a8/processing/writeMysql.py
echo "insert into db" >> /home/centos/db.out

sleep 120
done
