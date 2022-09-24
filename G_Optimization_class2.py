#    This is a module class which calculate the optimized G (hkl) to maximize the EMCD signal -------------------------------------------------------------
#    This module is called by the main menu option to do the G optimizatio calculation -------------------------------------------------------------------------
#  ****************************************************************************************************************************************
from __future__ import division
import numpy as np
import EMCD_GUI_beta as Main_Frame
import math, os
import Make_Main_Menu as Make_Menu
import Load_structure_info as Load_Structure
import matplotlib.pyplot as plt
from matplotlib import rc
import Tem_properties as TEM
import  volume_dhkl_class as VDHKL
import Lobato_parameter as Lobato
import Physics_Constant as Phys_Const

rc('text', usetex=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------
class Do_G_Optimization2():
    
        def __init__(self):
                #wx.Frame.__init__(self, None, title= "G Optimization")
                       
                #---------------- Load the structure file ---------------------------------------------------------------------------------------------------
                self.Author_Name = "DEVENDRA SINGH NEGI"
                       
                # self.Structure_File_Name =  os.path.basename(self.Structure_File_Path)
                # self.Structure_File_Extension = (self.Structure_File_Name).split(".")[1]

                #---------------- Getting the information from the input file --------------------------------------------------------------------------------
                self.Struct_Information =  Load_Structure.Extract_Structure_Info().Extract_Info(self.Structure_File_Path)

                self.Material_Name_From_File = self.Struct_Information[0]
                self.Lattice_Type_From_File = self.Struct_Information[1]
                self.Inequivalent_Atom_From_File = int(self.Struct_Information[2])
                self.Lattice_Parameter_Angle_List = self.Struct_Information[3]
                self.Multiplicity_List_From_File = self.Struct_Information[4]
                self.Atom_Name_List = self.Struct_Information[5]
                self.Atom_Z_LIST = self.Struct_Information[6]
                self.X_Coordinate_List = self.Struct_Information[7]
                self.Y_Coordinate_List = self.Struct_Information[8]
                self.Z_Coordinate_List = self.Struct_Information[9]
                                    

#*********************************************************************************************************************************************
#---------------------------------------- Final Calculation binding function -----------------------------------------------------------------
#*********************************************************************************************************************************************

        def ON_DO_CALCULATE_G_OPTIMIZATION(self, event):

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



class_Do_G_Optimization2 = Do_G_Optimization2()

