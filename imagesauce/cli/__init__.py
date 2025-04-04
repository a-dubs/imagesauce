#!/usr/bin/python3

import pathlib
import sys
import logging
import argparse

from imagesauce.image_customizer import customize_image_entry_point

logger = logging.getLogger(__name__)


def _parser():
    parser = argparse.ArgumentParser(description="change image")
    parser.add_argument("--log-level", choices=["info", "debug"], default="info")
    parser.add_argument("--log-file", type=pathlib.Path, help="write log to given file instead of stdout")
    parser.add_argument("--log-console", action="store_true", help="write log to stdout")
    p_sub = parser.add_subparsers(help="sub-command help")

    # customize-image
    p_customize = p_sub.add_parser("customize-image", help="Customize image")
    p_customize.add_argument("input_image_file", type=pathlib.Path, help="the path to the input image file")
    p_customize.add_argument("output_image_path", type=pathlib.Path, help="the path to the output image file")
    p_customize.add_argument("target_mount_point", type=pathlib.Path, help="the path to the target mount point")
    p_customize.add_argument("chimg_config_file", type=pathlib.Path, help="the path to the chimg config file")
    p_customize.add_argument("--overwrite", action="store_true", help="overwrite existing image file (if any)")
    p_customize.set_defaults(func=customize_image_entry_point)

    # example invocation:
    """
    imagesauce \
        --log-level debug \
        --log-console \
        customize-image \
        "oracle-jammy-minimal-20250316.img" \
        "chimg-modified-oracle-jammy-minimal-20250316.img" \
        "mount2" \
        "add-cloud-init-daily-ppa.yaml" \
        --overwrite
    """

    return parser


def main():
    parser = _parser()
    args = parser.parse_args()
    log_formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
    # log level
    loglevel = logging.INFO
    if args.log_level == "debug":
        loglevel = logging.DEBUG
    root_logger = logging.getLogger()
    root_logger.setLevel(loglevel)
    # log file
    if args.log_file:
        file_handler = logging.FileHandler(filename=args.log_file)
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)
    # log console
    if args.log_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)
    if "func" not in args:
        sys.exit(parser.print_help())
    args.func(args)
    sys.exit(0)


if __name__ == "__main__":
    main()
