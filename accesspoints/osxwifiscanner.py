import re
from basewifiscanner import BaseWifiScanner


class OSXWifiScanner(BaseWifiScanner):

	def get_cmd(self):
		cmd = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/"
		cmd += "airport -s"
		return cmd

	def parse_output(self, output):
		# print(output)
		data_lines = output.split("\n")[1:]
		ap_list = []

		for line in data_lines:
			sre_match = re.search("([a-z0-9]{2}:){5}[a-z0-9]{2}", line)
			if sre_match:
				bssid = sre_match.group(0)
				toks = line.split(bssid)
				ssid = toks[0].lstrip().rstrip()
				(rssi, _, _, _, security) = re.split("\s+", toks[1].lstrip().rstrip(), maxsplit=4)
				ap = {"bssid" : bssid, "ssid" : ssid, "rssi" : int(rssi), "security" : security}
				ap_list.append(ap)
			else:
				# no AP
				pass

		return ap_list