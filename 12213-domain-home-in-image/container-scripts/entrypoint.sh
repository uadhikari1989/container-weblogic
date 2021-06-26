#!/bin/bash



#[oracle@65c22b5edb4f custom-configs]$ echo $PATH
#/usr/java/jdk-8/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/java/jdk-8/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin
#
#
#
#[oracle@65c22b5edb4f custom-configs]$ echo $PATH
#/usr/java/jdk-8/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/java/jdk-8/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/user_projects/domains/mwidomain:/u01/oracle/user_projects/domains/mwidomain/bin:/u01/oracle


# user root

whoami

env



# user oracle



/u01/oracle/custom-configs/createWLSDomain.modified.sh


#pushd ${DOMAIN_HOME}
pushd /u01/oracle/custom-configs/

	startAdminServer.sh

popd 



#/u01/oracle/custom-configs/createWLSDomain.sh AFTER

