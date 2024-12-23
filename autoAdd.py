import zipfile,os,json,shutil

path=input("请输入文件路径：").strip("& ").strip('"').strip("'").strip()
print("输入路径：",path,sep="")
if os.path.exists(path) and zipfile.is_zipfile(path):
    zipfile=zipfile.ZipFile(path)
    
    lcn=[i for i in zipfile.namelist() if i.endswith("lang/zh_cn.json")]
    if lcn:
        print("该模组已存在汉化文件，请手动检查汉化内容！")
    len=[i for i in zipfile.namelist() if i.endswith("lang/en_us.json")]
    for i in len:
        print("正在解压：",i,sep="")
        en=zipfile.extract(i,"zbTranslationPack")
        cn=en.replace("en_us","zh_cn")
        if os.path.exists(cn):
            tr={}
            with open(cn,"r",encoding="utf-8") as f:
                cnjson=json.load(f)
            with open(en,"r",encoding="utf-8") as f:
                enjson=json.load(f)
            for k in enjson.keys():
                if k in cnjson.keys() and cnjson[k]:
                    tr[k]=cnjson[k]
                else:
                    tr[k]=enjson[k]
            with open(cn,"w",encoding="utf-8") as f:
                json.dump(tr,f,ensure_ascii=False,indent=2)
        else:
            try:
                zipfile.extract(i.replace("en_us","zh_cn"),"zbTranslationPack")
            except:
                pass
            shutil.copyfile(en,cn)