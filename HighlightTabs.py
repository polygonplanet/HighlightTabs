import sublime
import sublime_plugin

REGION_KEY = 'HighlightTabs_Highlight'
SETTINGS_KEY = 'HighlightTabs.sublime-settings'

DEFAULT_ENABLED = True
DEFAULT_REGEXP = '\t'
DEFAULT_HIGHLIGHT_COLOR = 'comment'
DEFAULT_MAX_FILE_SIZE = 1048576
DEFAULT_DELAY = 200

ST3 = int(sublime.version()) >= 3000

class Preferences:
  def load(self, settings):
    self.enabled = bool(settings.get('highlight_tabs_enabled', DEFAULT_ENABLED))
    self.regexp = settings.get('highlight_tabs_regexp', DEFAULT_REGEXP)
    self.highlight_color = settings.get('highlight_tabs_highlight_color', DEFAULT_HIGHLIGHT_COLOR)
    self.max_size = settings.get('highlight_tabs_max_file_size', DEFAULT_MAX_FILE_SIZE)
    self.delay = settings.get('highlight_tabs_delay', DEFAULT_DELAY)

Pref = Preferences()


def plugin_loaded():
  settings = sublime.load_settings(SETTINGS_KEY)
  Pref.load(settings)
  settings.add_on_change('reload', lambda: Pref.load(settings))


def highlight(view):
  if view.size() > Pref.max_size:
    return

  if not Pref.regexp:
    return

  view.erase_regions(REGION_KEY)

  regions = view.find_all(Pref.regexp)
  scope = Pref.highlight_color

  if ST3:
    flags = sublime.HIDE_ON_MINIMAP + sublime.DRAW_NO_FILL + sublime.DRAW_NO_OUTLINE + sublime.DRAW_SOLID_UNDERLINE
    view.add_regions(REGION_KEY, regions, scope, '', flags)
  else:
    flags = sublime.HIDE_ON_MINIMAP + sublime.DRAW_OUTLINED
    view.add_regions(REGION_KEY, regions, scope, flags)


class HighlightTabs(sublime_plugin.EventListener):
  def __init__(self):
    self.pending = 0

  def render(self, view):
    self.pending = self.pending - 1
    if self.pending > 0:
      return
    highlight(view)

  def on_modified(self, view):
    if Pref.enabled:
      self.pending = self.pending + 1
      if self.pending == 1:
        sublime.set_timeout(lambda: self.render(view), 1)
      else:
        sublime.set_timeout(lambda: self.render(view), Pref.delay)

  def on_activated(self, view):
    if Pref.enabled:
      highlight(view)

  def on_load(self, view):
    if Pref.enabled:
      highlight(view)


if not ST3:
  plugin_loaded()
