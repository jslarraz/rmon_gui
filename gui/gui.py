# -*- coding: utf-8 -*-
import wx
import  wx.lib.scrolledpanel as scrolled
import conexiones
import filter


##class Panel(wx.Panel):
##    def __init__(self, parent):
##        wx.Panel.__init__(self, parent)
##        
##        sizer = wx.BoxSizer()
##        quote = wx.StaticText(self, label="Your quote :")
##        sizer.Add(quote, 1, wx.EXPAND)
##        self.SetSizer(sizer)

class Panel(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.parent = parent
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        quote = wx.StaticText(self, label="Welcome")
        sizer.Add(quote, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()

class MainFrame(wx.Frame):
    conexion_seleccionada=None
    V = 20
    H = 20
    def __init__(self):
        wx.Frame.__init__(self, None, title="Be easy", size=wx.DisplaySize())        

        ## Creamos la barra de menus

        # File Menu
        fileMenu = wx.Menu()
        
        file_open = fileMenu.Append(wx.ID_OPEN, "Open"," Open a file to edit")
        self.Bind(wx.EVT_MENU, self.OnFile_Open, file_open)
        
        file_about= fileMenu.Append(wx.ID_ABOUT, "About"," About the program")
        self.Bind(wx.EVT_MENU, self.OnFile_About, file_about)

        file_exit = fileMenu.Append(wx.ID_EXIT,"Exit"," Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnFile_Exit, file_exit)

        # Conexion Menu
        conexionMenu = wx.Menu()
        
        conexion_add = conexionMenu.Append(wx.NewId(), "Add"," Add a new conexion")
        self.Bind(wx.EVT_MENU, self.OnConexion_Add, conexion_add)
        
        conexion_edit = conexionMenu.Append(wx.NewId(), "Edit"," Edit a existing conexion")
        self.Bind(wx.EVT_MENU, self.OnConexion_Edit, conexion_edit)

        conexion_delete = conexionMenu.Append(wx.NewId(), "Delete"," Delete a existing conexion")
        self.Bind(wx.EVT_MENU, self.OnConexion_Delete, conexion_delete)

        conexionMenu.AppendSeparator()

        conexion_select = conexionMenu.Append(wx.NewId(), "Select"," Select a existing conexion")
        self.Bind(wx.EVT_MENU, self.OnConexion_Select, conexion_select)

        # Filter Menu
        filterMenu = wx.Menu()
        
        filter_create = filterMenu.Append(wx.NewId(), "Create"," Create a new filter")
        self.Bind(wx.EVT_MENU, self.OnFilter_Create, filter_create)

        #filter_edit = filterMenu.Append(wx.NewId(), "Edit"," Edit an existing filter")
        #self.Bind(wx.EVT_MENU, self.OnFilter_Edit, filter_edit)

        filter_delete = filterMenu.Append(wx.NewId(), "Delete"," Delete an existing filter")
        self.Bind(wx.EVT_MENU, self.OnFilter_Delete, filter_delete)

        filterMenu.AppendSeparator()

        filter_add = filterMenu.Append(wx.NewId(), "Add"," Add an existing filter to an existing connection")
        self.Bind(wx.EVT_MENU, self.OnFilter_Add, filter_add)

        filter_show = filterMenu.Append(wx.NewId(), "Show"," Show filters")
        self.Bind(wx.EVT_MENU, self.OnFilter_Show, filter_show)

        # Creating the menubar.
        menuBar = wx.MenuBar()
        #menuBar.Append(fileMenu,"File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(conexionMenu,"Conexion") # Adding the "filemenu" to the MenuBar
        menuBar.Append(filterMenu,"Filter") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.


        ## Añadimos el Panel de bienvenida
        sizer = wx.BoxSizer()
        panel = Panel(self)
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def OnFile_Open(self,e):
        self.Close(True)  # Close the frame.

    def OnFile_About(self,e):
        self.Close(True)  # Close the frame.
                
    def OnFile_Exit(self,e):
        self.Close(True)  # Close the frame.

    def OnConexion_Add(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = conexiones.Add(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()
                
    def OnConexion_Edit(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = conexiones.Edit(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()
                
    def OnConexion_Delete(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = conexiones.Delete(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()

    def OnConexion_Select(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = conexiones.Select(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()

    def OnFilter_Create(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = filter.Create(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()  
        
#    def OnFilter_Edit(self,e):
#        self.DestroyChildren()
#        sizer = self.GetSizer()
#        mipanel = conexiones.Delete(self)
#        sizer.Add(mipanel, 1, wx.EXPAND)
#        sizer.Layout()

    def OnFilter_Delete(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = filter.Delete(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()

    def OnFilter_Add(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = filter.Add(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()

    def OnFilter_Show(self,e):
        self.DestroyChildren()
        sizer = self.GetSizer()
        mipanel = filter.Show(self)
        sizer.Add(mipanel, 1, wx.EXPAND)
        sizer.Layout()
        

app = wx.App()
frame = MainFrame()
frame.Show()
app.MainLoop()
