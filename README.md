# recognize
标题：文字识别程序；
输入：图片；
输出：文字（可以复制）；
功能：使用pyqt5和QTDesigner制作界面，opencv处理图片，调用百度云OCR(文字识别库)，识别文字，并输出。
注意：百度云OCR中，每个申请的appkey是限制次数的，每天也是限量的。如果识别不出文字，说明appkey当天的次数已用完。如果后一天还是识别不了文字，说明appkey总数用完了。
本程序还可以利用pyinstaller -F --distpath release XX.py打包，直接大包为exe文件，可以在window上使用。由于打包后文件太大，没有上传，有兴趣可以自己打包。
