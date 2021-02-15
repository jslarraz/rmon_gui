# -*- coding: utf-8 -*-
import wx
import  wx.lib.scrolledpanel as scrolled
import subprocess


#######################################################################
##                               Create                              ##
#######################################################################

class Create(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.parent = parent

        # Creamos un sizer para las columnas
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.AddSpacer(parent.V, -1)

        # Informacion
        self.inforSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.inforSizer.AddSpacer(parent.H,-1)
        inforForm = wx.FlexGridSizer(2, 2, 9, 25)
        # name
        self.lblName = wx.StaticText(self, label="Filter Name:")
        self.editName = wx.TextCtrl(self, value="", size=(200,30))
        # Owner
        self.lblOwner = wx.StaticText(self, label="Filter Owner:")
        self.editOwner = wx.TextCtrl(self, value="", size=(200,30))
        # Añadimos los objetos al formulario
        inforForm.AddMany([self.lblName, self.lblOwner, self.editName, self.editOwner])
        self.inforSizer.Add(inforForm, 1, wx.EXPAND)
        
        # Ethernet
        self.etherSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.etherSizer.AddSpacer(parent.H,-1)
        etherForm = wx.FlexGridSizer(2, 3, 9, 25)
        # srcMacAddr
        self.lblSrcMacAddr = wx.StaticText(self, label="SRC MAC Address:")
        self.editSrcMacAddr = wx.TextCtrl(self, value="*", size=(200,30))
        # dstMacAddr
        self.lblDstMacAddr = wx.StaticText(self, label="DST MAC Address:")
        self.editDstMacAddr = wx.TextCtrl(self, value="*", size=(200,30))
        # etherType
        etherType = ['*', 'IP', 'ARP']
        self.lblEtherType = wx.StaticText(self, label="Type:")
        self.editEtherType = wx.ComboBox(self, size=(200, 30), choices=etherType, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EtherType, self.editEtherType)
        # Añadimos los objetos al formulario
        etherForm.AddMany([self.lblSrcMacAddr, self.lblDstMacAddr, self.lblEtherType, \
                             self.editSrcMacAddr, self.editDstMacAddr, self.editEtherType])
        self.etherSizer.Add(etherForm, 1, wx.EXPAND)

        # IP
        self.ipSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ipSizer.AddSpacer(parent.H,-1)
        ipForm = wx.FlexGridSizer(2, 3, 9, 25)
        # srcIpAddr
        self.lblSrcIpAddr = wx.StaticText(self, label="SRC IP Address:")
        self.editSrcIpAddr = wx.TextCtrl(self, value="*", size=(200,30))
        # dstIpAddr
        self.lblDstIpAddr = wx.StaticText(self, label="DST IP Address:")
        self.editDstIpAddr = wx.TextCtrl(self, value="*", size=(200,30))
        # ipType
        ipType = ['*', 'TCP', 'UDP', 'ICMP']
        self.lblIpType = wx.StaticText(self, label="Type:")
        self.editIpType = wx.ComboBox(self, size=(200, 30), choices=ipType, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.IpType, self.editIpType)
        # Añadimos los objetos al formulario
        ipForm.AddMany([self.lblSrcIpAddr, self.lblDstIpAddr, self.lblIpType, self.editSrcIpAddr, self.editDstIpAddr, self.editIpType])
        self.ipSizer.Add(ipForm, 1, wx.EXPAND)

        # TCP
        self.tcpSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.tcpSizer.AddSpacer(parent.H,-1)
        tcpForm = wx.FlexGridSizer(2, 2, 9, 25)
        # srcPort
        self.lblSrcPort = wx.StaticText(self, label="SRC Port:")
        self.editSrcPort = wx.TextCtrl(self, value="*", size=(200,30))
        # dstPort
        self.lblDstPort = wx.StaticText(self, label="DST Port:")
        self.editDstPort = wx.TextCtrl(self, value="*", size=(200,30))
        # Añadimos los objetos al formulario
        tcpForm.AddMany([self.lblSrcPort, self.lblDstPort, self.editSrcPort, self.editDstPort])
        self.tcpSizer.Add(tcpForm, 1, wx.EXPAND)

        # ICMP
        self.icmpSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.icmpSizer.AddSpacer(parent.H,-1)
        icmpForm = wx.FlexGridSizer(2, 2, 9, 25)
        # type
        self.lblIcmpType = wx.StaticText(self, label="ICMP Type:")
        self.editIcmpType = wx.TextCtrl(self, value="*", size=(200,30))
        # dstPort
        self.lblIcmpCode = wx.StaticText(self, label="ICMP Code:")
        self.editIcmpCode = wx.TextCtrl(self, value="*", size=(200,30))
        # Añadimos los objetos al formulario
        icmpForm.AddMany([self.lblIcmpType, self.lblIcmpCode, self.editIcmpType, self.editIcmpCode])
        self.icmpSizer.Add(icmpForm, 1, wx.EXPAND)

        ## Botones
        self.botonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.botonSizer.AddSpacer(parent.H,-1)
        self.botonForm = wx.FlexGridSizer(1, 2, 9, 25)
        # Boton
        self.createBtn = wx.Button(self, -1, 'Create')
        self.Bind(wx.EVT_BUTTON, self.Create, id=self.createBtn.GetId())
        # Error panel
        self.lblError = wx.StaticText(self, label="")
        # Añadimos los objetos al formulario
        self.botonForm.AddMany([self.createBtn, self.lblError])
        self.botonSizer.Add(self.botonForm, 1, wx.EXPAND)



        ## Añadimos las filas al sizer principal
        self.sizer.Add(self.inforSizer, 0, wx.EXPAND)
        self.sizer.AddSpacer(parent.V, -1)
        self.sizer.Add(self.etherSizer, 0, wx.EXPAND)
        self.sizer.AddSpacer(parent.V, -1)
        self.sizer.Add(self.botonSizer, 0, wx.EXPAND)

        self.ipSizer.Hide(True)
        self.tcpSizer.Hide(True)
        self.icmpSizer.Hide(True)

        # Colocamos el sizer en el panel
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()        


    def EtherType(self,event):
        self.sizer.Detach(9)    # Botones
        self.sizer.Detach(8)    # Spacer
        self.sizer.Detach(7)    # TCP
        self.sizer.Detach(6)    # Spacer
        self.sizer.Detach(5)    # IP
        self.ipSizer.Hide(True)
        self.tcpSizer.Hide(True)
        self.icmpSizer.Hide(True)

        if self.editEtherType.GetValue() == 'IP':
            self.ipSizer.Show(True)
            self.sizer.Add(self.ipSizer, 0, wx.EXPAND)
            self.sizer.AddSpacer(self.parent.V, -1)
            self.sizer.Add(self.botonSizer, 0, wx.EXPAND)
            self.sizer.Layout()

        else:
            self.sizer.Add(self.botonSizer, 0, wx.EXPAND)
            self.sizer.Layout()

    def IpType(self,event):
        self.sizer.Detach(9)    # Botones
        self.sizer.Detach(8)    # Spacer
        self.sizer.Detach(7)    # TCP
        self.tcpSizer.Hide(True)
        self.icmpSizer.Hide(True)

        if self.editIpType.GetValue() == 'TCP' or self.editIpType.GetValue() == 'UDP':
            self.tcpSizer.Show(True)
            self.sizer.Add(self.tcpSizer, 0, wx.EXPAND)
            self.sizer.AddSpacer(self.parent.V, -1)
            self.sizer.Add(self.botonSizer, 0, wx.EXPAND)
            self.sizer.Layout()

        elif self.editIpType.GetValue() == 'ICMP':
            self.icmpSizer.Show(True)
            self.sizer.Add(self.icmpSizer, 0, wx.EXPAND)
            self.sizer.AddSpacer(self.parent.V, -1)
            self.sizer.Add(self.botonSizer, 0, wx.EXPAND)
            self.sizer.Layout()

        else:
            self.sizer.Add(self.botonSizer, 0, wx.EXPAND)
            self.sizer.Layout()


    def Create(self,event):

        if self.ComprobarBlanco():
            self.lblError.Label = "Algun campo en blanco"
            self.lblError.Layout()

        elif self.ComprobarExiste():
            self.lblError.Label = "Ya existe una entrada con este nombre"
            self.lblError.Layout()

        else:
            fd = open("filtros.cnf", 'a')
            fd.write(self.editName.GetValue() + "|")
            fd.write(self.editOwner.GetValue() + "|")
            fd.write(self.editSrcMacAddr.GetValue() + "|")
            fd.write(self.editDstMacAddr.GetValue() + "|")
            fd.write(self.editEtherType.GetValue() + "|")

            if self.editEtherType.GetValue() == 'IP':

                fd.write(self.editSrcIpAddr.GetValue() + "|")
                fd.write(self.editDstIpAddr.GetValue() + "|")
                fd.write(self.editIpType.GetValue() + "|")

                if self.editIpType.GetValue() == 'TCP' or self.editIpType.GetValue() == 'UDP':
                    fd.write( self.editSrcPort.GetValue() + "|" )
                    fd.write( self.editDstPort.GetValue() + "|" )

                elif self.editIpType.GetValue() == 'ICMP':
                    fd.write( self.editIcmpType.GetValue() + "|" )
                    fd.write( self.editIcmpCode.GetValue() + "|" )

            fd.write( "\n" )
            
            fd.close()
            self.lblError.Label = "Exito"
            self.lblError.Layout()
            #self.parent.Parent.Close()
            

    def ComprobarBlanco(self):
        if self.editName.GetValue() == "" or \
           self.editOwner.GetValue() == "":
            return True
        else:
            return False

    def ComprobarExiste(self):
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if (sub_line[0] == self.editName.GetValue()):
                fd.close()
                return True
            line = fd.readline()
        fd.close()
        return False




#######################################################################
##                               Delete                              ##
#######################################################################

class Delete(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.parent = parent

        self.filtros = self.CargarFiltros()

        # Creamos un sizer para las columnas
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.AddSpacer(parent.V, -1)

        # Informacion
        self.inforSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.inforSizer.AddSpacer(parent.H,-1)
        inforForm = wx.FlexGridSizer(2, 2, 9, 25)
        # name
        self.lblName = wx.StaticText(self, label="Filter Name:")
        self.editName = wx.ComboBox(self, choices=self.filtros, style=wx.CB_DROPDOWN, size=(200,30) )
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editName)
        # Owner
        self.lblOwner = wx.StaticText(self, label="Filter Owner:")
        self.editOwner = wx.StaticText(self, label="", size=(200,30))
        # Añadimos los objetos al formulario
        inforForm.AddMany([self.lblName, self.lblOwner, self.editName, self.editOwner])
        self.inforSizer.Add(inforForm, 1, wx.EXPAND)
        
        # Ethernet
        self.etherSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.etherSizer.AddSpacer(parent.H,-1)
        etherForm = wx.FlexGridSizer(2, 3, 9, 25)
        # srcMacAddr
        self.lblSrcMacAddr = wx.StaticText(self, label="SRC MAC Address:")
        self.editSrcMacAddr = wx.StaticText(self, label="", size=(200,30))
        # dstMacAddr
        self.lblDstMacAddr = wx.StaticText(self, label="DST MAC Address:")
        self.editDstMacAddr = wx.StaticText(self, label="", size=(200,30))
        # etherType
        self.lblEtherType = wx.StaticText(self, label="Type:")
        self.editEtherType = wx.StaticText(self, label="", size=(200,30))
        # Añadimos los objetos al formulario
        etherForm.AddMany([self.lblSrcMacAddr, self.lblDstMacAddr, self.lblEtherType, self.editSrcMacAddr, self.editDstMacAddr, self.editEtherType])
        self.etherSizer.Add(etherForm, 1, wx.EXPAND)

        # IP
        self.ipSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ipSizer.AddSpacer(parent.H,-1)
        ipForm = wx.FlexGridSizer(2, 3, 9, 25)
        # srcIpAddr
        self.lblSrcIpAddr = wx.StaticText(self, label="SRC IP Address:")
        self.editSrcIpAddr = wx.StaticText(self, label="", size=(200,30))
        # dstIpAddr
        self.lblDstIpAddr = wx.StaticText(self, label="DST IP Address:")
        self.editDstIpAddr = wx.StaticText(self, label="", size=(200,30))
        # ipType
        self.lblIpType = wx.StaticText(self, label="Type:")
        self.editIpType = wx.StaticText(self, label="", size=(200,30))
        # Añadimos los objetos al formulario
        ipForm.AddMany([self.lblSrcIpAddr, self.lblDstIpAddr, self.lblIpType, self.editSrcIpAddr, self.editDstIpAddr, self.editIpType])
        self.ipSizer.Add(ipForm, 1, wx.EXPAND)

        # TCP
        self.tcpSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.tcpSizer.AddSpacer(parent.H,-1)
        tcpForm = wx.FlexGridSizer(2, 2, 9, 25)
        # srcPort
        self.lblSrcPort = wx.StaticText(self, label="SRC Port:")
        self.editSrcPort = wx.StaticText(self, label="", size=(200,30))
        # dstPort
        self.lblDstPort = wx.StaticText(self, label="DST Port:")
        self.editDstPort = wx.StaticText(self, label="", size=(200,30))
        # Añadimos los objetos al formulario
        tcpForm.AddMany([self.lblSrcPort, self.lblDstPort, self.editSrcPort, self.editDstPort])
        self.tcpSizer.Add(tcpForm, 1, wx.EXPAND)

        # ICMP
        self.icmpSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.icmpSizer.AddSpacer(parent.H,-1)
        icmpForm = wx.FlexGridSizer(2, 2, 9, 25)
        # type
        self.lblIcmpType = wx.StaticText(self, label="ICMP Type:")
        self.editIcmpType = wx.StaticText(self, label="", size=(200,30))
        # dstPort
        self.lblIcmpCode = wx.StaticText(self, label="ICMP Code:")
        self.editIcmpCode = wx.StaticText(self, label="", size=(200,30))
        # Añadimos los objetos al formulario
        icmpForm.AddMany([self.lblIcmpType, self.lblIcmpCode, self.editIcmpType, self.editIcmpCode])
        self.icmpSizer.Add(icmpForm, 1, wx.EXPAND)


        ## Botones
        self.botonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.botonSizer.AddSpacer(parent.H,-1)
        self.botonForm = wx.FlexGridSizer(1, 2, 9, 25)
        # Boton
        self.deleteBtn = wx.Button(self, -1, 'Delete')
        self.Bind(wx.EVT_BUTTON, self.Delete, id=self.deleteBtn.GetId())
        # Error panel
        self.lblError = wx.StaticText(self, label="")
        # Añadimos los objetos al formulario
        self.botonForm.AddMany([self.deleteBtn, self.lblError])
        self.botonSizer.Add(self.botonForm, 1, wx.EXPAND)


        ## Añadimos las filas al sizer principal
        self.sizer.Add(self.inforSizer, 0, wx.EXPAND)

        self.etherSizer.Hide(True)
        self.ipSizer.Hide(True)
        self.tcpSizer.Hide(True)
        self.icmpSizer.Hide(True)
        self.botonSizer.Hide(True)

        # Colocamos el sizer en el panel
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()   


    def EvtComboBox(self, event):
        self.sizer.Detach(9)    # Botones
        self.sizer.Detach(8)    # Spacer
        self.sizer.Detach(7)    # TCP
        self.sizer.Detach(6)    # Spacer
        self.sizer.Detach(5)    # IP
        self.sizer.Detach(4)    # Spacer
        self.sizer.Detach(3)    # Ether
        self.sizer.Detach(2)    # Spacer
        self.etherSizer.Hide(True)
        self.ipSizer.Hide(True)
        self.tcpSizer.Hide(True)
        self.icmpSizer.Hide(True)
        self.botonSizer.Hide(True)


        # Cargamos el filtro
        name  = self.editName.GetValue()
        filtro = self.BuscaEntrada(name)

        # Informacion
        self.editOwner.Label = filtro[1]
        self.editOwner.Layout()

        # Ethernet
        self.etherSizer.Show(True)
        self.sizer.AddSpacer(self.parent.V, -1)
        self.sizer.Add(self.etherSizer, 0, wx.EXPAND)

        self.editSrcMacAddr.Label = filtro[2]
        self.editSrcMacAddr.Layout()
        self.editDstMacAddr.Label = filtro[3]
        self.editDstMacAddr.Layout()
        self.editEtherType.Label = filtro[4]
        self.editEtherType.Layout()

        # IP
        if filtro[4] == 'IP':
            self.ipSizer.Show(True)
            self.sizer.AddSpacer(self.parent.V, -1)
            self.sizer.Add(self.ipSizer, 0, wx.EXPAND)

            self.editSrcIpAddr.Label = filtro[5]
            self.editSrcIpAddr.Layout()
            self.editDstIpAddr.Label = filtro[6]
            self.editDstIpAddr.Layout()
            self.editIpType.Label = filtro[7]
            self.editIpType.Layout()

            # TCP
            if filtro[7] == 'TCP' or filtro[7] == 'UDP':
                self.tcpSizer.Show(True)
                self.sizer.AddSpacer(self.parent.V, -1)
                self.sizer.Add(self.tcpSizer, 0, wx.EXPAND)

                self.editSrcPort.Label = filtro[8]
                self.editSrcPort.Layout()
                self.editDstPort.Label = filtro[9]
                self.editDstPort.Layout()

            # ICMP
            if filtro[7] == 'ICMP':
                self.icmpSizer.Show(True)
                self.sizer.AddSpacer(self.parent.V, -1)
                self.sizer.Add(self.icmpSizer, 0, wx.EXPAND)

                self.editIcmpType.Label = filtro[8]
                self.editIcmpType.Layout()
                self.editIcmpCode.Label = filtro[9]
                self.editIcmpCode.Layout()

        self.botonSizer.Show(True)
        self.sizer.AddSpacer(self.parent.V, -1)
        self.sizer.Add(self.botonSizer, 0, wx.EXPAND)      


        self.sizer.Layout()

        
    def Delete(self, event):
        if not(self.ComprobarExiste()):
            self.lblError.Label = "No existe ningun filtro con ese nombre"
            self.lblError.Layout()

        else:
            fichero = ''
            fd = open("filtros.cnf")
            for line in fd:
                sub_line = line.split("|")
                if sub_line[0] != self.editName.GetValue():
                    fichero = fichero + line
            fd.close()
            
            fd = open("filtros.cnf", 'w')
            fd.write(fichero)
            fd.close()
                    
            self.lblError.Label = "Exito"
            self.lblError.Layout()

            self.filtros = self.CargarFiltros()
            self.editName.Items = self.filtros
            self.editName.Layout()

            #self.parent.Parent.Close()


    def CargarFiltros(self):
        filtros = []
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            filtros.append(sub_line[0])
            line = fd.readline()
        fd.close()
        return filtros


    def BuscaEntrada(self, name):
        filtro = []
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if sub_line[0] == name:
                return sub_line

            line = fd.readline()

        return 0

    def ComprobarExiste(self):
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if (sub_line[0] == self.editName.GetValue()):
                fd.close()
                return True
            line = fd.readline()
        fd.close()
        return False


#######################################################################
##                                Add                                ##
#######################################################################

class Add(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.parent = parent

        filtros = self.CargarFiltros()
        self.interfaces = self.GetInterfaces()

        # Creamos un sizer para las columnas
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(parent.H, -1)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer2.AddSpacer(parent.V, -1)
        sizer3 = wx.BoxSizer(wx.VERTICAL)
        sizer3.AddSpacer(parent.V, -1)

        # Creamos el formulario
        form = wx.FlexGridSizer(len(filtros), 2, 9, 25)

        # Cada una de las conexiones existentes
        self.fila = []
        for i in range(len(filtros)):
            columna = []
            columna.append( wx.CheckBox(self, label=filtros[i] ) )

            self.fila.append( columna )

            form.Add(self.fila[i][0], 1, wx.EXPAND)

        # Boton
        iniciarBtn = wx.Button(self, -1, 'Add', size=(100,30))
        self.Bind(wx.EVT_BUTTON, self.Add, id=iniciarBtn.GetId())


        # Añadimos el formulario en una columna
        sizer2.Add(form, 0, wx.EXPAND)
        sizer2.AddSpacer(self.parent.V, -1)
        sizer2.Add(iniciarBtn)

        # Sizer para interfaces
        interForm = wx.FlexGridSizer(1, 2, 9, 25)
        self.lblInterface = wx.StaticText(self, label="Interface:")
        self.editInterface = wx.ComboBox(self, choices=self.interfaces.keys(), style=wx.CB_DROPDOWN, size=(200,30) )
        interForm.AddMany([self.lblInterface, self.editInterface])
        sizer3.Add(interForm, 0, wx.EXPAND)

        
        sizer.Add(sizer2, 1, wx.EXPAND)
        sizer.Add(sizer3, 1, wx.EXPAND)


        # Colocamos el sizer en el panel
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()

    def Add(self,event):
        filtros_seleccionados = self.GetFiltrosSeleccionados()
        for name in filtros_seleccionados:
            line = self.BuscaEntrada(name)
            data, dataMask, dataNotMask = self.GeneraFiltro(line)
            self.LanzarFiltro(data, dataMask, dataNotMask, line[0], line[1])

    def LanzarFiltro(self, data, dataMask, dataNotMask, description, owner):
        name = self.parent.conexion_seleccionada[0]
        ip_addr = self.parent.conexion_seleccionada[1]
        community = self.parent.conexion_seleccionada[2]
        version = self.parent.conexion_seleccionada[3]
        oid_interface = self.interfaces[self.editInterface.GetValue()]
        print(oid_interface)
        indice = self.BuscaIndice()

        # Grupo filter
        # Primero creo el filtro
        # Creo la entrada con filterStatus
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.11." + indice, "i", "2"])
        # Le indico el propietario con filterOwner
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.10." + indice, "s", owner])
        # Le indico a que canal pertenece con filterChannelIndex
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.2." + indice, "i", indice])
        # Le indico el offset del paquete con filterPktDataOffset 14 de ethernet
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.3." + indice, "i", "0" ])
        # Le indico los datos que me interesan
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.4." + indice, "x", data ])
        # Le indico la mascara de los datos con filterPktDataMask
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.5." + indice, "x", dataMask ])
        # Le indico la mascara de los datos con filterPktDataNotMask
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.6." + indice, "x", dataNotMask ])
        # Le indico el estado que me interesan
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.7." + indice, "i", "0"])
        # Le indico la mascara de los datos con filterPktDataMask
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.8." + indice, "i", "7"])
        # Le indico la mascara de los datos con filterPktDataNotMask
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.9." + indice, "i", "0"])
        # Activo la entrada con filterStatus
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.1.1.11." + indice, "i", "1"])

        # Ahora tengo que crear el canal
        # Creo la entrada con channelStatus
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.12." + indice, "i", "2"])
        # Le indico el propietario con channelOwner
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.11." + indice, "s", owner])
        # Le doy una descriptcion textual
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.10." + indice, "s", description ])
        # Controlo el interfaz por el que filtro con channelIfIndex
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.2." + indice, "i", oid_interface])
        # Controlo la accion asociada con este canal con channelAcceptType
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.3." + indice, "i", "1"])
        # Controlo si el canal esta activado o no con channelDataControl
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.4." + indice, "i", "1"])
        # Controla el evento que se va a hacer que el canal se active, en caso de no
        # estarlo (0 es que no hay)
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.5." + indice, "i", "0"])
        # Controla el evento que se va a hacer que el canal se desactive, en caso de no
        # estarlo (0 es que no hay)
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.6." + indice, "i", "0"])
        # Controla el evento que se va a disparar el canal, en caso de no
        # estarlo (0 es que no hay)
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.7." + indice, "i", "0"])
        # Controla la forma en que se dispara eventos
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.8." + indice, "i", "2"])
        # Activo la entrada con channelStatus
        subprocess.call(["snmpset", "-v", version, "-c", community, ip_addr, "1.3.6.1.2.1.16.7.2.1.12." + indice, "i", "1"])



    def BuscaIndice(self):
        name = self.parent.conexion_seleccionada[0]
        address = self.parent.conexion_seleccionada[1]
        community = self.parent.conexion_seleccionada[2]
        version = self.parent.conexion_seleccionada[3]
        oid_description = "1.3.6.1.2.1.16.7.2.1.10"
        resp_description = subprocess.check_output(["snmpwalk", "-v", version, "-c", community, "-Oben", address, oid_description])
        indice = 0
        resp_description = resp_description.split('\n')
        line = resp_description[len(resp_description)-2]

        aux = line.split(' ')
        aux = aux[0].split('.')
        indice = str( int(aux[len(aux)-1]) + 1)

        return indice


    def GeneraFiltro(self, datos):
        data = ''
        dataMask = ''
        dataNotMask = ''
        
        #Detectar formato correcto en todos los campos al crear

        # SRC MAC Addr
        if datos[2] != '*':            
            data += ''.join(datos[2].split(':'))
            dataMask += "FFFFFFFFFFFF"
        else:
            data += "000000000000"
            dataMask += "000000000000"

        # DST MAC Addr
        if datos[3] != '*':
            data += ''.join(datos[3].split(':'))
            dataMask += "FFFFFFFFFFFF"
        else:
            data += "000000000000"
            dataMask += "000000000000"

        # Ether Type
        if datos[4] == 'ARP':
            data += "0806"
            dataMask += "FFFF"
        elif datos[4] == 'IP':
            data += "0800"
            dataMask += "FFFF"
        else:
            data += "0000"
            dataMask += "0000"

        # Si es IP
        if datos[4] == 'IP':
            # Relleno para los campos de la cabecera
            data += "000000000000000000"
            dataMask += "000000000000000000"

            # IP Type
            if datos[7] == 'TCP':
                data += "06"
                dataMask += "FF"
            elif datos[7] == 'UDP':
                data += "11"
                dataMask += "FF"            
            elif datos[7] == 'ICMP':
                data += "01"
                dataMask += "FF"
            else:
                data += "00"
                dataMask += "00"

            # Relleno para los campos de la cabecera
            data += "0000"
            dataMask += "0000"
                
            # SRC IP Addr
            if datos[5] != '*':
                aux = datos[5].split('.')
                for i in aux:
                    if int(i) < 16:
                        data += "0"
                    data += format(int(i),"x")
                dataMask += "FFFFFFFF"
            else:
                data += "00000000"
                dataMask += "00000000"
                
            # DST IP Addr
            if datos[6] != '*':
                aux = datos[6].split('.')
                for i in aux:
                    if int(i) < 16:
                        data += "0"
                    data += format(int(i),"x")
                dataMask += "FFFFFFFF"
            else:
                data += "00000000"
                dataMask += "00000000"

            # Si es TCP o UDP
            if datos[7] == 'TCP' or datos[7] == 'UDP':
                
                # SRC Port
                if datos[8] != '*':
                    if int(datos[8]) < 16:
                        data += "000"
                    elif int(datos[8]) < 256:
                        data += "00"
                    elif int(datos[8]) < 4096:
                        data += "0"                    
                    data += format(int(datos[8]),"x")
                    dataMask += "FFFF"
                else:
                    data += "0000"
                    dataMask += "0000"                    

                # DST Port
                if datos[9] != '*':
                    if int(datos[9]) < 16:
                        data += "000"
                    elif int(datos[9]) < 256:
                        data += "00"
                    elif int(datos[9]) < 4096:
                        data += "0"
                    data += format(int(datos[9]),"x")
                    dataMask += "FFFF"
                else:
                    data += "0000"
                    dataMask += "0000"                      

            # Si es ICMP
            if datos[7] == 'ICMP':

                # ICMP Type
                if datos[8] != '*':
                    if int(datos[8]) < 16:
                        data += "0"
                    data += format(int(datos[8]),"x")
                    dataMask += "FF"
                else:
                    data += "00"
                    dataMask += "00"

                # ICMP Code
                if datos[9] != '*':
                    if int(datos[9]) < 16:
                        data += "0"
                    data += format(int(datos[9]),"x")
                    dataMask += "FF"
                else:
                    data += "00"
                    dataMask += "00"
        
        dataNotMask = "0"*len(dataMask)

        return data, dataMask, dataNotMask


    def GetFiltrosSeleccionados(self):
        filtros_seleccionados = []
        for i in range(len(self.fila)):
            if self.fila[i][0].GetValue():
                filtros_seleccionados.append(self.fila[i][0].GetLabel() )
        return filtros_seleccionados
                
    def CargarFiltros(self):
        filtros = []
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            filtros.append(sub_line[0])
            line = fd.readline()
        fd.close()
        return filtros


    def BuscaEntrada(self, name):
        filtro = []
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if sub_line[0] == name:
                return sub_line

            line = fd.readline()

        return 0

    def ComprobarExiste(self):
        fd = open("filtros.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if (sub_line[0] == self.editName.GetValue()):
                fd.close()
                return True
            line = fd.readline()
        fd.close()
        return False

    def GetInterfaces(self):
        interfaces = dict()
        name = self.parent.conexion_seleccionada[0]
        address = self.parent.conexion_seleccionada[1]
        community = self.parent.conexion_seleccionada[2]
        version = self.parent.conexion_seleccionada[3]
        oid_interfaces = "1.3.6.1.2.1.2.2.1.2"
        resp_interfaces = subprocess.check_output(["snmpwalk", "-v", version, "-c", community, "-Oben", address, oid_interfaces])

        resp_interfaces = resp_interfaces.split('\n')
        for i in range(len(resp_interfaces)-1):
            line = resp_interfaces[i]
            aux = line.split('\"')
            nombre = aux[1]
            aux = aux[0].split(' ')
            aux = aux[0].split('.')
            indice = aux[len(aux)-1]
            interfaces[nombre] = indice

        return interfaces



#######################################################################
##                                Show                               ##
#######################################################################

class Show(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.parent = parent

        filtros = self.CargarFiltros()

        # Creamos un sizer para las columnas
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(parent.H, -1)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer2.AddSpacer(parent.V, -1)

        # Creamos el formulario
        self.form = wx.FlexGridSizer(len(filtros), 3, 9, 25)

        # Cada una de las conexiones existentes
        self.fila = []
        for i in range(len(filtros)):
            columna = []
            columna.append( wx.CheckBox(self, label=filtros[i][0] ) )
            columna.append( wx.StaticText(self, label=filtros[i][1] ) )
            columna.append( wx.StaticText(self, label=filtros[i][2] ) )

            self.fila.append( columna )

            self.form.Add(self.fila[i][0], 1, wx.EXPAND)
            self.form.Add(self.fila[i][1], 1, wx.EXPAND)
            self.form.Add(self.fila[i][2], 1, wx.EXPAND)

        # Boton
        self.iniciarBtn = wx.Button(self, -1, 'Delete')
        self.form.Add(self.iniciarBtn, 1, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.Delete, id=self.iniciarBtn.GetId())

        # Añadimos el formulario en una columna
        self.sizer2.Add(self.form, 1, wx.EXPAND)
        sizer.Add(self.sizer2, 1, wx.EXPAND)

        # Colocamos el sizer en el panel
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()

    def Delete(self,event):
        name = self.parent.conexion_seleccionada[0]
        address = self.parent.conexion_seleccionada[1]
        community = self.parent.conexion_seleccionada[2]
        version = self.parent.conexion_seleccionada[3]
        oid_channel = "1.3.6.1.2.1.16.7.2.1.12."
        oid_filter = "1.3.6.1.2.1.16.7.1.1.11."
        for i in range(len(self.fila)):
            if self.fila[i][0].GetValue():
                index = self.fila[i][0].GetLabel()
                subprocess.call(["snmpset", "-v", version, "-c", community, address, oid_channel + str(index), "i", "4"])
                subprocess.call(["snmpset", "-v", version, "-c", community, address, oid_filter + str(index), "i", "4"])

        # Recargamos la pantalla
        filtros = self.CargarFiltros()
        for i in range(len(self.fila)):
            self.fila[i][0].Destroy()
            self.fila[i][1].Destroy()
            self.fila[i][2].Destroy()
        self.iniciarBtn.Destroy()
        self.form.Clear()
        self.sizer2.Detach(self.form)

        # Creamos el formulario
        self.form = wx.FlexGridSizer(len(filtros), 3, 9, 25)

        # Cada una de las conexiones existentes
        self.fila = []
        for i in range(len(filtros)):
            columna = []
            columna.append( wx.CheckBox(self, label=filtros[i][0] ) )
            columna.append( wx.StaticText(self, label=filtros[i][1] ) )
            columna.append( wx.StaticText(self, label=filtros[i][2] ) )

            self.fila.append( columna )

            self.form.Add(self.fila[i][0], 1, wx.EXPAND)
            self.form.Add(self.fila[i][1], 1, wx.EXPAND)
            self.form.Add(self.fila[i][2], 1, wx.EXPAND)

        # Boton
        self.iniciarBtn = wx.Button(self, -1, 'Delete')
        self.form.Add(self.iniciarBtn, 1, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.Delete, id=self.iniciarBtn.GetId())

        # Añadimos el formulario en una columna
        self.sizer2.Add(self.form, 1, wx.EXPAND)
        self.sizer2.Layout()

        self.SetAutoLayout(1)
        self.SetupScrolling()

    def CargarFiltros(self):
        name = self.parent.conexion_seleccionada[0]
        address = self.parent.conexion_seleccionada[1]
        community = self.parent.conexion_seleccionada[2]
        version = self.parent.conexion_seleccionada[3]
        oid_description = "1.3.6.1.2.1.16.7.2.1.10"
        oid_matches = "1.3.6.1.2.1.16.7.2.1.9"
        resp_description = subprocess.check_output(["snmpwalk", "-v", version, "-c", community, "-Oben", address, oid_description])
        resp_matches = subprocess.check_output(["snmpwalk", "-v", version, "-c", community, "-Oben", address, oid_matches])

        filtros = self.ProcesaRespuesta(resp_description, resp_matches)
        return filtros

    def ProcesaRespuesta(self, resp_description, resp_matches):
        filtros = []
        resp_description = resp_description.split('\n')
        resp_matches = resp_matches.split('\n')
        for i in range(len(resp_description)-1):
            line = resp_description[i]
            aux = line.split('\"')
            description = aux[1]
            aux = aux[0].split(' ')
            aux = aux[0].split('.')
            indice = aux[len(aux)-1]

            line = resp_matches[i]
            aux = line.split(' ')
            matches = aux[len(aux)-1]
            filtros.append([indice, description, matches])

        return filtros
