sudo /home/a-dubs/.virtualenvs/imagesauce-cusa/bin/python -m imagesauce \
    --log-level info \
    --log-console \
    customize-image \
    "oracle-jammy-minimal-20250316.img" \
    "output-image.img" \
    "/tmp/imagesauce" \
    "example_chimg_configs/add-cloud-init-daily-ppa.yaml" \
    --overwrite
