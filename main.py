import time
import math
import sys
import os
import locale
import psutil
import GPUtil
import cpuinfo
import platform
import tkinter as tk
import customtkinter
from tkinter import *
from tkinter import messagebox
import clipboard
from time import localtime
from time import time
import webbrowser
import sqlite3
#from hurry.filesize import size
import json
import subprocess

ver = "3.2.1"
codename = "Core"

devmode = False
devmode = True # #OFF

tm = localtime(time())
yr = tm.tm_year
utm = time()
tm = localtime(utm)

def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return size
        size /= 1024
    return size

sys_ui_col = "System"

btn_color = '#ffffff'
btn_hv_color = '#fff'
t_color = '#000'

info_i = "🔮"
save_i = "💾"
copy_i = "📄"

mon = tm.tm_mon
mday = tm.tm_mday
tmd = f"{mon}/{mday}"

#🎄
if(tmd == "12/25"):
    btn_color = '#0CE880'
    btn_hv_color = '#0CE880'
    t_color = '#FF3F3F'
    info_i = "🎁"
    save_i = "🎉"
    copy_i = "🎄"

#🗓️️
elif(tmd == "1/1"):
    info_i = "🎆"
    save_i = "🎊"
    copy_i = "🗓️"

#😜
elif(tmd == "4/1"):
    print("JOKE")

#🌍
elif(tmd == "4/22"):
    sys_ui_col = "Dark"
    btn_color = '#333333'
    btn_hv_color = '#333333'
    t_color = '#eeeeee'

    info_i = "🌍"
    save_i = "🌱"
    copy_i = "🌲"

customtkinter.set_appearance_mode(sys_ui_col)
#customtkinter.set_default_color_theme("")

os_lang = os.getenv('LANG')
locale = locale.getdefaultlocale()
loco = locale[0]

Info_c = "Info"
Save_c = "Save"
Copy_c = "Copy"
Exit_c = "Exit"
CPUSearch_c = "CPU Search"

cm1p = ("P : 6c | E : 2c")
cm1pm = ("P : 6c | E : 4c")
cm2 = ("P : 4c | E : 4c")
cm2p = ("P : 6c | E : 4c")
cm2pm = ("P : 8c | E : 4c")
cm3 = ("P : 4c | E : 4c")

cpui = cpuinfo.get_cpu_info() #cpu info
pls = platform.system() #platform system info
plv = platform.version() #platform version
rams = psutil.virtual_memory().total #ram size
ramsGB = math.trunc(convert_bytes(rams))
ramsMB = math.trunc(convert_bytes(rams))
f_ram = 0
ramsize = "bit"

result=os.statvfs('/')
block_size=result.f_frsize
total_blocks=result.f_blocks
free_blocks=result.f_bfree
giga=1024*1024*1024

disk_total=math.trunc(total_blocks*block_size/giga)
disk_free=math.trunc(free_blocks*block_size/giga)
disk_use=disk_total - disk_free
disk_total_b=total_blocks*block_size/1024
disk_free_b=free_blocks*block_size/1024
disk_use_b=disk_total_b - disk_free_b


gpu = GPUtil.getGPUs()
gpuname = ""
gpuram = 0


#cpucore = psutil.cpu_count() #cpucore
lcc = psutil.cpu_count(logical=True) #none logical cpu core
c_brand_raw = cpui["brand_raw"]
c_arch = cpui["arch"]
c_arch_string_raw = cpui["arch_string_raw"]
c_bits = cpui["bits"]
c_count = cpui["count"]

applesli_chack = c_brand_raw[0:5]


#root = tk.Tk()
root = customtkinter.CTk()
root.title('PowerME')
root.geometry("390x760+560+40")
#text=tk.Text(root)

cpu_frame = customtkinter.CTkFrame(master=root)
ram_frame = customtkinter.CTkFrame(master=root)
os_frame = customtkinter.CTkFrame(master=root)
btn_frame = customtkinter.CTkFrame(master=root)
cpu_frame = customtkinter.CTkFrame(master=root)

con = sqlite3.connect('./Spaces.db')
cur = con.cursor()

if(devmode == True):
    loco = 'else'

#추가언어 : 프랑스 독일 네덜란드 러시아 이탈리아 체코 중화인민 중화민국 인도 스페인 말레이 베트남 태 그리 폴란드 스웨 스위스 노르웨이  // https://docs.oracle.com/cd/E23824_01/html/E26033/glset.html
if(loco == 'en_US'):
    Info_c = "Info"
    Save_c = "Save"
    Copy_c = "Copy"
    Exit_c = "Exit"
    CPUSearch_c = "CPU Search"
elif(loco == 'ko_KR'):
    Info_c = "정보"
    Save_c = "저장하기"
    Copy_c = "복사"
    Exit_c = "나가기"
    CPUSearch_c = "CPU 정보 검색"

elif(loco == 'ja_JP'):
    Info_c = "情報"
    Save_c = "保存する"
    Copy_c = "コピー"
    Exit_c = "出る"
    CPUSearch_c = "CPU情報検索"

