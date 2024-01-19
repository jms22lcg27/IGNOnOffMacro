import pyautogui as p
import keyboard
import time
import tkinter as tk
start_btn=0
on_btn=0
off_btn=0

def key(event):
    global start_btn
    global on_btn
    global off_btn

    key = event.keysym
    print(key)
    if key == 'Up':
        start_btn = p.position()
        #btn_list[0]==start_btn
        print(start_btn)
        btn1.config(text=start_btn)
        #btn1.config(text=("X=",start_btn.x," Y=",start_btn.y))
    elif key == 'Left':
        on_btn = p.position()
        #btn_list[1]==on_btn
        print(on_btn)
        btn2.config(text=on_btn)
    elif key == 'Right':
        off_btn = p.position()
        #btn_list[2]==off_btn
        print(off_btn)
        btn3.config(text=off_btn)
    else:
        btn1.config(text="잘못된 버튼입니다. 다시 입력하세요.")
        btn2.config(text="잘못된 버튼입니다. 다시 입력하세요.")
        btn3.config(text="잘못된 버튼입니다. 다시 입력하세요.")

    

def click():
    print(start_btn, on_btn, off_btn)
        
    btn.config(text="실행 중", bg="red")
    for i in range(30):#29
        p.click(start_btn) # start_btn
        p.click(off_btn) # off_btn
        time.sleep(0.4)
        p.click(start_btn) # start_btn
        p.click(on_btn) # on_btn
        time.sleep(0.4)
    btn.config(text="Start", bg="green")
    
        
window=tk.Tk()

window.title("IGN ON/OFF MACRO")
window.geometry("640x400+100+100")
window.resizable(True, True) # 창 조절 가능

label=tk.Label(window, text="IGN ON 상태에서 시작 \n좌표 입력 후 Start", width=30, height=5)
label.pack()
btn1=tk.Button(window,text="화살표 체크 - 키보드 up",padx=30, pady=5, fg="black", bg="white")
btn1.pack()
btn2=tk.Button(window,text="IGN ON - 키보드 left",padx=30, pady=5, fg="black", bg="white")
btn2.pack()
btn3=tk.Button(window,text="IGN OFF - 키보드 right",padx=30, pady=5, fg="black", bg="white")
btn3.pack()
btn=tk.Button(window,text="Start", padx=30, pady=15, fg="white", bg="green", command=click)
btn.pack()

window.bind("<Key>",key)
#window.bind("<Left>",key)
#window.bind("<Right>",key)


window.mainloop() #창 닫을때까지 유지