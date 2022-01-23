def gen_files(amount, min_size, max_size, directory):
    for _ in range(amount):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_ext = random.choice(exts)
        f_content = bytes(random.randint(0, 255) for _ in range(random.randint(min_size, max_size)))

        with open(os.path.join(directory, f'{f_name}.{f_ext}'), 'wb') as f:
            f.write(f_content)


if __name__ == '__main__':
    import os
    import random

    folder = 'files'
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    exts = ['txt', 'py', 'jpg', 'html', 'css', 'png']

    os.makedirs(folder, exist_ok=True)

    gen_files(random.randint(1, 10), 1, 100, folder)
    gen_files(random.randint(1, 10), 100, 1000, folder)
    gen_files(random.randint(1, 10), 1000, 10000, folder)
    gen_files(random.randint(1, 10), 10000, 100000, folder)
