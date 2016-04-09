HighlightTabs
=================

**[README (English)](README.md)**

タブ文字を強調表示する [Sublime Text 2](http://www.sublimetext.com/2) と [3](http://www.sublimetext.com/3) 用のプラグインです。

## 導入

### 1. レポジトリの追加

* **"コマンドパレット (Command Pallet)"** を開きます。 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (OSX の場合 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd>) で開けます。
* **"Package Control: Add Repository"** を選択します。
* 下のほうにでる入力欄に、このレポジトリの URL `https://github.com/polygonplanet/HighlightTabs` を入力し決定します。

### 2. パッケージのインストール

* **"コマンドパレット (Command Pallet)"** を開きます。 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (OSX の場合 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd>) で開けます。
* **"Package Control: Install Package"** を選択します。
* **HighlightTabs** を選択するとインストールされます。

## オプション

いくつかのオプションがプラグインの動作をカスタマイズするために利用可能です。  
これらの設定は、JSON として設定ファイルに保存されます。

"`Preferences` / `Package Settings` / `HighlightTabs` / `Settings - User`" から設定できます。

### highlight_tabs_enabled

*Default: `true`*

強調表示を有効にするかどうか。  
`true` にすると有効になり、`false` にすると無効になります。

### highlight_tabs_highlight_color

*Default: `"comment"`*

強調表示する `scope` を指定できます。
Sublime Text のカラーテーマをカスタマイズして任意の scope を定義することができます。

**例:**

```javascript
{
  "highlight_tabs_enabled": true,
  "highlight_tabs_highlight_color": "comment"
}
```

## ライセンス

MIT
