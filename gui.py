from tkinter import StringVar, Tk, ttk, filedialog, messagebox as msg
import payroll

class my_app():

    def __init__(self):
        # ---------------
        # window property
        # ---------------
        self.root = Tk()
        self.root.title('DSC to MYOB')
        # ---------------
        # window widgets
        # ---------------
        # Import Button
        self.import_b = ttk.Button(self.root,text='Import File',command=lambda:self.open_file())
        self.import_b.grid(row=0, column=0, sticky="NS", padx=50)
        self.import_sv = StringVar()
        self.import_l = ttk.Label(self.root, textvariable=self.import_sv)
        self.import_l.grid(row=0, column=1, sticky="NS")
        # Convert to Timesheet Button
        self.timesheet_b = ttk.Button(self.root, text='Convert To Timesheet File', command=lambda: self.convert_timesheet_file())
        self.timesheet_b.grid(row=1, column=2, sticky="NS", padx=50)
        self.timesheet_sv = StringVar()
        self.timesheet_l = ttk.Label(self.root, textvariable=self.timesheet_sv)
        self.timesheet_l.grid(row=1, column=3, sticky="NS")
        # Entry boxes
        # self.start_sv = StringVar()
        # self.end_sv = StringVar()
        # self.inv_sv = StringVar()
        # self.e_start = ttk.Entry(self.root, textvariable=self.start_sv)
        # self.e_end = ttk.Entry(self.root, textvariable=self.end_sv)
        # self.e_inv = ttk.Entry(self.root, textvariable=self.inv_sv)
        # self.l_start = ttk.Label(self.root, text='Start Date')
        # self.l_end = ttk.Label(self.root, text='End Date')
        # self.l_inv  = ttk.Label(self.root, text='Invoice Date')
        # self.e_start.grid(row=4, column=0, sticky="NS")
        # self.e_end.grid(row=4, column=1, sticky="NS")
        # self.e_inv.grid(row=4, column=2, sticky="NS")
        # self.l_start.grid(row=3, column=0, sticky="NS")
        # self.l_end.grid(row=3, column=1, sticky="NS")
        # self.l_inv.grid(row=3, column=2, sticky="NS")
        # ---------------
        # data containers
        # ---------------
        self.state = []
        self.raw_data = []
        self.detailed_processed_data = []
        self.summary_processed_data = []
        self.clients_data = []

    def open_file(self):
        # get path of csv file and initializes data containers
        self.import_sv.set(filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*"))))
        self.raw_data = payroll.data_to_csv(self.import_sv.get())
        if not self.raw_data:
            msg.showerror(title='Invalid Import', message='Import cannot be loaded. Mismatch on the data headers')
        self.state = []

    def convert_timesheet_file(self):
        if 'Process File' not in self.state:
            self.state.append('Process File')
            payroll.process_data(self.raw_data)


if __name__ == '__main__':
    app = my_app()
    app.root.mainloop()
