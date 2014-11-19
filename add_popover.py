from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Add_Popover(Gtk.Window):

    def __init__(self, page, data):
        #Initialize Data
        self.data = data
        # Create Widgets
        self.addGrid = Gtk.Grid()
        if page == "window":
            self.addIncomeRadio = Gtk.RadioButton(None, "Income")
            self.addExpenseRadio = Gtk.RadioButton(self.addIncomeRadio, "Expense")
            self.addStack = Gtk.Stack()
            self.addStackSwitcher = Gtk.StackSwitcher()
            self.addStack.add_titled(self.addIncomeRadio, "Income", "Income")
            self.addStack.add_titled(self.addExpenseRadio, "Expense", "Expense")
            self.addStackSwitcher.set_stack(self.addStack)
        self.addCategoryComboBoxText = Gtk.ComboBoxText()
        self.addEntryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.addEntryLabel = Gtk.Label("Entry")
        self.addDescriptionLabel = Gtk.Label("Description")
        self.addCurrencyLabel = Gtk.Label("$ ")
        self.addEntry = Gtk.Entry()
        self.addDescription = Gtk.Entry()
        self.addDate = Gtk.Calendar()
        self.addSubmitButton = Gtk.Button("Submit")
        
        self.addEntryBox.add(self.addCurrencyLabel)
        self.addEntryBox.add(self.addEntry)
        
        # Style Widgets
        if page == "window":
            self.addStackSwitcher.set_homogeneous(True)
            self.addStack.set_hexpand(True)        
            self.add_popover_margin(self.addStackSwitcher, 10)
        
        self.add_popover_margin(self.addCategoryComboBoxText, 10)
        self.add_popover_margin(self.addEntryBox, 10)
        self.add_popover_margin(self.addDescription, 10)
        self.addEntryBox.set_margin_top(0)
        self.addEntryBox.set_margin_end(4)
        self.addDescription.set_margin_top(0)
        self.addDescription.set_margin_start(4)
        self.add_popover_margin(self.addDate, 10)
        self.add_popover_margin(self.addSubmitButton, 10)

        self.addCategoryComboBoxText.set_property("height-request", 34)

        if page == "window" or page == "income":
            self.radioStatus = "income"
            for i in range(1,len(self.data.incomeMenu)):
                self.addCategoryComboBoxText.append_text(self.data.incomeMenu[i][1])
        
        if page == "expense":
            self.radioStatus = "expense"
            for i in range(1,len(self.data.expenseMenu)):
                self.addCategoryComboBoxText.append_text(self.data.expenseMenu[i][1])
        
        # Connect Widget Handlers
        if page == "window":
            self.addStackSwitcher.connect("set-focus-child", self.on_addRadio_toggled)
        
        # Add Widgets to Grid
        if page == "window":
            self.addGrid.attach(self.addStackSwitcher,0,0,2,1)
        
        self.addGrid.attach(self.addCategoryComboBoxText,0,1,2,1)
        self.addGrid.attach(self.addEntryLabel,0,2,1,1)
        self.addGrid.attach(self.addDescriptionLabel,1,2,1,1)
        self.addGrid.attach(self.addEntryBox,0,3,1,1)
        self.addGrid.attach(self.addDescription,1,3,1,1)
        self.addGrid.attach(self.addDate,0,4,2,1)
        self.addGrid.attach(self.addSubmitButton,0,5,2,1)
        self.addSubmitButton.connect("clicked", self.on_addSubmitButton_clicked)
    
    def add_popover_margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_end(margin)
        widget.set_margin_bottom(margin)
    
    def on_addButton_clicked(self, button, addPopover):
        if addPopover.get_visible():
            addPopover.hide()
        else:
            addPopover.show_all()

    def on_addRadio_toggled(self, *args):
        if args[1] != None:
            for i in range(0, len(self.data.incomeMenu) + len(self.data.expenseMenu)):
                self.addCategoryComboBoxText.remove(0)
            if args[1].get_group()[0].get_active():
                self.radioStatus = "income"
                for i in range(1,len(self.data.incomeMenu)):
                    self.addCategoryComboBoxText.append_text(self.data.incomeMenu[i][1])
            if args[1].get_group()[1].get_active():
                self.radioStatus = "expense"
                for i in range(1,len(self.data.expenseMenu)):
                    self.addCategoryComboBoxText.append_text(self.data.expenseMenu[i][1])
    
    def on_addSubmitButton_clicked(self, *args):
        print(self.radioStatus)
        print(self.addCategoryComboBoxText.get_active_text())
        print(self.addEntry.get_text())
        print(self.addDescription.get_text())
        print(self.addDate.get_date())