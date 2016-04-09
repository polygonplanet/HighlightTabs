HighlightTabs
=================

**[README (日本語)](README.ja.md)**

Highlight tab characters in [Sublime Text 2](http://www.sublimetext.com/2) and [3](http://www.sublimetext.com/3).

## Installation

### 1. Add Repository

* Open **"Command Pallet"** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (<kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> on OSX)
* Select **"Package Control: Add Repository"**
* Enter this repository URL `https://github.com/polygonplanet/HighlightTabs` 

### 2. Install Package

* Open **"Command Pallet"** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (<kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> on OSX)
* Select **"Package Control: Install Package"**
* Select **HighlightTabs**

## Options

Several options are available to customize the plugin's behavior.  
Those settings are stored in a configuration file, as JSON.

Go to "`Preferences` / `Package Settings` / `HighlightTabs` / `Settings - User`" to add your custom settings.

### highlight_tabs_enabled

*Default: `true`*

Whether to enable the Highlight Tabs.

### highlight_tabs_highlight_color

*Default: `"comment"`*

Highlight color is specified as a `scope`.
You may define and use a custom scope to better fit your colorscheme.
A value of empty string "" will make highlights invisible.

**Example:**

```javascript
{
  "highlight_tabs_enabled": true,
  "highlight_tabs_highlight_color": "comment"
}
```

## License

MIT

