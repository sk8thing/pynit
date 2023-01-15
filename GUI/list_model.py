from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

import operator


class List_Model(QAbstractTableModel):
    def __init__(self, data, vertical_header=None, horizontal_header=None, center_text=False):
        super(List_Model, self).__init__()
        self._data = data
        self._v_header = vertical_header
        self._h_header = horizontal_header
        self._center_text = center_text

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                if section < len(self._h_header):
                    return self._h_header[section]
                else:
                    return "<empty>"
            if orientation == Qt.Orientation.Vertical:
                if section < len(self._v_header):
                    return self._v_header[section]
                else:
                    return "<empty>"
            else:
                return section + 1

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return self._data[index.row()][index.column()]
            elif role == Qt.TextAlignmentRole and self._center_text:
                return Qt.AlignmentFlag.AlignCenter
        return None

    def sort(self, Ncol, order=None):
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=operator.itemgetter(Ncol))
        if order == Qt.SortOrder.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()

    def insertRow(self, row, parent=None, rowData=None):
        self.beginInsertRows(QModelIndex(), row, row)
        self._data.insert(row + 1, rowData)
        self.endInsertRows()
        self.dataChanged.emit(self.index(row, 0), self.index(row, self.columnCount() - 1))

    def removeRow(self, row, parent=None):
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._data[row]
        self.endRemoveRows()
        self.dataChanged.emit(self.index(row, 0), self.index(row, self.columnCount() - 1))

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        row = index.row()
        col = index.column()
        self._data[row][col] = value
        self.dataChanged.emit(index, index)
        return True

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0])
