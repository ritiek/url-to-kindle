#!/bin/bash

from="my_kindle_approved_email@gmail.com"
to="my_kindle_email@kindle.com"

get_domain_type() {
    declare -a domains=("@free.kindle.com"
                        "@kindle.com"
                        "@kindle.cn"
                        "@iduokan.com"
                        "@pbsync.com")

    len_domains=${#domains[@]}
    for (( i=0; i<${len_domains}; i++ ));
    do
        if [[ $1 == *${domains[i]} ]]; then
            domain_type=$(($i + 1))
            break
        fi
    done
}

get_domain_type $to
to_prefix="${to%@*}"

curl -X POST \
    --data-urlencode "from=$from" \
    --data "title=" \
    --data "email=$to_prefix" \
    --data "domain=$domain_type" \
    --data "context=send" \
    --data "url=$1" \
    --compressed \
    "https://pushtokindle.fivefilters.org/send.php"

echo
