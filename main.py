import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class SmartSecurity:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Security System")
        self.root.geometry("1050x700")
        self.root.configure(bg="#101827")
        self.root.minsize(850, 600)

        self.armed = False
        self.alarm_active = False

        self.sensors = {
            "Voordeur": "Gesloten",
            "Achterdeur": "Gesloten",
            "Raam woonkamer": "Gesloten",
            "Bewegingssensor": "Geen beweging"
        }

        self.create_interface()
        self.update_clock()

    def create_interface(self):


        header = tk.Frame(
            self.root, bg="#172338", height=85
        )
        header.pack(fill="x")

        tk.Label(
            header,
            text="SMART SECURITY",
            font=("Arial", 23, "bold"),
            fg="#38bdf8",
            bg="#172338"
        ).pack(side="left", padx=25, pady=20)

        self.clock = tk.Label(
            header,
            text="",
            font=("Arial", 12),
            fg="white",
            bg="#172338"
        )
        self.clock.pack(side="right", padx=25)


        main = tk.Frame(self.root, bg="#101827")
        main.pack(fill="both", expand=True, padx=20, pady=20)


        status_frame = tk.LabelFrame(
            main,
            text=" Beveiligingsstatus ",
            font=("Arial", 12, "bold"),
            bg="#172338",
            fg="white",
            padx=20,
            pady=15
        )
        status_frame.pack(fill="x", pady=10)

        self.status_label = tk.Label(
            status_frame,
            text="SYSTEEM UITGESCHAKELD",
            font=("Arial", 20, "bold"),
            fg="#f87171",
            bg="#172338"
        )
        self.status_label.pack(pady=10)

        controls = tk.Frame(status_frame, bg="#172338")
        controls.pack(pady=10)

        tk.Button(
            controls,
            text="INSCHAKELEN",
            command=self.arm_system,
            bg="#16a34a",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
            pady=10
        ).pack(side="left", padx=10)

        tk.Button(
            controls,
            text="UITSCHAKELEN",
            command=self.disarm_system,
            bg="#dc2626",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
            pady=10
        ).pack(side="left", padx=10)

        # Sensor section
        sensor_frame = tk.LabelFrame(
            main,
            text=" Sensoren ",
            font=("Arial", 12, "bold"),
            bg="#172338",
            fg="white",
            padx=15,
            pady=15
        )
        sensor_frame.pack(fill="x", pady=10)

        self.sensor_labels = {}

        for name, state in self.sensors.items():

            row = tk.Frame(sensor_frame, bg="#172338")
            row.pack(fill="x", pady=6)

            tk.Label(
                row,
                text=name,
                font=("Arial", 12),
                fg="white",
                bg="#172338",
                width=25,
                anchor="w"
            ).pack(side="left")

            label = tk.Label(
                row,
                text=state,
                font=("Arial", 11, "bold"),
                fg="#4ade80",
                bg="#172338"
            )
            label.pack(side="left", padx=20)

            self.sensor_labels[name] = label

            if name != "Bewegingssensor":
                tk.Button(
                    row,
                    text="Simuleer opening",
                    command=lambda n=name: self.open_sensor(n),
                    bg="#334155",
                    fg="white"
                ).pack(side="right")

            else:
                tk.Button(
                    row,
                    text="Simuleer beweging",
                    command=self.detect_motion,
                    bg="#334155",
                    fg="white"
                ).pack(side="right")

        # Alarm section
        alarm_frame = tk.Frame(main, bg="#172338")
        alarm_frame.pack(fill="x", pady=10)

        self.alarm_label = tk.Label(
            alarm_frame,
            text="ALARM: INACTIEF",
            font=("Arial", 16, "bold"),
            fg="#4ade80",
            bg="#172338",
            pady=15
        )
        self.alarm_label.pack()

        tk.Button(
            alarm_frame,
            text="Alarm resetten",
            command=self.reset_alarm,
            bg="#475569",
            fg="white",
            pady=7
        ).pack(pady=5)

        # Event log
        log_frame = tk.LabelFrame(
            main,
            text=" Gebeurtenissen / Logboek ",
            font=("Arial", 12, "bold"),
            bg="#172338",
            fg="white",
            padx=10,
            pady=10
        )
        log_frame.pack(fill="both", expand=True, pady=10)

        self.log = tk.Text(
            log_frame,
            height=8,
            bg="#0f172a",
            fg="#e2e8f0",
            font=("Consolas", 10),
            state="disabled"
        )
        self.log.pack(fill="both", expand=True)

        self.add_log("Smart Security systeem gestart.")

    def add_log(self, message):

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.log.config(state="normal")
        self.log.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )
        self.log.see("end")
        self.log.config(state="disabled")

    def arm_system(self):

        if self.alarm_active:
            messagebox.showwarning(
                "Alarm actief",
                "Reset eerst het alarm."
            )
            return

        self.armed = True

        self.status_label.config(
            text="SYSTEEM INGESCHAKELD",
            fg="#4ade80"
        )

        self.add_log("Beveiligingssysteem ingeschakeld.")

    def disarm_system(self):

        self.armed = False
        self.alarm_active = False

        self.status_label.config(
            text="SYSTEEM UITGESCHAKELD",
            fg="#f87171"
        )

        self.alarm_label.config(
            text="ALARM: INACTIEF",
            fg="#4ade80"
        )

        self.add_log("Beveiligingssysteem uitgeschakeld.")

    def open_sensor(self, name):

        self.sensors[name] = "Geopend"

        self.sensor_labels[name].config(
            text="GEOPEND",
            fg="#f87171"
        )

        self.add_log(f"{name}: opening gedetecteerd.")

        if self.armed:
            self.trigger_alarm(name)

    def detect_motion(self):

        self.sensors["Bewegingssensor"] = "Beweging gedetecteerd"

        self.sensor_labels["Bewegingssensor"].config(
            text="BEWEGING",
            fg="#f87171"
        )

        self.add_log("Bewegingssensor: beweging gedetecteerd.")

        if self.armed:
            self.trigger_alarm("Bewegingssensor")

        # Simulatie automatisch herstellen
        self.root.after(
            5000,
            self.reset_motion
        )

    def reset_motion(self):

        self.sensors["Bewegingssensor"] = "Geen beweging"

        self.sensor_labels["Bewegingssensor"].config(
            text="Geen beweging",
            fg="#4ade80"
        )

    def trigger_alarm(self, source):

        self.alarm_active = True

        self.alarm_label.config(
            text="!!! ALARM ACTIEF !!!",
            fg="#ef4444"
        )

        self.status_label.config(
            text="WAARSCHUWING: INBRAAKALARM",
            fg="#ef4444"
        )

        self.add_log(
            f"WAARSCHUWING: Alarm geactiveerd door {source}!"
        )

        messagebox.showwarning(
            "SMART SECURITY ALARM",
            f"Waarschuwing!\n\nActiviteit gedetecteerd: {source}"
        )

    def reset_alarm(self):

        self.alarm_active = False

        self.alarm_label.config(
            text="ALARM: INACTIEF",
            fg="#4ade80"
        )

        if self.armed:
            self.status_label.config(
                text="SYSTEEM INGESCHAKELD",
                fg="#4ade80"
            )
        else:
            self.status_label.config(
                text="SYSTEEM UITGESCHAKELD",
                fg="#f87171"
            )

        self.add_log("Alarm handmatig gereset.")

    def update_clock(self):

        now = datetime.now().strftime(
            "%d-%m-%Y | %H:%M:%S"
        )

        self.clock.config(text=now)

        self.root.after(1000, self.update_clock)


if __name__ == "__main__":

    root = tk.Tk()
    app = SmartSecurity(root)
    root.mainloop()
