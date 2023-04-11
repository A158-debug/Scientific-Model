#    This is a module class which calculate the optimized G (hkl) to maximize the EMCD signal -------------------------------------------------------------
#    This module is called by the main menu option to do the G optimizatio calculation -------------------------------------------------------------------------
#  ****************************************************************************************************************************************
from __future__ import division
import wx
import wx.grid as gridlib
import numpy as np
import EMCD_GUI_beta as Main_Frame
import math, os
import Make_Menus.Make_Main_Menu as Make_Menu
import Load_structure.Load_structure_info as Load_Structure
import matplotlib.pyplot as plt
from matplotlib import rc
import TEM_Properties.Tem_properties as TEM
import Volume_dhkl.volume_dhkl_class as VDHKL
import Lobato_Constants.Lobato_parameter as Lobato
import Physics_Constans.Physics_Constant as Phys_Const


rc('text', usetex=True)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Do_G_Optimization():
        
            def __init__(self):
                        #wx.Frame.__init__(self, None, title= "G Optimization")

            #---------------- Load the structure file ---------------------------------------------------------------------------------------------------
                        self.Author_Name = "DEVENDRA SINGH NEGI"
                        #---------------- Loading the file and extractiong the information from that file ------------------------
                        wildcard = "Structure Files (*.struct)|*.struct"
                        dialog = wx.FileDialog(None, "Open Text Files", wildcard=wildcard,
                                    style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                        if dialog.ShowModal() == wx.ID_CANCEL:
                                    dialog.Destroy()
                        else:
                                    self.Structure_File_Path = dialog.GetPath()
                                    self.Structure_File_Name =  os.path.basename(self.Structure_File_Path)
                                    self.Structure_File_Extension = (self.Structure_File_Name).split(".")[1]

                        #---------------- Getting the information from the input file -----------------------------------------------------------------------------------------------
                        #------- There exist a serpate module which reads the file and extract the information from the input structure file -
                                    self.Struct_Information =  Load_Structure.Extract_Structure_Info().Extract_Info(self.Structure_File_Path)

                                    self.Material_Name_From_File = self.Struct_Information[0]
                                    Lattice_Type_From_File = self.Struct_Information[1]
                                    self.Inequivalent_Atom_From_File = int(self.Struct_Information[2])
                                    self.Lattice_Parameter_Angle_List = self.Struct_Information[3]
                                    self.Multiplicity_List_From_File = self.Struct_Information[4]
                                    self.Atom_Name_List = self.Struct_Information[5]
                                    self.Atom_Z_LIST = self.Struct_Information[6]
                                    self.X_Coordinate_List = self.Struct_Information[7]
                                    self.Y_Coordinate_List = self.Struct_Information[8]
                                    self.Z_Coordinate_List = self.Struct_Information[9]


                        #--------------- Extracting the information from the loaded file -----------------------------------------------------------------------------------------------------------

            #************************* Starting making the Frame for the Final Template ------------------------------------------------------------------------------------------
            #----- Instance for getting the main frame variables and attributes -------------------------------------------------------------------------------------------------------------

                                    ins = Main_Frame.Create_Main_Dialog()
                                    size_x = ins.Window_Size_X/3
                                    size_y = ins.Window_Size_Y/1.5

                                    self.First_Template = wx.Frame(None, title="Input Template")
                                    self.First_Template.SetSize((size_x, size_y))
                                    self.First_Template.Center()
                                    self.G_Opti_Panel = wx.Panel(self.First_Template, style=wx.SUNKEN_BORDER)
                                    self.G_Opti_Panel.SetBackgroundColour("white")

            #---------------------Boxsizer to put all the input box -----------------------------------------------------------------------------------------------------------------------------------------

                                    self.Gopti_box = wx.BoxSizer(wx.VERTICAL)

                        #---------- Title box ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    title_box = wx.BoxSizer(wx.HORIZONTAL)
                                    Title_text = wx.StaticText(self.G_Opti_Panel, -1, " Title     : ")
                                    Title_text.SetFont(ins.Global_Font)
                                    self.Title_text_ctrl = wx.TextCtrl(self.G_Opti_Panel, -1,"Material", style=wx.TE_PROCESS_ENTER )
                                    self.Title_text_ctrl.SetValue(self.Material_Name_From_File)
                                    title_box.Add(Title_text, 0,  flag=wx.ALIGN_LEFT|wx.ALIGN_CENTER, border=2)
                                    title_box.Add(self.Title_text_ctrl, proportion=1, flag=wx.ALIGN_RIGHT| wx.EXPAND, border=2)

                        #----- Crystal Lattice type box --------------------------------------------------------------------------------------------------------------------------------------------------------
                                    lattice_box = wx.BoxSizer(wx.HORIZONTAL)
                                    lattice_text = wx.StaticText(self.G_Opti_Panel, -1, " Lattice : ")
                                    lattice_text.SetFont(ins.Global_Font)
                                    lattice_choice = ['Cubic', 'Tetragonal', 'Hexagonal', 'Orthorhombic', 'Rhombhohedral', 'Monoclinic', 'Triclinic']
                                    #self.lattice_text_ctrl = wx.TextCtrl(self.G_Opti_Panel, -1, "Cubic", style=wx.TE_PROCESS_ENTER)
                                    self.lattice_choice_combo_box = wx.ComboBox(self.G_Opti_Panel, -1, "Cubic",   choices=lattice_choice, style=wx.CB_SIMPLE)
                                    lattice_box.Add(lattice_text, 0, flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER, border=2)
                                    lattice_box.Add(self.lattice_choice_combo_box, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND, border=2)

                        #----- lattice parameter text -----------------------------------------------------------------------------------------------------------------------------------------------------------
                                    lattice_parameter_text_box = wx.BoxSizer(wx.HORIZONTAL)
                                    lattice_parameter_text = wx.StaticText(self.G_Opti_Panel, -1, "Lattice Parameter : ")
                                    lattice_parameter_text.SetFont(ins.Global_Font)
                                    lattice_parameter_text_box.Add(lattice_parameter_text, proportion=1, flag=wx.ALL|wx.ALIGN_LEFT, border=4)

                        #---- Lattice parameter a, b, c --------------------------------------------------------------------------------------------------------------------------------------------------------
                                    lattice_distance_box = wx.BoxSizer(wx.HORIZONTAL)
                                    self.lattice_a = wx.TextCtrl(self.G_Opti_Panel, -1, "a = x (nm)", style=wx.TE_PROCESS_ENTER)
                                    self.lattice_a.SetValue("%s"%(self.Lattice_Parameter_Angle_List[0]))
                                    self.lattice_b = wx.TextCtrl(self.G_Opti_Panel, -1, "b = x (nm)", style=wx.TE_PROCESS_ENTER)
                                    self.lattice_b.SetValue("%s" % (self.Lattice_Parameter_Angle_List[1]))
                                    self.lattice_c = wx.TextCtrl(self.G_Opti_Panel, -1, "c = x (nm)", style=wx.TE_PROCESS_ENTER)
                                    self.lattice_c.SetValue("%s" % (self.Lattice_Parameter_Angle_List[2]))
                                    lattice_distance_box.Add(self.lattice_a, proportion=1,flag=wx.ALL|wx.ALIGN_LEFT | wx.EXPAND, border=4)
                                    lattice_distance_box.Add(self.lattice_b, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER | wx.EXPAND, border=4)
                                    lattice_distance_box.Add(self.lattice_c, proportion=1,flag=wx.ALL|wx.ALIGN_RIGHT | wx.EXPAND, border=4)

                        #------ lattice angle self.alpha, self.beta, gamma ------------------------------------------------------------------------------------------------------------------------
                                    lattice_angle_box = wx.BoxSizer(wx.HORIZONTAL)
                                    self.alpha_ctrl = wx.TextCtrl(self.G_Opti_Panel, -1, "alpha = x (deg)", style=wx.TE_PROCESS_ENTER)
                                    self.alpha_ctrl.SetValue("%s"%(self.Lattice_Parameter_Angle_List[3]))
                                    self.beta_ctrl =  wx.TextCtrl(self.G_Opti_Panel, -1,  "beta =  x (deg)", style=wx.TE_PROCESS_ENTER)
                                    self.beta_ctrl.SetValue("%s" % (self.Lattice_Parameter_Angle_List[4]))
                                    self.gama_ctrl = wx.TextCtrl(self.G_Opti_Panel, -1, "gama = x (deg)", style=wx.TE_PROCESS_ENTER)
                                    self.gama_ctrl.SetValue("%s" % (self.Lattice_Parameter_Angle_List[5]))
                                    lattice_angle_box.Add(self.alpha_ctrl, proportion=1, flag=wx.ALL | wx.ALIGN_LEFT | wx.EXPAND, border=4)
                                    lattice_angle_box.Add(self.beta_ctrl, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER | wx.EXPAND, border=4)
                                    lattice_angle_box.Add(self.gama_ctrl, proportion=1, flag=wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND, border=4)

                        #--- Inequivlaent atoms ------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    inequiv_atom_box = wx.BoxSizer(wx.HORIZONTAL)
                                    inequiv_text = wx.StaticText(self.G_Opti_Panel, -1, "Inequivalent atoms   : ")
                                    inequiv_text.SetFont(ins.Global_Font)
                                    self.inequiv_text_ctrl = wx.TextCtrl(self.G_Opti_Panel, -1, "0" )#, style=wx.TE_PROCESS_ENTER)
                                    self.inequiv_text_ctrl.SetValue("%s"%self.Inequivalent_Atom_From_File)
                                    inequiv_atom_box.Add(inequiv_text, 0, flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER, border=2)
                                    inequiv_atom_box.Add(self.inequiv_text_ctrl, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND, border=2)

                        #------- Accelearation voltage of the probe -------------------------------------------------------------------------------------------------------------------------------
                                    accel_voltage_box = wx.BoxSizer(wx.HORIZONTAL)
                                    voltage_text = wx.StaticText(self.G_Opti_Panel, -1, "Acceleartion Voltage : ")
                                    voltage_text.SetFont(ins.Global_Font)
                                    Accel_Voltage_choice = ['60', '100', '200', '300', '1000']
                                    self.voltage_text_ctrl = wx.ComboBox(self.G_Opti_Panel, -1, "100", choices=Accel_Voltage_choice, style=wx.CB_SIMPLE)
                                    #self.voltage_text_ctrl = wx.TextCtrl(self.G_Opti_Panel, -1, " ex. 100 KV ")
                                    #self.voltage_text_ctrl.SetValue("%s"%self.volt_value)
                                    accel_voltage_box.Add(voltage_text, 0, flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER, border=2)
                                    accel_voltage_box.Add(self.voltage_text_ctrl, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND, border=2)

                        #--------- G vector range ---------------------------------------------------------------------------------------------------------------------------------------------------------
                                    g_vector_box = wx.BoxSizer(wx.HORIZONTAL)
                                    G_text = wx.StaticText(self.G_Opti_Panel, -1, "G Vector Range         : ")
                                    G_text.SetFont(ins.Global_Font)
                                    G_text.SetToolTip(wx.ToolTip("This set G range from : -G to G"))
                                    G_Vector_Choice =[str(x) for x in range(0,11)]
                                    self.Gh_text_ctrl = wx.ComboBox(self.G_Opti_Panel, -1, " h ", choices=G_Vector_Choice)
                                    self.Gk_text_ctrl = wx.ComboBox(self.G_Opti_Panel, -1, " k ", choices=G_Vector_Choice)
                                    self.Gl_text_ctrl =  wx.ComboBox(self.G_Opti_Panel, -1, " l ", choices=G_Vector_Choice)

                                    g_vector_box.Add(G_text, 0, flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER, border=2)
                                    g_vector_box.Add(self.Gh_text_ctrl, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND, border=2)
                                    g_vector_box.Add(self.Gk_text_ctrl, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND, border=2)
                                    g_vector_box.Add(self.Gl_text_ctrl, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND, border=2)

                        #------- Thickness of material information -----------------------------------------------------------------------------------------------------------------------
                                    thickness_box = wx.BoxSizer(wx.HORIZONTAL)
                                    self.thickness_text = wx.StaticText(self.G_Opti_Panel, -1, "Material Thickness    :")
                                    self.thickness_text.SetFont(ins.Global_Font)
                                    self.no_thickness = wx.CheckBox(self.G_Opti_Panel, -1, label="Not Known !")
                                    self.material_thickness = wx.TextCtrl(self.G_Opti_Panel, -1, "0.0")

                                    thickness_box.Add(self.thickness_text, 0, flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER, border=2)
                                    thickness_box.Add(self.material_thickness, proportion=1, flag=wx.ALIGN_LEFT | wx.EXPAND|wx.LEFT, border=4)
                                    thickness_box.Add(self.no_thickness, proportion=1, flag=wx.ALIGN_RIGHT | wx.EXPAND |wx.LEFT, border=75)

                        #--------- Exit and Done button -------------------------------------------------------------------------------------------------------------------------------------------

                                    exit_done_box = wx.BoxSizer(wx.HORIZONTAL)
                                    exit_button = wx.Button(self.G_Opti_Panel, -1, " Exit ")
                                    #exit_button.SetBackgroundColour("red")
                                    exit_button.SetForegroundColour("red")
                                    exit_button.Bind(wx.EVT_BUTTON, self.ON_EXIT)

                                    done_button = wx.Button(self.G_Opti_Panel, -1, " Next ")
                                    #done_button.SetBackgroundColour("green")
                                    done_button.SetForegroundColour("green")
                                    done_button.Bind(wx.EVT_BUTTON, self.ON_FIRST_TEMPLATE)

                                    exit_done_box.Add(exit_button, proportion=1, flag= wx.LEFT| wx.RIGHT| wx.TOP| wx.ALIGN_LEFT , border=25)
                                    exit_done_box.Add(done_button, proportion=1, flag= wx.RIGHT|wx.TOP|wx.LEFT| wx.ALIGN_RIGHT, border=25)


                        #------ Add upper box in main box ------------------------------------------------------------------------------

                                    self.Gopti_box.Add(title_box, flag= wx.TOP | wx.EXPAND, border=50)
                                    self.Gopti_box.Add(lattice_box, flag=wx.ALL | wx.EXPAND, border=4)
                                    self.Gopti_box.Add(lattice_parameter_text_box, flag=  wx.ALL | wx.EXPAND, border=8)
                                    self.Gopti_box.Add(lattice_distance_box, flag= wx.ALL |wx.EXPAND|wx.ALIGN_TOP, border=4)
                                    self.Gopti_box.Add(lattice_angle_box, flag=wx.ALL | wx.EXPAND | wx.ALIGN_TOP, border=4)
                                    self.Gopti_box.Add(inequiv_atom_box, flag=wx.ALL | wx.EXPAND, border=4)
                                    self.Gopti_box.Add(accel_voltage_box, flag=wx.ALL | wx.EXPAND, border=4)
                                    self.Gopti_box.Add(g_vector_box, flag=wx.ALL | wx.EXPAND, border=4)
                                    self.Gopti_box.Add(thickness_box, flag=wx.ALL | wx.EXPAND, border=4)
                                    self.Gopti_box.Add(exit_done_box, flag=wx.ALL |wx.EXPAND, border= 4)


                        #-------- Set sizer for the main panel ------------------------------------------------------------------------
                                    self.G_Opti_Panel.SetSizer(self.Gopti_box)

                                    self.First_Template.Show()


            #----- For exiting the First template
            def ON_EXIT(self, event):
                        self.First_Template.Close()
                        event.Skip()



#************************************************************************************************************************************************************************
#----------------------------------------- This create the first template to get the input ------------------------------------------------------------------------------------------------------------
#************************************************************************************************************************************************************************

            def ON_FIRST_TEMPLATE(self, event):

                        #----- We get the input value when we trigger the button, therfore now we first gather the variable
                        #----- Getting values from the dialogs ------------------------------------------------------------------------------------------------
                        #>>>  Need to convert them as the float/string/integer for the input purpose --------------------------------

                        self.Material_Title = str( self.Title_text_ctrl.GetValue() )
                        self.Lattice_type = str( self.lattice_choice_combo_box.GetValue() )
                        self.anm = float(self.lattice_a.GetValue())*1e-9                   #------ Lattice parameter are in nanometer
                        self.bnm = float(self.lattice_b.GetValue())*1e-9                   #----- Lattice parameter are in nanometer
                        self.cnm = float(self.lattice_c.GetValue())*1e-9                        # --- Lattice parameter are in nanometer
                        self.angle_alpha = float(self.alpha_ctrl.GetValue())             #-- angles are in degree
                        self.angle_beta = float(self.beta_ctrl.GetValue())
                        self.angle_gama = float(self.gama_ctrl.GetValue())
                        self.inequiv_atoms = int(self.inequiv_text_ctrl.GetValue())
                        self.h = int(self.Gh_text_ctrl.GetValue())
                        self.k = int(self.Gk_text_ctrl.GetValue())
                        self.l = int(self.Gl_text_ctrl.GetValue())
                        self.accel_voltage = float(self.voltage_text_ctrl.GetValue())  #--- Acceleration voltage are converted in KV
                        self.material_thickness_nm = float(self.material_thickness.GetValue())*1e-9    #---- Askng user to give the thickness in nanometer
                        self.No_thickness = self.no_thickness.GetValue()


            #------------- Create the New Frame Template for the input ---------------------------------------------------------------------------

                        size_x = Main_Frame.Create_Main_Dialog().Window_Size_X
                        size_y = Main_Frame.Create_Main_Dialog().Window_Size_Y

            #------ THIS Template need to be make global to be accessed by the binding function ------------------------------
                        self.Template = wx.Frame(None, title="Input_Template_002", size=(size_x/2, size_y-300))
                        self.Template.Center()
                        #self.Template_Panel = wx.Panel(self.Template, style=wx.SUNKEN_BORDER)
                        self.Template_Panel = wx.ScrolledWindow(self.Template, style=wx.SUNKEN_BORDER)
                        self.Template_Panel.SetScrollbars(1, 100, 1, 100)
                        # Template_Panel.SetBackgroundColour("grey")

                        self.atoms = []
                        #------- Main Box to contains the inputs ctrl -------------------------------------------------------------------------------------
                        Template_box = wx.BoxSizer(wx.VERTICAL)

                        for case in range(self.inequiv_atoms):
                                    Container = wx.BoxSizer(wx.HORIZONTAL)

                                    self.Atom_text = wx.StaticText(self.Template_Panel, -1, "Atom : %s    "%(case +1 ), name="Atom_%s"%(case) )
                                    self.Atom_text.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                    self.Atom_Name = wx.TextCtrl(self.Template_Panel, -1, " ", style=wx.TE_PROCESS_ENTER, name="Atom_Name_%s"%(case))
                                    self.Atom_Name.SetValue("%s"%(self.Atom_Name_List[case]))

                                    self.Atom_Z_text = wx.StaticText(self.Template_Panel, -1, " Z = ")
                                    self.Atom_Z_text.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                    self.Atom_Z = wx.TextCtrl(self.Template_Panel, -1, " 1", style=wx.TE_PROCESS_ENTER, name="Z_Number")
                                    self.Atom_Z.SetValue("%s"%float(self.Atom_Z_LIST[case]))  #----- Can't be integer, I gets some error ---------------

                                    Mult_text = wx.StaticText(self.Template_Panel, -1, "Multiplicity  ")
                                    Mult_text.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                    Mult_Number = wx.TextCtrl(self.Template_Panel, -1, "1", style=wx.TE_PROCESS_ENTER, name="Mult_Number")
                                    Mult_Number.SetValue("%s"%self.Multiplicity_List_From_File[case])


                                    Magnetic_ask = wx.CheckBox(self.Template_Panel, -1, label="Magnetic?", name="Is_Magnetic_Up")
                                    #Magnetic_ask_SpinDn = wx.CheckBox(self.Template_Panel, -1, " Spin Dn", name="Is_Magnetic_Dn")

                                    Container.Add(self.Atom_text, flag= wx.LEFT | wx.TOP | wx.ALIGN_BOTTOM | wx.EXPAND | wx.EXPAND, border =10)
                                    Container.Add(self.Atom_Name, flag=wx.ALL | wx.ALIGN_LEFT | wx.EXPAND, border=4)
                                    Container.Add(self.Atom_Z_text, flag=wx.TOP | wx.LEFT | wx.ALIGN_BOTTOM | wx.EXPAND, border=10)
                                    Container.Add(self.Atom_Z, flag=wx.ALL | wx.ALIGN_LEFT | wx.EXPAND, border=4)
                                    Container.Add(Mult_text, flag=wx.TOP | wx.LEFT| wx.ALIGN_LEFT | wx.ALIGN_CENTER| wx.EXPAND, border=10)
                                    Container.Add(Mult_Number, flag=wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND, border=4)
                                    Container.Add(Magnetic_ask, flag=wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND, border=4)
                                    #Container.Add(Magnetic_ask_SpinDn, flag=wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND, border=4)


                                    Template_box.Add(Container, flag= wx.EXPAND| wx.TOP , border =20)

                        #----------- Putting exit and Go Next button in box sizer -------------------------------------------------------------------
                        Template_Button_box = wx.BoxSizer(wx.HORIZONTAL)

                        #------------- To close the Template -----------------------------------------------------------------------------------------------------
                        Exit_Button = wx.Button(self.Template_Panel, -1, " Exit ")
                        #Exit_Button.SetBackgroundColour("red")
                        Exit_Button.SetForegroundColour("red")
                        Exit_Button.Bind(wx.EVT_BUTTON, self.ON_EXIT_TEMPLATE)

                        #----------- Button to trigger the function for the creating the final coordinate button ----------------------
                        Go_Final_Template = wx.Button(self.Template_Panel, -1, " Make Template ")
                        #Go_Final_Template.SetBackgroundColour("green")
                        Go_Final_Template.SetForegroundColour("green")
                        Go_Final_Template.Bind(wx.EVT_BUTTON, self.ON_GO_FINAL_TEMPLATE)

                        #----------- Add button on the  box sizer --------------------------------------------------------------------------------------------
                        Template_Button_box.Add(Exit_Button, flag = wx.ALL| wx.EXPAND, border = 50)
                        Template_Button_box.Add(Go_Final_Template, flag=wx.ALL | wx.EXPAND, border=50)
                        #------- Adding the box in parent box ------------------------------------------------------------------------------------------------
                        Template_box.Add(Template_Button_box, flag = wx.EXPAND, border = 10)

                        #------ Setting the sizer for the main panel ----------------------------------------------------------------------------------------
                        self.Template_Panel.SetSizer(Template_box)
                        #---- Hidiing the previous frame -------------------------------------------------------------------------------------------------------
                        self.First_Template.Close()
                        # ----- Puting the frame on the loop to keep viewing it ----------------------------------------------------------------------
                        self.Template.Show()
                        #---- As usual skip the event when executed -------------------------------------------------------------------------------------
                        event.Skip()


#**********************************************************************************************************************************************
#----------   This makes the final template --------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            def ON_GO_FINAL_TEMPLATE(self, event):

                        #---- self argument makes them accessible on the next buttron triggering event ------------------------------------------------------------------
                        self.Atoms_Name_List = []                     # String values, Name of the Atoms
                        self.Atoms_Z_List = []                            # Atomic Numbers of the Atoms
                        self.Atom_Multiplicty_List = []               # Multiplicity of individual Atoms
                        self.Magnetic_Atom_List = []                 # Boolean value (True/False ) Obtained from the check box -----------------------------------

                        counter_txtctrl = 0
                        #*****************************************************************************************************************************
                        # Important : How to get the input from the multiple textctrl/checkbox or more general widgets in wxpython -------------
                        #                 : Widget are the children of the parent panel and obtain from : Parent.GetChildren()
                        #                 : Widget type (i.e, wx.TextCtrl, wx.Button ) are the instance of the class wx
                        #*****************************************************************************************************************************
                        #----------- Extracting the children widget from the parent panel; In this case textctrl -------------------------------------------------------------

                        txtCtrls = [widget for widget in self.Template_Panel.GetChildren() if isinstance(widget, wx.TextCtrl)]
                        check_list = [check_widget for check_widget in self.Template_Panel.GetChildren() if isinstance(check_widget, wx.CheckBox) ]

                        #------- Getting the " Atom_Name, Atom_Z, Atom_Multiplicity "-----------------------------------------------------------------------------------------------
                        for i in range(int(self.inequiv_atoms)):
                                    self.Atoms_Name_List.append( str (txtCtrls[counter_txtctrl].GetValue()))
                                    self.Atoms_Z_List.append( float (txtCtrls[counter_txtctrl+1].GetValue()) )
                                    self.Atom_Multiplicty_List.append( int ( txtCtrls[counter_txtctrl+2].GetValue() ) )
                                    self.Magnetic_Atom_List.append( check_list[i].GetValue()  )

                                    counter_txtctrl += 3

           #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #------------- Making a frame for getting the co-ordinate from the multiplicity -----------------------------------------------------------------------------------

                        size_x = Main_Frame.Create_Main_Dialog().Window_Size_X
                        size_y = Main_Frame.Create_Main_Dialog().Window_Size_Y

            # !!!!!------------ Put them scrolled window ---------------------------------------------------------------------------
                        self.Final_Template = wx.Frame(None, title=" Input Template ", size=(size_x/2, size_y-200))
                        #self.Final_Template_Panel = wx.Panel(self.Final_Template, style=wx.SUNKEN_BORDER)
                        self.Final_Template_Panel = wx.ScrolledWindow(self.Final_Template, style=wx.SUNKEN_BORDER)
                        self.Final_Template_Panel.SetBackgroundColour("white")
                        self.Final_Template_Panel.SetScrollbars(1, 100, 2, 100)

                        self.Final_Template.SetPosition((size_x/4, 10))

            #--------- Creating Main BoxSizer -------------------------------------------------------------------------------------------
                        self.Final_Main_box = wx.BoxSizer(wx.VERTICAL)
                        #------- counter to fille the coordinatein in the textctrl --
                        coordinate_counter = 0
                        #------ For every atom putting the atomic cordinate and spin orientation -----------------
                        for ineqiv_atom_index in range(self.inequiv_atoms):

                                    atom_box = wx.BoxSizer(wx.VERTICAL)

                                    atom_counter_box = wx.BoxSizer(wx.HORIZONTAL)
                                    atom_name = wx.StaticText(self.Final_Template_Panel, -1, "%s : %s"%(self.Atoms_Name_List[ineqiv_atom_index], ineqiv_atom_index+1))
                                    atom_name.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                    atom_name.SetForegroundColour("green")
                                    atom_counter_box.Add(atom_name, flag=wx.ALL | wx.EXPAND, border = 5)

                                    atom_box.Add(atom_counter_box, flag = wx.ALL | wx.EXPAND, border = 5)

                                    for mult_index in range( self.Atom_Multiplicty_List[ineqiv_atom_index]):
                                                atom_info_box = wx.BoxSizer(wx.HORIZONTAL)

                                    #-------------- Writing the x cordinate ------------------------------------------------------------------------------------------------------
                                                x_text = wx.StaticText(self.Final_Template_Panel, -1, " x: ")
                                                x_text.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                                x_text.SetForegroundColour("blue")
                                                x_txt_ctrl = wx.TextCtrl(self.Final_Template_Panel, -1, "0.0")
                                                x_txt_ctrl.SetValue("%f"%(float(self.X_Coordinate_List[coordinate_counter])))

                                    # -------------- Writing the y cordinate ------------------------------------------------------------------------------------------------------
                                                y_text = wx.StaticText(self.Final_Template_Panel, -1, " y: ")
                                                y_text.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                                y_text.SetForegroundColour("blue")
                                                y_txt_ctrl = wx.TextCtrl(self.Final_Template_Panel, -1, "0.0")
                                                y_txt_ctrl.SetValue("%f" % (float(self.Y_Coordinate_List[coordinate_counter])))

                                    # -------------- Writing the z cordinate ------------------------------------------------------------------------------------------------------
                                                z_text = wx.StaticText(self.Final_Template_Panel, -1, " z: ")
                                                z_text.SetFont(Main_Frame.Create_Main_Dialog().Global_Font)
                                                z_text.SetForegroundColour("blue")
                                                z_txt_ctrl = wx.TextCtrl(self.Final_Template_Panel, -1, "0.0")
                                                z_txt_ctrl.SetValue("%f" % (float(self.Z_Coordinate_List[coordinate_counter])))

                                    # -------------- Putting the text and the ctrlbox in the box --------------------------------------------------------------------------
                                                atom_info_box.Add(x_text, flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER |wx.EXPAND, border = 10)
                                                atom_info_box.Add(x_txt_ctrl, flag=wx.ALL | wx.EXPAND, border=5)
                                                atom_info_box.Add(y_text, flag=wx.LEFT | wx.TOP |wx.ALIGN_CENTER | wx.EXPAND, border=10)
                                                atom_info_box.Add(y_txt_ctrl, flag=wx.ALL | wx.EXPAND, border=5)
                                                atom_info_box.Add(z_text, flag=wx.LEFT| wx.TOP | wx.ALIGN_CENTER | wx.EXPAND, border=10)
                                                atom_info_box.Add(z_txt_ctrl, flag=wx.ALL | wx.EXPAND, border=5)

                                    #------------- Putting the spin option only for the magnetic atoms ---------------------------------------------------------------
                                                if (self.Magnetic_Atom_List[ineqiv_atom_index]==True):
                                                            self.Magnetic_ask_SpinUp = wx.CheckBox(self.Final_Template_Panel, -1, label=" Spin Up", name="Is_Magnetic_Up")
                                                            self.Magnetic_ask_SpinDn = wx.CheckBox(self.Final_Template_Panel, -1, label=" Spin Dn", name="Is_Magnetic_Dn")
                                                            #print "atom and list", ineqiv_atom_index, self.Magnetic_Atom_List[ineqiv_atom_index]
                                                            atom_info_box.Add(self.Magnetic_ask_SpinUp, flag=wx.ALL | wx.EXPAND, border=8)
                                                            atom_info_box.Add(self.Magnetic_ask_SpinDn, flag=wx.ALL | wx.EXPAND, border=8)

                                                #atom_info_box.Add(self.Magnetic_ask_SpinDn, flag=wx.ALL | wx.EXPAND, border=8)

                                                coordinate_counter += 1
                                                #------- Dynamic box allocation in the box ------------------------------------------------------------------------------------------
                                                atom_box.Add(atom_info_box, flag=wx.ALL | wx.EXPAND, border=10)
                                    #----- Putting the overall container in the main box ----------------------------------------------------------------------------------------
                                    self.Final_Main_box.Add(atom_box, flag=wx.ALL | wx.EXPAND, border=10 )

            #!!---------- Put BUtton for either exiting or going to next  -----------------------------------------------------------------------------------------------------
                        Exit_Go_Button_box = wx.BoxSizer(wx.HORIZONTAL)

                        Exit_Final_Template_Button = wx.Button(self.Final_Template_Panel, -1, "Exit")
                        #Exit_Final_Template_Button.SetBackgroundColour("red")
                        Exit_Final_Template_Button.SetForegroundColour("red")
                        Exit_Final_Template_Button.Bind(wx.EVT_BUTTON, self.ON_EXIT_FINAL_TEMPLATE)

            #--------- Button to trigger the final calculation Function -------------------------------------------------------------------------------------------------------
                        Go_Final_Template_Button = wx.Button(self.Final_Template_Panel, -1, "Go")
                        #Go_Final_Template_Button.SetBackgroundColour("green")
                        Go_Final_Template_Button.SetForegroundColour("green")
                        Go_Final_Template_Button.Bind(wx.EVT_BUTTON, self.ON_DO_CALCULATE_G_OPTIMIZATION)

                        Exit_Go_Button_box.Add(Exit_Final_Template_Button, flag = wx.ALIGN_LEFT | wx.EXPAND | wx.ALL , border =25)
                        Exit_Go_Button_box.Add(Go_Final_Template_Button, flag=wx.ALIGN_LEFT | wx.EXPAND | wx.ALL, border=25)
                        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        self.Final_Main_box.Add(Exit_Go_Button_box, flag=wx.ALL | wx.EXPAND, border =10)

            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #-------- Setting the sizer for the final main box ----------------------------------------------------------------------------------------------------------------------------
                        self.Final_Template_Panel.SetSizer(self.Final_Main_box)
                        #----- Putting the Final_Template ( This have the coordinate in it -----------------------------------------------------------------------------------
                        self.Final_Template.Show()
            #----------- Closing the previous template frame to save memory. But the data is already absorbed -------------------------------------------
                        self.Template.Close()

#------- Binding function to CLose the window -------------------------------------------------------------------------------------------------------------------------------------------
#***********************************************************************************************************************************
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            def ON_EXIT_TEMPLATE(self, event):
                        self.Template.Close()
                        event.Skip()

            def ON_EXIT_FINAL_TEMPLATE(self, event):
                        self.Final_Template.Close()
                        event.Skip()


#*********************************************************************************************************************************************
#---------------------------------------- Final Calculation binding function --------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************

            def ON_DO_CALCULATE_G_OPTIMIZATION(self, event):

            #------ First gathering the prerequisite quantities -----------------------------------

                        #import G_Optimization.Result_Template as G_Result
                        #import G_Optimization.Result_grid_Template as G_Result_on_Grid

            #-------------------- Do TESTING HERE ----------------------------- ------------------------------------------------------------------------------------------------------------------------

            #------------------------ Dialogues creations done here --------------------------------------------------------------------------------------------------------------------------------

                        self.ao = Phys_Const.Constants().Bohr_Radius
                        self.electron_charge = Phys_Const.Constants().Electron_Charge

                        self.Crystal_Volume = VDHKL.Do_Calculate_Crystal_Volume_and_dhkl().Calculate_Crystal_Volume(self.anm, self.bnm, self.cnm, self.angle_alpha, self.angle_beta, self.angle_gama)
                        self.Relativistic_Wave_Length = TEM.Calculate_TEM_Properties().Calculate_Relativistic_WaveLength(self.accel_voltage)
                        #self.Vg_Prefactor = ( (2*np.pi*self.electron_charge*self.ao)/(self.Crystal_Volume))

            #******** Here according to kirkland book the electron unit (1.6e19) is converted to volt-angstrom:- 14.4 volt-angstrom
                        self.Vg_Prefactor = ((47.86*1e-20) / (self.Crystal_Volume))
            #************************************************************************************************************************************

                        #---- Grabbing all text_ctrl for getting the input from the user ---------------------------------------------------------------------------------------------
                        self.coordinate_txtctrl = [widget for widget in self.Final_Template_Panel.GetChildren() if isinstance(widget, wx.TextCtrl)]

                        #----------- To obtain the Max Partial Structure Factor (PSF) and corrosponding (hkl) and extinction distance ---------------------
                        Max_PSF = 0
                        self.MAX_PSF_Relation = np.zeros((1,5))  #--- Index (h,k,l,Max_PSF, Extinction_distance )

            #************ Getting spin alignment of every atoms -------------------------------------------------------------------------------------------------------------------------

                        Spin_check_list = [check_widget.GetValue() for check_widget in self.Final_Template_Panel.GetChildren() if isinstance(check_widget, wx.CheckBox)]
                        Spin_Alignment_List = []

                        for check_index in range(0, int(len(Spin_check_list)), 2):
                                    up_spin = Spin_check_list[check_index]
                                    if (up_spin == True):
                                                Spin_Alignment_List.append(1)
                                    #---- Putting spin dn as -1 in the Partial structure factor --------------------------------------------------------------------------------------------
                                    dn_spin = Spin_check_list[check_index + 1]
                                    if (dn_spin == True):
                                                Spin_Alignment_List.append(-1)

            #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #---------------- Calculating the Vg, Excitation coefficient, Partial Structure Factor starts from here -------------------------------------------------------

                        self.h_list = []
                        self.k_list = []
                        self.l_list = []
                        self.Vg_list = []
                        self.phase_list = []
                        self.PSF_list = []
                        self.Extinction_distance_list = []
                        self.EMCD_Optimized_Paramter_list = []

                        self.ch = (0 + 0j)
            #---------- Starting to calculate the various parameter for every G(hkl) vector ---------------------------------------------------------------------------------------

                        for h_index in range( self.h, -(self.h+1), -1):
                                    for k_index in range( self.k, -(self.k +1), -1):
                                                for l_index in range(self.l,  -(self.l +1), -1):
                                                            if (h_index == 0 and k_index ==0 and l_index ==0 ):
                                                                        continue
                                                            else:
                                                                        self.g_magnitude =  VDHKL.Do_Calculate_Crystal_Volume_and_dhkl().Calculate_Dhkl(self.Lattice_type, h_index, k_index, l_index, self.anm, self.bnm, self.cnm, self.angle_alpha, self.angle_gama, self.angle_gama)
                                                                        #print h_index, k_index, l_index, self.g_magnitude

                                                            #----------- Setting the counter and Variable. Variabl are being Rest for next (hkl) values -----------------------
                                                            counter_coordinate = 0
                                                            self.FSCATT =0
                                                            self.VG = 0
                                                            self.PSF = (0 + 0j)   #--- Partial structure factor : Only for the magnetic atoms ---------------------------------------------
                                                            self.Magnetic_Atoms_Basis_List = []

                                                            for atom_index in range(int(self.inequiv_atoms)):

                                                                        Z_Number = int(self.Atoms_Z_List[atom_index])
                                                                        self.Lobato_Inst =Lobato.Lobato_parameter()
                                                                        self.Lobato_Inst.Get_Parameters(Z_Number)
                                                                        self.Lobato_Ai = self.Lobato_Inst.ai
                                                                        self.Lobato_Bi = self.Lobato_Inst.bi

                                                                        #------------- Find the total Electron scattering factor for particular atoms --------------------------------------
                                                                        #------------- Since there are 5 differnt ai,bi numbers in the Lobato list -------------------------------------------
                                                                        self.Lobato_Scattering_Factor = 0
                                                                        for lobato_index in range(5):
                                                                                    ai = self.Lobato_Ai[lobato_index] * (1e-10)   #-- Since the unit of ai = 1e-10
                                                                                    bi = self.Lobato_Bi[lobato_index] * (1e-20)   #- Since the unit of  bi = 1e-20
                                                                                    lobato_nume =  ( ai * (2 + (bi*(self.g_magnitude**2)) ))
                                                                                    lobato_deno =   ((1 + (bi*(self.g_magnitude**2)))**2)
                                                                                    lobato_scattering_factor = (lobato_nume/lobato_deno)
                                                                                    self.Lobato_Scattering_Factor = self.Lobato_Scattering_Factor + lobato_scattering_factor


                                                                        #----- Getting all the co-ordinates of all the atoms ---------------------------------------------------------------------------
                                                                        for mult_index in range(int(self.Atom_Multiplicty_List[atom_index])):
                                                                                    x_coordinate = float(self.coordinate_txtctrl[counter_coordinate].GetValue())
                                                                                    y_coordinate = float(self.coordinate_txtctrl[counter_coordinate + 1].GetValue())
                                                                                    z_coordinate = float(self.coordinate_txtctrl[counter_coordinate + 2].GetValue())

                                                                                    #print x_coordinate, y_coordinate, z_coordinate
                                                                                    GU = (h_index*x_coordinate + k_index*y_coordinate + l_index*z_coordinate)
                                                                                    exp_factor = np.exp( (0 +1j)*(2*np.pi*GU))
                                                                                    self.FSCATT = self.FSCATT + (self.Lobato_Scattering_Factor * exp_factor)
                                                                                    counter_coordinate += 3

                                                                                    #------- Extracting only coordinates of the magnetic atoms -----------------------------------------------
                                                                                    if (bool(self.Magnetic_Atom_List[atom_index])==True):
                                                                                                self.Magnetic_Atoms_Basis_List.append(x_coordinate)
                                                                                                self.Magnetic_Atoms_Basis_List.append(y_coordinate)
                                                                                                self.Magnetic_Atoms_Basis_List.append(z_coordinate)

                                                            #------ Fourier component of crystal potential ------------------------------------------------------------------------------------------
                                                            self.VG = self.FSCATT * self.Vg_Prefactor
                                                            self.VG_Real_Part = self.VG.real
                                                            self.VG_Imaginary_Part = self.VG.imag
                                                            self.VG_Phase = math.atan(self.VG_Imaginary_Part/self.VG_Real_Part)
                                                            #print h_index, k_index, l_index, self.VG, self.Vg_Prefactor

                                                #****************************** <<  Magnetic Partial Structure Factor >> **********************************
                                                #------------- Finding the partial structure factor for the magnetic atoms ---------------------------------------------------------------
                                                            counter_basis_position = 0     #-- Counter for the magnetic atom coordinate ----------------------------------------
                                                            spin_counter = 0                    #-- Counter for the spin up/dn -------------------------------------------------------------------
                                                            for magnetic_atom_index in range(int(len(self.Magnetic_Atoms_Basis_List)/3 )):   #--- Since xyz(3)
                                                                        magnetic_cord_x = self.Magnetic_Atoms_Basis_List[counter_basis_position]
                                                                        magnetic_cord_y = self.Magnetic_Atoms_Basis_List[counter_basis_position +1]
                                                                        magnetic_cord_z = self.Magnetic_Atoms_Basis_List[counter_basis_position + 2]

                                                                        mag_GU = ( (h_index*magnetic_cord_x) +  (k_index*magnetic_cord_y) + (l_index*magnetic_cord_z) )

                                                                        #------------------------ Multiplying -1 for the antiferromagnetic alignment ----------------------------------------------------------------------------
                                                                        #self.PSF = self.PSF + ( (np.exp( (0+1j) * ( (2 * np.pi * mag_GU) + self.VG_Phase))) * Spin_Alignment_List[spin_counter])

                                                                        self.PSF = self.PSF +( ((np.exp((0 - 1j) * ((2 * np.pi * mag_GU) + self.VG_Phase))) ) * Spin_Alignment_List[spin_counter])
                                                                        #----- Just for the debugging purpose to check whether -1 being included or not, its working -----------------------------------------
                                                                        #print Spin_Alignment_List[spin_counter],   ((np.exp((0 - 1j) * ((2 * np.pi * mag_GU) + self.VG_Phase))) ) , ((np.exp((0 - 1j) * ((2 * np.pi * mag_GU) + self.VG_Phase))) ) * Spin_Alignment_List[spin_counter]
                                                                        #------------------------- Just for the debugging purpose ----------------------------------------------------------------------------------------------------------
                                                                        #if ( (h_index == 4)  and (k_index == 4) and (l_index == 4)  ):
                                                                        #print self.PSF,  ( ((np.exp((0 - 1j) * ((2 * np.pi * mag_GU) + self.VG_Phase))) )), ( ((np.exp((0 - 1j) * ((2 * np.pi * mag_GU) + self.VG_Phase))) ) * Spin_Alignment_List[spin_counter])
                                                                        #print ( ((np.exp((0 - 1j) * ((2 * np.pi * mag_GU) + self.VG_Phase))) ))

                                                                        spin_counter += 1
                                                                        counter_basis_position += 3


                                                            self.PSF_Real = self.PSF.real
                                                            self.PSF_Imaginary = self.PSF.imag

                                                            #*****************************************************************************************************************
                                                            #---------------- Calculating the Extinction distance for particular G(hkl) vector -------------------------------------------------------------
                                                            Bragg_angle = (np.arcsin(((self.Relativistic_Wave_Length * self.g_magnitude) / 2)))
                                                            Ext_nume = (np.pi * self.Crystal_Volume * np.cos(Bragg_angle/2))
                                                            Ext_denu = (self.Relativistic_Wave_Length * np.abs(self.FSCATT))
                                                            self.Extinction_distance = (Ext_nume / Ext_denu)

                                                            # Calculating the Optimized paramter as given in the paper [ Thickness_Function * Magnetic_Structure_Factor] ---
                                                            #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                            self.emcd_optimized_parameter =( (self.Extinction_distance / (np.pi * self.cnm))  *  ((np.sin(((np.pi * self.material_thickness_nm)/(self.Extinction_distance))))**2)  \
                                                                        * (abs(self.PSF_Real)) )

                                                            #print h_index, k_index, l_index,  self.material_thickness_nm, ((self.Extinction_distance / (np.pi * self.cnm))),  ((np.sin(((np.pi * self.material_thickness_nm)/(self.Extinction_distance))))**2)
                                                            #----- This is used later to extract some quantities -----------------------------------------------------------------------------------

                                                            self.h_list.append(h_index)
                                                            self.k_list.append(k_index)
                                                            self.l_list.append(l_index)
                                                            self.Vg_list.append(np.abs(self.VG))
                                                            self.PSF_list.append(abs(self.PSF_Real))
                                                            self.phase_list.append(self.VG_Phase)
                                                            self.Extinction_distance_list.append(self.Extinction_distance/1e-9)  #---- Extinction distance in nano-meter
                                                            self.EMCD_Optimized_Paramter_list.append( self.emcd_optimized_parameter )

                                                            #ap.AppendText("\t %s \t %s \t %s \t  %s \t %s, \t  %s, \t  %s \n" % (h_index, k_index, l_index, self.VG, self.VG_Phase, self.PSF, self.Extinction_distance/1e-9))

                        #-------- Printing the Final obtained Highest PSF and corrosponding (hkl) and the Extinction distance ----------------------------------
            # ------------------- Finding the Max PSF and corrosponding (hkl) and Extinction distance ----------------------------------------------------------------------
                                                            if ((h_index ==0 ) and (k_index ==0 ) and (l_index ==0 ) ):
                                                                        continue

                                                            elif ( np.abs(self.PSF_Real) > Max_PSF   ):
                                                                        Max_PSF = np.abs(self.PSF_Real)
                                                                        self.MAX_PSF_Relation[0, 0] = h_index
                                                                        self.MAX_PSF_Relation[0, 1] = k_index
                                                                        self.MAX_PSF_Relation[0, 2] = l_index
                                                                        self.MAX_PSF_Relation[0, 3] = Max_PSF
                                                                        self.MAX_PSF_Relation[0, 4] = self.Extinction_distance

                        #---------- Find the max values ------------------------------------------------------------------------------------------------------------------------------------------------
                        h_max = int(self.MAX_PSF_Relation[:,0])
                        k_max = int(self.MAX_PSF_Relation[:,1])
                        l_max = int(self.MAX_PSF_Relation[:,2])
                        max_psf = float(self.MAX_PSF_Relation[:,3])
                        max_ext = float(self.MAX_PSF_Relation[:, 4])/1e-9

                        #------ Safe option to hide the previous frame, as it can be used by next step ----------------------------------------------------------------------

                        self.Final_Template.Hide()

            #---------- Printing the maximum values as the information dialog -----------------------------------------------------------------------------------------------------

                        dlg_optimization_info = wx.MessageDialog(Main_Frame.Create_Main_Dialog().Main_Panel, " Optimum G(hkl) : (%s, %s, %s)  \n Max SF : %.2f \n Extinction Distance : %.2f nm" % (h_max, k_max, l_max, max_psf, max_ext), "Optimization based on PSF", wx.OK )
                        if (dlg_optimization_info.ShowModal()==wx.ID_OK):
                                    dlg_optimization_info.Destroy()

                                    #------------- Creates the grid for the  for the case when you don't know the thickness of your material -----------------------------------------------------
                                    #************************************************************************************************************************************
                                    #-------------------------------- Creating Grid frame to show the data with every G value --------------------------------------------------------------------------------------
                                    #*************************************************************************************************************************************

                                    self.Grid_Frame = wx.Frame(None, title="Result grid")
                                    self.Grid_Frame.Maximize()
                                    self.Grid_Panel = wx.Panel(self.Grid_Frame, style=wx.SUNKEN_BORDER)

                                    #----- Size equal to the size of the display window -------------------------------------------------------------------------------------------------------------------------
                                    sizex = Main_Frame.Create_Main_Dialog().Window_Size_X
                                    sizey = Main_Frame.Create_Main_Dialog().Window_Size_Y

                                    #---- Creating the wx.grid --------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    self.Data_grid = gridlib.Grid(self.Grid_Panel)

                                    #--- Nrow, and column will be feteched from the input file
                                    self.grid_n_row = len(self.h_list)
                                    self.grid_n_col = 8

                                    self.Data_grid.CreateGrid(self.grid_n_row, self.grid_n_col)
                                    wx.TipWindow(self.Data_grid, " Left click on the column label to sort \n Optimum thickness = Extinction distance / 2   \n Plot the result on desired paramter!", maxLength=1500)

                                    box = wx.BoxSizer(wx.VERTICAL)
                                    box.Add(self.Data_grid, proportion=1, flag=wx.EXPAND)
                                    self.Grid_Panel.SetSizer(box)

                        #----------Naming the column Label ------------------------------------------------------------------------------------------------------------------------------------

                                    self.Data_grid.SetColLabelValue(0, " h ")
                                    self.Data_grid.SetColLabelValue(1, " k ")
                                    self.Data_grid.SetColLabelValue(2, " l ")
                                    self.Data_grid.SetColLabelValue(3, " Vg (Volt)")
                                    self.Data_grid.SetColLabelValue(4, " Phase ")
                                    self.Data_grid.SetColLabelValue(5, " SF ")
                                    self.Data_grid.SetColLabelValue(6, " Extinction Distance (nm)")
                                    self.Data_grid.SetColLabelValue(7, " Optimized Paramerter ")

                        #---------- Filling the data in the grid ------------------------------------------------------------------------------------------------------------------------------------

                                    for i in range(self.grid_n_row):
                                                self.Data_grid.SetCellValue(i, 0, "%.5f" % (self.h_list[i]))
                                                self.Data_grid.SetCellValue(i, 1, "%.5f" % (self.k_list[i]))
                                                self.Data_grid.SetCellValue(i, 2, "%.5f" % (self.l_list[i]))
                                                self.Data_grid.SetCellValue(i, 3, "%.5f" % (self.Vg_list[i]))
                                                self.Data_grid.SetCellValue(i, 4, "%.5f" % (self.phase_list[i]))
                                                self.Data_grid.SetCellValue(i, 5, "%.5f" % (self.PSF_list[i]))
                                                self.Data_grid.SetCellValue(i, 6, "%.5f" % (self.Extinction_distance_list[i]))
                                                self.Data_grid.SetCellValue(i, 7, "%.5f" % (self.EMCD_Optimized_Paramter_list[i]))

                                    #------- Auto resize the cell width according the value ----------------------------------------------------------------------------------------------------------------------------------

                                    self.Data_grid.AutoSize()

                        #----------------- Binding the column label with single mouse click ----------------------------------------------------------------------------------------------------------------------
                                    self.Data_grid.Bind(gridlib.EVT_GRID_LABEL_LEFT_CLICK, self.ON_LABEL_LEFT_SClick)
                        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        #------ STATUSBAR on the wx.grid panel ----------------------------------------------------------------------------------------------------------------------------------------------------------
                        #------- Creating the statusbar with Save and Exit button ---------------------------------------------------------------------------------------------------------------------------------
                                    self.grid_status_bar = self.Grid_Frame.CreateStatusBar(style=wx.SUNKEN_BORDER)
                                    self.grid_status_bar.SetBackgroundColour("orange")
                                    self.grid_status_bar.SetMinHeight(40)

                        #------ Exit button on the status bar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    self.grid_Exit_Button = wx.Button(self.grid_status_bar, -1, "Exit", pos=(sizex-87,1), size=(78,35))
                                    #self.grid_Exit_Button.SetBackgroundColour("white")
                                    self.grid_Exit_Button.SetForegroundColour("red")
                                    self.grid_Exit_Button.Bind(wx.EVT_BUTTON, self.ON_EXIT_GRID)

                         #------- Button to save the data ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    self.grid_Save_Button=wx.Button(self.grid_status_bar, -1, "Save", pos=(1,1), size=(80,35))
                                    self.grid_Save_Button.SetBackgroundColour("white")
                                    self.grid_Save_Button.SetForegroundColour("green")
                                    self.grid_Save_Button.Bind(wx.EVT_BUTTON, self.ON_SAVE_GRID_DATA)

                        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    if (self.No_thickness == True):
                                                self.Plot_Optimize_Function = wx.Button(self.grid_status_bar, -1, "Plot Optimization",  pos=(100, 1), size=(170, 35))
                                                #self.Plot_Optimize_Function.SetBackgroundColour("yellow")
                                                self.Plot_Optimize_Function.SetForegroundColour("green")
                                                self.Plot_Optimize_Function.Bind(wx.EVT_BUTTON, self.ON_PLOT_GRID_DATA)

                                                self.Save_optimize_plot_button = wx.Button(self.grid_status_bar, -1, "Save Plot", pos=(290, 1), size=(90,35))
                                                #self.Save_optimize_plot_button.SetBackgroundColour("white")
                                                self.Save_optimize_plot_button.SetForegroundColour("green")
                                                self.Save_optimize_plot_button.Bind(wx.EVT_BUTTON, self.ON_SAVE_OPTIMIZE_PLOT)
                                    else:
                                                pass
                        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                    if (self.No_thickness == True):
                                                self.Data_grid.DeleteCols(7)
                                    self.Grid_Frame.Show()

                        event.Skip()


