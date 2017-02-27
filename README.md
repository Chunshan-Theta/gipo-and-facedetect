FaceDetect_GPIO/

GPIO24.py and GpioSet.py	

  - lib for control pi's GPIO
  - source:https://github.com/Chunshan-Theta/GPIO_ON_Raspberry
  
common.py and video.py

  - this lib for face detect
  
haarcascade_frontalface_alt.xml

  - kernel of face detect
  - could chenge this for detect another
  
main.py

  - run this would exec face detect process
  - Getting config json file from PHP API and setting pi's GPIO
  - according number of face detect to control self's GPIO
  - according number of face detect to control another's GPIO using request PHP API


web_GPIO/

GET_Insert.php	

  - insert data to Mysql
  - source: https://github.com/Chunshan-Theta/SQLCmdUsingPHP
  
GPIO24.py	

  - lib for control pi's GPIO
  - source:https://github.com/Chunshan-Theta/GPIO_ON_Raspberry 
  
GpioAjaxOff.php	and GpioAjaxOn.php	

  - Get PIN number and exec GPIO command 
RJ.php	

  - output data from Mysql and convert to Json's file 
  - source: https://github.com/Chunshan-Theta/SQLCmdUsingPHP
  
SQLstructure.sql	

  - It's SQL structure and sample data for index.php and RJ.php
  
index.php	a

  - insert Json data that recorded gpio setting to Mysql
  - It's a UI
  
off.py	

  - close Pi's GPIO 
  - for GpioAjaxOff.php
  
on.py

  - enable Pi's GPIO 
  - for GpioAjaxOn.php
  
未命名.jpg

  - 系統流程


----------------------------------------------------------------------------------------------------------------------------------------

系統安裝

          Step 1 建立網路伺服器端

1.1    建立資料庫：
重建或新建資料庫可利用web_GPIO/SQLstructure.sql建立，裡面包含資料表 `config`與數筆範例資料。

1.2    確保新增資料ui界面成功建立（index.php）：
至web_GPIO/index.php中的註解點`Note-(DB config)` 修改網路伺服器位址，在透過瀏覽器進入此頁面，輸入完gpio資料後按下〝go〞按鍵，若頁尾動態跑出〝傳輸成功〞則完成此步驟。



1.3    確保資料庫資料輸出ui界面成功建立（RJ.php）：

至web_GPIO/RJ.php中的註解點`Note-(DB config) `填寫資料庫資料（伺服器地址，資料庫名稱，資料庫帳號，資料庫密碼），若有跑出Json資料則正確。

若無請確定資料庫帳號位址等資料正確與資料庫是否存在，重建或新建資料庫可利用web_GPIO/SQLstructure.sql建立。

1.4    確保網頁遠距開啟gpio指令成功建立：

至web_GPIO/GpioAjaxOn.php中註解點`Note—(python command)` 修改路徑指向至on.py，若透過瀏覽器進入此網頁(此網頁有get參數,變數名稱為n)後成功啟動gpio則成功。

若無反應請確定是否已開啟網路伺服器執行本機指令的權限。

1.5    確保網頁遠距關閉gpio指令成功建立：
至web_GPIO/GpioAjaxOff.php中註解點`Note—(python command) `修改路徑指向至off.py，若透過瀏覽器進入此網頁(此網頁有get參數,變數名稱為n)後成功關閉gpio則成功。

***若無反應請確定是否已開啟網路伺服器執行本機指令的權限。***

權限開啟
 - sudo visudo
 - add to bottom of file : www-data ALL=(ALL)NOPASSWD:ALL
 - www-data is user_id , you can check by phpinfo()
 

          Step 2  建立臉部偵測本地端

2.0 環境需求 : git , opencv2.4
 - install git : apt-get install git
 - install opencv2.4 : apt-get install python-opencv
 
2.1 至FaceDetect_GPIO/main.py中註解點`Note-(WebServer address)`修改路徑指向網路伺服器位址。

2.2 至FaceDetect_GPIO/main.py中註解點`Note—(Rule of turn on)`可以調整開燈的需要人數。


