import sublime, sublime_plugin

class FormatArrayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("Hello Array")
		self.view.insert(edit, self.view.sel()[0].begin(), "[\n")
		FormatChildCommand.run(self, edit, True)
		self.view.insert(edit, self.view.sel()[0].begin(), "]")
		# self.view.insert(edit, 0, "[")
		# self.view.insert(edit, 0, "Hello, World!")
		# Convert `[]`, when user types `[`, into [{t:"p",T:"dorem ipsum"}], formatted

class FormatChildCommand(sublime_plugin.TextCommand):#todo - rather than always make autoformatted text, make sure the user is not putting the `{` after an `attributes` tag
	def run(self, edit, nest=False):#if nest, we increase the tab count by 1 because the children are now nested in an array
		print("Hello Child")
		tabs = ""

		if nest:
			tabs += "\t"

		self.view.insert(edit, self.view.sel()[0].begin(), tabs + "{\n")
		self.view.insert(edit, self.view.sel()[0].begin(), tabs + "\tt: \"p\",\n")
		self.view.insert(edit, self.view.sel()[0].begin(), tabs + "\tT: \"dorem ipsum\",\n")
		self.view.insert(edit, self.view.sel()[0].begin(), tabs + "}")

		if nest:
			self.view.insert(edit, self.view.sel()[0].begin(), "\n")


		# self.view.insert(edit, 0, "{")
		# self.view.insert(edit, 0, "Hello, World!")
		# Convert `{}`, when user types `{`, into {t:"p",T:"dorem ipsum"}, formatted
