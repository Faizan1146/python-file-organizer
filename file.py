from pathlib import Path
import shutil

categories = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".mp3": "Music",
    ".txt": "Documents",
    ".mp4": "Video",
    ".py": "Python",
    ".jpeg": "Images",
    ".wav": "Music",
    ".mkv": "Video"
}

# folder = input("Enter path:")
try:
    folder = Path.cwd()
    print(Path.cwd())
    f = input("Input folder: ")
    t_folder = Path(folder / f)

    for item in t_folder.iterdir():
        if item.is_file():
            print(item.name)
            # print(item.suffix)
            if item.suffix in categories:
                print(item.name, "→", categories[item.suffix])
                n_folder = Path(t_folder / categories[item.suffix])
                n_folder.mkdir(parents=True , exist_ok=True)
                if Path.exists(n_folder / item.name):
                    print("Already exist")
                else:
                    shutil.move(item,n_folder)
            else:
                print(f"Unsupported file type: {item.suffix}")
except FileNotFoundError:
    print("The folder does not exist")
            
