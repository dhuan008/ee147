import wx

class Menu(wx.Frame):

    def __init__(self, *args, **kw):
        super(Menu, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        blurButton = wx.Button(pnl, label='Blur', pos=(20, 20))
        blurButton.Bind(wx.EVT_BUTTON, self.blur)

        edgesButton = wx.Button(pnl, label='Edges', pos=(20, 60))
        edgesButton.Bind(wx.EVT_BUTTON, self.edges)

        embossButton = wx.Button(pnl, label='Emboss', pos=(20, 100))
        embossButton.Bind(wx.EVT_BUTTON, self.emboss)

        sharpenButton = wx.Button(pnl, label='Sharpen', pos=(20, 140))
        sharpenButton.Bind(wx.EVT_BUTTON, self.sharpen)

        sobelButton = wx.Button(pnl, label='Sobel', pos=(20, 180))
        sobelButton.Bind(wx.EVT_BUTTON, self.sobel)


        self.SetSize((120, 300))
        self.SetTitle('EE147 Project')
        self.Centre()

    def OnClose(self, e):
        self.Close(True)

    def blur( self, event ):
        event.Skip()
    
    def edges( self, event ):
        event.Skip()
    
    def emboss( self, event ):
        event.Skip()
    
    def sharpen( self, event ):
        event.Skip()
    
    def sobel( self, event ):
        event.Skip()


def main():
    app = wx.App()
    ex = Menu(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  
