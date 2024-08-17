import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def dbfs_to_dbspl(dbfs_value, sensitivity_db_spl_mw):
    """
    将 dBFS 转换为 dBSPL。
    
    :param dbfs_value: dBFS 值
    :param sensitivity_db_spl_mw: 耳机灵敏度 (dB SPL/mW)
    :return: 实际 dBSPL 值
    """
    output_power_mw = 10 ** (dbfs_value / 10.0)  # 将 dBFS 转换为输出功率 (mW)
    actual_dbspl = sensitivity_db_spl_mw + 10 * math.log10(output_power_mw)  # 根据输出功率计算 dBSPL
    return actual_dbspl

def dbspl_to_dbfs(desired_dbspl, sensitivity_db_spl_mw):
    """
    将目标 dBSPL 转换为 dBFS。
    
    :param desired_dbspl: 目标 dBSPL 值
    :param sensitivity_db_spl_mw: 耳机灵敏度 (dB SPL/mW)
    :return: 所需的 dBFS 值
    """
    required_output_power_mw = 10 ** ((desired_dbspl - sensitivity_db_spl_mw) / 10.0)  # 根据目标 dBSPL 计算所需输出功率
    required_dbfs = 10 * math.log10(required_output_power_mw)  # 根据输出功率计算所需 dBFS
    return required_dbfs

def validate_input(value):
    """
    验证用户输入是否为有效数字。
    
    :param value: 用户输入的字符串
    :return: 转换后的浮点数或 None（如果输入无效）
    """
    try:
        return float(value)  # 尝试将输入转换为浮点数
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字")  # 如果转换失败，显示错误提示
        return None

def calculate_dbspl():
    """
    计算实际的 dBSPL 值并显示在界面上。
    """
    dbfs_value = validate_input(dbfs_entry.get())
    sensitivity = validate_input(sensitivity_entry.get())
    if dbfs_value is not None and sensitivity is not None:
        dbspl = dbfs_to_dbspl(dbfs_value, sensitivity)
        result_label.config(text=f"实际 dBSPL 值: {dbspl:.2f} dB SPL")

def calculate_dbfs():
    """
    计算所需的 dBFS 值并显示在界面上。
    """
    desired_dbspl = validate_input(target_dbspl_entry.get())
    sensitivity = validate_input(sensitivity_entry.get())
    if desired_dbspl is not None and sensitivity is not None:
        dbfs = dbspl_to_dbfs(desired_dbspl, sensitivity)
        result_label.config(text=f"所需的 dBFS 值: {dbfs:.2f} dBFS")

# 创建主窗口
root = tk.Tk()
root.title("dBFS 和 dBSPL 计算器")

# 创建标签页控件
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, padx=10, pady=10)

# 创建计算器页面
calculator_frame = ttk.Frame(notebook)
notebook.add(calculator_frame, text="计算器")

# 在计算器页面创建输入框和标签
tk.Label(calculator_frame, text="dBFS 值:").grid(row=1, column=0, padx=10, pady=5)
dbfs_entry = tk.Entry(calculator_frame)
dbfs_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(calculator_frame, text="耳机灵敏度 (dB SPL/mW):").grid(row=2, column=0, padx=10, pady=5)
sensitivity_entry = tk.Entry(calculator_frame)
sensitivity_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(calculator_frame, text="目标 dBSPL 值:").grid(row=3, column=0, padx=10, pady=5)
target_dbspl_entry = tk.Entry(calculator_frame)
target_dbspl_entry.grid(row=3, column=1, padx=10, pady=5)

# 创建计算按钮
calculate_dbspl_button = ttk.Button(calculator_frame, text="计算实际 dBSPL", command=calculate_dbspl)
calculate_dbspl_button.grid(row=4, column=0, padx=10, pady=10)

calculate_dbfs_button = ttk.Button(calculator_frame, text="计算所需 dBFS", command=calculate_dbfs)
calculate_dbfs_button.grid(row=4, column=1, padx=10, pady=10)

# 创建结果标签
result_label = tk.Label(calculator_frame, text="结果将在此显示")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 创建原理说明页面
principle_frame = ttk.Frame(notebook)
notebook.add(principle_frame, text="计算原理")

# 在原理说明页面添加说明内容
principle_text = tk.Text(principle_frame, wrap='word', height=10, width=60)
principle_text.insert(tk.END, (
    "这是一个可以滚动的文本，看完了可以滚动鼠标查看更多\n"
    "dBFS (Decibels Full Scale) 是数字音频中的电平单位，表示相对于满刻度的电平。\n"
    "dBSPL (Decibels Sound Pressure Level) 是声压级单位，表示声音的响度，以 20 µPa 为基准。\n"
    "\n"
    "转换公式:\n"
    "- dBFS 转换为 dBSPL:\n"
    "  P_mW = 10^(dBFS/10)\n"
    "  dBSPL = 灵敏度 + 10 * log10(P_mW)\n"
    "\n"
    "- dBSPL 转换为 dBFS:\n"
    "  P_mW = 10^((目标 dBSPL - 灵敏度)/10)\n"
    "  dBFS = 10 * log10(P_mW)\n"
    "\n"
    "这些公式用于计算数字音频信号的声压级或根据目标声压级确定所需的 dBFS。"
))
principle_text.config(state=tk.DISABLED)
principle_text.grid(row=0, column=0, padx=10, pady=10)

# 创建关于作者页面
about_frame = ttk.Frame(notebook)
notebook.add(about_frame, text="关于作者")

# 在关于页面添加作者信息
about_text = tk.Text(about_frame, wrap='word', height=10, width=60)
about_text.insert(tk.END, (
    "作者:  Bilibili@我是Yelina\n"
    "这个工具是一个简单的 dBFS 和 dBSPL 计算器，旨在帮助音频工程师和音频爱好者。\n"
    "如有问题或建议，Email:squat.flunk-0m@icloud.com"
))
about_text.config(state=tk.DISABLED)
about_text.grid(row=0, column=0, padx=10, pady=10)

# 启动主循环
root.mainloop()
