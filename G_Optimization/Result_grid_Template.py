#---------- This class make the wx.grid to show the final result and sort them -----------------------------------------------------------
#*******************************************************************************************************************

import wx
import EMCD_GUI_beta as Main_Frame
import os
import wx.grid as gridlib
import numpy as np
import G_Optimization.G_Optimization_class as Goptimization_Class

class Make_Result_Grid(wx.Frame):
            def __init__(self):
                        wx.Frame.__init__(self, None, title="Result Grid")
                        #self.Center()
                        self.Maximize()
                        self.Grid_Panel = wx.Panel(self, style=wx.SUNKEN_BORDER)

                        #---------- Getting the main window display size -------------------------------------------------------------------------------------
                        sizex = Main_Frame.Create_Main_Dialog().Window_Size_X
                        sizey = Main_Frame.Create_Main_Dialog().Window_Size_Y

            #-------- Creating the wx.grid ----------------------------------------------------------------------------------------------------------------------------

                        self.Data_grid = gridlib.Grid(self.Grid_Panel)
                        #--- Nrow, and column will be feteched from the input file
                        self.Data_grid.CreateGrid(10, 3)
                        wx.TipWindow(self.Data_grid, "Left click on the column label to sort ", maxLength=500)

                        box = wx.BoxSizer(wx.VERTICAL)
                        box.Add(self.Data_grid, proportion=1, flag=wx.EXPAND)
                        self.Grid_Panel.SetSizer(box)


                        row_data = range(10)
                        col_data = range(3)

                        self.x_data = [1, 5, 6, 7, 2, 9, 10, 12, 4, 3]
                        self.phase = [4, 0, 1, 9, 3, 2, 9, 5, 1, 12]
                        self.ext_dist = [2, 5, 7, 9, 1, 19, 2, 5, 9, 12]

                        for i in range(10):
                                    self.Data_grid.SetCellValue(i, 0, "%.5f" % (self.x_data[i]))
                                    self.Data_grid.SetCellValue(i, 1, "%.5f" % (self.phase[i]))
                                    self.Data_grid.SetCellValue(i, 2, "%.5f" % (self.ext_dist[i]))

                        self.Data_grid.AutoSize()
            #------- Create Status Bar and Button ----------------------------------------------------------------------------------------------------------------
                        self.status_bar = self.CreateStatusBar(style=wx.SUNKEN_BORDER)
                        self.status_bar.SetBackgroundColour("lime green")
                        self.status_bar.SetMinHeight(40)

                        #------ Exit button on the status bar ------------------------------------------------------------------------------------------------------
                        self.Exit_Button = wx.Button(self.status_bar, -1, "Exit", pos=(sizex-87,2), size=(80,35))
                        self.Exit_Button.SetBackgroundColour("red")
                        self.Exit_Button.SetForegroundColour("yellow")
                        self.Exit_Button.Bind(wx.EVT_BUTTON, self.ON_EXIT)

                        self.Save_Button=wx.Button(self.status_bar, -1, "Save", pos=(1,1), size=(80,35))
                        self.Save_Button.SetBackgroundColour("green")
                        self.Save_Button.SetForegroundColour("yellow")
                        self.Save_Button.Bind(wx.EVT_BUTTON, self.ON_SAVE_DATA)

            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                        #inst = Goptimization_Class.Do_G_Optimization()

                        #print inst.Author_Name
                        #inst.ON_DO_CALCULATE_G_OPTIMIZATION(event)

#---------------------------------- BINDING FUNCTION STARTS HERE -----------------------------------------------------
#**************************************************************************************************

            def ON_EXIT(self, event):
                        self.Close()
                        event.Skip()

            #-------- Save the data -------------------------------------------------------------------------------------------------------------------
            def ON_SAVE_DATA(self, event):

                        # -------------------- Creting the Dialogs to save the data ----------------------------------------------------------------------------------------------------------------------------------------------
                        file_name_dlg = wx.TextEntryDialog(self.Grid_Panel, "File name to save the data ", "File Name", style=wx.OK | wx.CANCEL)
                        file_name_dlg.SetValue("File.txt")
                        if file_name_dlg.ShowModal() == wx.ID_OK:
                                    self.Data_File_Name = file_name_dlg.GetValue()
                                    file_name_dlg.Destroy()

                                    # ----- Getting Directory name to save the above text file -------------------------------------------------------------------------------------------------------------------------
                                    dir_dlg = wx.DirDialog(self.Grid_Panel, "Choose directory", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
                                    if dir_dlg.ShowModal() == wx.ID_OK:
                                                self.Data_File_Directory = dir_dlg.GetPath()
                                    dir_dlg.Destroy()


                        #*********** THIS SECTION WILL WRITE THE DATA FROM THE GRID TO TEXT FILE **********************************************************

                                    #self.Save_Data_File = os.path.join(self.Data_File_Directory, self.Data_File_Name)
                                    #write_data = open("%s" % self.Save_Data_File, 'w')
                                    # write_data.write(" -----------------------------------------------------------------------------------------------------------------------------------\n")
                                    #write_data.write("%s" % self.Gopt_Result_Textctrl.GetValue())

                        event.Skip()



#-------------- For testing purpose only --------------------------------
"""
app = wx.App()
Make_Result_Grid().Show()
app.MainLoop()
"""