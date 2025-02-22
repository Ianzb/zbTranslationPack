import zipfile, os, json, shutil
from tkinter import filedialog

path = filedialog.askopenfilename()
print("输入路径：", path, sep="")
if os.path.exists(path) and zipfile.is_zipfile(path):
    zipfile = zipfile.ZipFile(path)

    lcn = [i for i in zipfile.namelist() if i.endswith("lang/zh_cn.json")]
    if lcn:
        print("该模组已存在汉化文件，请手动检查汉化内容！")
    len = [i for i in zipfile.namelist() if i.endswith("lang/en_us.json")]
    for i in len:
        print("正在解压：", i, sep="")
        en = zipfile.extract(i, "zbTranslationPack")
        cn = en.replace("en_us", "zh_cn")
        if os.path.exists(cn):
            with open(cn, "r", encoding="utf-8") as f:
                cnstr = f.read()
                cnjson = json.loads(cnstr)
            with open(en, "r", encoding="utf-8") as f:
                enstr = f.read()
                enjson = json.loads(enstr)
            tr = enstr
            for k in enjson.keys():
                if k in cnjson.keys() and cnjson[k]:
                    tr = tr.replace(f'"{enjson[k]}"', f'"{cnjson[k]}"')
            with open(cn, "w", encoding="utf-8") as f:
                f.write(tr)
        else:
            try:
                zipfile.extract(i.replace("en_us", "zh_cn"), "zbTranslationPack")
            except:
                pass
            shutil.copyfile(en, cn)
