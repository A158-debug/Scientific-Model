# ************************' This code creates the GUI which calcuates the following *********************************************************************************
# 1 - Optimized G(hkl) for the EMCD experimentation (  Fourier component V(G), Extinction Distance (xi), Phase(phi), Partial Structure factor **********************
#
#
# Writting by : Devendra Singh Negi , Uppsala University, Sweden
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#**********************************************************************************************************************************************************************

import numpy as np
import matplotlib.pyplot as plt
import wx
import os,sys
import wx.richtext as RichText
import wx.lib.agw.aquabutton as AB
import wx.lib.agw.gradientbutton as GB
import wx.richtext as RichText

#------------------------------------- Class Begins from here --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Create_Main_Dialog(wx.Frame):
            def __init__(self):
                        wx.Frame.__init__(self, None, title= "EMCD GUI")
                        self.Work_Folder = os.getcwd()
                        self.Maximize()
                        self.Window_Size_X, self.Window_Size_Y = wx.GetDisplaySize()
                        self.Global_Font =  wx.Font(10, wx.ROMAN, wx.NORMAL, wx.BOLD)

            #--------  Setting GUI icon picture ----------------------------------------------------------------------------------

                        self.SetIcon(wx.Icon("/home/dev/PycharmProjects/EMCD_GUI/Images/TEM.jpeg", wx.BITMAP_TYPE_JPEG))

            #------- Creating Main Panel Background ---------------------------------------------------------------------

                        self.Main_Panel = wx.Panel(self, style=wx.SUNKEN_BORDER)
                        #self.Main_Panel.SetBackgroundColour(wx.GREEN)
                        self.Main_Box_Sizer = wx.BoxSizer(wx.VERTICAL)

            #------- Creating Statusbar -------------------------------------------------------------------------------------------
                        #-------- Statusbar with 2 section : You can change here
                        self.Statusbar = self.CreateStatusBar(2, style = wx.SUNKEN_BORDER)
                        self.Statusbar.SetBackgroundColour("green")
                        self.Statusbar.SetMinHeight(50)
                        #self.Statusbar.SetStatusWidths([10, 100])

            #------ Creating the side vertical panel and the splitter panel in the Main panel window -
                        #---- Creates box to put the vertical panel and the splitter window --------------
                        box_vertical_panel_splitter_window = wx.BoxSizer(wx.HORIZONTAL)

                        self.Side_Vertical_Panel = wx.Panel(self.Main_Panel, size=(40, self.Window_Size_Y))
                        self.Side_Vertical_Panel.SetBackgroundColour("violet")

                        #------- Creating the splitter window ------------------------------------------------------------
                        self.Main_Splitter_Window = wx.SplitterWindow(self.Main_Panel)
                        self.Left_Splitter_Panel = wx.Panel(self.Main_Splitter_Window)
                        self.Left_Splitter_Panel.SetBackgroundColour("light green")
                        self.Right_Splitter_Panel = wx.ScrolledWindow(self.Main_Splitter_Window)
                        self.Right_Splitter_Panel.SetBackgroundColour("indigo")
                        self.Right_Splitter_Panel.SetScrollbars(10, 10, 100, 500)

                        self.Main_Splitter_Window.SetMinimumPaneSize(1)
                        self.Main_Splitter_Window.SplitVertically(self.Left_Splitter_Panel, self.Right_Splitter_Panel, 300)

                        box_vertical_panel_splitter_window.Add(self.Side_Vertical_Panel,  flag=wx.ALL|wx.EXPAND, border=1)
                        box_vertical_panel_splitter_window.Add(self.Main_Splitter_Window, proportion=1, flag=wx.EXPAND| wx.ALL, border=1)

            #----- Addings stuff in main box ----------------------------------------------------------------------------------------
                        self.Main_Box_Sizer.Add(box_vertical_panel_splitter_window, flag=wx.ALL | wx.EXPAND, border=2)

            #---- Setting the Main sizer with the Main top panel --------------------------------------------------------

                        self.Main_Panel.SetSizer(self.Main_Box_Sizer)

            #----Adding the left arrow button on the left vertical panel -----------------------------------------------
                        self.Split_arrow_button = wx.BitmapButton(self.Side_Vertical_Panel, -1,
                                                                  wx.Bitmap("/home/dev/PycharmProjects/EMCD_GUI/Images/left_arrow.jpeg", wx.BITMAP_TYPE_JPEG),  pos =(2,10), name="LEFT_DIRECTION")

                        self.Split_arrow_button.Bind(wx.EVT_BUTTON, self.ON_SPLIT_ARROW_BUTTON)

            #---------- Adding the directory control on the left panel ----------------------------------------------------
                        left_splitter_panel_box = wx.BoxSizer(wx.VERTICAL)
                        self.Directory_Tree = wx.GenericDirCtrl(self.Left_Splitter_Panel, -1, dir=os.getcwd())
                        self.Directory_Tree.SetBackgroundColour("violet")
                        left_splitter_panel_box.Add(self.Directory_Tree, proportion=1, flag=wx.EXPAND |wx.ALL, border=2)
                        self.Left_Splitter_Panel.SetSizer(left_splitter_panel_box)

                        # ------- Binding the Dir tree with function -------------------------------------------
                        self.Dir_Name = self.Directory_Tree.GetTreeCtrl()
                        self.Dir_Name.Bind(wx.EVT_TREE_SEL_CHANGED, self.ON_DIRECTORY_TREE)

            #---------- Adding the text ctrl on the right splitter panel --------------------------------------------------
                        right_splitter_panel_box = wx.BoxSizer(wx.VERTICAL)
                        self.Richtext_right_splitter_panel = RichText.RichTextCtrl(self.Right_Splitter_Panel, -1, style=wx.TE_MULTILINE, name="Rich_Text")
                        right_splitter_panel_box.Add(self.Richtext_right_splitter_panel, proportion=1, flag=wx.EXPAND, border=1)
                        self.Right_Splitter_Panel.SetSizer(right_splitter_panel_box)

                        # ---- Setting Rich text property here --------------------------------------------------------------------------
                        self.Richtext_right_splitter_panel.BeginFont(self.Global_Font)
                        self.Richtext_right_splitter_panel.BeginTextColour(wx.BLACK)
                        self.Richtext_right_splitter_panel.BeginFontSize(10)
                        self.Richtext_right_splitter_panel.BeginLeftIndent(10)
                        self.Richtext_right_splitter_panel.BeginAlignment(wx.TEXT_ALIGNMENT_LEFT)
                        self.Richtext_right_splitter_panel.BeginLineSpacing(12)
                        self.Richtext_right_splitter_panel.BeginTextColour(wx.BLACK)

                        # ----- Set Left and Top Margin --------------------------------------------------------------------------------
                        self.Richtext_right_splitter_panel.SetMargins((40, 40))

            # --------- Creates Menus items on the status bar ----------------------------------------------------------------
            def Create_Menu_On_StatusBar(self):
                        statusbar_half_width = self.Window_Size_X/2

                        #---- Creating "Show Menu Button", which will pop out calculation menu -----
                        self.Show_Menu_Button = wx.Button(self.Statusbar, -1, "Show Menu", pos = (statusbar_half_width-100, 3), size=(150, 40))
                        self.Show_Menu_Button.SetBackgroundColour("white")
                        self.Show_Menu_Button.SetForegroundColour("red")

                        self.Show_Menu_Button.Bind(wx.EVT_BUTTON, self.ON_SHOW_MENU_BUTTON)

                        #---- Creating Exit Button on the status bar ------------------------------------------------
                        #self.Exit_Button= wx.Button(self.Statusbar, -1, "EXIT", pos=(self.Window_Size_X-80,5), size=(70,40),style= wx.BORDER_NONE)
                        self.Exit_Button =GB.GradientButton(self.Statusbar, -1, None, "Exit",pos=(self.Window_Size_X-80,5), size=(70,40) )
                        self.Exit_Button.SetBackgroundColour(wx.RED)
                        self.Exit_Button.SetForegroundColour(wx.YELLOW)

                        self.Exit_Button.Bind(wx.EVT_BUTTON, self.ON_EXIT_BUTTON)



