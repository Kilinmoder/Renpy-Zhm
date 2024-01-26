# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define z = Character("怀民")
define l = Character("冰酱")

image splash = "splash.png"
image pure_black = "#000"
image pure_white =  "#ffffff"
image end = "end.png"


# 游戏在此开始。

label splashscreen:
    scene pure_black
    show pure_white with Dissolve(2.0)
    show splash at truecenter with Dissolve(2.0)
    # $ renpy.pause(1, hard=True) #开头动画不能被跳过
    pause 1.0
    hide splash with Dissolve(2.0)
    return

label before_main_menu:
    "本作不含血腥暴力内容，请放心游玩！"

label main_menu:

    # 添加主菜单选项，可以使用menu语句
    menu:
        "开始游戏":
            # 在这里添加开始游戏的逻辑
            jump start
        "退出游戏":
            $ renpy.quit()

label start:

    z "如你所见，我们被困在这个世界了！"
    l "唔姆，这是很重要的事吗！有你在我身边，我会管这些吗"
    show end with Dissolve(2.0)
    hide end
    pause 1.0
    jump main_menu



