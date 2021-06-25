#Copyright (c) 2014, 2020, Oracle and/or its affiliates.
#
#Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#
# WebLogic on Docker Default Domain
#
# Domain, as defined in DOMAIN_NAME, will be created in this script. Name defaults to 'base_domain'.
#
# ==============================================

import os
import socket



def getEnvVar(var):
  val=os.environ.get(var)
  if val==None:
    print "ERROR: Env var ",var, " not set."
    sys.exit(1)
  return val

# This python script is used to create a WebLogic domain

#domain_uid                           = DOMAIN_UID
ssl_enabled                           = os.environ.get("SSL_ENABLED")
server_port_string_array              = os.environ.get("MANAGED_SERVER_PORT") # Need to change (int)
server_port_array                     = server_port_string_array.split()
managed_server_ssl_port_string_array  = os.environ.get("MANAGED_SERVER_SSL_PORT") # Need to change (int)
managed_server_ssl_port_array         = managed_server_ssl_port_string_array.split()
domain_path                           = os.environ.get("DOMAIN_HOME")
admin_server_name                     = os.environ.get("ADMIN_NAME")
admin_port                            = int(os.environ.get("ADMIN_PORT"))
admin_server_ssl_port                 = int(os.environ.get("ADMIN_SERVER_SSL_PORT"))
domain_name                           = os.environ.get("DOMAIN_NAME")
t3_channel_port                       = int(os.environ.get("T3_CHANNEL_PORT"))
t3_public_address                     = os.environ.get("T3_PUBLIC_ADDRESS")
number_of_ms                          = int(os.environ.get("CONFIGURED_MANAGED_SERVER_COUNT"))
managed_server_name_base              = os.environ.get("MANAGED_SERVER_NAME_BASE")
production_mode_enabled               = os.environ.get("PRODUCTION_MODE_ENABLED")
managed_server_name_string_array      = os.environ.get("MANAGED_SERVER_NAME")
managed_server_name_array             = managed_server_name_string_array.split()

admin_server_username                 = os.environ.get("ADMIN_SERVER_USERNAME")
admin_server_password                 = os.environ.get("ADMIN_SERVER_PASSWORD")
machine_name                          = os.environ.get("MACHINE_NAME")

managed_server_needs_jms_string_array = os.environ.get("MANAGED_SERVER_NEEDS_JMS")
managed_server_needs_jms_array        = managed_server_needs_jms_string_array.split()


dsname                                = os.environ.get("DS_NAME")
dsjndiname                            = os.environ.get("DS_JNDI_NAME")
dsdriver                              = os.environ.get("DS_DRIVER")
dsusername                            = os.environ.get("DS_USER_NAME")
dspassword                            = os.environ.get("DS_PASSWORD")
dsdbname                              = os.environ.get("DS_DB_NAME")
dsurl                                 = os.environ.get("DS_URL")
dsinitalcapacity                      = int(os.environ.get("DS_INITIAL_CAPACITY"))

# Read the domain secrets from the common python file
#execfile('%s/read-domain-secret.py' % script_dir)

print('domain_path                    : [%s]' % domain_path);
print('domain_name                    : [%s]' % domain_name);
print('ssl_enabled                    : [%s]' % ssl_enabled);
print('admin_server_name              : [%s]' % admin_server_name);
print('admin_port                     : [%s]' % admin_port);
print('admin_server_ssl_port          : [%s]' % admin_server_ssl_port);
print('server_port_array              : [%s]' % server_port_array);
print('managed_server_ssl_port_array  : [%s]' % managed_server_ssl_port_array);
print('number_of_ms                   : [%s]' % number_of_ms);
print('managed_server_name_base       : [%s]' % managed_server_name_base);
print('production_mode_enabled        : [%s]' % production_mode_enabled);
print('dsname                         : [%s]' % dsname);
print('t3_channel_port                : [%s]' % t3_channel_port);
print('t3_public_address              : [%s]' % t3_public_address);
print('managed_server_name_array      : [%s]' % managed_server_name_array);
print('managed_server_needs_jms_array : [%s]' % managed_server_needs_jms_array);

