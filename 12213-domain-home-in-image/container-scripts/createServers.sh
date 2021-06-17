
#Start the Admin Server:
docker run -d --name wlsadmin --hostname wlsadmin -p 7001:7001 -v  /home/umesh/docker-weblogic/OracleWebLogic/12213-domain-home-in-image/properties/docker-run:/u01/oracle/properties domain-home-in-image:12.2.1.3

#Start Managed servers:
docker run -d --name CS_MS1 --link wlsadmin:wlsadmin -p 8001:8001 -v  /home/umesh/docker-weblogic/OracleWebLogic/12213-domain-home-in-image/properties/docker-run:/u01/oracle/properties -e MANAGED_SERV_NAME=CS_MS1 domain-home-in-image:12.2.1.3 startManagedServer.sh

docker run -d --name FP_MS1 --link wlsadmin:wlsadmin -p 8002:8002 -v  /home/umesh/docker-weblogic/OracleWebLogic/12213-domain-home-in-image/properties/docker-run:/u01/oracle/properties -e MANAGED_SERV_NAME=FP_MS1 domain-home-in-image:12.2.1.3 startManagedServer.sh

docker run -d --name FM_MS1 --link wlsadmin:wlsadmin -p 8003:8003 -v   /home/umesh/docker-weblogic/OracleWebLogic/12213-domain-home-in-image/properties/docker-run:/u01/oracle/properties -e MANAGED_SERV_NAME=FM_MS1 domain-home-in-image:12.2.1.3 startManagedServer.sh


