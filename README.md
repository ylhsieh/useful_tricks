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
