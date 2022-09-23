#--------------------- class to make the result frame ---------------------------
import wx
import EMCD_GUI_beta as Main_Frame
import os

class Make_Result_Frame(wx.Frame):
            def __init__(self):
                        wx.Frame.__init__(self, None, title="Result Frame")
                        self.Maximize()
                        #self.Gopti_Result_Panel = wx.Panel(self)
                        self.Gopti_Result_Panel = wx.ScrolledWindow(self)
                        self.Gopti_Result_Panel.SetScrollbars(1, 100, 1, 100)

                        self.Gopti_Result_Panel.SetBackgroundColour("white")

                        sizex = Main_Frame.Create_Main_Dialog().Window_Size_X
                        sizey = Main_Frame.Create_Main_Dialog().Window_Size_Y

            #----------- creates statusbar on the on the frame -------------------------------------------------------------------------------------------
                        self.Result_status_bar = self.CreateStatusBar(2, style=wx.SUNKEN_BORDER)
                        self.Result_status_bar.SetBackgroundColour("grey")
                        self.Result_status_bar.SetMinHeight(40)
                        #---------- Creates Exit and Save Button on the statusbar -----------------------------------------------------------------------
                        self.Result_Exit_Button = wx.Button(self.Result_status_bar, -1, "Exit", pos=(sizex-120, 2), size=(100, 35))
                        self.Result_Exit_Button.SetBackgroundColour(wx.RED)
                        self.Result_Exit_Button.SetForegroundColour(wx.YELLOW)
                        self.Result_Exit_Button.Bind(wx.EVT_BUTTON,  self.ON_EXIT_RESULT_PANEL)

                        #---------- Creates the save button on the statusbar -------------------------------------------------------------------------------
                        self.Result_Save = wx.Button(self.Result_status_bar, -1, "Save", pos=(2, 2), size=(100, 35))
                        self.Result_Save.SetBackgroundColour("green")
                        self.Result_Save.SetForegroundColour("yellow")
                        self.Result_Save.Bind(wx.EVT_BUTTON, self.ON_SAVE_RESULT)
            #---------------------------------------------------------------------------------------------------------------------------------------------------------
                        G_opti_result_box = wx.BoxSizer(wx.VERTICAL)
                        self.Gopt_Result_Textctrl = wx.TextCtrl(self.Gopti_Result_Panel, -1, style=wx.TE_MULTILINE)
                        G_opti_result_box.Add(self.Gopt_Result_Textctrl, proportion=1, flag=wx.EXPAND)
                        self.Gopti_Result_Panel.SetSizer(G_opti_result_box)

#***************** Binding function -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            #------------ Close the panel ------------------------------

            def ON_EXIT_RESULT_PANEL(self, event):
                        self.Close()
                        event.Skip()


            #---------- Save the data on a text file --------------

            def ON_SAVE_RESULT(self, event):
                       # -------------------- Creting the Dialogs to save the data ----------------------------------------------------------------------------------------------------------------------------------------------
                        file_name_dlg = wx.TextEntryDialog(self.Gopti_Result_Panel, "File name to save the data ", "File Name", style=wx.OK |wx.CANCEL)
                        file_name_dlg.SetValue("File.txt")
                        if file_name_dlg.ShowModal() == wx.ID_OK:
                                    self.Data_File_Name = file_name_dlg.GetValue()
                                    file_name_dlg.Destroy()

                        # ----- Getting Directory name to save the above text file -------------------------------------------------------------------------------------------------------------------------
                                    dir_dlg = wx.DirDialog(self.Gopti_Result_Panel, "Choose directory", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
                                    if dir_dlg.ShowModal() == wx.ID_OK:
                                                self.Data_File_Directory = dir_dlg.GetPath()
                                    dir_dlg.Destroy()

                                    self.Save_Data_File = os.path.join(self.Data_File_Directory, self.Data_File_Name)
                                    write_data = open("%s"%self.Save_Data_File, 'w')
                                    #write_data.write(" -----------------------------------------------------------------------------------------------------------------------------------\n")
                                    write_data.write("%s"% self.Gopt_Result_Textctrl.GetValue())