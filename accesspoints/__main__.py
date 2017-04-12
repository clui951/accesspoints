from osxwifiscanner import OSXWifiScanner

def main():
    wifi_scanner = OSXWifiScanner()
    access_points = wifi_scanner.get_access_points()
    print(access_points)

if __name__ == '__main__':
    main()