#*****************************************************************************************************************************************************************
#-------------------------------------- Binding Function starts from here -----------------------------------------------------------------------------------------------------------------------------------------------------
# *****************************************************************************************************************************************************************

            #------- Quit the main menu -----------------------------------------------------------------------------------

            def ON_EXIT_BUTTON(self, event):
                        wx.Exit()
                        event.Skip()


            #----- Show the menus -------------------------------------------------------------------------------------------

            def ON_SHOW_MENU_BUTTON(self, event):

                        #------ Here I open other class which open the menu panel ----------------------
                        import Make_Main_Menu as Main_Menu
                        Main_Menu.Make_Option_Menu().Show_Menu_Opition()
                        event.Skip()


            #---------- Binding function for the Directory tree --------------------------------------------------
            def ON_DIRECTORY_TREE(self, event):
                        # --- To Enable new file open freshly--------------------------------------------------------
                        self.Richtext_right_splitter_panel.Clear()
                        item = event.GetItem()
                        Full_File_Name = self.Directory_Tree.GetFilePath()
                        self.Only_File_Name = self.Dir_Name.GetItemText(item)

                        if (self.Only_File_Name.endswith("py") or self.Only_File_Name.endswith("struct") or self.Only_File_Name.endswith("txt")):
                                    f = open(Full_File_Name, 'r')
                                    self.Richtext_right_splitter_panel.WriteText(f.read())

                                    self.Statusbar.SetStatusText("Chosen File : %s" % (self.Only_File_Name))
                                    f.close()


                        elif (self.Only_File_Name.endswith("png") or self.Only_File_Name.endswith("jpeg")):
                                    # ----------------------- With this case any format can be open --------------------------
                                    # self.File_Data.WriteImage(wx.Bitmap(Only_File_Name).ConvertToImage(), wx.BITMAP_TYPE_PNG)

                                    self.Statusbar.SetStatusText("Chosen Image : %s" % (self.Only_File_Name))
                                    self.Richtext_right_splitter_panel.AddImage(wx.Image(self.Only_File_Name, wx.BITMAP_TYPE_ANY))

                        else:
                                    dlg = wx.MessageDialog(self, "Select a text or image file file", "Message", wx.CANCEL | wx.OK)
                                    dlg.ShowModal()
                                    dlg.Destroy()

                        event.Skip()

            #----------- Function of left split arrow button -------------------------------------------------------------------------------------

            def ON_SPLIT_ARROW_BUTTON(self, event):
                        Button_Name = self.Split_arrow_button.GetName()
                        if (Button_Name == "LEFT_DIRECTION"):
                                    self.Main_Splitter_Window.SetSashPosition(1)
                                    self.Split_arrow_button.SetBitmap(wx.Bitmap("/home/dev/PycharmProjects/EMCD_GUI/Images/right_arrow.jpeg", wx.BITMAP_TYPE_JPEG))
                                    self.Split_arrow_button.SetName("RIGT_DIRECTION")
                        else:
                                    self.Split_arrow_button.SetName("LEFT_DIRECTION")
                                    self.Split_arrow_button.SetBitmap(wx.Bitmap("/home/dev/PycharmProjects/EMCD_GUI/Images/left_arrow.jpeg", wx.BITMAP_TYPE_JPEG))
                                    self.Main_Splitter_Window.SetSashPosition(300)

                        event.Skip()


#*************************************************************************************************************************************************************************
#-------------------------------------------------- Instantiation done here ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#*************************************************************************************************************************************************************************

if (__name__=="__main__"):
    app = wx.App()
    Inst = Create_Main_Dialog()
    Inst.Create_Menu_On_StatusBar()
    Inst.Show()
    app.MainLoop()