# RMON GUI
RMON GUI is a simple graphical interface to configure and visualize entries in the RMON filter group. The easiest way
to get started is to use this GUI as a docker container and x410.

```
sudo docker run --env DISPLAY=127.0.0.1:0.0 --name rmon_gui jslarraz/rmon_gui
```

If you are using a remote docker server rather than a local one (like Docker for Windows), you must modify the 
DISPLAY environment variable with the IP address of your local computer (where the x410 server is running). 

The first step is to define the connection with your rmon device (Conexion->Add) and select it (Conexion->Select). 
After that, you can define new filter types (Filter->Create), add the filter to the selected rmon device (Filter->Add) 
and show the packets count of the filters running on the selected device (Filter->Show).

Code in this repository was initially developed as part of my Final undergraduate project, and full details about the
gui usage is available at project report (only Spanish).

https://zaguan.unizar.es/record/31543?ln=en
