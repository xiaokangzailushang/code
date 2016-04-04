import wx
 
########################################################################
class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""        
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "wx lambda tutorial",
                          size=(600,400)
                          )
        panel = wx.Panel(self)
 
        button8 = wx.Button(panel, label="8")
        button8.Bind(wx.EVT_BUTTON, lambda evt, name=button8.GetLabel(): self.onButton(evt, name))
        button10 = wx.Button(panel, label="10")
        button10.Bind(wx.EVT_BUTTON, lambda evt, name=button10.GetLabel(): self.onButton(evt, name))
 
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(button8, 0, wx.ALL, 5)
        sizer.Add(button10, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onButton(self, event, buttonLabel):
        """"""
        print "You pressed the %s button!" % buttonLabel
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = DemoFrame().Show()
    app.MainLoop()
