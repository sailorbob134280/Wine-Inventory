# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Windows\\WinSxS\\x86_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.17134.1_none_50c6cb8431e7428f', 
		     'D:\\Documents\\GitHub\\Wine-Inventory', 
		     'D:\\Documents\\GitHub\\Wine-Inventory\\win_build_dependencies', 
		     'C:\\Program Files (x86)\\Python37-32\\python-virtual-environments\\wineinv\\Lib\\site-packages', 
		     'C:\Program Files (x86)\Python37-32\Lib\site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Vinny',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
