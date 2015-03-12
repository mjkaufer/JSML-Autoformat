import sublime, sublime_plugin

class FormatArrayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if not is_JSML(self.view):
			return

		write(self.view, "[\n")
		FormatChildCommand.run(self, edit, True)
		write(self.view, "]")


class FormatChildCommand(sublime_plugin.TextCommand):
	def run(self, edit, nest=False):
		if not is_JSML(self.view):
			return

		tabs = ""
		end = ""

		if nest:
			tabs = "\t"
			end = "\n"

		
		write(self.view, tabs + "{\n")
		write(self.view, tabs + "\tt: \"p\",\n")
		write(self.view, tabs + "\tT: \"dorem ipsum\",\n")
		write(self.view, tabs + "}" + end)


def is_JSML(view):
	filename = view.file_name();
	
	extension = ".jsml"

	if not extension in filename.lower():
		return False

	return filename.lower().index(extension) == len(filename) - len(extension)#ensure it's not part of the folder, etc., but rather the actual file extension

def write(view, content):
	view.run_command("insert_snippet", {"contents": content})