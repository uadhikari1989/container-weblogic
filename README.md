# container-weblogic

Go to the folder where these files are present.

ls
create-wls-domain.modified.py  createWLSDomain.modified.sh  Dockerfile  entrypoint.sh  startAdminServer.sh 

Run the below command if there is already a container present.
docker stop weblogic-testing && docker rm weblogic-testing

Run below command to re-create a container
 
sudo docker run -d      --name weblogic-testing      --publish 7002:7001      --publish 9003:9002      --env PROPERTIES_FILE_DIR="/u01/oracle/custom-configs"      --env SSL_ENABLED=false      --env ADMIN_PORT=7001      --env ADMIN_SERVER_SSL_PORT=7002      --env MANAGED_SERVER_NAME="CS_MS1 FP_MS1 FM_MS1"      --env MANAGED_SERVER_NEEDS_JMS="true true false"      --env MANAGED_SERVER_PORT="8001 8002 8003"      --env MANAGED_SERVER_SSL_PORT="10001 10002 10003"      --env MANAGED_SERVER_NAME_BASE=MS      --env MACHINE_NAME=$(hostname)      --env CONFIGURED_MANAGED_SERVER_COUNT=4      --env DEBUG_PORT=8453      --env DEBUG_FLAG=true      --env ADMIN_NAME=admin-server      --env ADMIN_HOST=wlsadmin      --env CLUSTER_NAME="cluster-1"      --env CUSTOM_SSL_ENABLED=false      --env DB_PORT=1527      --env DS_NAME=DS2      --env DS_JNDI_NAME="jndi/ds2"      --env DS_DRIVER="oracle.jdbc.OracleDriver"      --env DS_USER_NAME=CUSTOMERINFO      --env DS_PASSWORD="PWD4CUSTOMERINFO"      --env DS_DB_NAME="XEPDB1"      --env DS_URL="jdbc:oracle:thin:@//10.115.85.92:1522/XEPDB1"      --env DS_INITIAL_CAPACITY="1"      --env PRODUCTION_MODE_ENABLED=true      --env CLUSTER_TYPE=DYNAMIC      --env JAVA_OPTIONS='-Dweblogic.StdoutDebugEnabled=false'      --env T3_CHANNEL_PORT=30012      --env T3_PUBLIC_ADDRESS=kubernetes      --env ADMIN_SERVER_USERNAME=weblogic      --env ADMIN_SERVER_PASSWORD=weblogic1      --env WEBLOGIC_JAVA_OPTIONS="-Dweblogic.StdoutDebugEnabled=false"      --restart always      --volume /app/weblogic-testing:/u01/oracle/custom-configs      new-weblogic-image      tail -f /dev/null


Go inside the container using this command docker exec -it weblogic-testing /bin/bash

Then execute the entrypoint script using this command: ./entrypoint.sh
