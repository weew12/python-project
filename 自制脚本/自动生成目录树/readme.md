# 目录树生成

---

### 最近有一个生成项目的目录树的需求，虽然 window 的 cmd 提供了这个命令，但是自己试着实现了一下，可以更具功能自行调整

---

### 附上 windows 命令

    tree /F

---

### 程序使用

    打开cmd或者powerShell
    输入python ./DirectoryTree.py
    程序会打印生成的目录树的结构
    生成一个输出文件DirectoryTree.txt

---

### 结果展示

#### 执行

![](images/res1.png)

#### 生成文件 DirectoryTree.txt

![](images/res2.png)

#### DirectoryTree.txt 内容

![](images/res3.png)

#### DirectoryTree.txt

	├─.idea
	│  ├─.gitignore
	│  ├─encodings.xml
	│  ├─misc.xml
	│  ├─modules.xml
	│  ├─vcs.xml
	│  ├─workspace.xml
	│  └─项目实战.iml
	├─PetStore
	│  ├─.idea
	│  │  ├─encodings.xml
	│  │  ├─misc.xml
	│  │  ├─modules.xml
	│  │  ├─vcs.xml
	│  │  └─workspace.xml
	│  ├─db
	│  │  └─mysql-connector-java-5.1.41-bin.jar
	│  ├─out
	│  │  └─production
	│  │     └─PetStore
	│  │        ├─com
	│  │        │  └─weew12
	│  │        │     └─jpetstore
	│  │        │        ├─dao
	│  │        │        │  ├─mysql
	│  │        │        │  │  ├─AccountDaoImp.class
	│  │        │        │  │  ├─config.properties
	│  │        │        │  │  ├─DBHelper.class
	│  │        │        │  │  ├─OrderDaoImp.class
	│  │        │        │  │  ├─OrderDetailDaoImp.class
	│  │        │        │  │  └─ProductDaoImp.class
	│  │        │        │  ├─AccountDao.class
	│  │        │        │  ├─OrderDao.class
	│  │        │        │  ├─OrderDetailDao.class
	│  │        │        │  └─ProductDao.class
	│  │        │        ├─domain
	│  │        │        │  ├─Account.class
	│  │        │        │  ├─Order.class
	│  │        │        │  ├─OrderDetail.class
	│  │        │        │  └─Product.class
	│  │        │        └─ui
	│  │        │           ├─CartFrame.class
	│  │        │           ├─CartTableModel.class
	│  │        │           ├─LoginFrame.class
	│  │        │           ├─MainApp.class
	│  │        │           ├─MyFrame$1.class
	│  │        │           ├─MyFrame.class
	│  │        │           ├─ProductListFrame.class
	│  │        │           └─ProductTableModel.class
	│  │        └─images
	│  │           ├─bird1.gif
	│  │           ├─bird1.jpg
	│  │           ├─bird2.gif
	│  │           ├─bird2.jpg
	│  │           ├─bird3.gif
	│  │           ├─bird4.gif
	│  │           ├─bird5.gif
	│  │           ├─bird6.gif
	│  │           ├─cat1.gif
	│  │           ├─cat1.jpg
	│  │           ├─cat2.gif
	│  │           ├─cat2.jpg
	│  │           ├─cat3.gif
	│  │           ├─cat4.gif
	│  │           ├─dog1.gif
	│  │           ├─dog1.jpg
	│  │           ├─dog2.gif
	│  │           ├─dog2.jpg
	│  │           ├─dog3.gif
	│  │           ├─dog3.jpg
	│  │           ├─dog4.gif
	│  │           ├─dog4.jpg
	│  │           ├─dog5.gif
	│  │           ├─dog5.jpg
	│  │           ├─dog6.gif
	│  │           ├─dog6.jpg
	│  │           ├─fish1.gif
	│  │           ├─fish1.jpg
	│  │           ├─fish2.gif
	│  │           ├─fish2.jpg
	│  │           ├─fish3.gif
	│  │           ├─fish3.jpg
	│  │           ├─fish4.gif
	│  │           ├─fish4.jpg
	│  │           ├─lizard1.gif
	│  │           ├─lizard1.jpg
	│  │           ├─lizard2.gif
	│  │           ├─lizard3.gif
	│  │           ├─snake1.gif
	│  │           ├─snake1.jpg
	│  │           └─splash.gif
	│  ├─src
	│  │  ├─com
	│  │  │  └─weew12
	│  │  │     └─jpetstore
	│  │  │        ├─dao
	│  │  │        │  ├─mysql
	│  │  │        │  │  ├─AccountDaoImp.java
	│  │  │        │  │  ├─config.properties
	│  │  │        │  │  ├─DBHelper.java
	│  │  │        │  │  ├─OrderDaoImp.java
	│  │  │        │  │  ├─OrderDetailDaoImp.java
	│  │  │        │  │  └─ProductDaoImp.java
	│  │  │        │  ├─AccountDao.java
	│  │  │        │  ├─OrderDao.java
	│  │  │        │  ├─OrderDetailDao.java
	│  │  │        │  └─ProductDao.java
	│  │  │        ├─domain
	│  │  │        │  ├─Account.java
	│  │  │        │  ├─Order.java
	│  │  │        │  ├─OrderDetail.java
	│  │  │        │  └─Product.java
	│  │  │        └─ui
	│  │  │           ├─CartFrame.java
	│  │  │           ├─CartTableModel.java
	│  │  │           ├─LoginFrame.java
	│  │  │           ├─MainApp.java
	│  │  │           ├─MyFrame.java
	│  │  │           ├─ProductListFrame.java
	│  │  │           └─ProductTableModel.java
	│  │  └─images
	│  │     ├─bird1.gif
	│  │     ├─bird1.jpg
	│  │     ├─bird2.gif
	│  │     ├─bird2.jpg
	│  │     ├─bird3.gif
	│  │     ├─bird4.gif
	│  │     ├─bird5.gif
	│  │     ├─bird6.gif
	│  │     ├─cat1.gif
	│  │     ├─cat1.jpg
	│  │     ├─cat2.gif
	│  │     ├─cat2.jpg
	│  │     ├─cat3.gif
	│  │     ├─cat4.gif
	│  │     ├─dog1.gif
	│  │     ├─dog1.jpg
	│  │     ├─dog2.gif
	│  │     ├─dog2.jpg
	│  │     ├─dog3.gif
	│  │     ├─dog3.jpg
	│  │     ├─dog4.gif
	│  │     ├─dog4.jpg
	│  │     ├─dog5.gif
	│  │     ├─dog5.jpg
	│  │     ├─dog6.gif
	│  │     ├─dog6.jpg
	│  │     ├─fish1.gif
	│  │     ├─fish1.jpg
	│  │     ├─fish2.gif
	│  │     ├─fish2.jpg
	│  │     ├─fish3.gif
	│  │     ├─fish3.jpg
	│  │     ├─fish4.gif
	│  │     ├─fish4.jpg
	│  │     ├─lizard1.gif
	│  │     ├─lizard1.jpg
	│  │     ├─lizard2.gif
	│  │     ├─lizard3.gif
	│  │     ├─snake1.gif
	│  │     ├─snake1.jpg
	│  │     └─splash.gif
	│  └─PetStore.iml
	└─DirectoryTree.py

---

### TODO

1. [ ] 目录树过滤选定后缀文件
2. [ ] 优化改善