else:
    Info_c = "Info"
    Save_c = "Save"
    Copy_c = "Copy"
    Exit_c = "Exit"
    CPUSearch_c = "CPU Search"

if(rams < 1073741824):
    f_ram = ramsMB
    ramsize = " MB"
else:
    f_ram = ramsGB
    ramsize = " GB"


if(pls == 'Darwin'):
    plname = ' MacOS'
    plvsize = 5.4

elif(pls == 'Windows'):
    plname = 'Microsoft Windows'
    plvsize = 12

elif(pls == 'Linux'):
    plname = 'Linux'
    plvsize = 12

elif(pls == 'BSD'):
    plname = 'Berkeley Software Distribution'
    plvsize = 12

else:
    plname = pls
    plvsize = 12

if(applesli_chack == 'Apple'):
    gpuname = c_brand_raw
    gpuram = ramsGB
    npu_C = 'YES'
    Logical = ''
    lcc = ''
    npumecpack = 1

    if(c_brand_raw == 'Apple M1'):
        mee = "h264,HEVC Encode Decode"
    else:
        mee = "h264,HEVC,ProRes,ProRAW Encode Decode"

    apc = 0
    aec = 0

    if(c_count == 8):
        apc = 4
    if 'Pro' in c_brand_raw:
        if(c_count == 10):
            apc = 6
        elif(c_count == 12):
            apc = 8

    elif 'Max' in c_brand_raw:
        if(c_count == 10):
            apc = 8
        elif(c_count == 12):
            apc = 8
            
    elif 'Ultra' in c_brand_raw:
        if(c_count == 20):
            apc = 16

    if(apc == 4 or apc == 6):
        aec = 4
    elif(apc == 8 or apc == 16):
        aec = 2

    lcc = f"| P : {apc} / E : {aec}"



elif(applesli_chack == 'Intel'):
    print()
else:
    npu_C = '?'
    lcc = f"/ Logical : {lcc} Core"
    npumecpack = 0

spacchart = f"""== Spaces ==
CPU : {c_brand_raw}
Arch : {c_arch} ({c_arch_string_raw})
Bits : {c_bits}
CPU Core : {c_count} {lcc}
OS : {plname} [{pls}] ({plv})
RAM : {ramsMB}{ramsize} ({rams} byte)
Disk :TotalDisk({disk_total}GB _ {disk_total_b}Byte) / UseDisk({disk_use}GB _ {disk_use_b}Byte) / FreeDisk({disk_free}GB _ {disk_free_b}Byte)"""

def info():
    messagebox.showinfo('Info', f'Ver.{ver} ({codename}) \n©2022-{yr} chriskong \nThe GPL Licence\n')

def savetxt():

    ftm = f"{tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}_{tm.tm_mon}, {tm.tm_mday}, {tm.tm_year}"
    file_date = str(ftm)
    tspacs = "Spaces " + file_date
    spacestxt = open(tspacs,"w")
    spacestxt.write(spacchart)
    spacestxt.close()
    messagebox.showinfo('Save', 'Saved!\n File is in "Spaces (date)" Format and in same folder as software')
    #subprocess.Popen('explorer "/Users/"')
    #cur.execute("CREATE TABLE Spaces(CPU text, Arch text, Bits text, Core text, Logical_core text, OS text, RAM text);")
    #cur.execute('SELECT * FROM Spaces')
    #cur.execute('INSERT INTO Spaces VALUES(?, ?, ?, ?, ?, ?, ?,);',(c_brand_raw, c_arch_string_raw, c_bits, c_count, lcc, plname, rams))

def exit():
    sys.exit()

def copy_c():
    clipboard.copy(spacchart)
    messagebox.showinfo('Copy', 'Copyed!')

def cpusearch():
    webbrowser.open(f"https://www.google.com/search?q={c_brand_raw}")


cpuname = customtkinter.CTkLabel(master=root,text="CPU",font=("Open Sans",30))
Cbrandraw = customtkinter.CTkLabel(master=root,text=f"CPU : {c_brand_raw}",font=("Open Sans",12))
arch = customtkinter.CTkLabel(master=root,text=f"Arch : {c_arch}  ({c_arch_string_raw})",font=("Open Sans",12))
bits = customtkinter.CTkLabel(master=root,text=f"Bits : {c_bits} bit",font=("Open Sans",12))
cpucore = customtkinter.CTkLabel(master=root,text=f"CPU Core : {c_count} Core {lcc}",font=("Open Sans",12))

ops = customtkinter.CTkLabel(master=root,text="OS",font=("Open Sans",30))
Pls = customtkinter.CTkLabel(master=root,text=f"{plname} ({pls})",font=("Open Sans",12))
Plv = customtkinter.CTkLabel(master=root,text=f"OS Ver : {plv}",font=("Open Sans",plvsize))

ram = customtkinter.CTkLabel(master=root,text="RAM",font=("Open Sans",30))
Rams = customtkinter.CTkLabel(master=root,text=f"{f_ram} {ramsize} \n({rams} Byte)",font=("Open Sans",12))


