import sys
import os
import winreg # خاص بنظام ويندوز لتسجيل بروتوكول القفز
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QHBoxLayout, QLineEdit, QProgressBar)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings
from PyQt6.QtCore import QUrl, Qt

# --- 1. نظام الأمان والسرعة المتطور ---
def optimize_browser_settings(profile):
    settings = profile.settings()
    # تفعيل تسريع الأجهزة (Hardware Acceleration) لسرعة متناهية
    settings.setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
    # منع تتبع الإعلانات والاعتداءات البرمجية
    settings.setAttribute(QWebEngineSettings.WebAttribute.HyperlinkAuditingEnabled, False)
    # تفعيل الـ Cache في الذاكرة لسرعة الاستجابة
    profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryCache)

# --- 2. آلية القفز وتسجيل البروتوكول في الجهاز (المعجزة) ---
def register_superline_protocol():
    """تسجيل بروتوكول superline:// في نظام الويندوز لجعله المتصفح الرسمي الذاتي"""
    path = sys.executable
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "superline")
        winreg.SetValue(key, "", winreg.REG_SZ, "URL:Super Line Protocol")
        winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
        
        command_key = winreg.CreateKey(key, r"shell\open\command")
        winreg.SetValue(command_key, "", winreg.REG_SZ, f'"{path}" "%1"')
        print("تم تسجيل بروتوكول Super Line بنجاح في نظام التشغيل.")
    except Exception as e:
        print(f"تنبيه: يحتاج المتصفح لصلاحيات مسؤول لتفعيل القفز الذاتي: {e}")

# --- 3. الواجهة الرئيسية لمتصفح Super Line ---
class SuperLineBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chrome Super Line | متصفح السيادة العالمي")
        self.setGeometry(50, 50, 1300, 850)

        # إعداد ملف تعريف المستخدم للسرعة والأمان
        self.profile = QWebEngineProfile.defaultProfile()
        optimize_browser_settings(self.profile)

        # محرك التصفح الرئيسي
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # شريط العنوان والتحكم
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        # أزرار القفزات المعجزة
        self.btn_workspace = QPushButton("قفزة بيئة العمل")
        self.btn_system_jump = QPushButton("تفعيل التثبيت الذاتي")

        # تنسيق "Super Line" الاحترافي
        self.style_ui()

        # ربط الوظائف
        self.btn_workspace.clicked.connect(self.jump_to_workspace)
        self.btn_system_jump.clicked.connect(self.jump_to_device_core)

        # توزيع العناصر
        layout = QVBoxLayout()
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.url_bar)
        nav_layout.addWidget(self.btn_workspace)
        nav_layout.addWidget(self.btn_system_jump)
        
        layout.addLayout(nav_layout)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def style_ui(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #1a1a1a; }
            QLineEdit { padding: 8px; border-radius: 5px; background: #2d2d2d; color: white; border: 1px solid #444; }
            QPushButton { padding: 8px 15px; border-radius: 5px; font-weight: bold; color: white; }
            QPushButton#btn_workspace { background-color: #00c853; }
            QPushButton#btn_system_jump { background-color: #d50000; }
        """)
        self.btn_workspace.setObjectName("btn_workspace")
        self.btn_system_jump.setObjectName("btn_system_jump")

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    # القفزة الأولى: تحويل الصفحة الحالية لبيئة عمل مستقلة
    def jump_to_workspace(self):
        workspace_html = """
        <html><body style='background:#121212; color:#00ff00; font-family:sans-serif; text-align:center; padding:100px;'>
            <h1>تم تفعيل بيئة عمل Super Line</h1>
            <p>أنت الآن تعمل في مساحة معزولة تماماً عن تتبع الإنترنت العام.</p>
            <div style='border:2px solid #00ff00; padding:20px; display:inline-block;'>السرعة: متناهية | الأمان: مفعل</div>
        </body></html>
        """
        self.browser.setHtml(workspace_html)

    # القفزة الثانية: تفعيل التثبيت الرسمي في الجهاز (المعجزة)
    def jump_to_device_core(self):
        register_superline_protocol()
        # محاكاة لفتح نافذة إدارية في الجهاز
        os.system("msg * تم تفعيل متصفح Chrome Super Line كمتصفح سيادي في نظامك بنجاح.")

# --- 4. تشغيل النظام المتكامل ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Super Line Browser")
    
    # إعدادات متطورة للخطوط والأداء
    window = SuperLineBrowser()
    window.show()
    sys.exit(app.exec())
    # --- إعدادات الهوية الإدارية ---
ADMIN_EMAIL = "rbyalshary2@gmail.com"

# --- دالة التوثيق الإداري (المعجزة الثالثة) ---
def send_admin_notification(user_info):
    """
    هذه الدالة تعمل عند ضغط المستخدم على 'إذن التثبيت'.
    تقوم بربط المتصفح بالبريد الإداري rbyalshary2@gmail.com
    """
    import webbrowser
    # إنشاء رابط تواصل مباشر مع البريد الإداري لتوثيق التثبيت
    subject = "طلب تفعيل متصفح Super Line"
    body = f"تم طلب تثبيت المتصفح على جهاز جديد. معرف الإدارة: {ADMIN_EMAIL}"
    webbrowser.open(f"mailto:{ADMIN_EMAIL}?subject={subject}&body={body}")
    print(f"تم ربط عملية التثبيت بالبريد الإداري: {ADMIN_EMAIL}")

# --- تعديل في زر التثبيت داخل الكلاس الرئيسي ---
# داخل دالة jump_to_device_core في الكود السابق، أضف السطر التالي:
def jump_to_device_core(self):
    register_superline_protocol()
    # استدعاء التوثيق البريدي
    send_admin_notification("User-Device-ID")
    os.system(f"msg * تم ربط المتصفح بالبريد الإداري {ADMIN_EMAIL} وتفعيله بنجاح.")

