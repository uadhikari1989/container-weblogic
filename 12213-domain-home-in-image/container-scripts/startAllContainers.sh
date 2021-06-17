adminConId=`docker ps -a | grep -i admin | cut -d " " -f 1`

docker start $adminConId

for containerid in `docker ps -a | cut -d " " -f 1 | grep -v CONTAINER`
do 
docker start $containerid
done
