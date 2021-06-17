for containerid in `docker ps | cut -d " " -f 1 | grep -v CONTAINER`;do docker stop $containerid;done
