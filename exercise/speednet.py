from speedtest import Speedtest
import platform


st = Speedtest()  # создание объекта(экземпляра) класса

# --------------------------------

sys_info = platform.platform()
cpu_info = platform.processor()
compiler_info = platform.python_compiler()
python_ver = platform.python_version()

print(
    sys_info,
    cpu_info,
    compiler_info,
    python_ver,
    sep='\n'
)

# --------------------------------

download = st.download()  # скорость загрузки
upload = st.upload()  # скорость отдачи


print('Скорость загрузки: {:.2f}'.format(download / (8 * 1024 * 1024)))
print('Скорость отдачи: {:.2f}'.format(upload / (8 * 1024 * 1024)))
