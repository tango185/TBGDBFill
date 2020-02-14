from AddCard import *

window = tk.ThemedTk()
window.get_themes()
window.set_theme("plastik")
my_win = AddCard(window)
window.title("TBGCalc - Add Card")
window.geometry("400x375+10+10")
window.mainloop()
