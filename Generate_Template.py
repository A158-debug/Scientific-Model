#--------------------- Class to generate the input template ---------------------------
import wx
import numpy as np
import G_Optimization_class as gopt

class Make_First_Template(wx.Frame):

            def __init__(self):
                        wx.Frame.__init__(self, None, title="First_Template")
                        self.Center()
                        self.First_Template_Panel = wx.Panel(self)
                        self.First_Template_Panel.SetBackgroundColour("pink")


                        ins = gopt.Do_G_Optimization()

                        #print ins.accel_voltage