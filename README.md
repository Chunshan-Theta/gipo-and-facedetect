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
  
index.php	

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
