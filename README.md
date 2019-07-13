Trying to demonstrate the useful nature of geohash to increase performance of SQL queries. My tests with Postgres SQL show no real improvement mainly due to the fact that Postgres is in fact able to combine several indexes with BETWEEN statements really efficiently.

    geohash=# explain select count(*) from location where 2 < x and x < 3 and 9 < y and y < 10;
                                                                      QUERY PLAN                                                                      
    ------------------------------------------------------------------------------------------------------------------------------------------------------
     Aggregate  (cost=1024.68..1024.69 rows=1 width=8)
       ->  Bitmap Heap Scan on location  (cost=361.93..1024.07 rows=242 width=0)
             Recheck Cond: (('9'::double precision < y) AND (y < '10'::double precision) AND ('2'::double precision < x) AND (x < '3'::double precision))
             ->  BitmapAnd  (cost=361.93..361.93 rows=242 width=0)
                   ->  Bitmap Index Scan on ix_location_y  (cost=0.00..123.31 rows=5089 width=0)
                         Index Cond: (('9'::double precision < y) AND (y < '10'::double precision))
                   ->  Bitmap Index Scan on ix_location_x  (cost=0.00..238.25 rows=9783 width=0)
                         Index Cond: (('2'::double precision < x) AND (x < '3'::double precision))
    (8 rows)

As a consequence the queries using Geohash are only less flexible (it is harder to do proximity queries for distances that are different than the size of the cells).

There is still an advantage in using Geohash in that case though, which would be partitioning for instance.