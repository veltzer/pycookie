"""
main entry point to the program
"""
import os

import pylogconf.core
import tqdm
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint
from pycookie.static import VERSION_STR
import browsercookie


@register_endpoint(
    description="dump cookies",
    configs=[
    ],
)
def dump_cookies() -> None:
    # cj = browsercookie.load()
    # cj = browsercookie.chrome()
    cj = browsercookie.firefox()
    # print(len(cj._cookies))
    # print(cj._cookies)
    # noinspection PyProtectedMember
    for k, v in cj._cookies.items():
        print("=======================")
        print(k, v)
    # print(dir(cj))
    # help(cj.make_cookies)
    # help(cj.extract_cookies)


@register_main(
    main_description="pycookie will help you remove duplicate files",
    app_name="pycookie",
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
