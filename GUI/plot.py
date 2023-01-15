from pyqtgraph import PlotWidget, ViewBox


class Plot(PlotWidget):
    def __init__(self, parent=None, grid=True, no_auto=True, limits=None):
        super(Plot, self).__init__(parent)
        self.style = {'color': '#969696', 'font-family': 'Consolas'}
        self.setBackground(background="#31363b")
        self.plotItem.showGrid(x=grid, y=grid, alpha=0.3)
        self.plotItem.setDefaultPadding(padding=0)
        if limits is not None:
            self.plotItem.setLimits(xMin=limits[0][0], xMax=limits[0][1], yMin=limits[1][0], yMax=limits[1][1])
            self.plotItem.setRange(xRange=limits[0], yRange=limits[1])
        if no_auto and limits is not None:
            self.plotItem.disableAutoRange(ViewBox.XYAxes)
        self.plotItem.setMouseEnabled(x=False, y=False)
        self.plotItem.hideButtons()
        self.plotItem.ctrlMenu.menuAction().setVisible(False)
        for menu in self.plotItem.getViewBox().menu.actions():
            menu.setVisible(False)
