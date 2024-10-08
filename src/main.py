# main.py
#
# Copyright 2024 Programmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os, sys, time, webbrowser
#main package
try:
    from banner import banner
    from color.warna import orange
    from color.warna import putih
    from color.warna import merah
    from color.warna import hijau
    from color.warna import biru
    from color.warna import borange
    from color.warna import bputih
    from color.warna import bhijau
    from color.warna import bbiru
    from color.warna import bmerah
    from color.warna import kelabu
    from color.warna import borangekelip
    from color.warna import banmerah
    from color.warna import banhijau
    from color.warna import banorange
    from color.warna import reset
except ImportError:
    print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()
#main package 2
try:
    from PIL import Image, UnidentifiedImageError
    import os
    import cv2
    import numpy as np
    import webbrowser
except ImportError:
    print(putih+" ["+banorange+"!"+reset+putih+"]"+merah+" Installasi paket penting akan segera dilakukan(for debian users)"+reset)
    if os.platform in ['linux', 'linux2']:
        os.system('apt install python3-opencv python3-numpy python3-pil')
    else:
        os.system('pip install opencv-python numpy pillow')
#main
def main_1():
    kosong = ""
    try:
        print(banner)
        subs = input(putih+"\n ["+banhijau+"&"+reset+putih+"] Subscribe yukk... (y/n)")
        if subs.lower() == 'y':
            print(kelabu+' [+]'+putih+' Thanks...'+reset)
            webbrowser.open('https://www.youtube.com/@linggachannel4781')
        else:
            pass
        path1 = input(kelabu+" ["+banhijau+">"+reset+kelabu+"]"+putih+" Masukkan path folder gambar yang akan di sortir: "+reset)
        path2 = input(kelabu+" ["+banhijau+">"+reset+kelabu+"]"+putih+" Masukkan path folder output untuk menyimpan gambar: "+reset)
        width0 = input(kelabu+" ["+banhijau+"-"+reset+kelabu+"]"+putih+" Masukan ukuran minimum panjang gambar (Pixel): "+reset)
        height0 = input(kelabu+" ["+banhijau+"|"+reset+kelabu+"]"+putih+" Masukan ukuran minimum tinggi gambar (Pixel): "+reset)
        if width0 is kosong or height0 is kosong:
            print(kelabu+"\n ["+banmerah+"!"+reset+kelabu+"]"+putih+" Isi pixel minimum nya bang(12x15|panjangxtinggi)"+reset);sys.exit()
        if path1 is kosong or path2 is kosong:
            print(kelabu+"\n ["+banmerah+"!"+reset+kelabu+"]"+putih+" Kok path nya kosong sih kayak hati kamu wkwk"+reset);sys.exit()
        #bluerr
        def is_blurry(imgpath, threshold=100):
            image = cv2.imread(imgpath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            return laplacian_var < threshold
        for filename in os.listdir(path1):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                imgpath = os.path.join(path1, filename)
                try:
                    img = Image.open(imgpath)
                    width, height = img.size
                    if width >= int(width0) and height >= int(height0):
                        if not is_blurry(imgpath, threshold=100):
                            output_path = os.path.join(path2, filename)
                            if not os.path.exists(output_path):
                                print(kelabu+'\r ['+banhijau+'#'+reset+kelabu+']'+putih+' Menyimpan '+hijau+str(filename)+reset)
                                img.save(output_path)
                            else:
                                print(kelabu+" ["+banmerah+">"+reset+kelabu+"]"+hijau+" File sudah ada, dilewatkan."+reset)
                        else:
                            print(kelabu+" ["+banmerah+"<"+reset+kelabu+"]"+orange+" Gambar buriq"+reset)
                    else:
                        print(kelabu+" ["+banmerah+"<"+reset+kelabu+"]"+orange+" Gambar tidak sesuai"+reset)
                except UnidentifiedImageError: print('gagal')
                except cv2.error: print('gagal2')
        print(putih+' ['+banhijau+'✔️'+reset+putih+']'+hijau+' Selesai, File anda telah disortir!');sys.exit()
    except (KeyboardInterrupt, EOFError): print(kelabu+" ["+banmerah+"!"+reset+kelabu+"]"+merah+" Exit!..."+reset);sys.exit()

#start
if __name__=="__main__":
    main_1()
