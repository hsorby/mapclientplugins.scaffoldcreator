# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\meshgeneratorwidget.ui'
#
# Created: Mon Jul  2 12:34:46 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MeshGeneratorWidget(object):
    def setupUi(self, MeshGeneratorWidget):
        MeshGeneratorWidget.setObjectName("MeshGeneratorWidget")
        MeshGeneratorWidget.resize(1093, 872)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeshGeneratorWidget.sizePolicy().hasHeightForWidth())
        MeshGeneratorWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(MeshGeneratorWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(MeshGeneratorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(353, 197))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -32, 316, 830))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.identifier_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.identifier_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.identifier_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.identifier_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.identifier_frame.setObjectName("identifier_frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.identifier_frame)
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.identifier_label = QtGui.QLabel(self.identifier_frame)
        self.identifier_label.setObjectName("identifier_label")
        self.verticalLayout_4.addWidget(self.identifier_label)
        self.line = QtGui.QFrame(self.identifier_frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_3.addWidget(self.identifier_frame)
        self.meshType_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.meshType_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meshType_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.meshType_frame.setObjectName("meshType_frame")
        self.formLayout_3 = QtGui.QFormLayout(self.meshType_frame)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.meshType_label = QtGui.QLabel(self.meshType_frame)
        self.meshType_label.setObjectName("meshType_label")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.meshType_label)
        self.meshType_comboBox = QtGui.QComboBox(self.meshType_frame)
        self.meshType_comboBox.setObjectName("meshType_comboBox")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.meshType_comboBox)
        self.verticalLayout_3.addWidget(self.meshType_frame)
        self.meshTypeOptions_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.meshTypeOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meshTypeOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.meshTypeOptions_frame.setObjectName("meshTypeOptions_frame")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.meshTypeOptions_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3.addWidget(self.meshTypeOptions_frame)
        self.modifyOptions_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.modifyOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.modifyOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.modifyOptions_frame.setObjectName("modifyOptions_frame")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.modifyOptions_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.deleteElementRanges_label = QtGui.QLabel(self.modifyOptions_frame)
        self.deleteElementRanges_label.setObjectName("deleteElementRanges_label")
        self.verticalLayout_6.addWidget(self.deleteElementRanges_label)
        self.deleteElementsRanges_lineEdit = QtGui.QLineEdit(self.modifyOptions_frame)
        self.deleteElementsRanges_lineEdit.setObjectName("deleteElementsRanges_lineEdit")
        self.verticalLayout_6.addWidget(self.deleteElementsRanges_lineEdit)
        self.scale_label = QtGui.QLabel(self.modifyOptions_frame)
        self.scale_label.setObjectName("scale_label")
        self.verticalLayout_6.addWidget(self.scale_label)
        self.scale_lineEdit = QtGui.QLineEdit(self.modifyOptions_frame)
        self.scale_lineEdit.setObjectName("scale_lineEdit")
        self.verticalLayout_6.addWidget(self.scale_lineEdit)
        self.verticalLayout_3.addWidget(self.modifyOptions_frame)
        self.displayOptions_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayOptions_groupBox.sizePolicy().hasHeightForWidth())
        self.displayOptions_groupBox.setSizePolicy(sizePolicy)
        self.displayOptions_groupBox.setObjectName("displayOptions_groupBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.displayOptions_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.displayAxes_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayAxes_checkBox.setObjectName("displayAxes_checkBox")
        self.verticalLayout_7.addWidget(self.displayAxes_checkBox)
        self.displayLines_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayLines_checkBox.setObjectName("displayLines_checkBox")
        self.verticalLayout_7.addWidget(self.displayLines_checkBox)
        self.displaySurfaces_frame = QtGui.QFrame(self.displayOptions_groupBox)
        self.displaySurfaces_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.displaySurfaces_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.displaySurfaces_frame.setObjectName("displaySurfaces_frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.displaySurfaces_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName("displaySurfaces_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)
        self.displaySurfacesExterior_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName("displaySurfacesExterior_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)
        self.displaySurfacesTranslucent_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName("displaySurfacesTranslucent_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)
        self.displaySurfacesWireframe_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName("displaySurfacesWireframe_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)
        self.verticalLayout_7.addWidget(self.displaySurfaces_frame)
        self.displayElementNumbers_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayElementNumbers_checkBox.setObjectName("displayElementNumbers_checkBox")
        self.verticalLayout_7.addWidget(self.displayElementNumbers_checkBox)
        self.displayNodeNumbers_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayNodeNumbers_checkBox.setObjectName("displayNodeNumbers_checkBox")
        self.verticalLayout_7.addWidget(self.displayNodeNumbers_checkBox)
        self.displayNodeDerivatives_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayNodeDerivatives_checkBox.setObjectName("displayNodeDerivatives_checkBox")
        self.verticalLayout_7.addWidget(self.displayNodeDerivatives_checkBox)
        self.displayXiAxes_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayXiAxes_checkBox.setObjectName("displayXiAxes_checkBox")
        self.verticalLayout_7.addWidget(self.displayXiAxes_checkBox)
        self.displayImagePlane_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayImagePlane_checkBox.setObjectName("displayImagePlane_checkBox")
        self.verticalLayout_7.addWidget(self.displayImagePlane_checkBox)
        self.displayFiducialMarkers_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayFiducialMarkers_checkBox.setObjectName("displayFiducialMarkers_checkBox")
        self.verticalLayout_7.addWidget(self.displayFiducialMarkers_checkBox)
        self.verticalLayout_3.addWidget(self.displayOptions_groupBox)
        self.time_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.time_groupBox.setObjectName("time_groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.time_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.timePlayStop_pushButton = QtGui.QPushButton(self.time_groupBox)
        self.timePlayStop_pushButton.setObjectName("timePlayStop_pushButton")
        self.gridLayout_4.addWidget(self.timePlayStop_pushButton, 1, 1, 1, 1)
        self.timeValue_label = QtGui.QLabel(self.time_groupBox)
        self.timeValue_label.setObjectName("timeValue_label")
        self.gridLayout_4.addWidget(self.timeValue_label, 0, 0, 1, 1)
        self.timeValue_doubleSpinBox = QtGui.QDoubleSpinBox(self.time_groupBox)
        self.timeValue_doubleSpinBox.setMaximum(12000.0)
        self.timeValue_doubleSpinBox.setObjectName("timeValue_doubleSpinBox")
        self.gridLayout_4.addWidget(self.timeValue_doubleSpinBox, 0, 1, 1, 1)
        self.timeLoop_checkBox = QtGui.QCheckBox(self.time_groupBox)
        self.timeLoop_checkBox.setObjectName("timeLoop_checkBox")
        self.gridLayout_4.addWidget(self.timeLoop_checkBox, 1, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.time_groupBox)
        self.video_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.video_groupBox.setObjectName("video_groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.video_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameIndex_label = QtGui.QLabel(self.video_groupBox)
        self.frameIndex_label.setObjectName("frameIndex_label")
        self.gridLayout_2.addWidget(self.frameIndex_label, 0, 0, 1, 1)
        self.framesPerSecond_spinBox = QtGui.QSpinBox(self.video_groupBox)
        self.framesPerSecond_spinBox.setMinimum(1)
        self.framesPerSecond_spinBox.setProperty("value", 25)
        self.framesPerSecond_spinBox.setObjectName("framesPerSecond_spinBox")
        self.gridLayout_2.addWidget(self.framesPerSecond_spinBox, 1, 1, 1, 1)
        self.framesPerSecond_label = QtGui.QLabel(self.video_groupBox)
        self.framesPerSecond_label.setObjectName("framesPerSecond_label")
        self.gridLayout_2.addWidget(self.framesPerSecond_label, 1, 0, 1, 1)
        self.frameIndex_spinBox = QtGui.QSpinBox(self.video_groupBox)
        self.frameIndex_spinBox.setMinimum(1)
        self.frameIndex_spinBox.setMaximum(10000)
        self.frameIndex_spinBox.setObjectName("frameIndex_spinBox")
        self.gridLayout_2.addWidget(self.frameIndex_spinBox, 0, 1, 1, 1)
        self.numFrames_frame = QtGui.QFrame(self.video_groupBox)
        self.numFrames_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.numFrames_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.numFrames_frame.setObjectName("numFrames_frame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.numFrames_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.numFrames_label = QtGui.QLabel(self.numFrames_frame)
        self.numFrames_label.setObjectName("numFrames_label")
        self.horizontalLayout_4.addWidget(self.numFrames_label)
        self.numFramesValue_label = QtGui.QLabel(self.numFrames_frame)
        self.numFramesValue_label.setObjectName("numFramesValue_label")
        self.horizontalLayout_4.addWidget(self.numFramesValue_label)
        self.gridLayout_2.addWidget(self.numFrames_frame, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.video_groupBox)
        self.alignment_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.alignment_groupBox.setObjectName("alignment_groupBox")
        self.gridLayout = QtGui.QGridLayout(self.alignment_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.activeModel_comboBox = QtGui.QComboBox(self.alignment_groupBox)
        self.activeModel_comboBox.setObjectName("activeModel_comboBox")
        self.activeModel_comboBox.addItem("")
        self.activeModel_comboBox.addItem("")
        self.gridLayout.addWidget(self.activeModel_comboBox, 1, 1, 1, 2)
        self.activeModel_label = QtGui.QLabel(self.alignment_groupBox)
        self.activeModel_label.setObjectName("activeModel_label")
        self.gridLayout.addWidget(self.activeModel_label, 1, 0, 1, 1)
        self.toImage_pushButton = QtGui.QPushButton(self.alignment_groupBox)
        self.toImage_pushButton.setObjectName("toImage_pushButton")
        self.gridLayout.addWidget(self.toImage_pushButton, 3, 1, 1, 1)
        self.toImage_label = QtGui.QLabel(self.alignment_groupBox)
        self.toImage_label.setObjectName("toImage_label")
        self.gridLayout.addWidget(self.toImage_label, 3, 0, 1, 1)
        self.fixImagePlane_checkBox = QtGui.QCheckBox(self.alignment_groupBox)
        self.fixImagePlane_checkBox.setObjectName("fixImagePlane_checkBox")
        self.gridLayout.addWidget(self.fixImagePlane_checkBox, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.alignment_groupBox)
        self.fiducialMarkers_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.fiducialMarkers_groupBox.setObjectName("fiducialMarkers_groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.fiducialMarkers_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fiducialMarker_comboBox = QtGui.QComboBox(self.fiducialMarkers_groupBox)
        self.fiducialMarker_comboBox.setObjectName("fiducialMarker_comboBox")
        self.gridLayout_3.addWidget(self.fiducialMarker_comboBox, 0, 1, 1, 1)
        self.fiducialMarkerLabels_label = QtGui.QLabel(self.fiducialMarkers_groupBox)
        self.fiducialMarkerLabels_label.setObjectName("fiducialMarkerLabels_label")
        self.gridLayout_3.addWidget(self.fiducialMarkerLabels_label, 0, 0, 1, 1)
        self.fiducialMarkerTransform_label = QtGui.QLabel(self.fiducialMarkers_groupBox)
        self.fiducialMarkerTransform_label.setObjectName("fiducialMarkerTransform_label")
        self.gridLayout_3.addWidget(self.fiducialMarkerTransform_label, 1, 0, 1, 1)
        self.fiducialMarkerTransform_pushButton = QtGui.QPushButton(self.fiducialMarkers_groupBox)
        self.fiducialMarkerTransform_pushButton.setObjectName("fiducialMarkerTransform_pushButton")
        self.gridLayout_3.addWidget(self.fiducialMarkerTransform_pushButton, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.fiducialMarkers_groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewAll_button = QtGui.QPushButton(self.frame)
        self.viewAll_button.setObjectName("viewAll_button")
        self.horizontalLayout_2.addWidget(self.viewAll_button)
        self.done_button = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_button.sizePolicy().hasHeightForWidth())
        self.done_button.setSizePolicy(sizePolicy)
        self.done_button.setObjectName("done_button")
        self.horizontalLayout_2.addWidget(self.done_button)
        self.verticalLayout.addWidget(self.frame)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.sceneviewer_widget = AlignmentSceneviewerWidget(MeshGeneratorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.horizontalLayout.addWidget(self.sceneviewer_widget)
        self.annotationPanel_dockWidget = QtGui.QDockWidget(MeshGeneratorWidget)
        self.annotationPanel_dockWidget.setObjectName("annotationPanel_dockWidget")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.annotation_treeWidget = QtGui.QTreeWidget(self.dockWidgetContents_2)
        self.annotation_treeWidget.setObjectName("annotation_treeWidget")
        self.gridLayout_5.addWidget(self.annotation_treeWidget, 0, 0, 1, 1)
        self.annotationPanel_dockWidget.setWidget(self.dockWidgetContents_2)
        self.horizontalLayout.addWidget(self.annotationPanel_dockWidget)

        self.retranslateUi(MeshGeneratorWidget)
        QtCore.QMetaObject.connectSlotsByName(MeshGeneratorWidget)

    def retranslateUi(self, MeshGeneratorWidget):
        MeshGeneratorWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Mesh Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.identifier_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Identifier", None, QtGui.QApplication.UnicodeUTF8))
        self.meshType_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Mesh type:", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteElementRanges_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Delete element ID ranges (e.g. 1,2-5,13):", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Scale x*y*z:", None, QtGui.QApplication.UnicodeUTF8))
        self.displayOptions_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Display options:", None, QtGui.QApplication.UnicodeUTF8))
        self.displayAxes_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Axes", None, QtGui.QApplication.UnicodeUTF8))
        self.displayLines_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Lines", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfaces_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Surfaces", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfacesExterior_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Exterior", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfacesTranslucent_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Transluc.", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfacesWireframe_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Wireframe", None, QtGui.QApplication.UnicodeUTF8))
        self.displayElementNumbers_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Element numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.displayNodeNumbers_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Node numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.displayNodeDerivatives_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Node derivatives", None, QtGui.QApplication.UnicodeUTF8))
        self.displayXiAxes_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Xi axes", None, QtGui.QApplication.UnicodeUTF8))
        self.displayImagePlane_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Image plane", None, QtGui.QApplication.UnicodeUTF8))
        self.displayFiducialMarkers_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Fiducial markers", None, QtGui.QApplication.UnicodeUTF8))
        self.time_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.timePlayStop_pushButton.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.timeValue_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Time value:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLoop_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.video_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Video:", None, QtGui.QApplication.UnicodeUTF8))
        self.frameIndex_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Frame index:", None, QtGui.QApplication.UnicodeUTF8))
        self.framesPerSecond_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Frames per second:", None, QtGui.QApplication.UnicodeUTF8))
        self.numFrames_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "# frames:", None, QtGui.QApplication.UnicodeUTF8))
        self.numFramesValue_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.alignment_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Alignment:", None, QtGui.QApplication.UnicodeUTF8))
        self.activeModel_comboBox.setItemText(0, QtGui.QApplication.translate("MeshGeneratorWidget", "Image Plane", None, QtGui.QApplication.UnicodeUTF8))
        self.activeModel_comboBox.setItemText(1, QtGui.QApplication.translate("MeshGeneratorWidget", "Generated Mesh", None, QtGui.QApplication.UnicodeUTF8))
        self.activeModel_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Active Model:", None, QtGui.QApplication.UnicodeUTF8))
        self.toImage_pushButton.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "To Image", None, QtGui.QApplication.UnicodeUTF8))
        self.toImage_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Align View:", None, QtGui.QApplication.UnicodeUTF8))
        self.fixImagePlane_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Fix image plane", None, QtGui.QApplication.UnicodeUTF8))
        self.fiducialMarkers_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Fiducial markers:", None, QtGui.QApplication.UnicodeUTF8))
        self.fiducialMarkerLabels_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Labels:", None, QtGui.QApplication.UnicodeUTF8))
        self.fiducialMarkerTransform_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Transform:", None, QtGui.QApplication.UnicodeUTF8))
        self.fiducialMarkerTransform_pushButton.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "To Scaffold", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAll_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self.done_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.annotationPanel_dockWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Annotation Panel", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.alignmentsceneviewerwidget import AlignmentSceneviewerWidget
