# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/general_widget.ui'
#
# Created: Sat Feb 15 15:53:31 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_general_widget(object):
    def setupUi(self, general_widget):
        general_widget.setObjectName(_fromUtf8("general_widget"))
        general_widget.resize(829, 852)
        self.gridLayout_5 = QtGui.QGridLayout(general_widget)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.widget_container = QtGui.QWidget(general_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_container.sizePolicy().hasHeightForWidth())
        self.widget_container.setSizePolicy(sizePolicy)
        self.widget_container.setObjectName(_fromUtf8("widget_container"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_container)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.widget = QtGui.QWidget(self.widget_container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(20, 20))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_backend = QtGui.QLabel(self.widget)
        self.label_backend.setObjectName(_fromUtf8("label_backend"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_backend)
        self.label_resolution = QtGui.QLabel(self.widget)
        self.label_resolution.setObjectName(_fromUtf8("label_resolution"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_resolution)
        self.frame_resolution = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_resolution.sizePolicy().hasHeightForWidth())
        self.frame_resolution.setSizePolicy(sizePolicy)
        self.frame_resolution.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_resolution.setObjectName(_fromUtf8("frame_resolution"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_resolution)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spinbox_width = QtGui.QSpinBox(self.frame_resolution)
        self.spinbox_width.setMinimum(1)
        self.spinbox_width.setMaximum(10000)
        self.spinbox_width.setObjectName(_fromUtf8("spinbox_width"))
        self.horizontalLayout_3.addWidget(self.spinbox_width)
        self.label_6 = QtGui.QLabel(self.frame_resolution)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.spinbox_height = QtGui.QSpinBox(self.frame_resolution)
        self.spinbox_height.setMinimum(1)
        self.spinbox_height.setMaximum(10000)
        self.spinbox_height.setObjectName(_fromUtf8("spinbox_height"))
        self.horizontalLayout_3.addWidget(self.spinbox_height)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.frame_resolution)
        self.label_colors = QtGui.QLabel(self.widget)
        self.label_colors.setObjectName(_fromUtf8("label_colors"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_colors)
        self.frame_colors = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_colors.sizePolicy().hasHeightForWidth())
        self.frame_colors.setSizePolicy(sizePolicy)
        self.frame_colors.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_colors.setObjectName(_fromUtf8("frame_colors"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_colors)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.edit_foreground = color_edit(self.frame_colors)
        self.edit_foreground.setObjectName(_fromUtf8("edit_foreground"))
        self.gridLayout_6.addWidget(self.edit_foreground, 0, 1, 1, 1)
        self.label_foreground = QtGui.QLabel(self.frame_colors)
        self.label_foreground.setObjectName(_fromUtf8("label_foreground"))
        self.gridLayout_6.addWidget(self.label_foreground, 0, 0, 1, 1)
        self.label_background = QtGui.QLabel(self.frame_colors)
        self.label_background.setObjectName(_fromUtf8("label_background"))
        self.gridLayout_6.addWidget(self.label_background, 1, 0, 1, 1)
        self.edit_background = color_edit(self.frame_colors)
        self.edit_background.setObjectName(_fromUtf8("edit_background"))
        self.gridLayout_6.addWidget(self.edit_background, 1, 1, 1, 1)
        self.label_colors_examples = QtGui.QLabel(self.frame_colors)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_colors_examples.sizePolicy().hasHeightForWidth())
        self.label_colors_examples.setSizePolicy(sizePolicy)
        self.label_colors_examples.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_colors_examples.setWordWrap(True)
        self.label_colors_examples.setObjectName(_fromUtf8("label_colors_examples"))
        self.gridLayout_6.addWidget(self.label_colors_examples, 2, 0, 1, 2)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.frame_colors)
        self.label_font = QtGui.QLabel(self.widget)
        self.label_font.setObjectName(_fromUtf8("label_font"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_font)
        self.frame_font = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_font.sizePolicy().hasHeightForWidth())
        self.frame_font.setSizePolicy(sizePolicy)
        self.frame_font.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_font.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_font.setObjectName(_fromUtf8("frame_font"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_font)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.widget_font = font_widget(self.frame_font)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_font.sizePolicy().hasHeightForWidth())
        self.widget_font.setSizePolicy(sizePolicy)
        self.widget_font.setMinimumSize(QtCore.QSize(10, 10))
        self.widget_font.setObjectName(_fromUtf8("widget_font"))
        self.horizontalLayout_4.addWidget(self.widget_font)
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.frame_font)
        self.label_advanced = QtGui.QLabel(self.widget)
        self.label_advanced.setObjectName(_fromUtf8("label_advanced"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_advanced)
        self.frame_advanced = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_advanced.sizePolicy().hasHeightForWidth())
        self.frame_advanced.setSizePolicy(sizePolicy)
        self.frame_advanced.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_advanced.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_advanced.setObjectName(_fromUtf8("frame_advanced"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_advanced)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.button_backend_settings = QtGui.QCommandLinkButton(self.frame_advanced)
        self.button_backend_settings.setObjectName(_fromUtf8("button_backend_settings"))
        self.horizontalLayout_6.addWidget(self.button_backend_settings)
        self.button_script_editor = QtGui.QCommandLinkButton(self.frame_advanced)
        self.button_script_editor.setObjectName(_fromUtf8("button_script_editor"))
        self.horizontalLayout_6.addWidget(self.button_script_editor)
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.frame_advanced)
        self.checkbox_transparent_variables = QtGui.QCheckBox(self.widget)
        self.checkbox_transparent_variables.setObjectName(_fromUtf8("checkbox_transparent_variables"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.checkbox_transparent_variables)
        self.label_miscellaneous = QtGui.QLabel(self.widget)
        self.label_miscellaneous.setTextFormat(QtCore.Qt.AutoText)
        self.label_miscellaneous.setObjectName(_fromUtf8("label_miscellaneous"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_miscellaneous)
        self.checkbox_bidi = QtGui.QCheckBox(self.widget)
        self.checkbox_bidi.setObjectName(_fromUtf8("checkbox_bidi"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.checkbox_bidi)
        self.widget_backend = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_backend.sizePolicy().hasHeightForWidth())
        self.widget_backend.setSizePolicy(sizePolicy)
        self.widget_backend.setObjectName(_fromUtf8("widget_backend"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_backend)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.combobox_backend = QtGui.QComboBox(self.widget_backend)
        self.combobox_backend.setObjectName(_fromUtf8("combobox_backend"))
        self.horizontalLayout.addWidget(self.combobox_backend)
        self.label_backend_2 = QtGui.QLabel(self.widget_backend)
        self.label_backend_2.setOpenExternalLinks(True)
        self.label_backend_2.setObjectName(_fromUtf8("label_backend_2"))
        self.horizontalLayout.addWidget(self.label_backend_2)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget_backend)
        self.horizontalLayout_5.addWidget(self.widget)
        self.gridLayout_5.addWidget(self.widget_container, 0, 0, 1, 1)

        self.retranslateUi(general_widget)
        QtCore.QMetaObject.connectSlotsByName(general_widget)

    def retranslateUi(self, general_widget):
        general_widget.setWindowTitle(_translate("general_widget", "Form", None))
        self.label_backend.setText(_translate("general_widget", "<h3>Back-end</h3>", None))
        self.label_resolution.setText(_translate("general_widget", "<h3>Resolution</h3>", None))
        self.spinbox_width.setToolTip(_translate("general_widget", "The display resolution (width) in pixels", None))
        self.spinbox_width.setSuffix(_translate("general_widget", "px", None))
        self.label_6.setText(_translate("general_widget", "x", None))
        self.spinbox_height.setToolTip(_translate("general_widget", "The display resolution (height) in pixels", None))
        self.spinbox_height.setSuffix(_translate("general_widget", "px", None))
        self.label_colors.setText(_translate("general_widget", "<h3>Colors</h3>", None))
        self.label_foreground.setText(_translate("general_widget", "Foreground", None))
        self.label_background.setText(_translate("general_widget", "Background", None))
        self.label_colors_examples.setText(_translate("general_widget", "<small><i>Examples: \'white\', \'#FFFFFF\'</i></small>", None))
        self.label_font.setText(_translate("general_widget", "<h3>Font</h3>", None))
        self.label_advanced.setText(_translate("general_widget", "<h3>Advanced</h3>", None))
        self.button_backend_settings.setToolTip(_translate("general_widget", "Advanced settings for the selected back-end", None))
        self.button_backend_settings.setText(_translate("general_widget", "Back-end settings", None))
        self.button_script_editor.setToolTip(_translate("general_widget", "Edit the script for the entire experiment", None))
        self.button_script_editor.setText(_translate("general_widget", "Script editor", None))
        self.checkbox_transparent_variables.setToolTip(_translate("general_widget", "Allows you to access experimental variables directly by name", None))
        self.checkbox_transparent_variables.setText(_translate("general_widget", "Transparent variable management", None))
        self.label_miscellaneous.setText(_translate("general_widget", "<html><head/><body><p><span style=\" font-size:large; font-weight:600;\">Miscellaneous</span></p></body></html>", None))
        self.checkbox_bidi.setToolTip(_translate("general_widget", "Enables support for bi-directional languages, such as Arabic and Hebrew", None))
        self.checkbox_bidi.setText(_translate("general_widget", "Bi-directional-text support", None))
        self.label_backend_2.setText(_translate("general_widget", "<html><head/><body><p><a href=\"http://osdoc.cogsci.nl/back-ends/about\"><span style=\"font-size:small;font-style:italic; text-decoration: underline; color:#0057ae;\">Why is this important?</span></a></p></body></html>", None))

from libqtopensesame.widgets.font_widget import font_widget
from libqtopensesame.widgets.color_edit import color_edit
