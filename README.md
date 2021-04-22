# Verify-Email-GUI-Python
It creates an account only if OTP has been verified. It uses sqlite database for store information.

## Used Modules
* **PyQt5**
* **sqlite3**
* **smtplib**
* **random**
* **datetime**

#### PyQt5
----
* Used **Qt Designer** for create awesome GUIs and used some css so that it looks better.

#### sqlite3
----
* Used **sqlite studio** for create *Database*.

#### smtplib
----
* Sending **OTP** for verify _Email_.

#### random
----
* Generate random 6-digits OTP. 

#### datetime
----
* Take real date and time when account is made.

## How to use this?
* Make sure all modules are working in your device. Check **Used Modules** section.
* After downloading, you have to update ***senderdetail.py*** file. Change EMAIL and PASSWORD with your email and password.
* Make sure you have enabled less secure apps. [Click here to know about this](https://support.google.com/accounts/answer/6010255?hl=en#:~:text=If%20an%20app%20or%20site,helps%20keep%20your%20account%20safe.)
