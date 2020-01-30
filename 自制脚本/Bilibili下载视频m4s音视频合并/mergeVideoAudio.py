import os

'''
	前提条件:
		https://ffmpeg.org/ 下载ffmpeg
	利用ffmpeg 合并 bilibili手机端下载的以m4s为格式的音频视频独立的文件到一个mp4文件
	ffmpeg使用:
		ffmpeg -i .\video.m4s -i .\audio.m4s -vcodec copy -acodec copy output.mp4

	参数：
        @programPath : ffmpeg 程序的路径
        @args ： 使用ffmpeg 的命令参数(根据处理需求进行更改)
        @args : 最终通过python调用执行的完整语句
        @rootDirectory ： 下载的视频的更目录(整个视频合集的大目录)
        @directory1 ：视频单集的目录
        @directory2 ：视频存储目录(64 为720P 清晰度的目录 可以根据情况进行变更)
        @directory3 ：视频所在目录 包含audio.m4s 音频文件 与 video.m4s 视频文件

'''

programPath = r"C:\Users\ASUS\Downloads\ffmpeg-20190502-7eba264-win64-static \\ffmpeg-20190502-7eba264-win64-static\bin\ffmpeg.exe"
args = r" -i .\video.m4s -i .\audio.m4s -vcodec copy -acodec copy output.mp4"
comand = programPath + args
# print(comand)

# 查找程序是否存在
if os.path.exists(programPath):
    print("program is found\n--------------------------\n start to deal")
else:
    print("program is not found")
    os._exit(0)

# 获取root 目录信息
rootDirectory = input("Please input the root directory：")
print(rootDirectory)
directory1 = os.listdir(rootDirectory)  # 获取目录列表
directory1 = sorted([int(i) for i in directory1])  # 按数字进行排序
directory1 = [str(i) for i in directory1]  # 转换成目录名字的字符串

for i in directory1:
    print("/++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++/")
    print("/***************************************************************/")
    directory2 = rootDirectory + "\\" + i
    # print(directory2)
    try:
        if "64" in os.listdir(directory2):
            directory3 = directory2 + "\\" + os.listdir(directory2)[0]
            # print(directory3)
        else:
            continue
    except Exception as err:
        print("find directory default --> ", directory2)
        continue

    dealPath = directory3

    if "output.mp4" in os.listdir(dealPath):
        print(dealPath + "\\output.mp4  allready exists")
    else:
        os.chdir(dealPath)
        print("now in -- ", os.getcwd())
        f = os.popen(comand)
        data = f.readlines()
        f.close()
        print(data)
    print("/***************************************************************/")
    print("/++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++/")
