import sys
from osxwifiscanner import OSXWifiScanner

def main():
    wifi_scanner = OSXWifiScanner()
    access_points = wifi_scanner.get_access_points()
    if '-n' in sys.argv:
        print(len(access_points))
    else:
        print(access_points)

if __name__ == '__main__':
    main()