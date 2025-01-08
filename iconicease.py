import os
import win32api
import win32con
import win32gui
import ctypes
from ctypes import wintypes

class IconicEase:
    def __init__(self):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    def list_icons(self):
        """Lists all icons on the desktop."""
        icons = [f for f in os.listdir(self.desktop_path) if os.path.isfile(os.path.join(self.desktop_path, f))]
        print("Icons on Desktop:")
        for icon in icons:
            print(icon)
        return icons

    def arrange_icons(self, by='name'):
        """Arrange icons based on the specified parameter: name, type."""
        shell = win32com.client.Dispatch("Shell.Application")
        desktop = shell.Namespace(0)

        items = []
        for i in range(desktop.Items().Count):
            item = desktop.Items().Item(i)
            items.append((item.Name, item.Path))

        if by == 'name':
            items.sort(key=lambda x: x[0].lower())
        elif by == 'type':
            items.sort(key=lambda x: os.path.splitext(x[1])[1].lower())

        self.set_icon_positions(items)

    def set_icon_positions(self, items):
        """Sets the icon positions on the desktop."""
        hDesktopWnd = win32gui.GetDesktopWindow()
        hDesktopDC = win32gui.GetDC(hDesktopWnd)

        icon_width = ctypes.windll.user32.GetSystemMetrics(win32con.SM_CXICON)
        icon_height = ctypes.windll.user32.GetSystemMetrics(win32con.SM_CYICON)

        x = 0
        y = 0
        for name, path in items:
            win32gui.SetWindowPos(path, 0, x, y, 0, 0, win32con.SWP_NOZORDER | win32con.SWP_NOSIZE)
            x += icon_width
            if x + icon_width > win32api.GetSystemMetrics(win32con.SM_CXSCREEN):
                x = 0
                y += icon_height

        win32gui.ReleaseDC(hDesktopWnd, hDesktopDC)

    def customize_icon(self, icon_name, new_name=None, new_position=None):
        """Customize an icon's name or position on the desktop."""
        icons = self.list_icons()
        if icon_name not in icons:
            print(f"Icon '{icon_name}' not found on the desktop.")
            return

        old_path = os.path.join(self.desktop_path, icon_name)
        if new_name:
            new_path = os.path.join(self.desktop_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed '{icon_name}' to '{new_name}'")

        if new_position:
            # Additional logic can be implemented for setting a new position
            print(f"Setting new position for {icon_name} to {new_position}")

if __name__ == "__main__":
    iconic_ease = IconicEase()
    iconic_ease.list_icons()
    iconic_ease.arrange_icons(by='name')
    iconic_ease.customize_icon("example_icon.lnk", new_name="new_example_icon.lnk")