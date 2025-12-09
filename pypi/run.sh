nohup bandersnatch \
    -c bandersnatch.conf mirror --force-check \
    1> /dev/null \
    2> log/$(date +"%Y-%m-%d_%H-%M-%S").log &
