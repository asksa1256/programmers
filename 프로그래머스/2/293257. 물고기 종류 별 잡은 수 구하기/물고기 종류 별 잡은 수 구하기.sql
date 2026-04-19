select count(*) as FISH_COUNT,
       A.fish_name as FISH_NAME
    from fish_name_info A
    join fish_info B
      on A.fish_type = B.fish_type
    group by A.fish_name
    order by fish_count desc
;