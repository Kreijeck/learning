from PySide2 import QtWidgets
import sys
import os

from DLTAnalyzer.HU.testcases import coredump_check
from DLTAnalyzer.UI.HU_mainWidget_Designer import Ui_frm_main
import DLTAnalyzer.HU.config.path_handler as ph

import DLTAnalyzer.Utilities.File_Converter as converter

from DLTAnalyzer.UI.Gui_Logger import GuiLogger
from DLTAnalyzer.Utilities.settingsFile import SettingsFileHU

from DLTAnalyzer.HU.testcases import *

import pandas as pd
import configparser

class MainWidget(QtWidgets.QWidget):
    """
    Starting Main Window for the HU-Analyze
    * all buttons
    * gui-logger
    * pathHandler
    *settings file
    * Pandas Dataframe
    are in
    """
    def __init__(self, parent=None):
        #Initialize auto generated Window
        super().__init__(parent)
        self.ui = Ui_frm_main()
        self.ui.setupUi(self)

        self.setWindowTitle("HU-DLT-Analyzer")
        self.ui.txt_input.setReadOnly(True)
        self.ui.txt_destination.setReadOnly(True)

        #Initialize Dataframe
        self.csv_df = pd.DataFrame()

        #Initialize Logger
        setting_reader = SettingsFileHU()
        try:
            loglevel_gui = setting_reader.read('logging', 'loglevel_gui')
            loglevel_stream = setting_reader.read('logging', 'loglevel_stream')
        except configparser.NoSectionError:
            #set default loglevel, when no settings.ini exist
            loglevel_gui = 20
            loglevel_stream = 10

        self.hu_logger = GuiLogger(loglevel_gui=loglevel_gui, loglevel_stream=loglevel_stream)
        self.hu_logger = self.hu_logger.add_logger("main", self.ui.txt_logger)

        #Initialize Pathhandler, ButtonAction and Settings
        self.setting = SettingsFileHU(logger=self.hu_logger)
        # write hu_settings if they don't exist
        self.setting.write_hu_settings(force=False)
        self.path_handler = ph.PathHandler(self.hu_logger)
        self.btn_action = ButtonAction(self)


        #Initialize button_on_click events
        self.ui.btn_performance.clicked.connect(self.on_click_performance)
        self.ui.btn_spam_check.clicked.connect(self.on_click_spam_check)
        self.ui.btn_error_logs.clicked.connect(self.on_click_default_logs)
        self.ui.btn_client_server.clicked.connect(self.on_click_client_server_check)
        self.ui.btn_fps_check.clicked.connect(self.on_click_fps_check)
        self.ui.btn_core_dump_check.clicked.connect(self.on_click_core_dump_check)
        self.ui.btn_imu_check.clicked.connect(self.on_click_imu_check)
        self.ui.btn_wpc_check.clicked.connect(self.on_click_wpc_check)
        self.ui.btn_imu_wpc_interactive_plots.clicked.connect(self.on_click_imu_wpc_interactive_plots)
        self.ui.btn_get_it_all.clicked.connect(self.on_click_get_it_all)
        self.ui.btn_arc_imu_calibration.clicked.connect(self.on_click_arc_imu_calibration)
        self.ui.btn_video_signal.clicked.connect(self.on_click_video_signal)

        self.ui.dlg_open_read_file.clicked.connect(self.on_click_dlg_open_file)
        self.ui.dlg_choose_destination.clicked.connect(self.on_click_choose_destination)

        self.ui.txt_destination.setText(self.path_handler.destination_path)
        self.ui.lbl_success_read.setStyleSheet("background-color: rgb(0,200,50)")
        self.enableButtons(False)

    def enableButtons(self, bool):
        """
        bool: Enable/disable all buttons for Analysis
        """
        buttons = [self.ui.btn_spam_check,
                   self.ui.btn_performance,
                   self.ui.btn_get_it_all,
                   self.ui.btn_error_logs,
                   self.ui.btn_client_server,
                   self.ui.btn_fps_check,
                   self.ui.btn_core_dump_check,
                   self.ui.btn_imu_check,
                   self.ui.btn_wpc_check,
                   self.ui.btn_imu_wpc_interactive_plots,
                   self.ui.btn_arc_imu_calibration,
                   self.ui.btn_video_signal]
        for button in buttons:
            button.setEnabled(bool)
        self.ui.lbl_success_read.setVisible(bool)


    ### On Click Methods ###
    def on_click_performance(self):
        augmented_performance.tc_get_performance_diagram(self.csv_df, self.hu_logger, self.path_handler)

        self.hu_logger.info("Diagram for Performance are created in: {0}".format(self.path_handler.destination_path))

    def on_click_spam_check(self):
        augmented_spamcheck.tc_spam_check(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_default_logs(self):
        augmented_log_messages.tc_augmented_log_msg(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_client_server_check(self):
        augmented_client_server_check.tc_client_server_check(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_fps_check(self):
        fps_check.tc_check_fps(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_core_dump_check(self):
        coredump_check.tc_check_core_dumps(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_imu_check(self):
        imu_check.tc_check_imu(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_wpc_check(self):
        wpc_check.tc_check_wpc(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_imu_wpc_interactive_plots(self):
        imu_wpc_interactive_plots.tc_imu_wpc_interactive_plots(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_arc_imu_calibration(self):
        arc_imu_calibration.tc_check_arc_imu_calibration(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_video_signal(self):
        video_signal_check.tc_video_signal(csv_df=self.csv_df, hu_logger=self.hu_logger, path_handler=self.path_handler)

    def on_click_get_it_all(self):
        self.hu_logger.info("Run all Testcases in suite...")
        self.on_click_performance()
        self.on_click_spam_check()
        self.on_click_default_logs()
        self.on_click_client_server_check()
        self.on_click_fps_check()
        self.on_click_imu_check()
        self.on_click_core_dump_check()
        self.on_click_imu_wpc_interactive_plots()
        self.on_click_wpc_check()
        self.on_click_arc_imu_calibration()
        self.on_click_video_signal()

    def on_click_dlg_open_file(self):
        """
        choose a .csv/dlt File and load it as a Dataframe
        add all relevant paths to the path-handler
        """
        self.enableButtons(False)

        #Start Dialog Manager for File
        start_dir = self.path_handler.source_path
        currentPath = self.btn_action.openFileDialog(start_dir)

        #setPathToHandler
        self.path_handler.set_paths(currentPath)

        # convert convert_dlt and set new path
        if self.path_handler.extension == "dlt":
            print(self.setting.read('paths', 'dlt_viewer_exe'))
            dlt_exe = self.setting.read('paths', 'dlt_viewer_exe')
            try:
                self.path_handler.set_paths(converter.convert_dlt(dlt_exe, self.path_handler.complete_path))
            except:
                self.hu_logger.error("Can't convert DLT-File, do you have the right version and path?")
                self.path_handler.set_paths("")

        #write current path to input
        self.ui.txt_input.setText(self.path_handler.complete_path)

        # Create Pandas Dataframe if valid File
        if self.path_handler.extension == "csv":
            self.csv_df = self.btn_action.createDataframe(self.path_handler.complete_path)

        #Enable Buttons if .csv was converted
        if len(self.csv_df) != 0:
            self.enableButtons(True)


    def on_click_choose_destination(self):
        dest_dir = self.ui.txt_destination.text()
        folder = self.btn_action.openDirectoryDialog(dest_dir)
        self.ui.txt_destination.setText(folder)
        self.path_handler.setDestinationPath(folder)
        self.hu_logger.info("All result files are written in: {0}".format(self.path_handler.destination_path))

class ButtonAction:
    """
    Action - Methods for on_button_click
    """
    def __init__(self, MainWidget):
        self.hu_logger = MainWidget.hu_logger

    def openFileDialog(self, start_dir):
        chosen_path = ""
        try:
            file_dialog = QtWidgets.QFileDialog
            chosen_path, _ = file_dialog.getOpenFileName(None,
                                                           caption="Select CSV-File",
                                                           dir=start_dir,
                                                           filter="all available Files (*.csv *.dlt);;"
                                                                  "CSV Files (*.csv);;"
                                                                  "DLT Files (*.dlt)")
            #for winsystem use \
            chosen_path = os.path.abspath(chosen_path)
        except Exception as e:
            self.hu_logger.error("Uuups, can't open the chosen File!")

        return chosen_path

    def openDirectoryDialog(self, start_dir):
        chosen_folder = ""
        try:
            chosen_folder = os.path.abspath(QtWidgets.QFileDialog.getExistingDirectory(None,
                                                                       caption="Select Directory",
                                                                       dir=start_dir))
            self.hu_logger.debug("New Result Folder: {}".format(chosen_folder))
        except:
            self.hu_logger.error("Can't open the folder, try again please")

        #if the dialog has been canceled write again the start_destination
        if chosen_folder != "":
            folder = chosen_folder
        else:
            folder = start_dir

        return folder

    def createDataframe(self, path):
        df = pd.DataFrame()

        if path.endswith(".csv"):
            #Create Dataframe
            try:
                df = converter.csv2pandasDf(path)
                self.hu_logger.info("File {} successfully read in".format(path))
                self.hu_logger.debug("File {} successfully parsed in a pandas.dataframe".format(path))
            except Exception as e:
                self.hu_logger.error("Can't read the csv-File...{0}".format(e))
        else:
            self.hu_logger.warning("No File is loaded!")

        return df


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    start = MainWidget()
    start.show()
    start.hu_logger.info("Started the HU-Analyzer")

    sys.exit(app.exec_())
