#    This is a module class which calculate the optimized G (hkl) to maximize the EMCD signal ---------------------------------------------
#    This module is called by the main menu option to do the G optimizatio calculation ----------------------------------------------------
#  ****************************************************************************************************************************************
from __future__ import division
from turtle import position
import numpy as np
# import EMCD_GUI_beta as Main_Frame
import math, os
# import Make_Main_Menu as Make_Menu
import Load_structure_info as Load_Structure
# import Load_structure_info_new as Load_Structure
import matplotlib.pyplot as plt
from matplotlib import rc
import Tem_properties as TEM
import  volume_dhkl_class as VDHKL
from Lobato_parameter import Lobato_parameter1 as Lobato
import Physics_Constant as Phys_Const

rc('text', usetex=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------



class Do_G_Optimization():
    
        def __init__(self,extracted_data_with_magnetic_atoms):
 
 
                self.Struct_Information = extracted_data_with_magnetic_atoms['extracted_data']  #----> dictonary
                self.checked_magetic_atoms = extracted_data_with_magnetic_atoms['magnetic_atoms']
                # print(self.Struct_Information)
                #---------------- Load the structure file ---------------------------------------------------------------------------------------------------
                self.Author_Name = "DEVENDRA SINGH NEGI"
                       
                #---------------- Getting the information from the input file --------------------------------------------------------------------------------
                # self.Struct_Information =  Load_Structure.Extract_Structure_Info().Extract_Info('FeGe.struct')
                # self.Material_Name_From_File = self.Struct_Information[0]
                # self.Lattice_Type = self.Struct_Information[1]
                # self.inequiv_atoms = int(self.Struct_Information[2])
                # self.Lattice_Parameter = self.Struct_Information[3]
                # self.Atom_Multiplicty_List = self.Struct_Information[4]
                # self.Atom_Name_List = self.Struct_Information[5]
                # self.Atom_Z_LIST = self.Struct_Information[6]
                # self.X_Coordinate_List = self.Struct_Information[7]
                # self.Y_Coordinate_List = self.Struct_Information[8]
                # self.Z_Coordinate_List = self.Struct_Information[9]
                
                self.Material_Name_From_File = self.Struct_Information['Material_Name']
                self.Lattice_Type = self.Struct_Information['Lattice_Type']
                self.inequiv_atoms = int(self.Struct_Information['Inequivalent_Atoms'])
                self.Lattice_Parameter = self.Struct_Information['Lattice_Parameter']
                self.Atom_Multiplicty_List = self.Struct_Information['Mult_list']
                self.Atom_Name_List = self.Struct_Information['Atom_Name_List']
                self.Atom_Z_LIST = self.Struct_Information['Atom_Z_List']
                self.X_Coordinate_List = self.Struct_Information['X_Coordinate_List']
                self.Y_Coordinate_List = self.Struct_Information['Y_Coordinate_List']
                self.Z_Coordinate_List = self.Struct_Information['Z_Coordinate_List']
                
                
                # print(type(self.Material_Name_From_File))    # string
                # print(type(self.Lattice_Type))               # string    
                # print(type(self.inequiv_atoms))              # int
                # print(self.Lattice_Parameter)
                # print(self.Atom_Multiplicty_List)
                # print(self.Atom_Name_List)
                # print(self.Atom_Z_LIST)
                # print(self.X_Coordinate_List)
                # print(self.Y_Coordinate_List)
                # print(self.Z_Coordinate_List)
                
                #------ Lattice parameter are in nanometer
                self.anm = float(self.Lattice_Parameter[0])*1e-9                    #----- Lattice parameter are in nanometer
                self.bnm = float(self.Lattice_Parameter[1])*1e-9                    #----- Lattice parameter are in nanometer
                self.cnm = float(self.Lattice_Parameter[2])*1e-9                    # --- Lattice parameter are in nanometer
                
                self.angle_alpha = self.Lattice_Parameter[3]                         # --- Lattice parameter are in degree
                self.angle_beta = self.Lattice_Parameter[4]                          # --- Lattice parameter are in degree
                self.angle_gama = self.Lattice_Parameter[5]                          # --- Lattice parameter are in degree
                
                
                self.accel_voltage = 300                             
                self.material_thickness_nm= 5*1e-9 
                
                self.All_G_points_parameter = []              # --- For storing all G parameters ----
                self.Result_G_points_parameter = []           # --- For storing optimized G Paramters ----
                
                self.All_Atom_List = {}
                for atom_name in self.Atom_Name_List:
                        self.All_Atom_List[atom_name] = False
                        
                for magetic_atoms in  self.checked_magetic_atoms:
                        self.All_Atom_List[magetic_atoms] = True  
                        
                self.Magnetic_Atom_List = [magnetic_atoms for magnetic_atoms in self.All_Atom_List.values()]  
                # Boolean value (True/False ) Obtained from the check box 
                # print(self.Magnetic_Atom_List)       
                        
                 
               
                
                
        
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
                
                Max_PSF = 0
                self.MAX_PSF_Relation = np.zeros((1,5))  #--- Index (h,k,l,Max_PSF, Extinction_distance )
                self.atom_position_dict = {}
                         
            #************ Getting spin alignment of every atoms -------------------------------------------------------------------------------------------------------------------------

                # Spin_check_list = [True, False, True, False, True, False, True, False]
                Spin_check_list = []
                for i in range(len(self.Magnetic_Atom_List)):
                        if(self.Magnetic_Atom_List[i]==True):
                                for j in range(self.Atom_Multiplicty_List[i]):
                                     Spin_check_list.append(True)
                                     Spin_check_list.append(False)   
                                
                Spin_Alignment_List = []

                for check_index in range(0, int(len(Spin_check_list)), 2):
                        up_spin = Spin_check_list[check_index]
                        if (up_spin == True):
                                Spin_Alignment_List.append(1)
                        #---- Putting spin dn as -1 in the Partial structure factor --------------------------------------------------------------------------------------------
                        dn_spin = Spin_check_list[check_index + 1]
                        if (dn_spin == True):
                                Spin_Alignment_List.append(-1)
                # print("Spin_Alignment_List : ",Spin_Alignment_List)
                
            #-------------------------------------------------------------------------------------------------------------------------------------------------------------
            #---------------- Calculating the Vg, Excitation coefficient, Partial Structure Factor starts from here -------------------------------------------------------
                self.h = 4
                self.k = 4
                self.l = 4
                
                self.miller_indices_list = [] 
                self.ch = (0 + 0j)
      
            #---------- Starting to calculate the various parameter for every G(hkl) vector ---------------------------------------------------------------------------------------
 
                for h_index in range( self.h, -(self.h+1), -1):   
                        for k_index in range( self.k, -(self.k +1), -1):
                                for l_index in range(self.l,  -(self.l +1), -1):
                                        # single_parameter_list=[]
                                        self.miller_indices_list = []
                                        if (h_index == 0 and k_index ==0 and l_index ==0 ):
                                                continue
                                        else:
                                                self.g_magnitude =  VDHKL.Do_Calculate_Crystal_Volume_and_dhkl().Calculate_Dhkl( self.Lattice_Type, h_index, k_index, l_index, self.anm, self.bnm, self.cnm, self.angle_alpha, self.angle_beta, self.angle_gama)
                                        
                           #----------- Setting the counter and Variable. Variabl are being Rest for next (hkl) values -----------------------   
                                        counter_coordinate = 0          
                                        self.FSCATT =0
                                        self.VG = 0
                                        self.PSF = (0 + 0j)   #--- Partial structure factor : Only for the magnetic atoms ---------------------------------------------
                                        self.Magnetic_Atoms_Basis_List = []

                                        for atom_index in range(int(self.inequiv_atoms)):

                                                Z_Number = float(self.Atom_Z_LIST[atom_index])
                                                self.Lobato_Ai, self.Lobato_Bi = Lobato(Z_Number)
                                
                                                #------------- Find the total Electron scattering factor for particular atoms --------------------------------------
                                                #------------- Since there are 5 differnt ai,bi numbers in the Lobato list -------------------------------------------
                                                self.Lobato_Scattering_Factor = 0
                                                for lobato_index in range(5):
                                                        ai = self.Lobato_Ai[lobato_index] * (1e-10)   #-- Since the unit of ai = 1e-10
                                                        bi = self.Lobato_Bi[lobato_index] * (1e-20)   #- Since the unit of  bi = 1e-20
                                                        lobato_nume =  ( ai * (2 + (bi*(self.g_magnitude**2)) ))
                                                        lobato_deno =   ((1 + (bi*(self.g_magnitude**2)))**2)
                                                        lobato_scattering_factor = (lobato_nume/lobato_deno)
                                                        self.Lobato_Scattering_Factor +=  lobato_scattering_factor
                                                               
                                                               
                                                #----- Getting all the co-ordinates of all the atoms ---------------------------------------------------------------------------
                                                for mult_index in range(int(self.Atom_Multiplicty_List[atom_index])):
                                                        x_coordinate = float(self.X_Coordinate_List[counter_coordinate])
                                                        y_coordinate = float(self.Y_Coordinate_List[counter_coordinate])
                                                        z_coordinate = float(self.Z_Coordinate_List[counter_coordinate])
                                                        counter_coordinate += 1
                                                        
                                                        #print x_coordinate, y_coordinate, z_coordinate
                                                        GU = (h_index*x_coordinate + k_index*y_coordinate + l_index*z_coordinate)
                                                        exp_factor = np.exp( (0 +1j)*(2*np.pi*GU))
                                                        self.FSCATT = self.FSCATT + (self.Lobato_Scattering_Factor * exp_factor)
                                                                
                                                        #------- Extracting only coordinates of the magnetic atoms -----------------------------------------------
                                                        if (bool(self.Magnetic_Atom_List[atom_index])==True):
                                                                self.Magnetic_Atoms_Basis_List.append(x_coordinate)
                                                                self.Magnetic_Atoms_Basis_List.append(y_coordinate)
                                                                self.Magnetic_Atoms_Basis_List.append(z_coordinate)


                                        #------ Fourier component of crystal potential ------------------------------------------------------------------------------------------
                                        self.VG = self.FSCATT * self.Vg_Prefactor
                                        self.VG_Real_Part = self.VG.real
                                        self.VG_Imaginary_Part = self.VG.imag
                                        
                                        #----------if(self.VG_Imaginary_Part==0):
                                        #----------print("VG_Real_Part : ", self.VG_Real_Part)
                                        
                                        if(self.VG_Real_Part !=0):
                                             self.VG_Phase = math.atan(self.VG_Imaginary_Part/self.VG_Real_Part)
                                        #----------print h_index, k_index, l_index, self.VG, self.Vg_Prefactor

                                        #****************************** <<  Magnetic Partial Structure Factor >> **********************************
                                        #------------- ---------------------Finding the partial structure factor for the magnetic atoms ---------------------------------------------------------------
                                        
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

                                        # Calculating the Optimized paramter as given in the paper [ Thickness_Function * Magnetic_Structure_Factor] ---------
                                        #---------------------------------------------------------------------------------------------------------------------
                                                
                                        self.emcd_optimized_parameter =( (self.Extinction_distance / (np.pi * self.cnm))  *  ((np.sin(((np.pi * self.material_thickness_nm)/(self.Extinction_distance))))**2)  \
                                                                                * (abs(self.PSF_Real)) )

                                        #print h_index, k_index, l_index,  self.material_thickness_nm, ((self.Extinction_distance / (np.pi * self.cnm))),  ((np.sin(((np.pi * self.material_thickness_nm)/(self.Extinction_distance))))**2)
                                        #----- This is used later to extract some quantities -----------------------------------------------------------------------------------
                                        self.miller_indices_list.append(h_index)
                                        self.miller_indices_list.append(k_index)
                                        self.miller_indices_list.append(l_index)
                                        self.miller_indices_list.append(np.abs(self.VG)) #voltage
                                        self.miller_indices_list.append(self.VG_Phase) #Phase
                                        self.miller_indices_list.append(abs(self.PSF_Real)) #SF
                                        self.miller_indices_list.append(self.Extinction_distance/1e-9)              #---- Extinction distance in nano-meter
                                         
                                        # single_parameter_list.append(self.miller_indices_list) 
                                        # print(self.miller_indices_list)
                                        self.All_G_points_parameter.append(self.miller_indices_list)

                          
                                        # print(All_G_points_parameter)
                                        
                                        # print(self.G_points_parameter)
                                        #ap.AppendText("\t %s \t %s \t %s \t  %s \t %s, \t  %s, \t  %s \n" % (h_index, k_index, l_index, self.VG, self.VG_Phase, self.PSF, self.Extinction_distance/1e-9))

            #-------- ------------Printing the Final obtained Highest PSF and corrosponding (hkl) and the Extinction distance ----------------------------------
            # ------------------- Finding the Max PSF and corrosponding (hkl) and Extinction distance ----------------------------------------------------------------------
                                        if ((h_index ==0 ) and (k_index ==0 ) and (l_index ==0 )):
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
                # print("h_max : ", h_max)
                # print("k_max : ", k_max)
                # print("l_max : ", l_max)
                # print("max_psf : ", max_psf)
                # print("max_ext : ", max_ext)
                
                self.Result_G_points_parameter.append(h_max)
                self.Result_G_points_parameter.append(k_max)
                self.Result_G_points_parameter.append(l_max)
                self.Result_G_points_parameter.append(max_psf)
                self.Result_G_points_parameter.append(max_ext)
                
                # print(len(All_G_points_parameter))
                return self.All_G_points_parameter, self.Result_G_points_parameter
                
                
                
#--------------------------------------------------------------------------------------------- END -------------------------------------------
class_Do_G_Optimization2 = Do_G_Optimization({'magnetic_atoms': {'O1': True, 'Fe1': True, 'O2': True, 'O5': True, 'Ba1': True, 'Fe5': True}, 'extracted_data': {'Material_Name': 'BaFe12O19', 'Lattice_Type': 'H', 'Inequivalent_Atoms': 11.0, 'Mult_list': [12, 24, 12, 6, 4, 4, 4, 4, 4, 2, 2], 'Atom_Name_List': ['O1', 'Fe1', 'O2', 'O3', 'Fe2', 'Fe3', 'O4', 'O5', 'Fe4', 'Ba1', 'Fe5'], 'Atom_Z_List': [8.0, 26.0, 8.0, 8.0, 26.0, 26.0, 8.0, 8.0, 26.0, 56.0, 26.0], 'Lattice_Parameter': [0.5900000222852999, 0.5900000222852999, 2.3200000230528, 90.0, 90.0, 120.0], 'X_Coordinate_List': [0.15647, 0.84353, 0.84353, 0.15647, 0.31294, 0.68706, 0.68706, 0.31294, 0.84353, 0.15647, 0.15647, 0.84353, 0.16867, 0.83133, 0.83132, 0.16868, 0.33735, 0.66265, 0.66265, 0.33735, 0.16868, 0.83132, 0.83133, 0.16867, 0.83133, 0.16867, 0.16868, 0.83132, 0.66265, 0.33735, 0.33735, 0.66265, 0.83132, 0.16868, 0.16867, 0.83133, 0.5026, 0.4974, 0.4974, 0.5026, 0.0052, 0.9948, 0.9948, 0.0052, 0.4974, 0.5026, 0.5026, 0.4974, 0.18213, 0.81787, 0.81787, 0.18213, 0.36426, 0.63574, 0.33333333, 0.66666667, 0.66666666, 0.33333334, 0.33333333, 0.66666667, 0.66666666, 0.33333334, 0.33333333, 0.66666667, 0.66666666, 0.33333334, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.33333333, 0.66666667, 0.0, 0.0], 'Y_Coordinate_List': [0.31294, 0.68706, 0.15647, 0.84353, 0.15647, 0.84353, 0.84353, 0.15647, 0.68706, 0.31294, 0.84353, 0.15647, 0.33735, 0.66265, 0.16867, 0.83133, 0.16867, 0.83133, 0.83132, 0.16868, 0.33735, 0.66265, 0.66265, 0.33735, 0.16868, 0.83132, 0.83133, 0.16867, 0.83133, 0.16867, 0.16868, 0.83132, 0.66265, 0.33735, 0.83132, 0.16868, 0.0052, 0.9948, 0.5026, 0.4974, 0.5026, 0.4974, 0.4974, 0.5026, 0.9948, 0.0052, 0.4974, 0.5026, 0.36426, 0.63574, 0.18213, 0.81787, 0.18213, 0.81787, 0.66666667, 0.33333333, 0.33333333, 0.66666667, 0.66666667, 0.33333333, 0.33333333, 0.66666667, 0.66666667, 0.33333333, 0.33333333, 0.66666667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.66666667, 0.33333333, 0.0, 0.0], 'Z_Coordinate_List': [0.05192, 0.94808, 0.55192, 0.44808, 0.55192, 0.44808, 0.05192, 0.94808, 0.55192, 0.44808, 0.05192, 0.94808, 0.60825, 0.39175, 0.10825, 0.89175, 0.10825, 0.89175, 0.60825, 0.39175, 0.60825, 0.39175, 0.10825, 0.89175, 0.10825, 0.89175, 0.60825, 0.39175, 0.60825, 0.39175, 0.10825, 0.89175, 0.10825, 0.89175, 0.60825, 0.39175, 0.14957, 0.85043, 0.64957, 0.35043, 0.64957, 0.35043, 0.14957, 0.85043, 0.64957, 0.35043, 0.14957, 0.85043, 0.25, 0.75, 0.75, 0.25, 0.75, 0.25, 0.02713, 0.97287, 0.52713, 0.47287, 0.1903, 0.8097, 0.6903, 0.3097, 0.55454, 0.44546, 0.05454, 0.94546, 0.15094, 0.84906, 0.65094, 0.34906, 0.24267, 0.75733, 0.74267, 0.25733, 0.75, 0.25, 0.0, 0.5]}})
Output_G_points_parameter= class_Do_G_Optimization2.ON_DO_CALCULATE_G_OPTIMIZATION()
# class_Do_G_Optimization2 = Do_G_Optimization()


