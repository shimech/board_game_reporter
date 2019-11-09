# Board Game Reporter


## 0. OS
macOS Catalina 10.15


## 1. 環境構築
Homebrewでpyenvをインストール  
`$ brew install pyenv`

`~/.zshrc`に以下を追加  
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

pyenvでPythonをインストール  
`$ pyenv install 3.8.0`  
`$ pyenv local 3.8.0`

pipをupdateし、パッケージをインストール  
`$ pip install --upgrade pip`  
`$ pip install -r requirements.txt`


## 2. APIトークンなどを設定
* `slackbot_settings.py`
* `models/googlespreadsheet_information.py`

の変数に適宜設定する。また、`models/`にJSONを配置する。


## 3. メッセージをチャンネルにポスト
`$ python run.py -y`

|オプション             |動作                  |
|-----------------------|----------------------|
|-y, --yes              |本番チャンネルにPOST  |
|-t, --test, -d, --debug|テストチャンネルにPOST|