GPU = customtkinter.CTkLabel(master=root,text="GPU & Other",font=("Open Sans",30))
Gpuname = customtkinter.CTkLabel(master=root,text=f"GPU Name : {gpuname}",font=("Open Sans",12))
Gpuram = customtkinter.CTkLabel(master=root,text=f"GPU RAM : {gpuram} GB",font=("Open Sans",12))
Npu = customtkinter.CTkLabel(master=root,text=f"NPU : {npu_C}",font=("Open Sans",12))
Mee = customtkinter.CTkLabel(master=root,text=f"Media Engine : {mee}",font=("Open Sans",12))
Nop = customtkinter.CTkLabel(master=root,text="[NO Other Chip]",font=("Open Sans",12))

Disk = customtkinter.CTkLabel(master=root,text="Disk",font=("Open Sans",30))
DISK = customtkinter.CTkLabel(master=root,text=f"Total : {disk_total} GB | Use : {disk_use} GB | free : {disk_free} GB",font=("Open Sans",12))
DISK_B = customtkinter.CTkLabel(master=root,text=f"[Byte] Total : {disk_total_b} | Use : {disk_use_b} | free : {disk_free_b}",font=("Open Sans",10))

nl1 = customtkinter.CTkLabel(master=root,text="")



info_btn = customtkinter.CTkButton(master=root, text = f"{info_i}{Info_c}", width=250,height=30,command=info,corner_radius=50,fg_color=btn_color,hover_color=btn_hv_color,text_color=t_color)
save_btn = customtkinter.CTkButton(master=root, text = f"{save_i}{Save_c}", width=250,height=30,command=savetxt,corner_radius=50,fg_color=btn_color,hover_color=btn_hv_color,text_color=t_color)
copy_btn = customtkinter.CTkButton(master=root, text = f"{copy_i}{Copy_c}", width=250,height=30,command=copy_c,corner_radius=50,fg_color=btn_color,hover_color=btn_hv_color,text_color=t_color)
exit_btn = customtkinter.CTkButton(master=root, text = f"{Exit_c}", width=250,height=30,command=exit,corner_radius=50,fg_color=btn_color,hover_color='#FF2620',text_color='#111111')
cpusearch_btn = customtkinter.CTkButton(master=root, text = f"🔍{CPUSearch_c}", width=80,height=20,command=cpusearch,corner_radius=50,fg_color=btn_color,hover_color=btn_hv_color,text_color=t_color)


#cpu_frame.pack(fill="both",expand = True,pady=10,padx=10)
cpuname.pack(pady=0.5)
Cbrandraw.pack(pady=0.5)
arch.pack(pady=0.5)
bits.pack(pady=0.5)
cpucore.pack(pady=0.5)
cpusearch_btn.pack(padx=1,pady=1)

ops.pack(pady=0.5)
Pls.pack(pady=0.5)
Plv.pack(pady=0.5)

ram.pack(pady=0.5)
Rams.pack(pady=1)

GPU.pack(pady=0.5)
Gpuname.pack(pady=0.5)
Gpuram.pack(pady=0.5)

if(npumecpack == 1):
    Npu.pack(pady=0.5)
    Mee.pack(pady=0.5)

else:
    Nop.pack(pady=0.5)

Disk.pack(pady=0.5)
DISK.pack(pady=0.5)
DISK_B.pack(pady=0.5)

info_btn.pack(pady=5,padx=10)
copy_btn.pack(pady=5,padx=10)
save_btn.pack(pady=5,padx=10)
#exit_btn.pack(pady=15,padx=10)

root.mainloop()




#     sec = 1
#     min = 0
#     hor = 0
#
#     cunt = 0
#
#     c_sum = 0
#     c_avg = 0
#     c_sco = 0
#
#     while True:
#         cpup = psutil.cpu_percent() #cpu use
#         ram = psutil.virtual_memory()# ram use
#         swapm = psutil.swap_memory() #swaping info
#         iodisk = psutil.disk_io_counters(perdisk=False, nowrap=True) #disk io info
#         nwio = psutil.net_io_counters(pernic=False, nowrap=True) # netwark io info
#         c_sum += cpup
#         print("-----------------------------------------------------------------------------------------")
#         print("hor",hor,"min",min,"sec",sec)
#         print("cpu",cpup,"%")
#         print(ram)
#         print(swapm)
#         print(iodisk)
#         print(nwio)
#         cunt += 1
#         #cpu
#         c_avg = c_sum / cunt
#         c_sco = c_avg * 100
#         c_sco = round(c_sco)
#
#         print("count : ", cunt)
#         print("CPUBanchMark | sum : ", c_sum,"| avg : ",c_avg," | score : ",c_sco)
#         time.sleep(1)
#
#         #time
#         sec += 1
#         if(sec == 60):
#             sec = 0
#             min += 1
#         elif(min == 60):
#             min = 0
#             hor += 1

