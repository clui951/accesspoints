import subprocess

class BaseWifiScanner(object):

	def get_cmd(self):
		raise NotImplementedError

	def parse_output(self, output):
		raise NotImplementedError

	def get_access_points(self):
		output = self.call_subprocess(self.get_cmd())
		results = self.parse_output(output)
		return results

	@staticmethod
	def call_subprocess(cmd):
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		(out, _) = proc.communicate()
		return out