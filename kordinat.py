import customtkinter as ctk
import pyautogui
import mouse

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class CoordinateTrackerApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Koordinat Takip")
        self.app.geometry("360x520")
        self.app.resizable(False, False)

        self.is_tracking = False
        self.click_count = 1

        self.title = ctk.CTkLabel(
            self.app,
            text="KOORDİNAT TAKİP",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title.pack(pady=20)

        self.card = ctk.CTkFrame(self.app, corner_radius=22)
        self.card.pack(padx=20, pady=10, fill="x")

        self.coord_label = ctk.CTkLabel(
            self.card,
            text="X: -   Y: -",
            height=40,
            font=ctk.CTkFont(size=16)
        )
        self.coord_label.pack(pady=15)

        self.btn_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.btn_frame.pack(pady=15)

        self.start_btn = ctk.CTkButton(
            self.btn_frame,
            text="BAŞLAT",
            width=140,
            height=50,
            corner_radius=25,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.start_tracking
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = ctk.CTkButton(
            self.btn_frame,
            text="DURDUR",
            width=140,
            height=50,
            corner_radius=25,
            fg_color="#aa3333",
            hover_color="#882222",
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.stop_tracking,
            state="disabled"
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.list_label = ctk.CTkLabel(
            self.app,
            text="Kaydedilen Koordinatlar",
            font=ctk.CTkFont(size=14)
        )
        self.list_label.pack(pady=(10, 0))

        self.listbox = ctk.CTkTextbox(
            self.app,
            height=150,
            corner_radius=12
        )
        self.listbox.pack(padx=20, pady=10, fill="x")
        self.listbox.configure(state="disabled")

        self.info = ctk.CTkLabel(
            self.app,
            text="Ekranın herhangi bir yerine tıklayarak koordinat kaydedebilirsin",
            font=ctk.CTkFont(size=11),
            text_color="gray",
            wraplength=300
        )
        self.info.pack(pady=10)

        mouse.on_click(self.on_mouse_click)

        self.app.mainloop()

    def start_tracking(self):
        self.is_tracking = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.update_coordinates()

    def stop_tracking(self):
        self.is_tracking = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")

    def update_coordinates(self):
        if not self.is_tracking:
            return

        x, y = pyautogui.position()
        self.coord_label.configure(text=f"X: {x}   Y: {y}")
        self.app.after(100, self.update_coordinates)

    def on_mouse_click(self):
        if not self.is_tracking:
            return

        x, y = pyautogui.position()
        self.app.after(0, self.add_coordinate, x, y)

    def add_coordinate(self, x, y):
        self.listbox.configure(state="normal")
        self.listbox.insert("end", f"{self.click_count}. X: {x}, Y: {y}\n")
        self.listbox.configure(state="disabled")
        self.listbox.see("end")
        self.click_count += 1

if __name__ == "__main__":
    CoordinateTrackerApp()
