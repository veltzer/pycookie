"""
main entry point to the program
"""

import browsercookie
import pylogconf.core
from pytconf import config_arg_parse_and_launch, register_endpoint, register_main

from pycookie.static import APP_NAME, DESCRIPTION, VERSION_STR


@register_endpoint(
    description="dump cookies",
    configs=[
    ],
)
def dump_cookies() -> None:
    # cj = browsercookie.load()
    # cj = browsercookie.chrome()
    cj = browsercookie.firefox()
    for cookie in cj:
        print("=======================")
        print(cookie.domain, cookie)
    # print(dir(cj))
    # help(cj.make_cookies)
    # help(cj.extract_cookies)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
