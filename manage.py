import os
import requests


cookie_literal = ''
res_path = r''
url_base = 'http://www.lintcode.com/api/problems/?page='


def get_all_files(path):
    allfile = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            allfile.append(os.path.join(dirpath, dir))
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))
    return allfile


def get_cookies(cookie_literal):
    cookies = {}
    for line in cookie_literal.split(';'):
        k, v = line.strip().split('=', 1)
        cookies[k] = v
    return cookies


def filter_pr_of_one_page(url, cookies, written):
    resp = requests.get(url, cookies=cookies)
    problems = resp.json()['problems']
    for problem in problems:
        if problem['user_status'] == 'Accepted':
            fake_name = str(problem['id']) + '-' + problem['unique_name']
            if fake_name not in written:
                print(problem)
            # print(problem)


if __name__ == '__main__':
    written = [f.split("\\")[-1].split(".")[0] for f in get_all_files(res_path)]
    cookies = get_cookies(cookie_literal)

    for i in range(1, 10):
        url = url_base + str(i)
        filter_pr_of_one_page(url, cookies, written)
