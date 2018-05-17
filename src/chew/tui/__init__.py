
from bite.service.bugzilla.jsonrpc import BugzillaJsonrpc
import urwid


class SearchWalker(urwid.ListWalker):

    def __init__(self):
        self.focus = 0


class Client(object):

    def __init__(self, **kw):
        self.service = BugzillaJsonrpc(base='https://bugs.gentoo.org/')
        self.listbox = urwid.ListBox(SearchWalker())
        self.footer = urwid.AttrWrap(urwid.Text('foo'), 'bar')
        self.view = urwid.Frame(urwid.AttrWrap(self.listbox, 'blah'), footer=self.footer)

    def run(self):
        self.loop = urwid.MainLoop(
            self.view, handle_mouse=False, unhandled_input=self.unhandled_keypress)
        self.loop.run()

    def unhandled_keypress(self, k):
        if k in ('q', 'Q'):
            self.quit()

    def quit(self):
        raise urwid.ExitMainLoop()