#************************************************ BINDING FUNCTINO FOR THE GRID RELATED EVENT **************************************************************************************
#*************************************************************************************************************************************************************************************************
            #---------------------- Binding function of the grid event ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            def ON_LABEL_LEFT_SClick(self, event):

                        selected_col = event.GetCol()
                        selected_row = event.GetRow()
                        #------- Collecting the element from the selected column -----------------------------------------------------------------------------------------------------------------------------------------------
                        grab_list = []
                        for i in range(int(self.grid_n_row)):
                                    grab_list.append(float(self.Data_grid.GetCellValue(i, selected_col)))

                        if (sorted(grab_list) == grab_list):
                                    wx.TipWindow(self.Data_grid, "Same list dude", maxLength=400)

                        if (sorted(grab_list) != grab_list):
                                    sorted_argument = np.argsort(grab_list)
                                    h_data = [self.h_list[i] for i in sorted_argument]
                                    k_data = [self.k_list[i] for i in sorted_argument]
                                    l_data =  [self.l_list[i] for i in sorted_argument]
                                    Vg_data =[self.Vg_list[i] for i in sorted_argument]
                                    phase_data = [self.phase_list[i] for i in sorted_argument]
                                    psf_data = [self.PSF_list[i] for i in sorted_argument]
                                    ext_dist_data = [self.Extinction_distance_list[i] for i in sorted_argument]
                                    if (self.No_thickness == True):
                                                pass
                                    else:
                                                optimized_parameter_data = [ self.EMCD_Optimized_Paramter_list[i] for i in sorted_argument  ]

                                    self.h_list = h_data
                                    self.k_list = k_data
                                    self.l_list = l_data
                                    self.Vg_list = Vg_data
                                    self.phase_list = phase_data
                                    self.PSF_list = psf_data
                                    self.Extinction_distance_list = ext_dist_data
                                    if (self.No_thickness == True):
                                                pass
                                    else:
                                                self.EMCD_Optimized_Paramter_list = optimized_parameter_data

                                    self.Data_grid.ClearGrid()

                                    for i in range(int(self.grid_n_row)):
                                                self.Data_grid.SetCellValue(i, 0, "%.5f" % (self.h_list[i]))
                                                self.Data_grid.SetCellValue(i, 1, "%.5f" % (self.k_list[i]))
                                                self.Data_grid.SetCellValue(i, 2, "%.5f" % (self.l_list[i]))
                                                self.Data_grid.SetCellValue(i, 3, "%.5f" % (self.Vg_list[i]))
                                                self.Data_grid.SetCellValue(i, 4, "%.5f" % (self.phase_list[i]))
                                                self.Data_grid.SetCellValue(i, 5, "%.5f" % (self.PSF_list[i]))
                                                self.Data_grid.SetCellValue(i, 6, "%.5f" % (self.Extinction_distance_list[i]))

                                                if (self.No_thickness == True):
                                                            pass
                                                else:
                                                            self.Data_grid.SetCellValue(i, 7, "%.5f" % (self.EMCD_Optimized_Paramter_list[i]))
                                    #-------- Below is reduntant, as already is set   --------------------------------------------------------------------
                                    #self.Data_grid.AutoSize()
                        #-------- Skip the event ---------------------------------------------------------------------------------------------------------------------
                        event.Skip()

            #--------- Exit the grid function ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            def ON_EXIT_GRID(self, event):
                        #---------- Closing the frame not the class; a safter option ---------------------------------------------------------------
                        self.Grid_Frame.Close()
                        event.Skip()

            #----------- Save the data from the grid to the text file ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            def ON_SAVE_GRID_DATA(self, event):

                        # -------------------- Creting the Dialogs to save the data ------------------------------------------------------------------------------------------------------------------------------------------------------
                        file_name_dlg = wx.TextEntryDialog(self.Grid_Panel, "File name to save the data ", "File Name", style=wx.OK | wx.CANCEL)
                        file_name_dlg.SetValue("File.txt")
                        if file_name_dlg.ShowModal() == wx.ID_OK:
                                    self.Data_File_Name = file_name_dlg.GetValue()
                                    file_name_dlg.Destroy()

                                    # ----- Getting Directory name to save the above text file ---------------------------------------------------------------------------------------------------------------------------------------------------
                                    dir_dlg = wx.DirDialog(self.Grid_Panel, "Choose directory", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
                                    if dir_dlg.ShowModal() == wx.ID_OK:
                                                self.Data_File_Directory = dir_dlg.GetPath()
                                    dir_dlg.Destroy()

            #----------------- This section writes the sorted data in the text file ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        #----------- Get the file name where to write the data -----------------------------------------------------------------
                        self.Save_Grid_Data_File = os.path.join(self.Data_File_Directory, self.Data_File_Name)

                        #----- Case: When you don't know the material thickness --------------------------------------------------------
                        if (self.No_thickness == True):
                                    All_data = np.column_stack((self.h_list, self.k_list, self.l_list, self.Vg_list, self.phase_list, self.PSF_list, self.Extinction_distance_list))
                                    Header = "h \t k \t l\t  Vg(volt) \t  phase \t   PSF \t   Extinction Distance(nm) \n" \
                                             "--------------------------------------------------------------------------------------------------------"
                                    # --------- Save the data ---------------------------------------------------------------------------------------------------
                                    np.savetxt(self.Save_Grid_Data_File, All_data, header=Header, fmt="%i\t %i \t %i\t %.5f \t %.5f\t %.5f \t %.5f")
                        #----- Case: When you know your material thickness ...............................................................
                        if(self.No_thickness == False):
                                    All_data = np.column_stack((self.h_list, self.k_list, self.l_list, self.Vg_list, self.phase_list, self.PSF_list, self.Extinction_distance_list, self.EMCD_Optimized_Paramter_list))
                                    Header ="h \t k \t l\t  Vg(volt) \t  phase \t   PSF \t   Extinction Distance(nm) \tThickness Function * PSF \n" \
                                            "------------------------------------------------------------------------------------------------------------------------------------------------------"
                                    #--------- Save the data ---------------------------------------------------------------------------------------------------
                                    np.savetxt(self.Save_Grid_Data_File, All_data, header=Header, fmt="%i\t %i \t %i\t %.5f \t %.5f\t %.5f \t %.5f  \t\t%.5f")

                        #-------- At last always skip the events -----------------------------------------------------------------------------
                        event.Skip()


            #------------------ PLOT THE OPTIMIZATION DATA ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            def ON_PLOT_GRID_DATA(self, event):

                        #------------ Make other name list as it can conflict with previous list --------------------------------------------------------------------------------------
                        self.Extinction_distance_round_list = [ np.abs(np.round(x, 2)) for x in self.Extinction_distance_list ]
                        unique_extinction_list = [ ]
                        repeated_extinction_distance_list = [ ]
                        for i in range(len(self.h_list)):
                                    repeating_count = self.Extinction_distance_round_list.count(self.Extinction_distance_round_list[i])
                                    if self.Extinction_distance_round_list[i] not in unique_extinction_list:
                                                unique_extinction_list.append(self.Extinction_distance_round_list[i])
                                                repeated_extinction_distance_list.append(repeating_count)

                        #--------------- Putting the optimized list after removing the repetative elements -----------------------------------------------------------------------
                        Optimized_h_list = [ ]
                        Optimized_k_list = [ ]
                        Optimized_l_list =  [ ]
                        Optimized_PSF_list = [ ]
                        Optimized_Extinction_list = [ ]

                        for i in range(len(repeated_extinction_distance_list)):
                                    index_list = int(sum(repeated_extinction_distance_list[0:i]))
                                    Optimized_h_list.append(self.h_list[index_list])
                                    Optimized_k_list.append(self.k_list[index_list])
                                    Optimized_l_list.append(self.l_list[index_list])
                                    Optimized_PSF_list.append(self.PSF_list[index_list] )
                                    Optimized_Extinction_list.append( self.Extinction_distance_list[index_list] )

                        #-------- Printing will start from here -----------------------------------------------------------------------------------------------------------------------------------------
                        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        fig, ax = plt.subplots(1, 1 )
                        #fig.set_size_inches(3.3, 2.8)
                        thickness_range_dlg = wx.TextEntryDialog(self.Grid_Panel, "Give thickness range to plot in nm", "Thickness range", style=wx.OK |wx.CANCEL )
                        if (thickness_range_dlg.ShowModal()== wx.ID_OK):
                                    thickness_range = range( int(thickness_range_dlg.GetValue()) )
                                    #specimen_thickness = (int(thickness_range_dlg.GetValue()) )
                                    hkl_range_dlg = wx.TextEntryDialog(self.Grid_Panel, "Give number of point to plot", " G points ", style=wx.OK | wx.CANCEL)
                                    if (hkl_range_dlg.ShowModal()== wx.ID_OK):
                                                hkl_points = int(hkl_range_dlg.GetValue())
                                                for j in range(hkl_points):
                                                            optimized_function = [  ( ((Optimized_Extinction_list[j]*1e-9)/ (np.pi*self.cnm)) *  ((np.sin(((np.pi*x*1e-9)/(Optimized_Extinction_list[j]*1e-9))))**2)  * np.abs(Optimized_PSF_list[j]) ) for x in thickness_range ]
                                                            #optimized_function = [  ((((Optimized_Extinction_list[j] * 1e-9) / (np.pi * self.cnm)) * ((np.sin(((np.pi * x * 1e-9) / (Optimized_Extinction_list[j] * 1e-9)))) ** 2) * np.abs(Optimized_PSF_list[j]))/(x*1e-9))    for x in thickness_range]
                                                            plt.plot(thickness_range, optimized_function, "-o", markersize=5,  label= "G(hkl) : %s %s %s "%(Optimized_h_list[j], Optimized_k_list[j],Optimized_l_list[j]) +  r" $ \mid \, \xi_{G}=\,$"+"%.1f "%(Optimized_Extinction_list[j]) + r"$\mid \,$" + "SF=  %.1f "%(Optimized_PSF_list[j]) )

                                                #plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=int(hkl_points/2), fancybox=True, shadow=False)
                                                plt.legend(loc="best",  prop={'size':8}, frameon=False, fancybox=None) #ncol=int(hkl_points/2),
                                                plt.xlabel(r" $\mathrm{Thickness \,(nm) }$", fontsize=18)
                                                plt.ylabel(r" $\mathrm{Thickness \, function \, \times \, Structure\, factor} $", fontsize=18)
                                                plt.tick_params(axis="both", labelsize=18)
                                                plt.tight_layout()
                                                plt.show()

                        thickness_range_dlg.Destroy()
                        hkl_range_dlg.Destroy()

                        #----------------- SKIP the event always --------------------------------------------------------------------------------------------------------------------------------------
                        event.Skip()

            #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #--------------- Save the optimization plots --------------------------------------------------------------------------------------------------------------------------------------------
            def ON_SAVE_OPTIMIZE_PLOT(self, event):

                        save_plot_name = wx.TextEntryDialog(self.Grid_Panel, "File name to save the Plot ", "Plot to save", style=wx.OK | wx.CANCEL)
                        save_plot_name.SetValue("Save_Optimization_Plot")
                        if save_plot_name.ShowModal() == wx.ID_OK:
                                    # ----- Getting Directory name to save the above text file ---------------------------------------------------------------------------------------------------------------------------------------------------
                                    dir_dlg = wx.DirDialog(self.Grid_Panel, "Choose directory to save plot", style=wx.DD_DEFAULT_STYLE)
                                    if dir_dlg.ShowModal() == wx.ID_OK:
                                                self.Plot_Save_Directory = dir_dlg.GetPath()
                                    dir_dlg.Destroy()

                                    plt.subplots_adjust(left=0.15, right=0.90, bottom=0.15, top=0.90)
                                    plt.savefig("%s/%s.pdf"%( self.Plot_Save_Directory, save_plot_name.GetValue()), dpi=300)

                        save_plot_name.Destroy()

                        event.Skip()

#--------------------------------------------------------------------------------------------- END -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------