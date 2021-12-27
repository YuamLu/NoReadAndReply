'''
/NoReadAndReply.ipynb
by_YuAN on 12/15/2021
'''
import pygame,time,win32clipboard as clip
import win32con
# ------顏色------
BLACK = 0, 0, 0
WHITE = 255, 255, 255
# ------交互------
text = "今天過得如何?"
# ----------------

if __name__ == '__main__':
    print('#----------------#')
    print('# NoReadAndReply #')
    print('#----------------#')
    pygame.init()
    font = pygame.font.SysFont('Microsoft YaHei', 100)    

    print('請按提示輸入文字並設定相關參數，此程式會生成圖片檔並複製到剪貼簿中。')

    text = input('請輸入文字: ');print(text)
    mode = input('聊天室是否為黑色背景?(y/N): ');print(mode)
    if mode == 'y':ftext = font.render(text, True, WHITE, BLACK)
    else:ftext = font.render(text, True, BLACK, WHITE)

    pygame.image.save(ftext, "image.bmp")
    clip.OpenClipboard()
    clip.EmptyClipboard()
    with open("image.bmp", "rb") as f: data = f.read()[14:]
    clip.SetClipboardData(win32con.CF_DIB, data)
    clip.CloseClipboard()

    



