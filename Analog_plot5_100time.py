
import jin as j
import global_value as g



def popupmenu2A(table):
    '''
    table               :メニューの配列

    戻り値               :インデックス番号
    '''
    import PySimpleGUI as sg

    menu_def = None
    ldict = {}


    menu_def = "g.menu_def=[['Menu',["
    for i in range(0,len(table)):
        menu_def=menu_def+"'"+table[i]+"',"
    menu_def=menu_def+"]]]"

    ##print(menu_def)
    exec(menu_def, globals(), ldict)

    layout = [
        [sg.Menu(g.menu_def)]
    ]

    window = sg.Window('Menuの設定',layout,size=(150,50))

    getflag=False


    while True:
        event, value = window.read() #イベント入力を待つ
        #id=getid("Menuの設定","TkTopLevel")
        #clkitem(id,"TkChild","clk_btn",1)

        j.sleep(100)
        for i in range(len(table)):
            if event == table[i]:
                getdata=i
                getflag=True
                break

        if event is None:
            getdata=6
            break

        if getflag == True:
            break

    window.close()

    return getdata





def Menu_SEL():
    while True:
        g.menu_list=list()
        g.menu_list.append("1相")
        g.menu_list.append("2相")
        g.menu_list.append("3相")
        g.menu_list.append("ALL")
        g.menu_list.append("Shunt_ALL")
        g.menu_list.append("Core_ALL")
        g.menu_list.append("終了")

        g.getmenu = popupmenu2A(g.menu_list)
        if g.getmenu == 6:
            break
        j.sleep(500)







def Menu_POP():
    cnt = 0
    while True:
        j.sleep(500)
        try:
            hwnd1 = j.getid("Menuの設定","TkTopLevel")

            if hwnd1 != 0:
                rect = j.status(hwnd1)
                j.ACW(hwnd1,(g.g_screen_w-rect[2]),0,rect[2],rect[3])
                j.ctrlwin(hwnd1,"fs_show")
                j.ctrlwin(hwnd1,"fs_topmost")
                cnt=0
            else:
                cnt+=1

            if cnt == 10:
                break
        except:
            pass





def main():


    import os
    import sys
    import time

    def get_CUR_DIR():
        import sys
        import os

        path_current_dir = os.path.dirname(sys.argv[0])

        #print(sys.argv[0])
        #print(path_current_dir)
        return  path_current_dir

    g.CUR_DIR=get_CUR_DIR()

    #print(sys.argv[0])#起動パラメータ


