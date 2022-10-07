#---------------------------- THis code will be called b# y the main code to make the menu ------------------
#--- This module file will have many class, which makes the pop up menus  -------------------------------


import numpy as np
import wx
import os
import EMCD_GUI_beta as Main_Frame
import wx.lib.agw.gradientbutton as GB

#---------------------------- Class to make the main menu, which shows the collection of the main calculation that can be performed with this code --------
# ***************************************************************************************************************************************************
class Make_Option_Menu():
            def __init__(self):
                        pass

            def Show_Menu_Opition(self):
            #-------- Main Menu_Frame is not inhertiated by the class, rather then it is inside the function and  and seperate panel
                        self.Menu_Frame =  wx.Frame(None, title="Choose Calculation")
                        self.Menu_Dimension_X = (Main_Frame.Create_Main_Dialog().Window_Size_X )/6
                        self.Menu_Dimension_Y = (Main_Frame.Create_Main_Dialog().Window_Size_Y)/6
                        self.Main_window_x, self.Main_window_y = wx.GetDisplaySize()

                        self.Menu_Frame.SetSize((self.Menu_Dimension_X, self.Menu_Dimension_Y))
                        self.Menu_Frame.Center()
                        #self.Menu_Frame.SetPosition(( self.Main_window_x/2 -100 , self.Main_window_y/2 -100   ))
                        self.Menu_Panel = wx.Panel(self.Menu_Frame, style = wx.SUNKEN_BORDER)
                        self.Menu_Panel.SetBackgroundColour("grey")

            #---------------- Creating the box sizer and putting the menu  buttons on that -------------------------------------------
                        Menu_Box_Sizer = wx.BoxSizer(wx.VERTICAL)

                        self.G_Optimization_Button = GB.GradientButton(self.Menu_Panel, -1, None, "%s"%"G Optimization")
                        self.G_Optimization_Button.Bind(wx.EVT_BUTTON, self.ON_G_OPTIMIZATON)
                        #self.G_Optimization_Button.SetForegroundColour(wx.RED)
                        #self.G_Optimization_Button.SetTopStartColour("grey")
                        #self.G_Optimization_Button.SetBottomEndColour("grey")
                        self.G_Optimization_Button.SetToolTip(wx.ToolTip("Find Optimized hkl value for best EMCD signal!"))


                        """
                        self.G_Extinction_Distance_Button = GB.GradientButton(self.Menu_Panel, -1, None,  "Extinction Distance")
                        self.Gen_Pot_Button = GB.GradientButton(self.Menu_Panel, -1, None,  "Generate Potential")
                        self.Multislice_Button = GB.GradientButton(self.Menu_Panel, -1, None, "Multislice")
                        self.Dyn_Diff_Button = GB.GradientButton(self.Menu_Panel, -1, None,  " Dynamical Diffraction")
                        
                        """

                        self.Menu_Exit_Button = GB.GradientButton(self.Menu_Panel, -1, None, "EXIT")
                        self.Menu_Exit_Button.Bind(wx.EVT_BUTTON, self.ON_MENU_EXIT)


                        Menu_Box_Sizer.Add(self.G_Optimization_Button, flag=wx.ALL|wx.TOP|wx.EXPAND, border= 10)
                        """
                        Menu_Box_Sizer.Add(self.G_Extinction_Distance_Button, flag=wx.ALL | wx.EXPAND, border=10)
                        Menu_Box_Sizer.Add(self.Gen_Pot_Button, flag=wx.ALL|wx.EXPAND, border= 10)
                        Menu_Box_Sizer.Add(self.Multislice_Button, flag=wx.ALL|wx.EXPAND, border= 10)
                        Menu_Box_Sizer.Add(self.Dyn_Diff_Button, flag=wx.ALL|wx.EXPAND, border= 10)
                        """
                        Menu_Box_Sizer.Add(self.Menu_Exit_Button, flag=wx.ALL | wx.EXPAND, border=10)

                        self.Menu_Panel.SetSizer(Menu_Box_Sizer)

                        self.Menu_Frame.Show()

            #------------ Binding function of the above class -------------------------------------------------------------

            def ON_MENU_EXIT(self, event):
                        self.Menu_Frame.Close()
                        event.Skip()

            #**************************************************************************************************************************************
            #------------- After Selecting the G optimization button -------------------------------------------------------------------------------------------------------------------------

            def ON_G_OPTIMIZATON(self, event):
                        #----- Closing the previous window ---------------------------------------------------------------------------------------------------
                        #----- A safe option is to hide the frame rather then to destroy it ------------------------------------------------------
                        self.Menu_Frame.Hide()

            #------------- Tell to user to load the structure file --------------------------------------------------------------------------------------------
                        dlg = wx.MessageDialog(None, 'Load the structure file', '', wx.OK | wx.CANCEL)
                        val = dlg.ShowModal()
                        dlg.Show()

                        if val == wx.ID_CANCEL:
                                    dlg.Destroy()

                        if val == wx.ID_OK:
                                    import G_Optimization_class as GOPTI
                                    GOPTI.Do_G_Optimization()

                        event.Skip()

#------------------ When plan to extend for the heigher version of the code and add more functionality for the calculation ----------------------------------
#************ Class to make the frame to gather the input for the extinction distance calculation ------------------------------------------------------------------

class Make_Extinction_Distance_Menu(wx.Frame):
            def __init__(self):
                        wx.Frame.__init__(self, None, title =" Extinction Distance " )
                        self.Menu_Dimension_X = (Main_Frame.Create_Main_Dialog().Window_Size_X )/4
                        self.Menu_Dimension_Y = (Main_Frame.Create_Main_Dialog().Window_Size_Y)/4

                        self.SetSize((self.Menu_Dimension_X, self.Menu_Dimension_Y))
                        self.Center()
                        self.Menu_Panel = wx.Panel(self, style = wx.SUNKEN_BORDER)
                        self.Menu_Panel.SetBackgroundColour("grey")





##-********** Class to make the menu for the mult, genpot, dd class frame ---------------------------------------------------------------------------------------------------------