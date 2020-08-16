"""
文件下载器
"""
import requests
import time

# 已下载文件大小
dl_size = 0
# 分块下载大小
chunk_size = 1024
# 初始化计时器
time_start = time.time()
# 初始化MB单位大小
mb = 0


def dl_file(url):
    res = requests.get(url, stream=True)
    with open(url.rsplit('/', 1)[-1], 'wb') as f:
        for chunk in res.iter_content(chunk_size=chunk_size):
            f.write(chunk)

            global dl_size
            # 更新已下载文件大小
            dl_size += chunk_size

            # 将已下载文件大小，以从大到小的单位存放
            echo_size = []
            div = dl_size
            while div >= 2 ** 10:
                div, mod = divmod(div, 2 ** 10)
                echo_size.insert(0, mod)
            else:
                echo_size.insert(0, div)

            global mb, time_start
            # 显示下载MB大小、下载速度
            if len(echo_size) == 3 and mb != echo_size[0]:
                mb = echo_size[0]
                time_end = time.time()
                time_elapsed = time_end - time_start
                time_start = time_end
                speed = 1024 / time_elapsed
                print('已经下载了 {} MB, 下载速度 {} KB/s'.format(mb, speed))
