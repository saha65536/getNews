# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['callNewspaper.py'],
             pathex=['D:\\eric6-21.6\\workspace\\newspaper'],
             binaries=[],
             datas=[('C:\\Users\\saha\\AppData\\Roaming\\Python\\Python37\\site-packages\\newspaper\\resources\\text\\*.txt', 'text'),
			('C:\\Users\\saha\\AppData\\Roaming\\Python\\Python37\\site-packages\\newspaper\\resources\\misc\\*.txt', 'misc'),],
             hiddenimports=['newspaper3k', 'beautifulsoup4', 'cssselect', 'feedfinder2', 'feedparser', 'jieba3k', 'lxml', 'nltk', 'Pillow', 'pythainlp', 'python-dateutil', 'PyYAML', 'requests', 'tinysegmenter', 'tldextract'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='callNewspaper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='callNewspaper')
