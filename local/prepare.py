import os
import shutil

home_dir = os.path.expanduser("~")
dest = os.path.join(
    home_dir, "Desktop" if os.name == "nt" else os.path.sep, "mvid_deps"
)

platforms = ["windows64", "windows32", "linux", "mac"]
ext = {"windows64": "zip", "windows32": "zip", "linux": "gztar", "mac": "zip"}


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


print("Copying files...")

src = "./build"
sync_dir = os.path.join(dest, "build/")
if os.path.isdir(sync_dir):
    shutil.rmtree(sync_dir)
    os.makedirs(sync_dir)

for platform in platforms:
    build_dst = os.path.join(dest, f"build_{platform}", "musicvid.org/bin")
    if os.path.isdir(build_dst):
        try:
            shutil.rmtree(build_dst)
        except:
            pass
        print("Removing: ", build_dst)
    try:
        print("Copying to", build_dst)
        shutil.copytree(src, build_dst)
        shutil.copy("./local/package.json", build_dst)
        copytree(os.path.join(dest, platform), build_dst)
        print("zipping to", os.path.join(sync_dir, platform))

        shutil.make_archive(
            os.path.join(sync_dir, "musicvid_" + platform),
            ext[platform],
            root_dir=os.path.join(dest, f"build_{platform}"),
        )

    except shutil.Error as e:
        print("Directory not copied. Error: %s" % e)
    except OSError as e:
        print("Directory not copied. Error: %s" % e)
