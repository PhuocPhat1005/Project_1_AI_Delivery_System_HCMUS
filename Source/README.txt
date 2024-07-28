# 1. Requirements
* Python version: 3.10+ with Pygame graphical module.
* Operating System: The command may vary across platforms, so you need run this program on Windows.
# 2. Installation
* Firstly, you need to install Python 3.10+ on your computer. You can download Python from this link: https://www.python.org/downloads/
* Secondly, you need to git clone my repo by using this command line below:
```python
git clone "https://github.com/PhuocPhat1005/22127174_22127322_22127388_22127441.git"
```
* Thirdly, you need to set up the virtual environment in Python by using this command line below:
```python
pip install virtualenv
python -m venv venv.
```
* Next, you need to activate the virtual environment in Python by using this command line below. Note that we need “cd” into the folder “Source”.
```python
.venv\Scripts\activate
```
*	Finally, we will install all libraries in the file requirements.txt by using this command line below.
```python
pip install -r requirements.txt
```  
# 3. Running Code
* You need to run the application by executing the command below in the console or terminal.
```python
python main.py
```
# 4. Structure of source code
```tex
Source
├── README.md
├── requirements.txt
├── main.py
├── utils
│   ├── board.py
|   ├── cells.py
|   ├── read_input.py
|   ├── write_output.py
|   └── vehicle_base.py
├── levels
│   ├── level_1
│   │   ├── algorithms
│   │   │   ├── a_star.py
│   │   │   ├── bfs.py
│   │   │   ├── dfs.py
│   │   │   ├── gbfs.py
│   │   │   └── ucs.py
│   │   └── vehicle_level1.py
│   ├── level_2
│   │   ├── algorithms
│   │   │   └── a_star.py
│   │   └── vehicle_level2.py
│   ├── level_3
│   |   ├── algorithms
│   |   │   └── a_star.py
│   |   └── vehicle_level3.py
|   └── level_4
|       └── vehicle_level4.py
├── input
│   ├── level1
│   │   ├── input1_level1.txt
│   │   ├── input2_level1.txt
│   │   ├── input3_level1.txt
│   │   ├── input4_level1.txt
│   │   └── input5_level1.txt
│   ├── level2
│   │   ├── input1_level2.txt
│   │   ├── input2_level2.txt
│   │   ├── input3_level2.txt
│   │   ├── input4_level2.txt
│   │   └── input5_level2.txt
│   ├── level3
│   │   ├── input1_level3.txt
│   │   ├── input2_level3.txt
│   │   ├── input3_level3.txt
│   │   ├── input4_level3.txt
│   │   └── input5_level3.txt
│   └── level4
│       ├── input1_level4.txt
│       ├── input2_level4.txt
│       ├── input3_level4.txt
│       ├── input4_level4.txt
│       └── input5_level4.txt
└── output
    ├── level1
    │   ├── output1_level1.txt
    │   ├── output2_level1.txt
    │   ├── output3_level1.txt
    │   ├── output4_level1.txt
    │   └── output5_level1.txt
    ├── level2
    │   ├── output1_level2.txt
    │   ├── output2_level2.txt
    │   ├── output3_level2.txt
    │   ├── output4_level2.txt
    │   └── output5_level2.txt
    ├── level3
    │   ├── output1_level3.txt
    │   ├── output2_level3.txt
    │   ├── output3_level3.txt
    │   ├── output4_level3.txt
    │   └── output5_level3.txt
    └── level4
        ├── output1_level4.txt
        ├── output2_level4.txt
        ├── output3_level4.txt
        ├── output4_level4.txt
        └── output5_level4.txt
...
```
