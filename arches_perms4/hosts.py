import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"arches_perms4"), "arches_perms4.urls", name="arches_perms4"
    ),
)
