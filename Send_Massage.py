import win32gui
import win32con
import win32clipboard
from Weather import main

class CSendQQMsg():
    def __init__(self, friendName, msg):
        self.friendName = friendName
        self.msg = msg

    # 把要发送的消息复制到剪贴板
    def setText(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        win32clipboard.CloseClipboard()

    # 给好友发送消息
    def sendmsg(self):
        self.setText()
        # 找到名字为'王三'的窗口
        hwndQQ = win32gui.FindWindow(None, self.friendName)
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


if __name__ == '__main__':
    friendName = 'y'
    msg = main()
    qq = CSendQQMsg(friendName, msg)
    qq.sendmsg()


