sudo imagesauce \
    --log-level debug \
    --log-console \
    customize-image \
    "oracle-jammy-minimal-20250316.img" \
    "output-image.img" \
    "/tmp/ImageSauce" \
    "example_chimg_configs/add-cloud-init-daily-ppa.yaml" \
    --overwrite