##    #web
##    #必要なライブラリをインポート
##    from selenium import webdriver
##    from selenium.webdriver.edge.service import Service
##    from selenium.webdriver.common.by import By
##
##
##    ex1,wb1 = j.ex_OPEN(j.path_join(g.CUR_DIR,"Edge_Driver_Update.xlsm"),False)
##    ex1.run(wb1.Name+"!main1")
##    wb1.Close(False)
##    ex1.Quit()
##
##
##    options = webdriver.EdgeOptions()
##    options.add_experimental_option("excludeSwitches", ['enable-automation'])
##    profile_path = j.path_join(r"C:\Users",j.getuser(),r"Local\Microsoft\Edge\User Data\Profile 1")
##    options.use_chromium = True
##    options.add_argument('disable-web-security')
##    options.add_argument("--user-data-dir="+ profile_path)
##    options.add_argument('--lang=ja')
##    ##options.add_argument('--headless')
##    options.add_argument("--no-sandbox")
##
##    options2 = webdriver.EdgeOptions()
##    options2.add_experimental_option("excludeSwitches", ['enable-automation'])
##    profile_path2 = j.path_join(r"C:\Users",j.getuser(),r"Local\Microsoft\Edge\User Data\Profile 2")
##    options2.use_chromium = True
##    options2.add_argument('disable-web-security')
##    options2.add_argument("--user-data-dir="+ profile_path2)
##    options2.add_argument('--lang=ja')
##    ##options.add_argument('--headless')
##    options2.add_argument("--no-sandbox")
##
##    if j.File_system("fs_exists",j.path_join(r"C:\Users",j.getuser(),
##                                r"AppData\Local\SeleniumBasic\edgedriver.exe")) == True:
##        g.edgeDriver = j.path_join(r"C:\Users",j.getuser(),r"AppData\Local\SeleniumBasic\edgedriver.exe")
##    else:
##        g.edgeDriver = r"C:\Program Files\SeleniumBasic\edgedriver.exe"
##
##    service = Service(executable_path=g.edgeDriver,options=options)
###
##
##
##    ##fukidasiやIE_msg用chromeの立ち上げ
##    fuki_id=0
##    g.driver0 = webdriver.Edge(service=service, options=options)
##
##    #j.ctrlwin(j.getid("新しいタブ - 職場 - Microsoft? Edge","Chrome_WidgetWin_1"),"fs_min")
##
##
##    ####################Edge立ち上げ####################
####    driver = webdriver.Edge(service=service, options=options2)
####    driver.set_page_load_timeout(5)
####    driver.maximize_window()
####
####    driver.get("https://p3.phoneappli.net/front/home")
####    j.BusyWait(driver)
####    j.sleep(10)
##    ####################Edge立ち上げ####################


    '''
    #ACCESS
    import pyodbc
    import pandas as pd
    '''

    j.get_gamen_size()



    #グローバル変数にはg.を付ける

    g.getmenu=0
    getmenu2=0
    getmenu=getmenu2


    th1=j.Thread(Menu_SEL)
    th2=j.Thread(Menu_POP)


    while True:
        j.sleep(10)
        hwnd1 = j.getid("Menuの設定","TkTopLevel")

        if hwnd1 != 0:
            break

    rect = j.status(hwnd1)
    j.ACW(hwnd1,(g.g_screen_w-rect[2]),0,rect[2],rect[3])
    j.ctrlwin(hwnd1,"fs_show")
    ##j.ctrlwin(hwnd1,"fs_topmost")



    while True:

        #############################グラフ設定#############################
        import matplotlib.pyplot as plt #pltという名前の関数名
    ##    plt.style.available
    ##    plt.style.use('seaborn-dark')

        fig = plt.figure(figsize=(8, 5),facecolor='lightyellow')
        ax1 = plt.axes([0.15, 0.12, 0.7, 0.72])##グラフエリアの設定 全体エリアに対する割合 left,bottom,width,height
    ##    fig.canvas.manager.full_screen_toggle() # toggle fullscreen mode
        ##ax1 = fig.add_subplot(111)
        #############################グラフ設定#############################


        #############################COMポートの読み出し#############################
        f1={}
        f1=j.fopen(j.path_join(g.CUR_DIR,"com_port.txt"),"f_read")
        COMPORT=j.fget(f1,1,1)
        j.fclose(f1)
        #############################COMポートの読み出し#############################


        g.delaytime=100
        g.pre_delaytime=100


        ################Serial通信開始################
        j.Serial_port()
        ##Port=j.Serial_begin("com3",115200)    ##ESP32
        Port=j.Serial_begin(COMPORT,115200)     ##Arduino Due

        while True:
            try:
                data=j.Serial_read(Port)
                break
            except:
                j.sleep(1000)
                continue
        ################Serial通信開始################


        j.sleep(500)
        get_DataTable=j.Hairetu(6,100)#########データ格納配列

        cyc=0
        while True:

            j.Serial_write(Port,g.delaytime)#######delay時間を送付
            j.sleep(800)#######通信delayの設定


            try:
                data=j.Serial_read(Port)#######Arduinoから受信
            except:
                j.sleep(1000)
                data=j.Serial_read(Port)
                continue


            data2=data.split(",")#######600個のデータを配列化
            if len(data2) != 600:
                data=j.Serial_read(Port)
                continue

            #######データを配列に入れる
            t=0
            for ii in range(0,6):
                for i in range(0,100):
                    get_DataTable[ii][i]=data2[t]
                    t+=1
            ##    import matplotlib.pyplot as plt #pltという名前の関数名

            x1=j.Hairetu(100)
            xmemori=j.Hairetu(11)

            y1=j.Hairetu(100)
            y2=j.Hairetu(100)
            y3=j.Hairetu(100)
            y4=j.Hairetu(100)
            y5=j.Hairetu(100)
            y6=j.Hairetu(100)

            ####### X軸 時間の目盛り表示の設定#######
            for i in range(0,11):
                xmemori[i] = j.round((g.delaytime/1000*100+25)/10*i,"0.1")

            ####### X軸 データの作成#######
            for i in range(0,100):
                x1[i] = i

            ####### Y軸 データの作成#######
            for i in range(0,100):
                if getmenu == "1相":
                    y1[i] = (int(get_DataTable[0][i])/4095*5000-2500)*5+4500
                    y2[i] = int(get_DataTable[3][i])
                elif getmenu == "2相":
                    y1[i] = (int(get_DataTable[1][i])/4095*5000-2500)*5+4500
                    y2[i] = int(get_DataTable[4][i])
                elif getmenu == "3相":
                    y1[i] = (int(get_DataTable[2][i])/4095*5000-2500)*5+4500
                    y2[i] = int(get_DataTable[5][i])
                elif getmenu == "ALL":
                    y1[i] = (int(get_DataTable[0][i])/4095*5000-2500)*5+4500
                    y2[i] = (int(get_DataTable[1][i])/4095*5000-2500)*5+4500
                    y3[i] = (int(get_DataTable[2][i])/4095*5000-2500)*5+4500
                    y4[i] = int(get_DataTable[3][i])
                    y5[i] = int(get_DataTable[4][i])
                    y6[i] = int(get_DataTable[5][i])
                elif getmenu == "Shunt_ALL":
                    y1[i] = int(get_DataTable[3][i])
                    y2[i] = int(get_DataTable[4][i])
                    y3[i] = int(get_DataTable[5][i])
                elif getmenu == "Core_ALL":
                    y1[i] = (int(get_DataTable[0][i])/4095*5000-2500)*5+4500
                    y2[i] = (int(get_DataTable[1][i])/4095*5000-2500)*5+4500
                    y3[i] = (int(get_DataTable[2][i])/4095*5000-2500)*5+4500


            ax1.cla()####### グラフのリセット

            ax1.set_facecolor ('white')####### グラフの背景色の設定

            ####### プロット #######
            if getmenu == "1相":
                ax1.plot(x1,y1,linewidth=2,color="red",linestyle="-",label="Core1")##ax1.plot(x1,y1,marker=".",linewidth=3,color="red",linestyle="-",label="Sen1")
                ax1.plot(x1,y2,linewidth=2,color="deeppink",linestyle="-",label="Shunt1")
            elif getmenu == "2相":
                ax1.plot(x1,y1,linewidth=2,color="blue",linestyle="-",label="Core2")##ax1.plot(x1,y1,marker=".",linewidth=3,color="red",linestyle="-",label="Sen1")
                ax1.plot(x1,y2,linewidth=2,color="skyblue",linestyle="-",label="Shunt2")
            elif getmenu == "3相":
                ax1.plot(x1,y1,linewidth=2,color="green",linestyle="-",label="Core3")##ax1.plot(x1,y1,marker=".",linewidth=3,color="red",linestyle="-",label="Sen1")
                ax1.plot(x1,y2,linewidth=2,color="lightgreen",linestyle="-",label="Shunt3")
            elif getmenu == "ALL":
                ax1.plot(x1,y1,linewidth=2,color="red",linestyle="-",label="Core1")##ax1.plot(x1,y1,marker=".",linewidth=3,color="red",linestyle="-",label="Sen1")
                ax1.plot(x1,y2,linewidth=2,color="blue",linestyle="-",label="Core2")
                ax1.plot(x1,y3,linewidth=2,color="green",linestyle="-",label="Core3")
                ax1.plot(x1,y4,linewidth=2,color="deeppink",linestyle="-",label="Shunt4")
                ax1.plot(x1,y5,linewidth=2,color="skyblue",linestyle="-",label="Shunt5")
                ax1.plot(x1,y6,linewidth=2,color="lightgreen",linestyle="-",label="Shunt6")
            elif getmenu == "Shunt_ALL":
                ax1.plot(x1,y1,linewidth=2,color="deeppink",linestyle="-",label="Shunt1")
                ax1.plot(x1,y2,linewidth=2,color="skyblue",linestyle="-",label="Shunt2")
                ax1.plot(x1,y3,linewidth=2,color="lightgreen",linestyle="-",label="Shunt3")
            elif getmenu == "Core_ALL":
                ax1.plot(x1,y1,linewidth=2,color="red",linestyle="-",label="Core1")
                ax1.plot(x1,y2,linewidth=2,color="blue",linestyle="-",label="Core2")
                ax1.plot(x1,y3,linewidth=2,color="green",linestyle="-",label="Core3")

            ax1.set_title("Current Sensor Output")####### グラフのタイトル

            ax1.set_yscale("linear")##ax.set_yscale("log")###### ｙ軸設定
            ax1.set_xlabel("Time(ms)",style ="italic" , size = "xx-large", color ="black")###### X軸タイトル

            ##ax1.get_yaxis().set_tick_params(pad=5)#####軸と目盛りのマージン設定
            ax1.set_ylabel("Output V(mV)",style ="italic" , size = "xx-large", color ="black")###### y軸タイトル
            ax1.yaxis.set_label_coords(-0.1,0.5)####Y1軸のラベル位置調整

            ax1.set_xticks([0,10,20,30,40,50,60,70,80,90,100])###### X軸目盛り
            ax1.set_xticklabels(xmemori)###### X軸目盛り2　 こちらを表示
            ax1.set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000])###### Y軸目盛り

            ax1.set_ylim(0, 5000)###### Y軸目盛り
            ##ax1.set_xlim(0, 100)
            ax1.text(-20, 5400, "Current Sensor", alpha=1,fontsize=20,color="orange")###### Text表示

            ##ax1.text(-23, 1100, "Current Sensor", alpha=1,fontsize=12,color="blue",rotation=90)###### Text表示

    ##        plt.legend(loc='upper left')######凡例の表示方法
            plt.legend(loc='upper left', bbox_to_anchor=(1, 1))######凡例の表示方法

            ax1.grid() ######グリッド
            plt.pause(.001)######更新頻度設定


            ####### delaytime設定 #######
            g.pre_delaytime=g.delaytime
            getstr=j.getkeystate()

            if j.pos("vk_ctrl",getstr)>0:
                getdata = j.inputbox("Delay時間","Message",0,str(g.delaytime))
                if getdata == None:
                    pass
                elif getdata == "":
                    pass
                elif j.IsNum(getdata) == False:
                    pass
                else:
                    g.delaytime = int(getdata)
##            elif j.pos("vk_alt",getstr)>0:
##                plt.close()######グラフ終了
##                j.Serial_close(Port)######Serial終了
##                break

            print(g.getmenu)
            getmenu2 = g.menu_list[g.getmenu]
            getmenu=getmenu2

            if getmenu2 == "終了":
                plt.close()######グラフ終了
                j.Serial_close(Port)######Serial終了

                j.sleep(10)
##                hwnd2 = j.getid("Figure 1","TkTopLevel")
##                j.ctrlwin(hwnd2,"fs_close")
##                j.ctrlwin(hwnd1,"fs_close")
                j.Thread_end(th1)
                j.Thread_end(th2)
                j.End()
            ####### delaytime設定 #######

            j.sleep(10)















if __name__ == '__main__':
    main()
