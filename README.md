# matplotlib set Chinese fonts

```python
import matplotlib.font_manager

matplotlib.font_manager.fontManager.addfont('/some_dir/NotoSansTC-Regular.otf')
matplotlib.font_manager.fontManager.addfont('/some_dir/NotoSansSC-Regular.otf')

# list currently loaded font files
# [f.name for f in matplotlib.font_manager.fontManager.ttflist if 'C' in f.name]

# use in seaborn
# must check if font name is correct!
font_rc = {'font.family': ['Noto Sans TC', 'Noto Sans SC']}
sns.set(rc=font_rc)

# use in plain matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Noto Sans TC', 'Noto Sans SC']
# additional setting for the minus `-` sign
plt.rcParams['axes.unicode_minus'] = False
```

# Pandas print full content

```python
def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')
```

# ffmpeg convert .mov to GIF
```bash
brew install ffmpeg
ffmpeg -i 輸入檔名.mov -vf "fps=10,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 輸出檔名.gif 
```
