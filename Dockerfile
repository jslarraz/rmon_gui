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

# Install dependencies for RMON gui
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN apt-get -y install python-wxgtk3.0

# Copy files
ADD . /tmp

ENV DISPLAY 127.0.0.1:0.0
CMD ["python", "/tmp/gui/gui.py"]