for port in server_port_array:
  name = port
  print('server_port_array element is %s' % name);

for port in managed_server_ssl_port_array:
  name = port
  print('managed_server_ssl_port_array element is %s' % name);

for port in managed_server_name_array:
  name = port
  print('managed_server_name_array element is %s' % name);

for port in managed_server_needs_jms_array:
  name = port
  print('managed_server_needs_jms_array element is %s' % name);

# Open default domain template
# ============================
readTemplate("/u01/oracle/wlserver/common/templates/wls/wls.jar")

set('Name', domain_name)
setOption('DomainName', domain_name)
create(domain_name,'Log')
cd('/Log/%s' % domain_name);
set('FileName', '%s.log' % (domain_name))

# Configure the Administration Server
# ===================================
cd('/Servers/AdminServer')
#set('ListenAddress', '%s-%s' % (domain_uid, admin_server_name_svc))
set('ListenPort', admin_port)
set('Name', admin_server_name)


create('T3Channel', 'NetworkAccessPoint')
cd('/Servers/%s/NetworkAccessPoints/T3Channel' % admin_server_name)
set('PublicPort', t3_channel_port)
set('PublicAddress', t3_public_address)
#set('ListenAddress', '%s-%s' % (domain_uid, admin_server_name_svc))
set('ListenPort', t3_channel_port)

#cd('/Servers/%s' % admin_server_name)
#create(admin_server_name, 'Log')
#cd('/Servers/%s/Log/%s' % (admin_server_name, admin_server_name))
#set('FileName', '%s.log' % (admin_server_name))

if (ssl_enabled == 'true'):
    print 'Enabling SSL in the Admin server...'
    cd('/Servers/' + admin_server_name)
    create(admin_server_name, 'SSL')
    cd('/Servers/' + admin_server_name + '/SSL/' + admin_server_name)
    set('ListenPort', admin_server_ssl_port)
    set('Enabled', 'True')

# Set the admin user's username and password
# ==========================================
cd('/Security/%s/User/weblogic' % domain_name)
cmo.setName(admin_server_username)
cmo.setPassword(admin_server_password)

# Write the domain and close the domain template
# ==============================================
setOption('OverwriteDomain', 'true')

# Create Machine
# ================
print "Creating Machines"
cd('/')
create_machine = create(machine_name,'Machine')
if (machine_name != ""):
    print "\tSetting Machine Name",machine_name
    create_machine.setName(machine_name)
print "Done with Machine Creation"



# Create Node Manager
# ===================
cd('/NMProperties')
set('SecureListener', 'false')

# Create managed servers
# ======================
#servers = ['CS_MS1', 'FP_MS1', 'FM_MS1']   # We need to modify this to read from environment variable.
for server in managed_server_name_array:
  cd('/')
  name = server
  create(name, 'Server')
  cd('/Servers/%s/' % name )
  print('managed server name is %s' % name);
# set('ListenAddress', '%s-%s' % (domain_uid, name_svc))
  index = managed_server_name_array.index(server)
  server_port = int(server_port_array[index])

  print('server_port : [%s]' % server_port);


  set('ListenPort', server_port)
  set('NumOfRetriesBeforeMSIMode', 0)
  set('RetryIntervalBeforeMSIMode', 1)

  if (ssl_enabled == 'true'):
    print 'Enabling SSL in the managed server...'
    create(name, 'SSL')
    cd('/Servers/' + name+ '/SSL/' + name)
    set('ListenPort', managed_server_ssl_port)
    set('Enabled', 'True')









#
# Write Domain
# ============
writeDomain(domain_path)
closeTemplate()
print 'Domain Created'

# Update Domain
readDomain(domain_path)
cd('/')
if production_mode_enabled == "true":
  cmo.setProductionModeEnabled(true)
else:
  cmo.setProductionModeEnabled(false)
updateDomain()
closeDomain()
print 'Domain Updated'
print 'Done'

# Exit WLST
# =========
exit()


## Update Domain, Close It, Exit
## ==========================
#updateDomain()
#closeDomain()
#exit()
#









