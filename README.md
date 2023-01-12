# Description
"pynit" (<u>py</u>thon mo<u>nit</u>or) is a minimalistic, lightweight and cross-platform
system monitoring tool. It is capable of providing basic information about the operating
system, CPU, RAM, Disks, and GPU (NVIDIA and AMD/ATI chipsets). Currently, supports the following platforms:
- **Linux**
- **Windows**

<sup>*Requires Python 3.7+</sup>\
<sup>**Please check [PyQt](https://wiki.qt.io/Qt_for_Python) for detailed information about compatibility</sup>
## Installation
Start by cloning the repository:
```
git clone https://github.com/sk8thing/pynit.git
```
Make sure you install the requirements, I also suggest creating a virtual environment:
```
cd pynit
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```
After all that you can run:
```
python3 main.py
```
### Requirements
- [PySide6](https://pypi.org/project/PySide6/) (GUI)
- [qt-material](https://pypi.org/project/qt-material/) (Styling)
- [pyqtgraph](https://pypi.org/project/pyqtgraph/) (Graphics)
- [distro](https://pypi.org/project/distro/) (Information about Linux distribution)
- [psutil](https://pypi.org/project/psutil/) (System utilization information)
- [cpuinfo](https://github.com/pydata/numexpr/blob/master/numexpr/cpuinfo.py) (CPU information such as name arch etc.)
- [winstats](https://pypi.org/project/winstats/) (Information gathering for Windows systems)
- [GPUtil](https://pypi.org/project/GPUtil/) (Information gathering for NVIDIA GPUs)
- [pyadl](https://pypi.org/project/pyadl/) (Information gathering for AMD/ATI GPUs)