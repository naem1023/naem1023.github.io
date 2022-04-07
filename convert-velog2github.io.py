from pathlib import Path
import subprocess as sp
import os

velog_path_str = 'backup/content'
img_base_path = 'backup/'
asset_path = 'assets/images/'

velog_path = Path(velog_path_str)
postings = velog_path.iterdir()
# print(f'Number of postings: {len(list(postings))}')

img_target = '![](/images'

run_flag = True

for idx, posting in enumerate(postings):
    print(f'{idx} file path = {posting}')
    if posting.exists():
        with open(str(posting), 'r', encoding='utf-8') as md_file:
            lines = md_file.readlines()
            date = lines[3].split()[-1][:10]
            title = lines[1].split(":")[-1][2:-2]
            # print(title)
            new_filename = date + '-' + posting.stem

            for line_num, line in enumerate(lines):
                # print(line[-10:])
                if line[:len(img_target)] == img_target:
                    origin_img_path = img_base_path + line[5:-2]
                    img_path = os.path.join(asset_path, title, origin_img_path.split('/')[-1])
                    print(f'{origin_img_path} => {img_path}')

                    # Modify markdown
                    lines[line_num] = lines[line_num][:5] + img_path + lines[line_num][-2:]

                    # print(Path(img_path).parent)
                    target_dir = str(Path(img_path).parent)
                    mkdir_command = ['mkdir', target_dir]

                    cp_command = [
                        'cp', origin_img_path, img_path
                    ]
                    # print(cp_command)

                    if run_flag:
                        sp.run(mkdir_command)
                        sp.run(cp_command)
        with open(str(posting), 'w', encoding='utf-8') as md_file:
            md_file.writelines(lines)

        md_cp_command = [
            'cp', str(posting), '_posts/' + new_filename + '.md'
        ]
        print(md_cp_command)
        sp.run(md_cp_command)
    else:
        print(f'{posting} is not exist.')
