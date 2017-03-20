# -*- coding: utf-8 -*-
import wx
import  wx.lib.scrolledpanel as scrolled
#import os

class Add(scrolled.ScrolledPanel):
    
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        
        # Separacion vertical entre filas
        V1 = 30
        # Separacion vertical extra hasta el boton
        V2 = 10
        # Offset hasta la primera columna
        H1 = 20
        # Offset hasta la segunda columna
        H2 = 140
        # Offset hasta el boton
        H3 = 100
        # Ancho de campo de datos
        A1 = 140
        # Ancho de Boton
        A2 = 100

        # Name
        self.lblName = wx.StaticText(self, label="Name:", pos=(H1, V1))
        self.editName = wx.TextCtrl(self, value="", pos=(H2, V1), size=(A1,-1))

        # Address
        self.lblAddress = wx.StaticText(self, label="Address:", pos=(H1, V1*2))
        self.editAddress = wx.TextCtrl(self, value="", pos=(H2, V1*2), size=(A1,-1))

        # Community
        self.lblCommunity = wx.StaticText(self, label="Community:", pos=(H1, V1*3))
        self.editCommunity = wx.TextCtrl(self, value="", pos=(H2, V1*3), size=(A1,-1))

        # Version
        self.sampleList = ['1', '2c', '3']
        self.lblVersion = wx.StaticText(self, label="Version:", pos=(H1, V1*4))
        self.editVersion = wx.ComboBox(self, pos=(H2, V1*4), size=(A1, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        # Boton
        iniciarBtn = wx.Button(self, -1, 'Add', pos=(H3, V1*5+V2), size=(A2, -1))
        self.Bind(wx.EVT_BUTTON, self.Add, id=iniciarBtn.GetId())

        # Error panel
        self.lblError = wx.StaticText(self, label="", pos=(70, 200))

    def Add(self,event):
        self.lblError.Destroy()

        if Funciones().ComprobarCamposBlanco(self):
            self.lblError = wx.StaticText(self, label="Algun campo en blanco", pos=(70, 200))

        elif Funciones().ComprobarExiste(self):
            self.lblError = wx.StaticText(self, label="Ya existe una entrada con este nombre", pos=(15, 200))

        else:
            fd = open("conexiones.cnf", 'a')
            fd.write(self.editName.GetValue() + "|")
            fd.write(self.editAddress.GetValue() + "|")
            fd.write(self.editCommunity.GetValue() + "|")
            fd.write(self.editVersion.GetValue() + "\n")
            fd.close()
            self.lblError = wx.StaticText(self, label="Exito", pos=(130, 200) )       
            #self.parent.Parent.Close()


class Edit(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        # Separacion vertical entre filas
        V1 = 30
        # Separacion vertical extra hasta el boton
        V2 = 10
        # Offset hasta la primera columna
        H1 = 20
        # Offset hasta la segunda columna
        H2 = 140
        # Offset hasta el boton
        H3 = 100
        # Ancho de campo de datos
        A1 = 140
        # Ancho de Boton
        A2 = 100

        self.conexiones = Funciones().CargarConexiones()

        # Name
        self.lblName = wx.StaticText(self, label="Name:", pos=(H1, V1))
        self.editName = wx.ComboBox(self, pos=(H2, V1), size=(A1, -1), choices=self.conexiones, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editName)

        # Address
        self.lblAddress = wx.StaticText(self, label="Address:", pos=(H1, V1*2))
        self.editAddress = wx.TextCtrl(self, value="", pos=(H2, V1*2), size=(A1,-1))

        # Community
        self.lblCommunity = wx.StaticText(self, label="Community:", pos=(H1, V1*3))
        self.editCommunity = wx.TextCtrl(self, value="", pos=(H2, V1*3), size=(A1,-1))

        # Version
        self.sampleList = ['1', '2c', '3']
        self.lblVersion = wx.StaticText(self, label="Version:", pos=(H1, V1*4))
        self.editVersion = wx.ComboBox(self, pos=(H2, V1*4), size=(A1, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        # Boton
        iniciarBtn = wx.Button(self, -1, 'Save', pos=(H3, V1*5+V2), size=(A2, -1))
        self.Bind(wx.EVT_BUTTON, self.Edit, id=iniciarBtn.GetId())

        # Error panel
        self.lblError = wx.StaticText(self, label="", pos=(70, 200))        

    def Edit(self,event):
        self.lblError.Destroy()

        if Funciones().ComprobarCamposBlanco(self):
            self.lblError = wx.StaticText(self, label="Algun campo en blanco", pos=(70, 200))

        elif not(Funciones().ComprobarExiste(self)):
            self.lblError = wx.StaticText(self, label="No existe ninguna conexion con ese nombre", pos=(70, 200))

        else:
            fichero = ''
            fd = open("conexiones.cnf")
            for line in fd:
                sub_line = line.split("|")
                if sub_line[0] != self.editName.GetValue():
                    fichero = fichero + line
                else:
                    fichero = fichero + self.editName.GetValue() + "|"
                    fichero = fichero + self.editAddress.GetValue() + "|"
                    fichero = fichero + self.editCommunity.GetValue() + "|"
                    fichero = fichero + self.editVersion.GetValue() + "\n"
            fd.close()
            
            fd = open("conexiones.cnf", 'w')
            fd.write(fichero)
            fd.close()
                    
            self.lblError = wx.StaticText(self, label="Exito", pos=(130, 200) )       
            #self.parent.Parent.Close()

    def EvtComboBox(self, event):
        name  = self.editName.GetValue()
        conexion = Funciones().BuscaEntrada(name)
        self.editAddress.SetValue(conexion[1])
        self.editCommunity.SetValue(conexion[2])
        self.editVersion.SetValue(conexion[3])


class Delete(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        # Separacion vertical entre filas
        V1 = 30
        # Separacion vertical extra hasta el boton
        V2 = 10
        # Offset hasta la primera columna
        H1 = 20
        # Offset hasta la segunda columna
        H2 = 140
        # Offset hasta el boton
        H3 = 100
        # Ancho de campo de datos
        A1 = 140
        # Ancho de Boton
        A2 = 100

        self.conexiones = Funciones().CargarConexiones()

        # Name
        self.lblName = wx.StaticText(self, label="Name:", pos=(H1, V1))
        self.editName = wx.ComboBox(self, pos=(H2, V1), size=(A1, -1), choices=self.conexiones, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editName)

        # Address
        self.lblAddress = wx.StaticText(self, label="Address:", pos=(H1, V1*2))
        self.editAddress = wx.StaticText(self, label="", pos=(H2, V1*2), size=(A1,-1))

        # Community
        self.lblCommunity = wx.StaticText(self, label="Community:", pos=(H1, V1*3))
        self.editCommunity = wx.StaticText(self, label="", pos=(H2, V1*3), size=(A1,-1))

        # Version
        self.lblVersion = wx.StaticText(self, label="Version:", pos=(H1, V1*4))
        self.editVersion = wx.StaticText(self, label="", pos=(H2, V1*4), size=(A1, -1))

        # Boton
        iniciarBtn = wx.Button(self, -1, 'Delete', pos=(H3, V1*5+V2), size=(A2, -1))
        self.Bind(wx.EVT_BUTTON, self.Delete, id=iniciarBtn.GetId())

        # Error panel
        self.lblError = wx.StaticText(self, label="", pos=(70, 200))        

    def Delete(self,event):
        self.lblError.Destroy()

        if not(Funciones().ComprobarExiste(self)):
            self.lblError = wx.StaticText(self, label="Algun campo en blanco", pos=(70, 200))

        else:
            fichero = ''
            fd = open("conexiones.cnf")
            for line in fd:
                sub_line = line.split("|")
                if sub_line[0] != self.editName.GetValue():
                    fichero = fichero + line
            fd.close()
            
            fd = open("conexiones.cnf", 'w')
            fd.write(fichero)
            fd.close()
                    
            self.lblError = wx.StaticText(self, label="Exito", pos=(130, 200) )       

            self.conexiones = Funciones().CargarConexiones()
            self.editName.Items = self.conexiones
            self.editName.Layout()
            #self.parent.Parent.Close()


    def EvtComboBox(self, event):
        self.editAddress.Destroy()
        self.editCommunity.Destroy()
        self.editVersion.Destroy()

        name  = self.editName.GetValue()
        conexion = Funciones().BuscaEntrada(name)
        self.editAddress = wx.StaticText(self, label=conexion[1], pos=(140, 30*2), size=(140,-1))
        self.editCommunity = wx.StaticText(self, label=conexion[2], pos=(140, 30*3), size=(140,-1))
        self.editVersion = wx.StaticText(self, label=conexion[3], pos=(140, 30*4), size=(140, -1))


class Select(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.parent = parent

        # Cargamos la lista de conexiones
        conexiones = Funciones().CargarConexiones()

        # Creamos un sizer para las columnas
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(parent.H, -1)

        # Creamos el formulario
        form = wx.FlexGridSizer(len(conexiones), 1, 9, 25)
        form.AddSpacer(parent.V, -1)

        # Cada una de las conexiones existentes
        self.check = []
        for i in range(len(conexiones)):
            self.check.append( wx.RadioButton(self, label=conexiones[i]) )
            form.Add(self.check[i], 1, wx.EXPAND)

        # Boton
        iniciarBtn = wx.Button(self, -1, 'Select')
        form.Add(iniciarBtn, 1, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.Select, id=iniciarBtn.GetId())

        # Añadimos el formulario en una columna
        sizer.Add(form, 1, wx.EXPAND)

        # Colocamos el sizer en el panel
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()

    def Select(self,event):
        for i in range(len(self.check)):
            if self.check[i].GetValue():
                name = self.check[i].GetLabel()
                
        self.parent.conexion_seleccionada = Funciones().BuscaEntrada(name)


class Funciones:

    def CargarConexiones(self):
        conexiones = []
        fd = open("conexiones.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            conexiones.append(sub_line[0])
            line = fd.readline()
        fd.close()
        return conexiones

    def BuscaEntrada(self, name):
        conexion = []
        fd = open("conexiones.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if sub_line[0] == name:
                conexion.append(sub_line[0])
                conexion.append(sub_line[1])
                conexion.append(sub_line[2])
                aux = sub_line[3].split("\n")
                conexion.append(aux[0])
                conexion.append(str(3))  # Oid interface
                fd.close()
                return conexion

            line = fd.readline()

        return 0

    def ComprobarCamposBlanco(self, parent):
        if (parent.editName.GetValue() == "") or \
           (parent.editAddress.GetValue() == "") or \
           (parent.editCommunity.GetValue() == "") or \
           (parent.editVersion.GetValue() == ""):
            return True
        else:
            return False

    def ComprobarExiste(self, parent):
        fd = open("conexiones.cnf")
        line = fd.readline()
        while line:
            sub_line = line.split("|")
            if (sub_line[0] == parent.editName.GetValue()):
                fd.close()
                return True
            line = fd.readline()
        fd.close()
        return False
