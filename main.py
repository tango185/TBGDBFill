from ttkthemes import themed_tk as tk
from AddCard import *

window = tk.ThemedTk()
window.get_themes()
window.set_theme("plastik")
my_win = AddCard(window)
window.title("wwesctbgfill")
window.geometry("400x325+10+10")
window.mainloop()
