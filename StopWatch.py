import time
import tkinter as tk


class StopwatchApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x160")
        self.root.resizable(False, False)

        self.running = False
        self.start_time = 0.0
        self.elapsed_time = 0.0

        # Time display label
        self.time_label = tk.Label(
            root, text="00:00:00.00", font=("Helvetica", 30, "bold"), pady=20
        )
        self.time_label.pack()

        # Button container
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(
            btn_frame, text="Start", width=8, command=self.start
        )
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(
            btn_frame, text="Stop", width=8, command=self.stop
        )
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(
            btn_frame, text="Reset", width=8, command=self.reset
        )
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update_timer(self):
        if self.running:
            current_elapsed = self.elapsed_time + (
                time.perf_counter() - self.start_time
            )
            self.display_time(current_elapsed)
            self.root.after(10, self.update_timer)

    def display_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        self.time_label.config(
            text=f"{int(hours):02d}:{int(mins):02d}:{secs:05.2f}"
        )

    def start(self):
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True
            self.update_timer()

    def stop(self):
        if self.running:
            self.elapsed_time += time.perf_counter() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0.0
        self.display_time(0.0)


if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
