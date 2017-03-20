# Seleccionamos la imagen base
FROM debian

# Set some environment vars
ENV DEBIAN_FRONTEND noninteractive

# Supress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Update repository
RUN apt-get update

# Install apt-utils
RUN apt-get -y install apt-utils

# Install MySQL database
RUN apt-get -y install mysql-server
RUN apt-get -y install mysql-client

# Let MySQL listen on all interfaces
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

# Create a new admin user for MySQL 
RUN /usr/sbin/mysqld & \
    sleep 10s &&\
    echo "GRANT ALL ON *.* TO admin@'%' IDENTIFIED BY 'admin' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql

# Restore de database
ADD ./mysql_config /tmp/mysql_config

# Install NetSNMP agent and manager
RUN apt-get -y install snmpd
RUN apt-get -y install snmp

# Change snmp default port
RUN sed -i -e"s/^agentAddress\s*udp:127.0.0.1:161/agentAddress  udp:0.0.0.0:162/" /etc/snmp/snmpd.conf

# Install dependencies for RMON
RUN apt-get -y install python
RUN apt-get -y install python-mysqldb
RUN apt-get -y install libpcap-dev
RUN apt-get -y install python-libpcap
RUN apt-get -y install tcpdump
RUN apt-get -y install wget
RUN apt-get -y install gcc

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install pyasn1
RUN pip install pysnmp

RUN apt-get -y install unzip
RUN wget http://www.secdev.org/projects/scapy/files/scapy-latest.zip
RUN unzip scapy-latest.zip -d /tmp
WORKDIR /tmp/scapy-2.2.0
RUN python setup.py install

# Install RMON
ADD ./etc/rmon /etc/rmon

EXPOSE 3306
EXPOSE 161

ADD start /start
#CMD ["/usr/bin/mysqld_safe"]
CMD ["/start"]
