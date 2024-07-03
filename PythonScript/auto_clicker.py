 import pyautogui
import time
import tkinter as tk
from tkinter import ttk

# 延迟函数，用于在指定延迟后获取鼠标位置
def get_mouse_position_after_delay(delay):
    time.sleep(delay)
    x, y = pyautogui.position()
    return x, y

# 自动点击函数，在指定位置执行自动化点击
def click_at_position(x, y, interval, click_count, total_duration, between_rounds_interval):
    start_time = time.time()
    while time.time() - start_time < total_duration and running:
        for _ in range(click_count):
            pyautogui.click(x, y)
            time.sleep(interval)
        time.sleep(between_rounds_interval)

# 启动自动化点击操作
def start_clicking():
    global running
    running = True
    delay_seconds = float(delay_entry.get())
    interval = float(interval_entry.get())
    click_count = int(click_count_entry.get())
    total_duration = float(total_duration_entry.get())
    between_rounds_interval = float(between_rounds_interval_entry.get())

    position = get_mouse_position_after_delay(delay_seconds)
    x_position = position[0]
    y_position = position[1]

    click_at_position(x_position, y_position, interval, click_count, total_duration, between_rounds_interval)

# 停止自动化点击操作
def stop_clicking():
    global running
    running = False

# 创建tkinter窗口
root = tk.Tk()
root.title("自动点击器")

# 创建并放置组件
delay_label = ttk.Label(root, text="延迟秒数:")
delay_label.grid(row=0, column=0, padx=10, pady=5)
delay_entry = ttk.Entry(root)
delay_entry.grid(row=0, column=1, padx=10, pady=5)

interval_label = ttk.Label(root, text="点击间隔:")
interval_label.grid(row=1, column=0, padx=10, pady=5)
interval_entry = ttk.Entry(root)
interval_entry.grid(row=1, column=1, padx=10, pady=5)

click_count_label = ttk.Label(root, text="点击次数:")
click_count_label.grid(row=2, column=0, padx=10, pady=5)
click_count_entry = ttk.Entry(root)
click_count_entry.grid(row=2, column=1, padx=10, pady=5)

total_duration_label = ttk.Label(root, text="总持续时间:")
total_duration_label.grid(row=3, column=0, padx=10, pady=5)
total_duration_entry = ttk.Entry(root)
total_duration_entry.grid(row=3, column=1, padx=10, pady=5)

between_rounds_interval_label = ttk.Label(root, text="每轮间隔:")
between_rounds_interval_label.grid(row=4, column=0, padx=10, pady=5)
between_rounds_interval_entry = ttk.Entry(root)
between_rounds_interval_entry.grid(row=4, column=1, padx=10, pady=5)

start_button = ttk.Button(root, text="开始", command=start_clicking)
start_button.grid(row=5, column=0, padx=10, pady=10)

stop_button = ttk.Button(root, text="停止", command=stop_clicking)
stop_button.grid(row=5, column=1, padx=10, pady=10)

# 初始化运行标志
running = False

# 运行tkinter主循环
root.mainloop()
