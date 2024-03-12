import tkinter as tk

# Can make this extend TopLevel to have a popup window
class NoteEntry(tk.Frame):
    """ A 'megawidget' for entering note details """

    def __init__(self, parent, notebutton, **kwargs):
        super().__init__(parent, **kwargs) 

        self._note_button = notebutton

        self._memo_label = tk.Label(self, text="Memo:")
        self._memo_label.grid(row=1, column=1)
        self._memo_entry = tk.Entry(self)
        self._memo_entry.grid(row=2, column=1)

        self._tags_label = tk.Label(self, text="Tags:")
        self._tags_label.grid(row=1, column=2)
        self._tags_entry = tk.Entry(self)
        self._tags_entry.grid(row=2, column=2)

        if self._note_button:
            self._enter_button = tk.Button(
                self, text="Enter", command=self.modify_callback)
        self._enter_button.grid(row=2, column=3)

    def modify_callback(self):
        self._note_button.update_memo(self._memo_entry.get())
        self._note_button.update_tags(self._tags_entry.get())
        
        
        self._note_button.update()
        self._note_button.pack()
        self.destroy()



    # def destroy(self) -> None:
    #     self._memo_label.destroy()
    #     self._memo_entry.destroy()
    #     self._tags_entry.destroy()
    #     self._tags_label.destroy()
    #     self._enter_button.destroy()
    #     return super().destroy()
        