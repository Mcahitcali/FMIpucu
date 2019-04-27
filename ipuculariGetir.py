from PIL import Image, ImageOps, ImageGrab as ig
import pytesseract, keyboard, os

def yakala(screen=None):
    screen = ig.grab()
    yeniResim = screen.crop((16,682,1815,730))
    yeniResim = ImageOps.invert(yeniResim)
    # yeniResim.show()
    yazdir(yeniResim)
    
def yazdir(resim):
    text = pytesseract.image_to_string(resim,lang="tur")
    if ipucuVarMi(text):
        sayi = len(os.listdir("resimler"))
        resim.save("resimler/ipucu"+str(sayi+1)+".png")
        print("ipucu yazildi")
        with open("ipuclar.txt","a+",encoding="utf8") as ipuclariTXT:
            ipuclariTXT.write(text.replace("\n"," ")+"\n\n")
        
def ipucuVarMi(text):
    if not text:
        print("text bos!")
        return False

    keywords = "Püf Noktaları:"
    def file_is_empty(path):
        return os.stat(path).st_size!=0

    varMi = (keywords in text)
    if varMi and file_is_empty('ipuclar.txt'):
        with open('ipuclar.txt', 'rt',encoding="utf8") as ipuclariTXT:
            read =ipuclariTXT.read()
            if text.replace("\n"," ") in read:
                print("var")
                varMi = False

    return varMi

# keyboard.add_hotkey('s', lambda: yakala())
# keyboard.wait('esc')   
if __name__ == "__main__":
    while(True):
        screen = ig.grab()
        yakala(screen)
        # cv2.imshow("test", np.array(screen))ss
        if keyboard.is_pressed("esc"):
            break
        
