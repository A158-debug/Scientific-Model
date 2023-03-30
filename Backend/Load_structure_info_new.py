# import json
import re
class Extract_Structure_Info:
    def __init__(self,string_a):
        self.string_a = string_a

    def print_input_string(self):
        print(self.string_a)

    def extract_info(self):
        #----------material name ------------------------------------
        # print(self.string_a)
        line_split_list = self.string_a.split('\n')
        print(line_split_list[0])
        count = 0 
        material_name = line_split_list[0]
        count += 1 
        lattice_type = line_split_list[count][0]
        find_index_noneq = line_split_list[count].rfind(':')
        non_eq_atoms = line_split_list[count][find_index_noneq+3:]
        count+=1
        # print(line_split_list[count])
        match_calc = re.search("CALC",line_split_list[count])
        # print(match_calc.start())
        match_unit = re.search("unit",line_split_list[count])
        # print(match_unit.start())

        
        mode_of_calculation = line_split_list[count][match_calc.end()+1:match_unit.start()]
        unit = line_split_list[count][match_unit.end()+1:]
        count +=1 
        lattice_parameters = line_split_list[count].split(" ")
        lattice_parameters_final = []
        for ele in lattice_parameters: #removing empty spaces
            if ele.strip():
                lattice_parameters_final.append(ele)
        # ((float(Lattice_Parameter_Angle[0]) * 0.529177) / 10)
        for xc in range(3):
            lattice_parameters_final[xc] = str((float(lattice_parameters_final[xc])*0.529177)/10)
        count+=1 
        atom_name_list = []
        atom_z_list = []
        x_coordinate_list = []
        y_coordinate_list = []
        z_coordinate_list = []
        isplit_list = []
        mult_list = []
        npt_list = []
        r_list = []
        rmt_list = []
        for i in range(int(non_eq_atoms)):
            x_start = line_split_list[count].rfind('X') +2 
            y_start = line_split_list[count].rfind('Y') 
            z_start = line_split_list[count].rfind('Z')
            x_cr = line_split_list[count][x_start:y_start]
            y_cr = line_split_list[count][y_start+2:z_start]
            z_cr = line_split_list[count][z_start+2:]
            z_cr = z_cr.replace('\r','')
            x_coordinate_list.append(x_cr)
            y_coordinate_list.append(y_cr)
            z_coordinate_list.append(z_cr)

            # print(x_cr)
            # print(y_cr) 
            # print(z_cr)
            count +=1 
            # print(line_split_list[count])
            match_mult = re.search("MULT",line_split_list[count])
            match_isplit = re.search("ISPLIT",line_split_list[count])
            mult = line_split_list[count][match_mult.end()+2:match_isplit.start()]
            mult = int(mult)
            mult_list.append(mult)
            isplit= int(line_split_list[count][match_isplit.end()+2:])
            isplit_list.append(isplit)
            # print(mult)
            # print(isplit)
            # print()
            for j in range(mult-1):
                count += 1 
                x_start = line_split_list[count].rfind('X') +2 
                y_start = line_split_list[count].rfind('Y') 
                z_start = line_split_list[count].rfind('Z')
                x_cr = line_split_list[count][x_start:y_start]
                y_cr = line_split_list[count][y_start+2:z_start]
                z_cr = line_split_list[count][z_start+2:]
                z_cr = z_cr.replace('\r','')
                
                x_coordinate_list.append(x_cr)
                y_coordinate_list.append(y_cr)
                z_coordinate_list.append(z_cr)
                # print(line_split_list[count])
                # print()
            
            count +=1 
            # print(line_split_list[count])
            match_npt = re.search("NPT= ",line_split_list[count])
            match_ro = re.search("R",line_split_list[count])
            match_rmt = re.search("RMT= ",line_split_list[count])
            # print(match_rmt.start())

            match_z = re.search("Z: ",line_split_list[count])
            
            atom_name = line_split_list[count][:match_npt.start()]
            # atom_name_list.append(atom_name)
            npt = line_split_list[count][match_npt.end():match_ro.start()]
            ro = line_split_list[count][match_ro.end()+2:match_rmt.start()]
            rmt = line_split_list[count][match_rmt.end():match_z.start()]
            z = line_split_list[count][match_z.end():]
            atom_name = atom_name.replace(" ","")
            atom_name_list.append(atom_name)
            # print("atom name=" , atom_name)
            # print("npt=" ,npt)
            npt_list.append(npt)
            # print("r0=" ,ro)
            r_list.append(ro)
            # print("rmt=",rmt)
            rmt_list.append(rmt)
            # print("z:",z)
            atom_z_list.append(z)
            count += 4
            
        print("material name:",material_name)   
        print("lattice type:" ,lattice_type)
        print("inequivalent atom:" ,non_eq_atoms)
        print("Mult list:" ,mult_list)
        print("atom name list:" , atom_name_list)
        print("atom z list:" , atom_z_list)
        print("lattice parameter :", lattice_parameters_final)
        print('x_coordinate_list',x_coordinate_list)
        print('y_coordinate_list:',y_coordinate_list)
        print('z_coordinate_list',z_coordinate_list)
        print()
        
        return(material_name,lattice_type,non_eq_atoms,lattice_parameters,mult_list,atom_name_list,atom_z_list,x_coordinate_list,y_coordinate_list,z_coordinate_list)

        #---------getting lattice type ------------------------------



aloo = Extract_Structure_Info("FeGe                                                        \r\nP   LATTICE,NONEQUIV.ATOMS:  2                               \r\nMODE OF CALC=RELA unit=ang \r\n  8.881716  8.881716  8.881716  90.000000 90.000000 90.000000\r\nATOM  -1:X=0.13500000 Y=0.13500000 Z=0.13500000\r\n          MULT= 4          ISPLIT= 8\r\nATOM  -1:X=0.63500000 Y=0.36500000 Z=0.86500000\r\nATOM  -1:X=0.86500000 Y=0.63500000 Z=0.36500000\r\nATOM  -1:X=0.36500000 Y=0.86500000 Z=0.63500000\r\nFe         NPT=  781  R0=0.00005000 RMT= 2.30        Z: 26.0\r\nLOCAL ROT MATRIX:    1.0000000 0.0000000 0.0000000\r\n                     0.0000000 1.0000000 0.0000000\r\n                     0.0000000 0.0000000 1.0000000\r\nATOM   2: X=0.84200000 Y=0.84200000 Z=0.84200000\r\n          MULT= 4          ISPLIT= 8\r\nATOM   2:X=0.34200000 Y=0.65800000 Z=0.15800000\r\nATOM   2:X=0.15800000 Y=0.34200000 Z=0.65800000\r\nATOM   2:X=0.65800000 Y=0.15800000 Z=0.34200000\r\nGe         NPT=  781  R0=0.00005000 RMT= 2.18        Z: 32.0\r\nLOCAL ROT MATRIX:    0.0000000 0.0000000 0.0000000\r\n                     0.0000000 0.0000000 0.0000000\r\n                     0.0000000 0.0000000 0.0000000\r\n   0      NUMBER OF SYMMETRY OPERATIONS\r\n")
aloo.extract_info()