####################################################################################################################################
# You will need to be connected to a running server to execute the following commands:
####################################################################################################################################
#
#for server in managed_server_name_array:
#  index = managed_server_name_array.index(server)
#  jms_enabled = managed_server_needs_jms_array[index]
#
#  print('server : [%s]' % server);
#  print('jms_enabled : [%s]' % jms_enabled);
#
#  if (jms_enabled == 'true'):
#
#    # Create JMS Config
#    # ===========================
#
#    #Create a Persistent Store
#    #================================================
#    cd('/')
#    myfilestore=create(server + 'FileStore', 'FileStore')
#
#    cd('/FileStores/' + server + 'FileStore')
#    myfilestore.setDirectory('/u01/oracle/user_projects/domains/base_domain/FileStore')
#
#    cd('/')
#    assign('FileStore', server + 'FileStore', 'Target', server)
#
#
#    # Create a JMS Server
#    # ===================
#    cd('/')
#    jmsserver_name='jmsserver-' + server
#    jmsserver=create(jmsserver_name, 'JMSServer')
#    print('Create JMSServer : [%s]' % jmsserver_name)
#
#    cd('/JMSServers/' + jmsserver_name)
#    set('PersistentStore', server + 'FileStore')
#    print('FileStore_name     : [%s]' % getMBean('/FileStores/' + server + 'FileStore'))
#
#    cd('/')
#    assign('JMSServer', jmsserver_name, 'Target', server)
#
#  # Create a JMS System resource
#  # ============================
#  cd('/')
#  create('jmsmodule2', 'JMSSystemResource')
#  cd('JMSSystemResource/jmsmodule2/JmsResource/NO_NAME_0')
#  assign('JMSSystemResource', 'jmsmodule2', 'Target', 'FP_MS1')
#
#  # Create a JMS Queue and its subdeployment
#  # ========================================
#  myq = create('queue2','Queue')
#  myq.setJNDIName('jndi/queue2')
#  myq.setSubDeploymentName('DockerQueueSubDeployment')
#
#  cd('/JMSSystemResource/jmsmodule2')
#  create('DockerQueueSubDeployment', 'SubDeployment')
#
#  # Target resources to the servers
#  # ===============================
#  cd('/')
#  assign('JMSSystemResource.SubDeployment', 'jmsmodule2.DockerQueueSubDeployment', 'Target', 'jmsserver-ms2')


####################################################################################################################################
#
#
#
## Create a Data Source
## ======================
#cd('/')
#print('Configuring a Data Source: %s' % dsname);
#
#
#create(dsname, 'JDBCSystemResource')
#cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
#cmo.setName(dsname)
#
#cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
#create('myJdbcDataSourceParams','JDBCDataSourceParams')
#cd('JDBCDataSourceParams/NO_NAME_0')
#set('JNDIName', java.lang.String(dsjndiname))
#set('GlobalTransactionsProtocol', java.lang.String('None'))
#
#cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
#create('myJdbcDriverParams','JDBCDriverParams')
#cd('JDBCDriverParams/NO_NAME_0')
#set('DriverName', dsdriver)
#set('URL', dsurl)
#set('PasswordEncrypted', dspassword)
#set('UseXADataSourceInterface', 'false')
#
#print 'create JDBCDriverParams Properties'
#create('myProperties','Properties')
#cd('Properties/NO_NAME_0')
#create('user','Property')
#cd('Property/user')
#set('Value', dsusername)
#
#cd('../../')
#create('databaseName','Property')
#cd('Property/databaseName')
#set('Value', dsdbname)
#
#print 'create JDBCConnectionPoolParams'
#cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
#create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
#cd('JDBCConnectionPoolParams/NO_NAME_0')
#set('TestTableName','SQL SELECT 1 FROM DUAL')
#set('InitialCapacity',int(dsinitalcapacity))
#
#print('Done setting attributes for Data Source: %s' % dsname);
#
## Assign
## ======
## Uncomment to target and enable the data source for the cluster
#assign('JDBCSystemResource', dsname, 'Target', 'CS_MS1')
