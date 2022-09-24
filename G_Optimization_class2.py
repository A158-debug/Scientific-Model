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
                self.Struct_Information =  Load_Structure.Extract_Structure_Info().Extract_Info('FeGe.struct')

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
                self.anm = *1e-9                   #------ Lattice parameter are in nanometer
                self.bnm = float( self.Y_Coordinate_List)*1e-9                   #----- Lattice parameter are in nanometer
                self.cnm = float(self.lattice_c.GetValue())*1e-9                    # --- Lattice parameter are in nanometer

#*********************************************************************************************************************************************
#---------------------------------------- Final Calculation binding function -----------------------------------------------------------------
#*********************************************************************************************************************************************

        def ON_DO_CALCULATE_G_OPTIMIZATION(self):

                self.ao = Phys_Const.Constants().Bohr_Radius
                self.electron_charge = Phys_Const.Constants().Electron_Charge
                
                self.Crystal_Volume = VDHKL.Do_Calculate_Crystal_Volume_and_dhkl().Calculate_Crystal_Volume(self.anm, self.bnm, self.cnm, self.angle_alpha, self.angle_beta, self.angle_gama)
                self.Relativistic_Wave_Length = TEM.Calculate_TEM_Properties().Calculate_Relativistic_WaveLength(self.accel_voltage)
                #self.Vg_Prefactor = ( (2*np.pi*self.electron_charge*self.ao)/(self.Crystal_Volume))

            #******** Here according to kirkland book the electron unit (1.6e19) is converted to volt-angstrom:- 14.4 volt-angstrom
                self.Vg_Prefactor = ((47.86*1e-20) / (self.Crystal_Volume))
            #************************************************************************************************************************************

            #---- Grabbing all text_ctrl for getting the input from the user ---------------------------------------------------------------------------------------------
                # self.coordinate_txtctrl = [widget for widget in self.Final_Template_Panel.GetChildren() if isinstance(widget, wx.TextCtrl)]

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

            #-------------------------------------------------------------------------------------------------------------------------------------------------------------
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
                                                        counter_basis_position = 0          #-- Counter for the magnetic atom coordinate ----------------------------------------
                                                        spin_counter = 0                    #-- Counter for the spin up/dn -------------------------------------------------------------------
                                                        for magnetic_atom_index in range(int(len(self.Magnetic_Atoms_Basis_List)/3 )):   #--- Since xyz(3)
                                                                magnetic_cord_x = self.Magnetic_Atoms_Basis_List[counter_basis_position]
                                                                magnetic_cord_y = self.Magnetic_Atoms_Basis_List[counter_basis_position +1]
                                                                magnetic_cord_z = self.Magnetic_Atoms_Basis_List[counter_basis_position + 2]

                                                                mag_GU = ( (h_index*magnetic_cord_x) +  (k_index*magnetic_cord_y) + (l_index*magnetic_cord_z) )

                                                                #------------------------ Multiplying -1 for the antiferromagnetic alignment --------------------------------------------------
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

            #---------- Printing the maximum values as the information dialog -----------------------------------------------------------------------------------------------------
                print("h_max : ", h_max)
                print("k_max : ", k_max)
                print("l_max : ", l_max)
                print("max_psf : ", max_psf)
                print("max_ext : ", max_ext)
                
#--------------------------------------------------------------------------------------------- END -------------------------------------------
class_Do_G_Optimization2 = Do_G_Optimization2()
class_Do_G_Optimization2.ON_DO_CALCULATE_G_OPTIMIZATION()


