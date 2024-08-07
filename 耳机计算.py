import math
import tkinter as tk
from tkinter import ttk

def dbfs_to_dbspl(dbfs_value, sensitivity_db_spl_mw):
    """
    将 dBFS 转换为 dBSPL。

    :param dbfs_value: dBFS 值
    :param sensitivity_db_spl_mw: 耳机灵敏度 (dB SPL/mW)
    :return: 实际 dBSPL 值
    """
    output_power_mw = 10 ** (dbfs_value / 10.0)
    actual_dbspl = sensitivity_db_spl_mw + 10 * math.log10(output_power_mw)
    return actual_dbspl

def dbspl_to_dbfs(desired_dbspl, sensitivity_db_spl_mw):
    """
    将目标 dBSPL 转换为 dBFS。

    :param desired_dbspl: 目标 dBSPL 值
    :param sensitivity_db_spl_mw: 耳机灵敏度 (dB SPL/mW)
    :return: 所需的 dBFS 值
    """
    required_output_power_mw = 10 ** ((desired_dbspl - sensitivity_db_spl_mw) / 10.0)
    required_dbfs = 10 * math.log10(required_output_power_mw)
    return required_dbfs

def calculate_dbspl():
    dbfs_value = float(dbfs_entry.get())
    sensitivity = float(sensitivity_entry.get())
    dbspl = dbfs_to_dbspl(dbfs_value, sensitivity)
    result_label.config(text=f"实际 dBSPL 值: {dbspl:.2f} dB SPL")

def calculate_dbfs():
    desired_dbspl = float(target_dbspl_entry.get())
    sensitivity = float(sensitivity_entry.get())
    dbfs = dbspl_to_dbfs(desired_dbspl, sensitivity)
    result_label.config(text=f"所需的 dBFS 值: {dbfs:.2f} dBFS")

# 创建主窗口
root = tk.Tk()
root.title("dBFS 和 dBSPL 计算器")

# 创建说明标签
explanation_label = tk.Label(root, text="dBFS 是指相对于满刻度的分贝值，用于表示数字音频信号的电平。\n"
                                        "dBSPL 是指声压级，用于表示声压的强度，以20 µPa为基准。\n"
                                        "此工具可计算给定 dBFS 的实际声压级或达到目标声压级所需的 dBFS。")
explanation_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# 创建输入框和标签
tk.Label(root, text="dBFS 值:").grid(row=1, column=0, padx=10, pady=5)
dbfs_entry = tk.Entry(root)
dbfs_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="耳机灵敏度 (dB SPL/mW):").grid(row=2, column=0, padx=10, pady=5)
sensitivity_entry = tk.Entry(root)
sensitivity_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="目标 dBSPL 值:").grid(row=3, column=0, padx=10, pady=5)
target_dbspl_entry = tk.Entry(root)
target_dbspl_entry.grid(row=3, column=1, padx=10, pady=5)

# 创建按钮
calculate_dbspl_button = ttk.Button(root, text="计算实际 dBSPL", command=calculate_dbspl)
calculate_dbspl_button.grid(row=4, column=0, padx=10, pady=10)

calculate_dbfs_button = ttk.Button(root, text="计算所需 dBFS", command=calculate_dbfs)
calculate_dbfs_button.grid(row=4, column=1, padx=10, pady=10)

# 创建结果标签
result_label = tk.Label(root, text="结果将在此显示")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 启动主循环
root.mainloop()
