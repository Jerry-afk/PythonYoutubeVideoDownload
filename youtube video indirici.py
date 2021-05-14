from pytube import YouTube
link = input("Video linki giriniz ")
kalite = input ("Video kalitesini seçiniz Yüksek kalite = 1 Orta kalite = 2 Düşük kalite = 3 ")
if kalite == "1":
 YouTube(link).streams.get_highest_resolution().download()
elif kalite == "2":
 YouTube(link).streams.get_by_resolution.download()
elif kalite == "3":
 YouTube(link).streams.get_lowest_resolution.download()
else:
    print("hatalı giriş")
