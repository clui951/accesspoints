from basewifiscanner import BaseWifiScanner

class OSXWifiScanner(BaseWifiScanner):

	def get_cmd(self):
		cmd = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/"
		cmd += "airport -s"
		return cmd

	def parse_output(self, output):
		return NotImplementedError